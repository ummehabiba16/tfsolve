"""Command-line interface. `tfsolve -c CSE313 -t pagetable -f KRV` builds a PDF; see `tfsolve -h`."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from . import __version__
from .bank import Bank, as_list, find_bank
from .lint import format_issues, lint
from .query import QueryError, select
from .render import BuildError, build_pdf, doctor

COMMANDS = ("build", "list", "todo", "lint", "check", "pages", "doctor")

EPILOG = """\
commands:
  (none) / build   build a PDF from the filters below
  list WHAT        list courses | topics | exams | faculty   (e.g. tfsolve list topics -c CSE313)
  todo             what to add, solve and review next, current teachers first
  lint             check the bank for mistakes (CI runs this on every pull request)
  check            lint + build a PDF and report parts whose layout breaks (run after adding a paper)
  pages FILE.pdf   render a scanned PDF's pages as PNG images (so Claude can read them)
  doctor           check that Pandoc and LaTeX are set up for PDF builds

examples:
  tfsolve -c CSE313 -t pagetable -f KRV          page-table questions set by KRV
  tfsolve -c CSE313 -f current                   everything set by this term's teachers
  tfsolve -c CSE313 -y 2025-09                   one full paper (exam month)
  tfsolve -c CSE313 --session 2023-24 --solutions none
"""


def _bank_arg(p):
    p.add_argument("--bank", help="path to the bank/ folder (default: found by searching upward from here)")


def _filters(p, course_required=True):
    p.add_argument("-c", "--course", required=course_required, help="course code, e.g. CSE313")
    p.add_argument("-t", "--topic", action="append", default=[], help="topic id or alias; repeat for OR")
    p.add_argument("-f", "--faculty", action="append", default=[],
                   help="faculty initials; 'current' = teaching this session; repeat for OR")
    p.add_argument("-y", "--year", action="append", default=[], help="exam year (2021), range (2016..2023) or folder (2025-09)")
    p.add_argument("--session", action="append", default=[], help="session as printed, e.g. 2019-20")
    p.add_argument("--batch", action="append", default=[], help="batch, e.g. 17")


def _build_parser(prog="tfsolve"):
    p = argparse.ArgumentParser(prog=prog, description="Compile BUET term-final questions (and solutions) into a PDF.",
                                epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=f"tfsolve {__version__}")
    _bank_arg(p)
    _filters(p)
    p.add_argument("--solutions", choices=["best", "all", "none", "human", "ai"], default="best",
                   help="which solutions to include (default: the best-checked one per part)")
    p.add_argument("--by", choices=["topic", "year", "faculty", "none"], default="topic", help="grouping (default: topic)")
    p.add_argument("--answers-at-end", action="store_true", help="put solutions in an appendix for self-testing")
    p.add_argument("-o", "--output", help="output PDF path (default: out/<filters>.pdf)")
    p.add_argument("--tex", action="store_true", help="also keep the generated .md and .tex next to the PDF")
    p.add_argument("--engine", default="xelatex", choices=["xelatex", "lualatex", "pdflatex"], help="LaTeX engine")
    return p


def _open_bank(args):
    root = Path(args.bank) if args.bank else (Path(os.environ["TFSOLVE_BANK"]) if os.environ.get("TFSOLVE_BANK") else find_bank())
    if not root or not Path(root).is_dir():
        sys.exit("tfsolve: no bank found. Run this inside a clone of the tfsolve repo, or pass --bank PATH.")
    return Bank(root)


def _selection(bank, args):
    try:
        return select(bank, args.course, args.topic, args.faculty, args.year, args.session, args.batch)
    except QueryError as e:
        sys.exit(f"tfsolve: {e}")


# ----------------------------------------------------------------- commands

def cmd_build(argv):
    args = _build_parser().parse_args(argv)
    bank = _open_bank(args)
    sel = _selection(bank, args)
    if not sel.parts:
        sys.exit(f"tfsolve: no questions match ({sel.describe()}).")
    out = Path(args.output) if args.output else Path("out") / f"{sel.slug()}.pdf"
    try:
        stats = build_pdf(bank, sel, out, args.by, args.solutions, args.answers_at_end, args.tex, args.engine)
    except BuildError as e:
        sys.exit(f"tfsolve: {e}")
    s = stats["solutions"]
    missing = f", {s['none']} without a solution" if s.get("none") else ""
    print(f"{out}  ({stats['parts']} parts, {stats['marks']:g} marks, {stats['exams']} exams{missing})")
    for w in stats.get("layout", []):
        print(f"  layout: {w}")
    return 0


def _table(rows, header):
    widths = [max(len(str(r[i])) for r in [header, *rows]) for i in range(len(header))]
    line = lambda r: "  ".join(str(c).ljust(w) for c, w in zip(r, widths)).rstrip()  # noqa: E731
    return "\n".join([line(header), line(["-" * w for w in widths]), *map(line, rows)])


def cmd_list(argv):
    p = argparse.ArgumentParser(prog="tfsolve list", description="List what is in the bank.")
    p.add_argument("what", choices=["courses", "topics", "exams", "faculty"])
    _bank_arg(p)
    _filters(p, course_required=False)
    args = p.parse_args(argv)
    bank = _open_bank(args)
    if args.what == "courses":
        rows = []
        for c in bank.courses.values():
            parts = [pt for e in c.exams for pt in e.parts]
            solved = sum(1 for pt in parts if bank.solutions.get(pt.uid))
            rows.append([c.code, c.title, len(c.exams), len(parts), solved])
        print(_table(rows, ["course", "title", "exams", "parts", "solved"]))
        return 0
    if not args.course:
        sys.exit(f"tfsolve list {args.what}: give a course with -c")
    sel = _selection(bank, args)
    course = sel.course
    if args.what == "topics":
        rows = []
        filtered = bool(args.topic or args.faculty or args.year or args.session or args.batch)
        for t in course.topics.values():
            ids = course.expand(t.id)
            ps = [pt for pt in sel.parts if set(pt.topics) & ids]
            if filtered and not ps:
                continue
            depth = len(course.ancestors(t.id))
            rows.append(["  " * depth + t.id, len(ps), sum(pt.marks or 0 for pt in ps),
                         t.name + (f"  [{', '.join(t.aliases)}]" if t.aliases else "")])
        print(f"{course.code} {course.title}: {sel.describe()}")
        print(_table(rows, ["topic", "parts", "marks", "name  [aliases]"]))
    elif args.what == "exams":
        rows = []
        for e in course.exams:
            ps = [pt for pt in sel.parts if pt.exam is e]
            if not ps and (args.topic or args.faculty):
                continue
            solved = sum(1 for pt in ps if bank.solutions.get(pt.uid))
            secs = []
            for s in e.sections.values():
                sp = [pt for pt in e.parts if pt.section == s.name]
                who = bank.setters(sp[0])[0] if sp else (s.set_by or bank.teaching_entry(course, e.session).get(s.name, []))
                secs.append(f"{s.name}: {'/'.join(who) or '?'} ({len(sp)} parts)")
            rows.append([e.label, e.session or "?", e.meta.get("level_term", ""), len(ps), solved, "  ".join(secs)])
        print(_table(rows, ["exam", "session", "L-T", "parts", "solved", "sections (setter, transcribed parts)"]))
    else:  # faculty
        dept = bank.depts[course.dept]
        current = set(bank.current_faculty(course))
        taught = {}
        for sess, entry in sorted(dept.teaching.get(course.code, {}).items()):
            for sec, who in entry.items():
                for f in who:
                    taught.setdefault(f, []).append(sess + (f"({sec})" if sec != "*" else ""))
        rows = []
        for f in sorted(set(taught) | {w for pt in sel.parts for w in bank.setters(pt)[0]}):
            n = sum(1 for pt in sel.parts if f in bank.setters(pt)[0])
            rows.append([f, "yes" if f in current else "", n, ", ".join(taught.get(f, []))])
        print(f"{course.code}: current session {dept.current_session or '?'}")
        print(_table(rows, ["faculty", "teaching now", "parts", "sessions (section)"]))
    return 0


def cmd_todo(argv):
    p = argparse.ArgumentParser(prog="tfsolve todo", description="What to add, solve and review next.")
    _bank_arg(p)
    p.add_argument("-c", "--course", action="append", default=[], help="course(s); default: all")
    p.add_argument("-n", type=int, default=15, help="max rows per list (default 15)")
    args = p.parse_args(argv)
    bank = _open_bank(args)
    courses = [bank.course(c) for c in args.course] if args.course else list(bank.courses.values())
    for course in filter(None, courses):
        dept = bank.depts[course.dept]
        cur = bank.current_faculty(course)
        cur_entry = bank.teaching_entry(course, dept.current_session)
        who = ", ".join(f"{'/'.join(v)} ({'Section ' + k if k != '*' else 'section unknown'})" for k, v in cur_entry.items())
        print(f"\n{course.code} {course.title}\nTeaching now ({dept.current_session or 'session not set'}): {who or 'unknown'}")

        missing = []
        for sess, entry in sorted(dept.teaching.get(course.code, {}).items(), reverse=True):
            if sess == dept.current_session:
                continue
            exams = [e for e in course.exams if e.session == sess]
            for sec, names in entry.items():
                if not set(names) & set(cur):
                    continue
                have = [pt for e in exams for pt in e.parts if sec == "*" or pt.section == sec]
                if not have:
                    missing.append(f"  {sess}  section {sec if sec != '*' else '?'}  ({'/'.join(names)}): no paper in the bank yet")
        print("\n1. Papers to add (years when this term's teachers taught):")
        print("\n".join(missing[:args.n]) if missing else "  none (add more sessions to teaching.yaml as you learn them)")

        def prio(pt):
            return (0 if set(bank.setters(pt)[0]) & set(cur) else 1, -int(pt.exam.label[:4] + pt.exam.label[5:7]), pt.sort_key)

        parts = sorted([pt for e in course.exams for pt in e.parts], key=prio)
        unsolved = [pt for pt in parts if not bank.solutions.get(pt.uid)]
        review = [pt for pt in parts if bank.solutions.get(pt.uid)
                  and bank.solutions_for(pt)[0].status in ("unverified", "disputed")]

        def show(title, items):
            print(f"\n{title}: {len(items)}")
            for pt in items[:args.n]:
                w = "/".join(bank.setters(pt)[0]) or "?"
                star = "*" if set(bank.setters(pt)[0]) & set(cur) else " "
                names = ", ".join(course.topics[t].name for t in pt.topics if t in course.topics)
                print(f" {star}{w:5} {pt.exam.label}  {pt.label:10} {names}")
            if len(items) > args.n:
                print(f"  ... and {len(items) - args.n} more (use -n)")

        show("2. Parts without a solution (* = set by a current teacher)", unsolved)
        show("3. Solutions waiting for a human check", review)
    return 0


def cmd_lint(argv):
    p = argparse.ArgumentParser(prog="tfsolve lint", description="Check the bank for mistakes.")
    _bank_arg(p)
    args = p.parse_args(argv)
    bank = _open_bank(args)
    issues = lint(bank)
    errors = [i for i in issues if i.level == "error"]
    if issues:
        print(format_issues(bank, issues))
    n_parts = len(bank.parts)
    n_sol = sum(len(v) for v in bank.solutions.values())
    print(f"{'FAILED' if errors else 'OK'}: {len(bank.courses)} courses, {n_parts} parts, {n_sol} solutions; "
          f"{len(errors)} errors, {len(issues) - len(errors)} warnings")
    return 1 if errors else 0


def cmd_check(argv):
    p = argparse.ArgumentParser(prog="tfsolve check",
                                description="Lint the bank, then build a PDF and report parts whose layout breaks.")
    _bank_arg(p)
    _filters(p, course_required=False)
    args = p.parse_args(argv)
    bank = _open_bank(args)
    issues = lint(bank)
    errors = [i for i in issues if i.level == "error"]
    if issues:
        print(format_issues(bank, issues))
    print(f"lint: {len(errors)} errors, {len(issues) - len(errors)} warnings")
    courses = [args.course] if args.course else sorted(bank.courses)
    problems = 0
    for code in courses:
        args.course = code
        sel = _selection(bank, args)
        if not sel.parts:
            continue
        out = Path("out") / "check" / f"{sel.slug()}.pdf"
        try:
            stats = build_pdf(bank, sel, out)
        except BuildError as e:
            print(f"build {code}: FAILED\n{e}")
            problems += 1
            continue
        print(f"build {code}: {out} ({stats['parts']} parts)")
        for w in stats["layout"]:
            print(f"  layout: {w}")
        problems += len(stats["layout"])
    ok = not errors and not problems
    print("CHECK OK" if ok else "CHECK FOUND PROBLEMS (fix them, then run tfsolve check again)")
    return 0 if ok else 1


def cmd_pages(argv):
    p = argparse.ArgumentParser(prog="tfsolve pages", description="Render each page of a PDF as a PNG image.")
    p.add_argument("pdf", help="the scanned question paper")
    p.add_argument("-o", "--out", help="output folder (default: out/pages/<file name>)")
    p.add_argument("--dpi", type=int, default=150, help="resolution (default 150; use 200 for small print)")
    args = p.parse_args(argv)
    try:
        import pymupdf
    except ImportError:
        sys.exit("tfsolve pages needs PyMuPDF: pip install -e '.[scan]'")
    src = Path(args.pdf).expanduser()
    if not src.is_file():
        sys.exit(f"tfsolve pages: no such file: {src}")
    out = Path(args.out) if args.out else Path("out") / "pages" / src.stem
    out.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(src)
    for i, page in enumerate(doc, 1):
        path = out / f"page-{i:02d}.png"
        page.get_pixmap(dpi=args.dpi).save(path)
        print(path)
    return 0


def cmd_doctor(argv):
    argparse.ArgumentParser(prog="tfsolve doctor").parse_args(argv)
    ok = True
    for good, msg in doctor():
        ok &= good
        print(("ok   " if good else "FIX  ") + msg)
    return 0 if ok else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    cmd = argv[0] if argv and argv[0] in COMMANDS else "build"
    if argv and argv[0] in COMMANDS:
        argv = argv[1:]
    return {"build": cmd_build, "list": cmd_list, "todo": cmd_todo, "lint": cmd_lint, "check": cmd_check,
            "pages": cmd_pages, "doctor": cmd_doctor}[cmd](argv)


if __name__ == "__main__":
    raise SystemExit(main())
