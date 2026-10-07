"""Build the static website: `tfsolve web` writes site/ (plain HTML + CSS + a little JS).

    site/index.html             home: every course in the bank
    site/about.html             what the project is, plus page-view and PDF-print counts
    site/help.html              how to use the site and the tfsolve command
    site/<COURSE>/index.html    one course: filters and an index; questions are fetched as the reader asks
    site/<COURSE>/q/<id>.html   one question with its solutions;  search.json: text for the search box
    site/style.css, site/app.js

Host the folder on GitHub Pages, or try it locally with `python3 -m http.server -d site`. (Opening index.html
straight from disk does not work: browsers refuse the page's requests for the question files.)
"""
from __future__ import annotations

import functools
import hashlib
import html
import json
import re
import shutil
import subprocess
from importlib import resources
from pathlib import Path

from .bank import as_list
from .render import PANDOC_FROM, BuildError, _Figures, pandoc_path

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
    out = [s.strip().replace("<img ", '<img loading="lazy" decoding="async" ') for s in run.stdout.split(SPLIT)]
    if len(out) != len(chunks):  # a snippet swallowed a separator (e.g. an unclosed ``` fence): go one by one
        return [to_html([c])[0] for c in chunks] if len(chunks) > 1 else ["".join(out)]
    return out


# ------------------------------------------------------------------- pages

@functools.lru_cache(maxsize=None)
def _v(name):
    data = (resources.files("tfsolve") / "assets" / "web" / name).read_bytes()
    return hashlib.sha1(data).hexdigest()[:8]


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
<link rel="stylesheet" href="{root}style.css?v={_v("style.css")}">
<script>{THEME_BOOT}</script>
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{root}index.html">tfsolve</a>
    <nav><a href="{root}index.html">Courses</a><a href="{root}help.html">Help</a><a href="{root}about.html">About</a><a href="{REPO}">GitHub</a>{THEME_BUTTON}</nav>
  </div>
</header>
<div class="wrap crumbs"><a href="{root}index.html">Home</a>{trail}</div>
<main class="wrap">
{body}
</main>
<footer class="wrap">BUET term-final questions and solutions, kept on
<a href="{REPO}">GitHub</a>. Spotted a mistake? Use the “Edit” link on any question.</footer>
<script defer src="{KATEX}/katex.min.js"></script>
<script defer src="{root}app.js?v={_v("app.js")}"></script>
</body>
</html>
"""


def _about():
    body = f"""<section class="hero">
  <h1>About tfsolve</h1>
  <p>A community bank of BUET term-final questions and solutions.</p>
</section>
<div class="about">
<h2>What it is</h2>
<p>Past term-final questions, kept as plain text in a Git repository, with worked solutions. You can filter them by
course, topic, teacher and exam. Every solution carries a badge: <b>verified</b>, <b>reviewed</b>,
<b>not yet verified</b> (every AI solution starts here) or <b>disputed</b>.</p>
<h2>Using it</h2>
<ul>
  <li><b>On this site:</b> pick a course, pick a topic or set the filters, read the questions, then press <i>Print / Save PDF</i>.</li>
  <li><b>On your computer:</b> <code>pip install tfsolve</code>, then for example
  <code>tfsolve -c CSE313 -topicwise</code> or <code>-yearwise</code> builds a PDF of the whole course, and
  <code>-f ABC</code> keeps only faculty ABC's questions. See <a href="help.html">Help</a>.
  See the <a href="{REPO}#readme">README</a> for all options.</li>
</ul>
<h2>Contributing</h2>
<p>Add a paper, write a solution or review one by opening a pull request on
<a href="{REPO}">GitHub</a>. Spotted a mistake? Use the “Edit” link on any question.</p>
<h2>Credits and licence</h2>
<p>Created and maintained by <a href="https://github.com/ummehabiba16">ummehabiba16</a>. The code was written with
<a href="https://www.anthropic.com/claude">Claude</a> (Anthropic) through Claude Code. Code: MIT. Transcriptions, tags and
solutions: CC BY-NC-SA 4.0. The original question papers belong to BUET and are reproduced for non-commercial study.</p>
<h2>Site usage</h2>
<div class="counts">
  <div class="card count"><span class="num" id="stat-views">…</span><span class="label">page views</span></div>
  <div class="card count"><span class="num" id="stat-prints">…</span><span class="label">PDF prints</span></div>
</div>
<p class="muted" id="stat-note">Counts update every few hours.</p>
<p class="muted">We count page views and Print / Save PDF clicks only: no cookies, no personal data. Browsers that
send Do Not Track are not counted.</p>
</div>"""
    return _page("About · tfsolve", body, "", [("About", None)])


def _help():
    body = f"""<section class="hero">
  <h1>Help</h1>
  <p>How to find questions, arrange them and print a PDF.</p>
</section>
<div class="about">
<h2>On a course page</h2>
<ol>
  <li><b>Arrange</b> (top of the left panel):
    <ul>
      <li><b>By topic</b>: every topic in turn, all its past questions together.</li>
      <li><b>By year</b>: exam by exam, newest first.</li>
    </ul>
  </li>
  <li><b>Choose what to see</b> with the filters on the left: <b>Teachers</b> (by initials, e.g. ABC), <b>Exams</b> and
  <b>Topics</b> each open a checklist where you can tick several. For example, two teachers, three exams and ten
  topics at once. A question is shown when it matches <i>one of</i> the teachers, <i>and one of</i> the exams,
  <i>and one of</i> the topics you ticked; a filter with nothing ticked allows everything. Ticking a topic includes its
  sub-topics. <b>Search</b> and <i>Only questions with solutions</i> narrow it further. The button shows how many
  questions match; press <b>Show questions</b> to see them. If you change a filter later, the page tells you and
  waits for <b>Update results</b>.</li>
  <li><b>Read</b>: the heading says what you are looking at. Questions come ten to a page; use the page numbers
  above or below, or <b>Show all</b> to put every selected question on one page (long lists load in parts). The <b>Jump to a topic</b> box (or <b>Jump to a year</b>, when arranged by year) lists the topics (or years)
  of the questions on screen, with counts. Tap one to go to its first question, on whichever page it is; your
  filters are not changed. Click a topic chip on a question to see just that topic, or a chip under the heading to
  remove that one choice.</li>
  <li><b>Print / Save PDF</b> prints <i>every</i> question matching the filters (not just the page on screen),
  contents included, with all solutions opened. Tick <i>Questions only when printing</i> to leave the solutions out.
  It may take a few seconds to gather them all.</li>
</ol>
<p>Search looks through the questions, their topics and each solution's short answer. The address bar keeps what
you are looking at, so you can bookmark or share it.</p>
<h2>Solution badges</h2>
<ul>
  <li><b>Verified</b>: checked by two people, or against a teacher's solution.</li>
  <li><b>Reviewed</b>: checked by one person other than the author.</li>
  <li><b>Not yet verified</b>: nobody has checked it yet; every AI solution starts here.</li>
  <li><b>Disputed</b>: someone reported an error.</li>
</ul>
<h2>On your computer</h2>
<p><code>pip install tfsolve</code>, then <code>tfsolve update</code> once to download the questions. Then (ABC = a
teacher's initials):</p>
<ul>
  <li><code>tfsolve -c CSE313 -topicwise</code>: the whole course as a PDF, topic by topic, with a table of contents
  that lists every question under its topic.</li>
  <li><code>tfsolve -c CSE313 -yearwise</code>: the same, exam by exam.</li>
  <li><code>-f ABC</code>: only ABC's questions. <code>tfsolve list faculty -c CSE313</code> shows the initials.</li>
  <li><code>-y 2025</code>, <code>-y 2021..2025</code> or <code>-y 2025-09</code>: chosen years.
  <code>tfsolve list years -c CSE313</code> shows which exist.</li>
  <li><code>tfsolve help</code> explains everything else.</li>
</ul>
<p>PDFs need LaTeX (MiKTeX on Windows, MacTeX on macOS, TeX Live on Linux). Without it, add <code>--tex</code> and
compile the file on <a href="https://www.overleaf.com">Overleaf</a>. Details are in the
<a href="{REPO}#readme">README</a>.</p>
</div>"""
    return _page("Help · tfsolve", body, "", [("Help", None)])


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


_IMG_TAG = re.compile(r'<img ([^>]*?)src="(fig/[^"]+)"([^>]*)>')
_NOISE = re.compile(r"[$`*#|\\{}\[\]()_>~]+")


class _WebFigures(_Figures):
    """Like the PDF figures, plus a lossless WebP copy of each PNG (same pixels, about half the download) and the
    image size, so the page can reserve the space and nothing jumps while figures load. Browsers without
    WebP simply use the PNG."""

    def __init__(self, tmp):
        super().__init__(tmp)
        self.sizes = {}  # "fig/<name>.png" -> (width, height, has a WebP copy)
        self._webp = {}  # source file -> its converted copy, so a figure used by many questions is converted once

    def _copy(self, src, dst):
        super()._copy(src, dst)
        try:
            from PIL import Image
            with Image.open(src) as im:
                size = im.size
                webp = dst.with_suffix(".webp")
                if src.suffix.lower() != ".png":
                    ok = False
                elif src in self._webp:
                    ok = self._webp[src] is not None
                    if ok:
                        shutil.copyfile(self._webp[src], webp)
                else:
                    im.save(webp, "WEBP", lossless=True, quality=100, method=4)
                    ok = webp.stat().st_size < src.stat().st_size * 0.9  # keep it only when it really is smaller
                    if not ok:
                        webp.unlink()
                    self._webp[src] = webp if ok else None
            self.sizes[f"fig/{dst.name}"] = (*size, ok)
        except Exception:  # Pillow missing or an unreadable image: the plain copy is still there
            pass

    def tag(self, html_text):
        """Give every <img> its width and height (and the WebP source) from what _copy recorded."""
        def repl(m):
            before, src, after = m.groups()
            size = self.sizes.get(src)
            if not size or "width=" in before + after:
                return m.group(0)
            w, h, webp = size
            img = f'<img {before}src="{src}"{after.rstrip(" /")} width="{w}" height="{h}">'
            if webp:
                return f'<picture><source srcset="{src[:-4]}.webp" type="image/webp">{img}</picture>'
            return img
        return _IMG_TAG.sub(repl, html_text)


def _plain(md):
    """Lower-case plain text of some Markdown, for the search box."""
    return " ".join(_NOISE.sub(" ", md).lower().split())


def _course(bank, course, repo_root, out_dir):
    """The course page is a small shell: filters plus an index of every question. Each question (with its
    solutions) is its own file under q/, fetched by the browser only when it is about to be shown."""
    for sub in ("fig", "q"):
        shutil.rmtree(out_dir / sub, ignore_errors=True)
    (out_dir / "q").mkdir(parents=True, exist_ok=True)
    figs = _WebFigures(out_dir)  # copies images into <out_dir>/fig and rewrites links (page sits in out_dir)
    exams = sorted(course.exams, key=lambda e: e.label, reverse=True)

    # Markdown for every question body, shared setup and solution, converted in one go.
    chunks, items = [], []
    for exam in exams:
        for part in exam.parts:
            stems = bank.stems_for(part)
            sols = bank.solutions_for(part)
            items.append((part, stems, sols))
            chunks += [figs.fix(s.body, s.path.parent) for s in stems] + [figs.fix(part.body, part.path.parent)]
            for s in sols:
                summary = f"**Answer.** {s.meta['summary']}\n\n" if s.meta.get("summary") else ""
                chunks.append(summary + figs.fix(s.body, s.path.parent))
    converted = iter(figs.tag(h) for h in to_html(chunks))

    used_topics, faculty, rows, texts, digest = set(), set(), [], [], hashlib.sha1()
    for part, stems, sols in items:
        exam = part.exam
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
            sol_html.append('<p class="note nosol">No solution yet.</p>')
        add = _github(part.path.parent / "solutions" / part.pid, repo_root, new=True)

        qid = f"{exam.label}-{part.pid}"
        card = f"""<article class="q" id="{esc(qid)}">
  <div class="qhead"><span class="qexam">{esc(exam.title)}</span><span class="qlabel">{esc(part.label)}</span>
    <span class="facts">{' · '.join(esc(f) for f in facts if f)}</span></div>
  <div class="chips">{chips}</div>
  {setup}<div class="body">{body_html}</div>{note}
  {''.join(sol_html)}
  <div class="links"><a href="{_github(part.path, repo_root)}">Edit question</a>
    <a href="{add}">Add a solution</a></div>
</article>"""
        (out_dir / "q" / f"{qid}.html").write_text(card, encoding="utf-8")
        digest.update(card.encode("utf-8"))
        rows.append([qid, exam.label, tids[0] if tids else "", sorted(tags), who, 1 if sols else 0])

        # Search covers the question, its topics and each solution's short answer; full solutions would make the
        # file several times bigger for little gain.
        words = [exam.title, part.label, *(course.topics[t].name for t in tids),
                 *(s.body for s in stems), part.body, *(str(s.meta.get("summary") or "") for s in sols)]
        texts.append(_plain(" ".join(words)))

    version = digest.hexdigest()[:8]
    (out_dir / "search.json").write_text(json.dumps({"v": version, "t": texts}, separators=(",", ":")),
                                         encoding="utf-8")

    def multi(fid, label, all_text, noun, options, find=None):
        """A filter you can pick several values from: a button that opens a checklist (no popup, so it works the
        same with a mouse and with a finger). options: (value, text, indent level)."""
        items = "".join(
            f'<li data-v="{esc(v)}" style="--lvl:{lvl}"><label><input type="checkbox" value="{esc(v)}">'
            f'<span class="t">{esc(t)}</span><span class="n"></span></label></li>' for v, t, lvl in options)
        finder = (f'<input type="search" class="pf" placeholder="{esc(find)}" aria-label="{esc(find)}">'
                  if find else "")
        return f"""<div class="field"><span class="flabel">{esc(label)}</span>
  <details class="multi" id="{fid}" data-all="{esc(all_text)}" data-noun="{esc(noun)}">
    <summary><span class="sum">{esc(all_text)}</span><span class="cnt" hidden></span></summary>
    <div class="pop">{finder}
      <div class="pact"><span class="hint"></span><button type="button" class="link" data-act="clear">Clear</button></div>
      <ul class="opts">{items}</ul>
    </div>
  </details></div>"""

    topic_opts = [(t.id, t.name, len(course.ancestors(t.id))) for t in course.topics.values() if t.id in used_topics]
    fac_opts = [(f, f, 0) for f in sorted(faculty)]
    exam_opts = [(e.label, e.title, 0) for e in exams if e.parts]
    # Topic tree (only topics in use, in course.yaml order), the exams, and one row per question.
    index = {
        "code": course.display_code, "v": version,
        "topics": [{"id": t.id, "name": t.name, "parent": t.parent}
                   for t in course.topics.values() if t.id in used_topics],
        "exams": [{"label": e.label, "title": e.title,
                   "rules": " ".join(f"Section {s.name}: {s.rule}" for s in e.sections.values() if s.rule)}
                  for e in exams if e.parts],
        "q": rows,  # [id, exam, first topic, topics with their parents, teachers, has solution]
    }
    index_json = json.dumps(index, separators=(",", ":")).replace("</", "<\\/")

    body = f"""<h1>{esc(course.display_code)}: {esc(course.title)}</h1>
<noscript><p class="empty">This page needs JavaScript to show the questions.</p></noscript>
<div class="layout">
<aside class="filters" id="filters">
  <button type="button" id="f-collapse" class="collapse" aria-expanded="true" aria-controls="filters"
    title="Hide the filters to give the questions the full width"><span class="arrow" aria-hidden="true">«</span><span class="txt">Hide filters</span></button>
  <div class="panel">
  <div class="arrange" role="group" aria-label="Arrange questions">
    <span class="arrange-label">Arrange questions</span>
    <div class="switch">
      <button type="button" data-arrange="topic" aria-pressed="true">By topic</button>
      <button type="button" data-arrange="year" aria-pressed="false">By year</button>
    </div>
    <p class="arrange-now" id="arrange-now">Grouped topic by topic</p>
  </div>
  <p class="how">Pick as many teachers, exams and topics as you like. A question is shown when it matches
    <b>one of the teachers</b> and <b>one of the exams</b> and <b>one of the topics</b> you picked.</p>
  {multi("f-faculty", "Teachers", "All teachers", "teacher", fac_opts)}
  {multi("f-exam", "Exams", "All exams", "exam", exam_opts)}
  {multi("f-topic", "Topics", "All topics", "topic", topic_opts, find="Find a topic")}
  <label>Search<input type="search" id="f-text" placeholder="e.g. deadlock, Gantt"></label>
  <label class="check"><input type="checkbox" id="f-solved"> Only questions with solutions</label>
  <label class="check"><input type="checkbox" id="f-open"> Show all solutions</label>
  <label class="check"><input type="checkbox" id="f-qonly"> Questions only when printing</label>
  <div class="showbar"><button type="button" id="f-show" class="primary">Show questions</button></div>
  <div class="buttons">
    <button type="button" id="f-clear" class="ghost">Clear filters</button>
    <button type="button" id="f-print" class="ghost">Print / Save PDF</button>
  </div>
  <p class="count" id="f-count"></p>
  <p class="muted"><a href="../help.html">How to use this page</a></p>
  </div>
</aside>
<div class="questions">
<details class="overview" id="overview" open>
  <summary id="overview-title">Jump to a topic</summary>
  <p class="muted" id="overview-hint"></p>
  <div id="overview-body"></div>
</details>
<section id="results" hidden>
  <div class="results-head">
    <h2 id="results-title" tabindex="-1">Results</h2>
    <p class="muted" id="results-sub"></p>
    <div class="active" id="results-chips"></div>
    <p class="stale" id="results-stale" role="status" hidden>Your filters changed.
      <button type="button" id="results-update">Update results</button></p>
  </div>
  <nav class="pager" id="pager-top" aria-label="Pages" hidden></nav>
  <div id="results-list" aria-live="polite"></div>
  <p class="status" id="results-progress" role="status" hidden></p>
  <p class="empty" id="f-empty" hidden>No questions match these filters.</p>
  <nav class="pager" id="pager-bottom" aria-label="Pages" hidden></nav>
</section>
</div>
</div>
<div id="print-area" aria-hidden="true"></div>
<script type="application/json" id="course-index">{index_json}</script>"""
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
    (out / "about.html").write_text(_about(), encoding="utf-8")
    (out / "help.html").write_text(_help(), encoding="utf-8")
    n = 3
    for course in bank.courses.values():
        (out / course.code).mkdir(exist_ok=True)
        (out / course.code / "index.html").write_text(_course(bank, course, repo_root, out / course.code), encoding="utf-8")
        n += 1
    return n
