"""Assemble selected parts into one Markdown document and compile it to PDF (Pandoc + XeLaTeX)."""
from __future__ import annotations

import datetime as dt
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from importlib import resources
from pathlib import Path

import yaml

from .bank import MONTHS, as_list

PANDOC_FROM = "markdown+lists_without_preceding_blankline-implicit_figures-citations-subscript-superscript"
TEX_PACKAGES = ["amsmath", "amssymb", "unicode-math", "microtype", "xcolor", "graphicx", "booktabs", "array",
                "tabularx", "adjustbox", "fvextra", "tikz", "tcolorbox", "fancyhdr", "lastpage", "xurl",
                "hyperref", "bookmark"]
_IMG = re.compile(r"(!\[[^\]]*\]\()([^)\s]+)(\))")


class BuildError(Exception):
    pass


def pandoc_path():
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except (ImportError, OSError):
        return shutil.which("pandoc")


def asset(name):
    return resources.files("tfsolve") / "assets" / name


def _num(x):
    return f"{x:g}" if isinstance(x, (int, float)) else str(x)


def _anchor(part):
    return "q-" + re.sub(r"[^A-Za-z0-9]+", "-", part.uid)


# ------------------------------------------------------------------ grouping

def _primary_topic(course, part, wanted):
    """The part's first topic, preferring one inside the requested topics."""
    topics = [t for t in part.topics if t in course.topics]
    if wanted:
        inside = [t for t in topics if t in wanted]
        if inside:
            return inside[0]
    return topics[0] if topics else None


def group(bank, sel, by):
    """Return [(heading, [(subheading or None, [parts])])] in reading order."""
    course = sel.course
    newest_first = lambda p: (-int(p.exam.label[:4] + p.exam.label[5:7]), p.sort_key)  # noqa: E731
    if by == "topic":
        wanted = set().union(*(course.expand(t) for t in sel.topics)) if sel.topics else None
        order = {tid: i for i, tid in enumerate(course.topics)}
        buckets = {}
        for p in sel.parts:
            prim = _primary_topic(course, p, wanted)
            root = course.root(prim) if prim else None
            buckets.setdefault(root, {}).setdefault(prim if prim != root else None, []).append(p)
        out = []
        for root in sorted(buckets, key=lambda r: order.get(r, 1e9)):
            subs = buckets[root]
            head = course.topics[root].name if root else "Untagged"
            out.append((head, [(course.topics[s].name if s else None, sorted(subs[s], key=newest_first))
                               for s in sorted(subs, key=lambda s: -1 if s is None else order.get(s, 1e9))]))
        return out
    if by == "year":
        exams = {}
        for p in sel.parts:
            exams.setdefault(p.exam, []).append(p)
        return [(f"{e.title}" + (f" · {e.meta.get('level_term')}" if e.meta.get("level_term") else ""),
                 [(None, sorted(ps, key=lambda p: p.sort_key))])
                for e, ps in sorted(exams.items(), key=lambda kv: kv[0].label, reverse=True)]
    if by == "faculty":
        fac = {}
        for p in sel.parts:
            who, how = bank.setters(p)
            key = ", ".join(who) + (" (taught; setter unknown)" if how == "taught" else "") if who else "Unknown"
            fac.setdefault(key, []).append(p)
        return [(k, [(None, sorted(v, key=newest_first))]) for k, v in sorted(fac.items())]
    return [("Questions", [(None, sorted(sel.parts, key=newest_first))])]


# ------------------------------------------------------------------ assembly

class _Figures:
    """Copies images next to the .tex (LaTeX runs with paranoid file access) and rewrites links."""

    def __init__(self, tmp):
        self.dir = Path(tmp) / "fig"
        self.n = 0

    def fix(self, text, base):
        def repl(m):
            src = (base / m.group(2)).resolve()
            if not src.is_file() or m.group(2).startswith(("http:", "https:")):
                return m.group(0)
            self.dir.mkdir(exist_ok=True)
            self.n += 1
            dst = self.dir / f"{self.n}-{src.name}"
            self._copy(src, dst)
            return f"{m.group(1)}fig/{dst.name}{m.group(3)}"
        return _IMG.sub(repl, text)

    def _copy(self, src, dst):
        shutil.copyfile(src, dst)


def _question_md(bank, part, figs, printed_stems, toc=None):
    exam, course = part.exam, part.exam.course
    who, how = bank.setters(part)
    head = [f"**{exam.when}**" + (f" ({exam.session})" if exam.session else ""), f"**{part.label}**"]
    if part.marks is not None:
        head.append(f"{_num(part.marks)} marks")
    if part.section:
        head.append(f"Section {part.section}")
    if who:
        head.append(("set by " if how == "set" else "taught by ") + ", ".join(who))
    if part.meta.get("mandatory"):
        head.append("compulsory")
    attrs = f"#{_anchor(part)}"
    if toc:  # one table-of-contents line per question, under its topic or exam heading
        level, text = toc
        attrs += f' toc-level="{level}" toc-text="{text.replace(chr(34), chr(39))}"'
    out = [f":::::: {{.tfq {attrs}}}", "::: tfhead", " · ".join(head), ":::"]
    names = [course.topics[t].name for t in part.topics if t in course.topics]
    if names:
        out += ["::: tfmeta", "Topics: " + " · ".join(names), ":::"]
    for stem in bank.stems_for(part):
        if stem.uid in printed_stems:
            out += ["::: tfmeta", f"Uses the shared setup of {stem.label}, printed above.", ":::"]
        else:
            printed_stems.add(stem.uid)
            out += ["::: tfstem", figs.fix(stem.body.strip(), stem.path.parent), ":::"]
    out += ["", figs.fix(part.body.strip(), part.path.parent), ""]
    if part.meta.get("note"):
        out += ["::: tfmeta", f"Transcription note: {part.meta['note']}", ":::"]
    rep = as_list(part.meta.get("repeat_of"))
    if rep:
        out += ["::: tfmeta", "Repeat of: " + ", ".join(rep), ":::"]
    out.append("::::::")
    return "\n".join(out)


SOL_TITLE = {
    "verified": "$\\checkmark$ Verified solution",
    "reviewed": "Reviewed solution",
    "unverified": "Solution (not yet verified)",
    "disputed": "Disputed solution: an error has been reported",
}


def _solution_md(sol, figs, label=None):
    by = "AI-generated" if sol.is_ai else f"by {sol.author}"
    rev = as_list(sol.meta.get("reviewed_by"))
    head = [SOL_TITLE.get(sol.status, "Solution"), by] + ([f"checked by {', '.join(rev)}"] if rev else [])
    if label:
        head.insert(0, f"**{label}**")
    out = [f":::::: {{.tfsol status={sol.status}}}", "::: tfhead", " · ".join(head), ":::"]
    if sol.meta.get("summary"):
        out += ["", f"**Answer.** {sol.meta['summary']}", ""]
    out += [figs.fix(sol.body.strip(), sol.path.parent), ""]
    src = as_list(sol.meta.get("sources"))
    if src:
        out += ["::: tfmeta", "Sources: " + "; ".join(src) + ".", ":::"]
    out.append("::::::")
    return "\n".join(out)


def _pick(bank, part, mode):
    sols = bank.solutions_for(part)
    if mode == "none":
        return []
    if mode == "human":
        sols = [s for s in sols if not s.is_ai]
    elif mode == "ai":
        sols = [s for s in sols if s.is_ai]
    if mode in ("best", "human", "ai"):
        good = [s for s in sols if s.status != "disputed"]
        return (good or sols)[:1]
    return sols  # all


def _bank_version(root):
    try:
        rev = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        if rev.returncode != 0:
            return "local files (not a git commit)"
        dirty = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--", "."],
                               capture_output=True, text=True, timeout=10).stdout.strip()
        return f"commit {rev.stdout.strip()}" + (" + uncommitted edits" if dirty else "")
    except (OSError, subprocess.SubprocessError):
        return "local files"


def _toc_entry(part, by, sub):
    marks = f" · {_num(part.marks)} marks" if part.marks is not None else ""
    if by == "topic":
        return ("subsubsection" if sub else "subsection", f"{part.exam.when} · {part.label}{marks}")
    if by == "year":
        course = part.exam.course
        names = [course.topics[t].name for t in part.topics if t in course.topics][:2]
        return ("subsection", f"{part.label}{marks}" + (f" · {'; '.join(names)}" if names else ""))
    return ("subsection", f"{part.exam.when} · {part.label}{marks}")


CONTENTS = {"topic": "Contents: topic by topic", "year": "Contents: exam by exam (year-wise)",
            "faculty": "Contents: by faculty", "none": "Contents"}


def assemble(bank, sel, tmp, by="topic", solutions="best", answers_at_end=False):
    """Return (markdown, stats) for the selection."""
    figs = _Figures(tmp)
    course = sel.course
    body, appendix = [], []
    counts, marks, exams = Counter(), 0, set()
    for head, subs in group(bank, sel, by):
        body.append(f"\n# {head}\n")
        printed = set()
        for sub, parts in subs:
            if sub:
                body.append(f"\n## {sub}\n")
            for p in parts:
                marks += p.marks if isinstance(p.marks, (int, float)) else 0
                exams.add(p.exam)
                body.append(_question_md(bank, p, figs, printed, _toc_entry(p, by, sub)))
                picked = _pick(bank, p, solutions)
                if not picked and solutions != "none":
                    counts["none"] += 1
                    body.append("::: tfmeta\nNo solution yet. Add one: see CONTRIBUTING.md.\n:::")
                for s in picked:
                    counts["ai" if s.is_ai and s.status == "unverified" else s.status] += 1
                    md = _solution_md(s, figs, label=f"{p.exam.when} {p.label}" if answers_at_end else None)
                    (appendix if answers_at_end else body).append(md)
    if appendix:
        body.append("\n# Solutions\n")
        body.extend(appendix)

    first = min(exams, key=lambda e: e.label) if exams else None
    last = max(exams, key=lambda e: e.label) if exams else None
    span = f"{first.when} to {last.when}" if first and first is not last else (first.when if first else "")
    sol_bits = [f"{counts[k]} {name}" for k, name in [
        ("verified", "verified"), ("reviewed", "reviewed"), ("ai", "AI-generated, not yet verified"),
        ("unverified", "not yet verified"), ("disputed", "disputed"), ("none", "missing")] if counts[k]]
    today = dt.date.today()
    meta = {
        "title": f"{course.display_code}: {course.title}",
        "subtitle": "Past term-final questions" + (" with solutions" if solutions != "none" else ""),
        "tf-header": f"{course.display_code} · {sel.describe()}",
        "tf-filters": sel.describe(),
        "tf-contents": CONTENTS.get(by, "Contents"),
        "tf-stats": f"{len(sel.parts)} question parts · {_num(marks)} marks · {len(exams)} exams"
                    + (f" ({span})" if span else ""),
        "tf-solutions": ", ".join(sol_bits) if solutions != "none" else "not included",
        "tf-generated": f"{today.day} {MONTHS[today.month - 1]} {today.year} · {_bank_version(bank.root)}",
    }
    doc = "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n" + "\n\n".join(body) + "\n"
    return doc, {"parts": len(sel.parts), "marks": marks, "exams": len(exams), "solutions": counts}


# ------------------------------------------------------------------ compile

def _run(cmd, cwd, env=None, timeout=180):
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                          timeout=timeout)


def _latex_error(log_text):
    lines = log_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("!") or re.match(r"^\S+\.tex:\d+:", line):
            return "\n".join(lines[i:i + 8])
    return "\n".join(lines[-20:])


def build_pdf(bank, sel, out_pdf, by="topic", solutions="best", answers_at_end=False, keep_tex=False,
              engine="xelatex"):
    pandoc = pandoc_path()
    if not pandoc:
        raise BuildError("Pandoc not found. Install tfsolve with pip (it bundles Pandoc) or install pandoc.")
    have_engine = bool(shutil.which(engine))
    if not have_engine and not keep_tex:
        raise BuildError(f"{engine} not found. Install TeX Live/MacTeX/MiKTeX (tfsolve doctor explains), "
                         f"or add --tex to get a .tex file you can compile on overleaf.com.")
    out_pdf = Path(out_pdf)
    with tempfile.TemporaryDirectory(prefix="tfsolve-") as tmp:
        md, stats = assemble(bank, sel, tmp, by, solutions, answers_at_end)
        (Path(tmp) / "doc.md").write_text(md, encoding="utf-8")
        tpl, lua = Path(tmp) / "template.tex", Path(tmp) / "tfsolve.lua"
        tpl.write_text(asset("template.tex").read_text(encoding="utf-8"), encoding="utf-8")
        lua.write_text(asset("tfsolve.lua").read_text(encoding="utf-8"), encoding="utf-8")
        r = _run([pandoc, "doc.md", "-f", PANDOC_FROM, "-t", "latex", "--template", tpl.name,
                  "--lua-filter", lua.name, "-o", "doc.tex"], tmp)
        if r.returncode != 0:
            raise BuildError("Pandoc failed:\n" + r.stderr.strip())
        if keep_tex:
            out_pdf.parent.mkdir(parents=True, exist_ok=True)
            for name in ("doc.md", "doc.tex"):
                shutil.copyfile(Path(tmp) / name, out_pdf.with_suffix(Path(name).suffix))
            if (Path(tmp) / "fig").is_dir():
                shutil.copytree(Path(tmp) / "fig", out_pdf.parent / "fig", dirs_exist_ok=True)
        if not have_engine:
            stats["pdf"] = False
            return stats
        # Paranoid file access + no shell escape: contributed content must not read or run anything.
        env = dict(os.environ, openin_any="p", openout_any="p")
        cmd = [engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape",
               "doc.tex"]
        for _ in range(3):
            r = _run(cmd, tmp, env)
            log = (Path(tmp) / "doc.log").read_text(encoding="utf-8", errors="replace") if (Path(tmp) / "doc.log").exists() else r.stdout
            if r.returncode != 0:
                raise BuildError(f"{engine} failed. First error:\n{_latex_error(log)}\n"
                                 f"(Re-run with --tex to keep the .tex file for debugging.)")
            if "Rerun to get" not in log and "Label(s) may have changed" not in log and _ > 0:
                break
        out_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(tmp) / "doc.pdf", out_pdf)
        names = {_anchor(p): f"{p.exam.label}/{p.pid} ({p.exam.when} {p.label})" for p in sel.parts}
        stats["layout"] = layout_problems((Path(tmp) / "doc.tex").read_text(encoding="utf-8", errors="replace"), log, names)
    return stats


def layout_problems(tex, log, names, min_pt=12.0):
    """Things that look wrong in the PDF, traced back to the question part they belong to:
    lines that run off the page (overfull boxes) and characters the font cannot show."""
    labels = [(i, m.group(1)) for i, line in enumerate(tex.splitlines(), 1)
              for m in [re.search(r"\\label\{(q-[^}]*)\}", line)] if m]

    def owner(line_no):
        found = None
        for i, anchor in labels:
            if i > line_no:
                break
            found = anchor
        return names.get(found, "cover or contents page") if found else "cover or contents page"

    out = []
    for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)[^\n]*?lines? (\d+)", log):
        if float(m.group(1)) >= min_pt:
            out.append(f"{owner(int(m.group(2)))}: something is {float(m.group(1)):.0f}pt too wide "
                       f"(long display math, a wide table or a long unbroken word)")
    for ch in sorted(set(re.findall(r"Missing character: There is no (\S+)", log))):
        out.append(f"the font has no glyph for '{ch}': use LaTeX math or plain ASCII instead")
    return list(dict.fromkeys(out))


def doctor():
    """Return a list of (ok, message) lines about the local PDF toolchain."""
    lines = []
    p = pandoc_path()
    if p:
        v = _run([p, "--version"], ".").stdout.splitlines()[:1]
        lines.append((True, f"Pandoc: {v[0] if v else p}"))
    else:
        lines.append((False, "Pandoc: not found (pip install pypandoc_binary)"))
    eng = shutil.which("xelatex")
    lines.append((bool(eng), f"XeLaTeX: {eng or 'not found (install TeX Live, MacTeX/BasicTeX or MiKTeX)'}"))
    if shutil.which("kpsewhich"):
        missing = [pkg for pkg in TEX_PACKAGES if not _run(["kpsewhich", f"{pkg}.sty"], ".").stdout.strip()]
        if missing:
            lines.append((False, "Missing LaTeX packages: " + " ".join(missing)))
            lines.append((False, "  fix: tlmgr install " + " ".join(missing)))
        else:
            lines.append((True, "LaTeX packages: all present"))
    return lines
