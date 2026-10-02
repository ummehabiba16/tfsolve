"""Consistency checks for the bank (run locally with `tfsolve lint`, and in CI)."""
from __future__ import annotations

import re

from .bank import EXAM_RE, STATUSES, Issue, as_list

# Raw LaTeX that could read or write files, run programs, or break out of the document.
DANGEROUS_TEX = re.compile(
    r"\\(input|include|includeonly|write|write18|immediate|openin|openout|read|readline|"
    r"catcode|special|usepackage|documentclass|def|let|csname|directlua|ShellEscape)(?![A-Za-z])")


_HTML = re.compile(r"<(table|tr|td|th|div|br|span|sup|sub)\b|\{=html\}", re.I)
_IMG_LINK = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def content_problems(body, base):
    """(level, message) pairs for text that renders badly on GitHub or in the PDF."""
    out, in_code, fences = [], False, 0
    for n, line in enumerate(body.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code, fences = not in_code, fences + 1
            continue
        if in_code:
            continue
        if _HTML.search(line):
            out.append(("warning", f"line {n}: raw HTML; use a pipe table or plain Markdown (the PDF drops HTML)"))
        if re.match(r"^ {4,}\S", line):
            out.append(("warning", f"line {n}: indented 4+ spaces; GitHub shows it as code. Start sub-items "
                                   f"like (a) at the left margin"))
        if "$$" in line and line.strip() != "$$" and not re.fullmatch(r"\$\$.*\$\$", line.strip()):
            out.append(("warning", f"line {n}: put display math $$...$$ on its own line"))
        for m in re.finditer(r"\$\$(.+?)\$\$", line):
            visible = re.sub(r"\\[a-zA-Z]+|[{}^_\\,;!]|\s+", "", m.group(1))
            if len(visible) > 80:
                out.append(("warning", f"line {n}: very long display equation; it will probably run off the page, "
                                       f"split it into several $$ lines"))
        if re.search(r"\\begin\{(tabular|itemize|enumerate|center|quote)\}", line):
            out.append(("warning", f"line {n}: raw LaTeX environment; use Markdown lists or a pipe table"))
        for m in _IMG_LINK.finditer(line):
            if not m.group(1).startswith("http") and not (base / m.group(1)).is_file():
                out.append(("error", f"line {n}: image not found: {m.group(1)}"))
    if fences % 2:
        out.append(("error", "a ``` code block is never closed"))
    return out


def _rel(bank, path):
    try:
        return path.relative_to(bank.root.parent)
    except (ValueError, AttributeError):
        return path


def lint(bank):
    out = list(bank.issues)

    def err(path, msg):
        out.append(Issue("error", path, msg))

    def warn(path, msg):
        out.append(Issue("warning", path, msg))

    for dept in bank.depts.values():
        for code, sessions in dept.teaching.items():
            for sess, entry in sessions.items():
                for who in entry.values():
                    for f in who:
                        if ":" not in f and f not in dept.faculty:
                            err(dept.path / "teaching.yaml", f"{code} {sess}: '{f}' is not in faculty.yaml")

    for course in bank.courses.values():
        if not course.topics:
            err(course.path / "course.yaml", "course has no topics")
        for exam in course.exams:
            pfile = exam.path / "paper.yaml"
            m = EXAM_RE.match(exam.label)
            if exam.exam_date and m and (exam.exam_date.year, exam.exam_date.month) != (int(m["year"]), int(m["month"])):
                err(pfile, f"folder is {exam.label} but exam_date is {exam.exam_date}; "
                           f"rename the folder to {exam.exam_date:%Y-%m}")
            if not exam.exam_date and m and m["month"] != "00":
                warn(pfile, "no exam_date; use YYYY-00 as the folder name if only the year is known")
            if str(exam.meta.get("course", course.code)) != course.code:
                err(pfile, f"course is '{exam.meta.get('course')}' but the folder is in {course.code}")
            if not exam.sections:
                err(pfile, "no sections (e.g. A: {questions: [1, 2, 3, 4]})")
            if not exam.session:
                warn(pfile, "no session; faculty cannot be looked up in teaching.yaml")
            seen = {}
            for s in exam.sections.values():
                for q in s.questions:
                    if q in seen:
                        err(pfile, f"question {q} is in both section {seen[q]} and {s.name}")
                    seen[q] = s.name
                for f in s.set_by:
                    if ":" not in f and f not in bank.depts[course.dept].faculty:
                        err(pfile, f"section {s.name}: '{f}' is not in faculty.yaml")

            for part in [*exam.parts, *exam.stems.values()]:
                is_stem = part.pid in exam.stems
                if part.section is None:
                    err(part.path, f"question {part.num} is not listed in any section of paper.yaml")
                if not part.body.strip():
                    err(part.path, "empty question text")
                if bad := DANGEROUS_TEX.search(part.body):
                    err(part.path, f"raw LaTeX command '{bad.group(0)}' is not allowed in content")
                for level, msg in content_problems(part.body, part.path.parent):
                    out.append(Issue(level, part.path, msg))
                if is_stem:
                    continue
                if not isinstance(part.marks, (int, float)) or part.marks <= 0:
                    err(part.path, "marks must be a positive number")
                if not part.topics:
                    err(part.path, "topics: must list at least one topic id from course.yaml")
                for t in part.topics:
                    if t not in course.topics:
                        sugg = course.suggest_topics(t)
                        hint = f" (did you mean {', '.join(sugg)}?)" if sugg else ""
                        err(part.path, f"unknown topic '{t}'{hint}")
                for f in as_list(part.meta.get("set_by")):
                    if ":" not in f and f.upper() not in bank.depts[course.dept].faculty:
                        err(part.path, f"set_by '{f}' is not in faculty.yaml")

    for sol in bank.orphan_solutions:
        err(sol.path, "solution for a part that does not exist (or is a stem with sub-parts)")
    for sols in bank.solutions.values():
        for sol in sols:
            if sol.status not in STATUSES:
                err(sol.path, f"status must be one of: {', '.join(STATUSES)}")
            author = str(sol.meta.get("author", ""))
            if not author:
                err(sol.path, "missing author (a GitHub username, or 'ai')")
            elif author != "ai" and author != sol.author:
                warn(sol.path, f"author '{author}' does not match the file name '{sol.author}.md'")
            if sol.is_ai and sol.status == "verified" and not as_list(sol.meta.get("reviewed_by")):
                err(sol.path, "an AI solution can only be 'verified' after a person reviews it (reviewed_by)")
            if sol.status in ("reviewed", "verified") and not as_list(sol.meta.get("reviewed_by")):
                err(sol.path, f"status '{sol.status}' needs reviewed_by")
            if not sol.body.strip():
                err(sol.path, "empty solution")
            if bad := DANGEROUS_TEX.search(sol.body):
                err(sol.path, f"raw LaTeX command '{bad.group(0)}' is not allowed in content")
            for level, msg in content_problems(sol.body, sol.path.parent):
                out.append(Issue(level, sol.path, msg))
    return out


def format_issues(bank, issues):
    lines = []
    for i in sorted(issues, key=lambda i: (i.level != "error", str(i.path))):
        where = _rel(bank, i.path) if i.path else ""
        lines.append(f"{i.level.upper():7} {where}: {i.message}")
    return "\n".join(lines)
