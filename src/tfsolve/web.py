"""Build the static website: `tfsolve web` writes site/ (plain HTML + CSS + a little JS).

    site/index.html             home: every course in the bank
    site/<COURSE>/index.html    one course: all questions, filtered in the browser
    site/style.css, site/app.js

No server is needed: open site/index.html, or host the folder on GitHub Pages.
"""
from __future__ import annotations

import html
import re
import subprocess
from importlib import resources
from pathlib import Path

from .bank import as_list
from .render import PANDOC_FROM, BuildError, pandoc_path

REPO = "https://github.com/ummehabiba16/tfsolve"
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"
SPLIT = "<!--TFSPLIT-->"
_GANTT = re.compile(r"^```gantt[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)

STATUS_TEXT = {
    "verified": "Verified",
    "reviewed": "Reviewed",
    "unverified": "Not yet verified",
    "disputed": "Disputed",
}

esc = html.escape

# Runs before first paint so a saved light/dark choice doesn't flash the other theme.
# No saved choice: CSS follows the device setting.
THEME_BOOT = ('try{var t=localStorage.getItem("tfsolve-theme");'
              'if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}catch(e){}')
THEME_BUTTON = """<button type="button" class="theme-toggle" id="theme-toggle" title="Switch light/dark mode"
  aria-label="Switch light/dark mode">
  <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
    stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
  <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
    stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4
    1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
</button>"""


# ------------------------------------------------------------ Markdown -> HTML

def _gantt_html(m):
    """```gantt lines like 'P1 0 30' -> a bar of coloured boxes (same input as the PDF filter)."""
    caption, segs = None, []
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("#"):
            caption = line.lstrip("#").strip()
        elif len(bits := line.split()) == 3:
            try:
                segs.append((bits[0], float(bits[1]), float(bits[2])))
            except ValueError:
                pass
    if not segs:
        return m.group(0)
    lo, hi = min(s[1] for s in segs), max(s[2] for s in segs)
    span = (hi - lo) or 1
    pct = lambda x: f"{(x - lo) * 100 / span:.3f}%"  # noqa: E731
    num = lambda x: f"{x:g}"  # noqa: E731
    bars = "".join(f'<div class="seg" style="left:{pct(a)};width:{(b - a) * 100 / span:.3f}%">{esc(lbl)}</div>'
                   for lbl, a, b in segs)
    ticks = sorted({a for _, a, _ in segs} | {hi})
    marks = "".join(f'<span style="left:{pct(t)}">{num(t)}</span>' for t in ticks)
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    return (f'```{{=html}}\n<figure class="gantt"><div class="bars">{bars}</div>'
            f'<div class="ticks">{marks}</div>{cap}</figure>\n```')


def to_html(chunks):
    """Convert many Markdown snippets with one Pandoc run; returns one HTML string per snippet."""
    if not chunks:
        return []
    pandoc = pandoc_path()
    if not pandoc:
        raise BuildError("Pandoc not found. Install the package with pip so pypandoc_binary comes with it.")
    sep = f"\n\n```{{=html}}\n{SPLIT}\n```\n\n"
    text = sep.join(_GANTT.sub(_gantt_html, c) for c in chunks)
    run = subprocess.run([pandoc, "-f", PANDOC_FROM, "-t", "html5", "--katex", "--wrap=none"],
                         input=text, capture_output=True, text=True, encoding="utf-8")
    if run.returncode != 0:
        raise BuildError(f"pandoc failed: {run.stderr.strip()}")
    out = [s.strip() for s in run.stdout.split(SPLIT)]
    if len(out) != len(chunks):  # a snippet swallowed a separator (e.g. an unclosed ``` fence): go one by one
        return [to_html([c])[0] for c in chunks] if len(chunks) > 1 else ["".join(out)]
    return out


# ------------------------------------------------------------------- pages

def _page(title, body, root, crumbs=()):
    trail = "".join(f' <span>›</span> <a href="{href}">{esc(name)}</a>' if href else f" <span>›</span> {esc(name)}"
                    for name, href in crumbs)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css">
<link rel="stylesheet" href="{root}style.css">
<script>{THEME_BOOT}</script>
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{root}index.html">tfsolve</a>
    <nav><a href="{root}index.html">Courses</a><a href="{REPO}">GitHub</a>{THEME_BUTTON}</nav>
  </div>
</header>
<div class="wrap crumbs"><a href="{root}index.html">Home</a>{trail}</div>
<main class="wrap">
{body}
</main>
<footer class="wrap">BUET term-final questions and solutions, kept on
<a href="{REPO}">GitHub</a>. Spotted a mistake? Use the “Edit” link on any question.</footer>
<script defer src="{KATEX}/katex.min.js"></script>
<script defer src="{root}app.js"></script>
</body>
</html>
"""


def _github(path, repo_root, new=False):
    rel = Path(path).resolve().relative_to(repo_root).as_posix()
    return f"{REPO}/{'new' if new else 'blob'}/main/{rel}"


def _home(bank):
    rows = []
    for dept in bank.depts.values():
        cards = []
        for c in (c for c in bank.courses.values() if c.dept == dept.code):
            parts = [p for e in c.exams for p in e.parts]
            solved = sum(1 for p in parts if bank.solutions.get(p.uid))
            cards.append(f"""<a class="card course" href="{esc(c.code)}/index.html">
  <span class="code">{esc(c.display_code)}</span>
  <span class="name">{esc(c.title)}</span>
  <span class="stats">{len(c.exams)} papers · {len(parts)} questions · {solved} with solutions</span>
</a>""")
        if cards:
            rows.append(f"<h2>{esc(dept.meta.get('name', dept.code))}</h2>\n<div class=\"grid\">{''.join(cards)}</div>")
    intro = """<section class="hero">
  <h1>Past term-final questions, with solutions</h1>
  <p>Pick a course. Then filter by topic, teacher or exam, and print what you need.</p>
</section>"""
    return _page("tfsolve: BUET term-final questions", intro + "\n".join(rows), "")


def _course(bank, course, repo_root):
    current = bank.current_faculty(course)
    exams = sorted(course.exams, key=lambda e: e.label, reverse=True)

    # Markdown for every question body, shared setup and solution, converted in one go.
    chunks, items = [], []
    for exam in exams:
        for part in exam.parts:
            stems = bank.stems_for(part)
            sols = bank.solutions_for(part)
            items.append((part, stems, sols))
            chunks += [s.body for s in stems] + [part.body]
            for s in sols:
                summary = f"**Answer.** {s.meta['summary']}\n\n" if s.meta.get("summary") else ""
                chunks.append(summary + s.body)
    converted = iter(to_html(chunks))

    used_topics, faculty, groups = set(), set(), []
    for exam in exams:
        cards = []
        for part, stems, sols in (it for it in items if it[0].exam is exam):
            stem_html = [next(converted) for _ in stems]
            body_html = next(converted)
            who, how = bank.setters(part)
            faculty.update(who)
            tids = [t for t in part.topics if t in course.topics]
            tags = set()
            for t in tids:
                tags.add(t)
                tags.update(course.ancestors(t))
            used_topics.update(tags)

            facts = [f"{part.marks:g} marks" if isinstance(part.marks, (int, float)) else None,
                     f"Section {part.section}" if part.section else None,
                     (("Set by " if how == "set" else "Taught by ") + ", ".join(who)) if who else None]
            chips = "".join(f'<button type="button" class="chip" data-topic="{esc(t)}">{esc(course.topics[t].name)}</button>'
                            for t in tids)
            setup = "".join(f'<div class="stem"><div class="label">Shared setup</div>{h}</div>' for h in stem_html)
            note = f'<p class="note">Transcription note: {esc(str(part.meta["note"]))}</p>' if part.meta.get("note") else ""

            sol_html = []
            for s in sols:
                by = "AI" if s.is_ai else s.author
                src = as_list(s.meta.get("sources"))
                sources = f'<p class="note">Sources: {esc("; ".join(src))}</p>' if src else ""
                sol_html.append(f"""<details class="solution">
  <summary>Solution by {esc(by)} <span class="badge {esc(s.status)}">{esc(STATUS_TEXT.get(s.status, s.status))}</span></summary>
  <div class="body">{next(converted)}{sources}</div>
</details>""")
            if not sols:
                sol_html.append('<p class="note">No solution yet.</p>')
            add = _github(part.path.parent / "solutions" / part.pid, repo_root, new=True)

            cards.append(f"""<article class="q" id="{esc(exam.label)}-{esc(part.pid)}" data-exam="{esc(exam.label)}"
  data-topics="{esc(' '.join(sorted(tags)))}" data-faculty="{esc(' '.join(who))}" data-solved="{'yes' if sols else 'no'}">
  <div class="qhead"><span class="qlabel">{esc(part.label)}</span>
    <span class="facts">{' · '.join(esc(f) for f in facts if f)}</span></div>
  <div class="chips">{chips}</div>
  {setup}<div class="body">{body_html}</div>{note}
  {''.join(sol_html)}
  <div class="links"><a href="{_github(part.path, repo_root)}">Edit question</a>
    <a href="{add}">Add a solution</a></div>
</article>""")
        if cards:
            rules = " ".join(f"Section {s.name}: {s.rule}" for s in exam.sections.values() if s.rule)
            groups.append(f"""<section class="exam" data-exam="{esc(exam.label)}">
  <h2>{esc(exam.title)}</h2>{f'<p class="note">{esc(rules)}</p>' if rules else ''}
  {''.join(cards)}
</section>""")

    def opt(value, text, extra=""):
        return f'<option value="{esc(value)}"{extra}>{esc(text)}</option>'

    topic_opts = "".join(opt(t.id, " " * len(course.ancestors(t.id)) + t.name)
                         for t in course.topics.values() if t.id in used_topics)
    fac_opts = (opt("current", f"Teaching now ({', '.join(current)})", f' data-list="{esc(" ".join(current))}"')
                if current else "") + "".join(opt(f, f) for f in sorted(faculty))
    exam_opts = "".join(opt(e.label, e.title) for e in exams if e.parts)

    body = f"""<h1>{esc(course.display_code)}: {esc(course.title)}</h1>
<div class="layout">
<aside class="filters">
  <label>Search<input type="search" id="f-text" placeholder="e.g. deadlock, Gantt"></label>
  <label>Topic<select id="f-topic"><option value="">All topics</option>{topic_opts}</select></label>
  <label>Teacher<select id="f-faculty"><option value="">All teachers</option>{fac_opts}</select></label>
  <label>Exam<select id="f-exam"><option value="">All exams</option>{exam_opts}</select></label>
  <label class="check"><input type="checkbox" id="f-solved"> Only questions with solutions</label>
  <label class="check"><input type="checkbox" id="f-open"> Show all solutions</label>
  <div class="buttons">
    <button type="button" id="f-clear" class="ghost">Clear filters</button>
    <button type="button" id="f-print">Print / Save PDF</button>
  </div>
  <p class="count" id="f-count"></p>
</aside>
<div class="questions">
{''.join(groups)}
<p class="empty" id="f-empty" hidden>No questions match these filters.</p>
</div>
</div>"""
    return _page(f"{course.display_code} {course.title} · tfsolve", body, "../", [(course.display_code, None)])


def build_site(bank, out_dir="site"):
    """Write the whole site to out_dir. Returns the number of pages written."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    repo_root = bank.root.resolve().parent
    for name in ("style.css", "app.js"):
        (out / name).write_text((resources.files("tfsolve") / "assets" / "web" / name).read_text(encoding="utf-8"),
                                encoding="utf-8")
    (out / "index.html").write_text(_home(bank), encoding="utf-8")
    n = 1
    for course in bank.courses.values():
        (out / course.code).mkdir(exist_ok=True)
        (out / course.code / "index.html").write_text(_course(bank, course, repo_root), encoding="utf-8")
        n += 1
    return n
