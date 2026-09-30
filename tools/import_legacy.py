#!/usr/bin/env python3
"""One-off import of the pre-tfsolve CSE313 material into bank/CSE/CSE313/.

    python tools/import_legacy.py           # write files that do not exist yet
    python tools/import_legacy.py --force   # overwrite existing files (loses hand edits!)

Sources, left unchanged:
    tfsolve-questions/          RRR, Section A: JSON exams + typed-block solutions (53 parts)
    cse313_mem_fs_solved.tex    KRV, Section B: LaTeX questions + solutions (2021-22 to 2023-24)

Imported solutions are marked author: ai, status: unverified, because they were written with
an AI assistant and have not been checked by a second person yet.

DONE on 2026-09-30. The imported files were then hand-edited (2021-22 Q7(a)/Q8(a) split into
stems and sub-parts, several solutions corrected; see each file's `changes:`). Do not re-run
with --force: it would overwrite those edits.
"""
import argparse
import json
import math
import re
import sys
from datetime import date
from pathlib import Path

import pypandoc
import yaml

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "tfsolve-questions"
TEX = ROOT / "cse313_mem_fs_solved.tex"
COURSE = ROOT / "bank" / "CSE" / "CSE313"
EXAM_FOLDER = {"2019-20": "2022-04", "2021-22": "2023-10", "2022-23": "2025-01", "2023-24": "2025-09"}
TOPIC_ID = {"process_thread": "process-thread"}

# KRV question key -> topics (first = where it is filed). Keys come from the .tex labels.
KRV_TOPICS = {
    "2122-6b": ["memory-api"], "2122-7b": ["segmentation"], "2324-8a": ["free-space"],
    "2223-6c": ["pte"], "2223-6b": ["tlb"], "2324-5a": ["multilevel-page-table"],
    "2223-5a": ["multilevel-page-table"], "2324-5c": ["page-replacement"], "2324-6a": ["page-replacement"],
    "2223-5c": ["page-replacement"], "2223-6d": ["thrashing"], "2122-5a": ["page-replacement", "tlb"],
    "2122-8b": ["thrashing"], "2324-7a": ["io-devices"], "2223-7c": ["io-devices"], "2223-7d": ["io-devices"],
    "2122-6a": ["io-devices", "files-directories"], "2324-6b": ["raid"], "2223-6a": ["raid"],
    "2122-8aiv": ["raid", "lfs"], "2223-6e": ["files-directories"], "2223-7a": ["vsfs"], "2223-7b": ["vsfs"],
    "2324-8b": ["ffs"], "2223-8a": ["ffs"], "2122-5b": ["ffs", "lfs"], "2122-7aii": ["ffs"],
    "2324-7b": ["journaling"], "2324-7c": ["journaling"], "2122-7ai": ["journaling"], "2324-5b": ["lfs"],
    "2324-6c": ["lfs"], "2324-8c": ["lfs"], "2223-5b": ["lfs"], "2223-8b": ["lfs"], "2223-8d": ["lfs"],
    "2122-8aiii": ["lfs"], "2223-8c": ["distributed"],
}
# Keys whose sub-parts were split in the .tex; they need a hand-made stem (q7a.md / q8a.md).
KRV_PID = {"2122-7ai": "q7a-i", "2122-7aii": "q7a-ii", "2122-8aiii": "q8a-i", "2122-8aiv": "q8a-iv"}


# ------------------------------------------------------------------ Markdown helpers

def split_math(s):
    """Yield (is_math, text) for a string using the legacy '@m{...}' inline-math marker."""
    i, n = 0, len(s)
    while i < n:
        j = s.find("@m{", i)
        if j < 0:
            yield False, s[i:]
            return
        if j > i:
            yield False, s[i:j]
        k, depth = j + 3, 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(s[k], 0)
            k += 1
        yield True, s[j + 3:k - 1]
        i = k


def esc(s):
    s = s.replace("\\", "\\\\")
    s = re.sub(r"([*`$|~])", r"\\\1", s)
    s = re.sub(r"<(?=[A-Za-z/!?])", r"\\<", s)
    s = re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", r"\\_", s)
    return re.sub(r"(?m)^([#>])", r"\\\1", s)


def md(s):
    out = []
    for is_math, t in split_math(str(s)):
        out.append(f"${t.strip()}$" if is_math else esc(t))
    return "".join(out)


def md_table(head, rows, cap=None):
    lines = ["| " + " | ".join(md(h) for h in head) + " |",
             "|" + "|".join([":--"] + [":-:"] * (len(head) - 1)) + "|"]
    lines += ["| " + " | ".join(md(c) for c in r) + " |" for r in rows]
    if cap:
        lines += ["", f"*{md(cap)}*"]
    return "\n".join(lines)


def blocks_md(blocks):
    out = []
    for b in blocks:
        t = b["t"]
        if t == "p":
            out.append(md(b["x"]))
        elif t == "steps":
            out.append("\n".join(f"{i}. {md(x)}" for i, x in enumerate(b["x"], 1)))
        elif t == "ul":
            out.append("\n".join(f"- {md(x)}" for x in b["x"]))
        elif t == "kv":
            out.append("\n".join(f"- **{md(k)}:** {md(v)}" for k, v in b["x"]))
        elif t == "tbl":
            out.append(md_table(b["head"], b["rows"], b.get("cap")))
        elif t == "gantt":
            lines = [f"# {b['cap']}"] if b.get("cap") else []
            lines += [f"{lbl} {a} {z}" for lbl, a, z in b["seg"]]
            out.append("```gantt\n" + "\n".join(lines) + "\n```")
        elif t == "code":
            out.append(f"```{b.get('lang', 'text')}\n{b['x'].rstrip()}\n```")
        elif t == "eq":
            out.append(f"$$\n{b['x'].strip()}\n$$")
        else:
            raise ValueError(f"unknown block type {t}")
    return "\n\n".join(out)


def dump(meta):
    """Block style at the top level, compact flow style for leaf lists and maps."""
    return "".join(yaml.safe_dump({k: v}, sort_keys=False, allow_unicode=True, width=4096,
                                  default_flow_style=None if isinstance(v, (dict, list)) and v else False)
                   for k, v in meta.items())


def write(path, meta, body, force):
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    text = (f"---\n{dump(meta)}---\n" if meta is not None else "") + body.strip() + "\n"
    path.write_text(text, encoding="utf-8")
    return True


# ------------------------------------------------------------------ RRR (JSON)

def params_md(p):
    """Render the machine-readable inputs as the tables printed on the paper."""
    t = p["type"]
    if t == "scheduling_workload":
        pr = "Priority" + (" (lowest number = highest)" if p.get("priority_convention") == "lowest_number_highest" else "")
        u = p["time_unit"]
        return md_table(["Process", pr, f"Duration ({u})", f"Arrival ({u})"],
                        [[x["pid"], x["priority"], x["burst"], x["arrival"]] for x in p["processes"]])
    if t in ("bankers_safety", "bankers_safety_single"):
        names = p["resource_names"]
        out = []
        for title, key in (("Current allocation", "allocation"), ("Maximum requirement", "max")):
            out.append(f"**{title}**\n\n" + md_table(["Process", *names], [[pid, *row] for pid, row in p[key].items()]))
        bits = []
        if p.get("total"):
            bits.append("Total: " + ", ".join(f"{n} = {v}" for n, v in zip(names, p["total"])))
        if p.get("available") and not p.get("available_derived"):
            bits.append("Available: (" + ", ".join(str(v) for v in p["available"]) + ")")
        if bits:
            out.append("; ".join(bits) + ".")
        return "\n\n".join(out)
    return ""


def import_rrr(force):
    written = 0
    solutions = {}
    topics = json.loads((LEGACY / "data" / "topics.json").read_text(encoding="utf-8"))["topics"]
    sub_parent = {s["key"]: t["key"] for t in topics for s in t["subtopics"]}
    for f in sorted((LEGACY / "data" / "solutions").glob("*.json")):
        solutions.update(json.loads(f.read_text(encoding="utf-8")))
    for f in sorted((LEGACY / "data" / "exams").glob("*.json")):
        e = json.loads(f.read_text(encoding="utf-8"))
        folder = COURSE / EXAM_FOLDER[e["exam"]]
        rule = e["section_A_rule"].replace("4 questions. ", "").replace("MANDATORY", "compulsory")
        notes = [n for n in e.get("notes", []) if not n.startswith("Section B")]
        if e["exam"] == "2019-20":
            notes.append("Section B (Q5-Q8) has not been transcribed yet.")
        paper = {
            "schema": 1,
            "course": "CSE313",
            "kind": "term-final",
            "exam_date": date.fromisoformat(e["exam_date"]),
            "session": e["exam"],
            "level_term": e["level_term"].replace("-", "").replace("/", ""),
            "students_dept": "CSE",
            "full_marks": e["full_marks"],
            "duration": f"{e['duration_hours']}h",
            "sections": {
                "A": {"questions": [1, 2, 3, 4], "answer_any": 2 if "TWO" in rule else 3, "rule": rule},
                "B": {"questions": [5, 6, 7, 8]},
            },
            "source": {"file": e["source_pdf"], "pages": f"{e['source_pages'][0]}-{e['source_pages'][1]}"},
            "notes": notes,
            "transcription": {"by": [], "checked_by": []},
        }
        if not notes:
            del paper["notes"]
        written += write(folder / "paper.yaml", None, dump(paper), force)

        for q in e["questions"]:
            pid = f"q{q['q_no']}{q['part']}"
            topics = list(q["subtopics"])
            for sec in q.get("secondary_topics", []):
                if not any(sub_parent.get(s) == sec for s in topics):
                    topics.append(TOPIC_ID.get(sec, sec))
            meta = {"marks": q["marks"], "topics": topics, "kind": q["kind"]}
            if q.get("mandatory"):
                meta["mandatory"] = True
            meta["source"] = {"page": q["source_page"]}
            if q.get("transcription_notes"):
                meta["note"] = q["transcription_notes"]
            if q.get("params"):
                meta["params"] = q["params"]
            body = [md(q["text"])]
            body += [md(s) for s in q.get("sub_questions", [])]
            if q.get("params") and (tbl := params_md(q["params"])):
                body.append(tbl)
            if q.get("figure"):
                fig = q["figure"]
                code = (LEGACY / "data" / fig["file"]).read_text(encoding="utf-8").rstrip()
                body.append(f"*{md(fig['caption'])}*\n\n```{fig.get('language', 'text')}\n{code}\n```")
            written += write(folder / f"{pid}.md", meta, "\n\n".join(body), force)

            sid = f"{e['exam']}-Q{q['q_no']}{q['part']}"
            s = solutions.get(sid)
            if s:
                smeta = {"author": "ai", "via": "chat", "status": "unverified", "summary": md(s["summary"]),
                         "sources": s.get("sources", []),
                         "imported_from": f"tfsolve-questions/data/solutions/{e['exam']}.json"}
                sbody = blocks_md(s["answer"])
                if s.get("explanation"):
                    sbody += "\n\n**Explanation.**\n\n" + blocks_md(s["explanation"])
                written += write(folder / "solutions" / pid / "ai.md", smeta, sbody, force)
    return written


# ------------------------------------------------------------------ KRV (LaTeX)

def read_group(s, pos):
    """Return (content, end) of the brace group starting at s[pos] (after optional spaces)."""
    while s[pos].isspace():
        pos += 1
    assert s[pos] == "{", s[pos:pos + 40]
    depth, j = 0, pos
    while True:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[pos + 1:j], j + 1
        j += 1


def parse_tex(tex):
    items, pos = [], tex.index("\\begin{document}")
    pat = re.compile(r"\\question\{")
    while m := pat.search(tex, pos):
        p = m.end() - 1
        args = []
        for _ in range(4):
            a, p = read_group(tex, p)
            args.append(a)
        s = tex.index("\\solution{", p)
        sbody, pos = read_group(tex, s + len("\\solution"))
        items.append((args[0], args[2], args[3], sbody))
    return items


def clean_code(s):
    s = re.sub(r"\\hspace\*\{([\d.]+)em\}", lambda m: " " * (4 * math.ceil(float(m.group(1)) / 1.5)), s)
    s = re.sub(r"\\\\\s*\n", "\n", s).replace("\\\\", "\n")
    for a, b in [("\\_", "_"), ("\\{", "{"), ("\\}", "}"), ("\\&", "&"), ("\\%", "%"), ("\\#", "#"),
                 ("\\$", "$"), ("\\ ", " "), ("\\small", ""), ("\\ttfamily", "")]:
        s = s.replace(a, b)
    lines = [ln.rstrip() for ln in s.strip("\n").splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    return "```text\n" + "\n".join(lines) + "\n```"


def tex_to_md(body):
    codes = []

    def keep_code(m):
        codes.append(clean_code(m.group(1)))
        return f"\n\nTFCODE{len(codes) - 1}\n\n"

    s = re.sub(r"\\begin\{quote\}\s*\\ttfamily(.*?)\\end\{quote\}", keep_code, body, flags=re.S)
    s = (s.replace("[label=\\roman*.]", "[i.]").replace("[label=\\Roman*.]", "[I.]")
          .replace("[label=(\\alph*)]", "[(a)]"))
    s = re.sub(r"\\begin\{center\}|\\end\{center\}|\\hfill\b|\\small\b|\\footnotesize\b", "", s)
    s = re.sub(r"\\centerline\{", r"\\par{", s)
    s = re.sub(r"\\shortstack\{([^{}]*)\}", lambda m: m.group(1).replace("\\\\", " "), s)
    out = pypandoc.convert_text(s, "markdown-simple_tables-multiline_tables-grid_tables", format="latex",
                                extra_args=["--wrap=none"])
    for i, c in enumerate(codes):
        out = out.replace(f"TFCODE{i}", c)
    # Display math on its own lines, so GitHub renders it as a block.
    out = re.sub(r"[ \t]*(\$\$.+?\$\$)[ \t]*", r"\n\n\1\n\n", out, flags=re.S)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def import_krv(force):
    written = 0
    for key, marks, qtex, stex in parse_tex(TEX.read_text(encoding="utf-8")):
        m = re.match(r"(\d{2})(\d{2})-(\d)([a-z])$", key)
        session = f"20{key[:2]}-{key[2:4]}"
        pid = KRV_PID.get(key) or f"q{m.group(3)}{m.group(4)}"
        folder = COURSE / EXAM_FOLDER[session]
        meta = {"marks": int(marks), "topics": KRV_TOPICS[key]}
        written += write(folder / f"{pid}.md", meta, tex_to_md(qtex), force)
        smeta = {"author": "ai", "via": "chat", "status": "unverified",
                 "imported_from": "cse313_mem_fs_solved.tex"}
        written += write(folder / "solutions" / pid / "ai.md", smeta, tex_to_md(stex), force)
    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    ap.add_argument("--only", choices=["rrr", "krv"])
    a = ap.parse_args()
    n = 0
    if a.only in (None, "rrr"):
        n += import_rrr(a.force)
    if a.only in (None, "krv"):
        n += import_krv(a.force)
    print(f"wrote {n} files under {COURSE.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
