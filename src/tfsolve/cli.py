"""Command-line interface. `tfsolve -c CSE313 -t pagetable -f ABC` builds a PDF; see `tfsolve -h`."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from . import __version__
from .bank import Bank, as_list, find_bank
from .lint import format_issues, lint
from .query import QueryError, available_years, select
from .render import BuildError, build_pdf, doctor

COMMANDS = ("build", "help", "list", "todo", "lint", "check", "pages", "update", "doctor", "web")

GUIDE = """\
tfsolve: BUET term-final questions and solutions as a PDF        (ABC = a teacher's initials)

1. A WHOLE COURSE, ARRANGED  (start here)
   tfsolve -c CSE313 -topicwise        every question, one chapter per topic;
                                       the contents list topic after topic
   tfsolve -c CSE313 -yearwise         every question, one chapter per exam;
                                       the contents list year after year

2. ONE TEACHER  (-f)
   tfsolve -c CSE313 -topicwise -f ABC    only the questions ABC set
   tfsolve list faculty -c CSE313         who set which section, by session

3. CHOSEN YEARS  (-y)
   tfsolve list years -c CSE313           which exam years are available
   tfsolve -c CSE313 -yearwise -y 2025    exams held in 2025
       -y 2021..2025   a range        -y 2025-09   one exam (by month)
       --session 2023-24   the session printed on the paper

4. MORE FILTERS AND OPTIONS
   -t pagetable        one topic (see: tfsolve list topics -c CSE313)
   --solutions none    questions only, for practice;  --solutions all  every solution
   --answers-at-end    solutions in an appendix instead of after each question
   -o FILE.pdf         output file (default: out/<course>_<filters>.pdf)
   --tex               also keep the .tex (compile it on overleaf.com if you have no LaTeX)

5. OTHER COMMANDS
   tfsolve update      download the latest questions (once after install, then whenever you like)
   tfsolve list courses|years|exams|topics|faculty -c CSE313
   tfsolve web         build the website;   tfsolve doctor   check your LaTeX setup
   tfsolve todo / check / pages             for contributors

All options: tfsolve -h        Website: https://ummehabiba16.github.io/tfsolve
"""

EPILOG = """\
commands: help, list, todo, lint, check, update, pages, doctor, web   (tfsolve help explains them)

examples (ABC = a teacher's initials):
  tfsolve -c CSE313 -topicwise                   whole course, topic by topic
  tfsolve -c CSE313 -yearwise                    whole course, exam by exam
  tfsolve -c CSE313 -topicwise -f ABC            only ABC's questions
  tfsolve -c CSE313 -yearwise -y 2021..2025      exams from 2021 to 2025
"""


def _bank_arg(p):
    p.add_argument("--bank", help="path to the bank/ folder (default: found by searching upward from here)")


def _filters(p, course_required=True):
    p.add_argument("-c", "--course", required=course_required, help="course code, e.g. CSE313")
    p.add_argument("-t", "--topic", action="append", default=[], help="topic id or alias; repeat for OR")
    p.add_argument("-f", "--faculty", action="append", default=[],
                   help="faculty initials, e.g. ABC; repeat for OR (default: all faculty)")
    p.add_argument("-y", "--year", action="append", default=[], help="exam year (2021), range (2016..2023) or folder (2025-09)")
    p.add_argument("--session", action="append", default=[], help="session as printed, e.g. 2019-20")
    p.add_argument("--batch", action="append", default=[], help="batch, e.g. 17")


def _build_parser(prog="tfsolve"):
    p = argparse.ArgumentParser(prog=prog, description="Compile BUET term-final questions (and solutions) into a PDF.",
                                epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter, allow_abbrev=False)
    p.add_argument("--version", action="version", version=f"tfsolve {__version__}")
    p.add_argument("-c", "--course", required=True, help="course code, e.g. CSE313")

    arrange = p.add_argument_group("arrangement (pick one; default: topicwise)")
    how = arrange.add_mutually_exclusive_group()
    how.add_argument("-topicwise", "--topicwise", dest="by", action="store_const", const="topic",
                     help="one chapter per topic; the contents list topic after topic")
    how.add_argument("-yearwise", "--yearwise", dest="by", action="store_const", const="year",
                     help="one chapter per exam; the contents list year after year")
    how.add_argument("--by", choices=["topic", "year", "faculty", "none"], help=argparse.SUPPRESS)

    filt = p.add_argument_group("filters (repeat a flag for OR; different flags combine with AND)")
    filt.add_argument("-f", "--faculty", action="append", default=[],
                      help="faculty initials, e.g. ABC (default: all faculty)")
    filt.add_argument("-y", "--year", action="append", default=[],
                      help="exam year (2025), range (2021..2025) or one exam (2025-09); see: tfsolve list years")
    filt.add_argument("-t", "--topic", action="append", default=[], help="topic id or alias; see: tfsolve list topics")
    filt.add_argument("--session", action="append", default=[], help="session as printed, e.g. 2023-24")
    filt.add_argument("--batch", action="append", default=[], help="batch, e.g. 19")

    out = p.add_argument_group("output")
    out.add_argument("--solutions", choices=["best", "all", "none", "human", "ai"], default="best",
                     help="which solutions to include (default: the best-checked one per part)")
    out.add_argument("--answers-at-end", action="store_true", help="put solutions in an appendix for self-testing")
    out.add_argument("-o", "--output", help="output PDF path (default: out/<filters>.pdf)")
    out.add_argument("--tex", action="store_true", help="also keep the generated .md and .tex next to the PDF")
    out.add_argument("--engine", default="xelatex", choices=["xelatex", "lualatex", "pdflatex"], help="LaTeX engine")
    _bank_arg(p)
    return p


def _open_bank(args):
    root = Path(args.bank) if args.bank else (Path(os.environ["TFSOLVE_BANK"]) if os.environ.get("TFSOLVE_BANK") else find_bank())
    if not root or not Path(root).is_dir():
        sys.exit("tfsolve: no question bank yet. Run `tfsolve update` to download it "
                 "(or run inside a clone of the tfsolve repo, or pass --bank PATH).")
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
        hint = f"\nYears in the bank: {available_years(sel.course)}" if (args.year or args.session) else ""
        sys.exit(f"tfsolve: no questions match ({sel.describe()}).{hint}")
    chosen = args.by
    args.by = args.by or "topic"
    suffix = {"topic": "_topicwise", "year": "_yearwise"}.get(chosen, "")
    out = Path(args.output) if args.output else Path("out") / f"{sel.slug()}{suffix}.pdf"
    try:
        stats = build_pdf(bank, sel, out, args.by, args.solutions, args.answers_at_end, args.tex, args.engine)
    except BuildError as e:
        sys.exit(f"tfsolve: {e}")
    if stats.get("pdf") is False:
        print(f"{out.with_suffix('.tex')}  (no LaTeX here: upload this .tex and the fig/ folder, if any, to overleaf.com "
              f"and compile with XeLaTeX)")
        return 0
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
    p.add_argument("what", choices=["courses", "years", "topics", "exams", "faculty"])
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
    elif args.what == "years":
        years = {}
        for e in course.exams:
            ps = [pt for pt in sel.parts if pt.exam is e]
            if ps:
                years.setdefault(e.year, []).append((e, len(ps)))
        rows = [[y, ", ".join(e.label for e, _ in v), ", ".join(e.session or "?" for e, _ in v), sum(n for _, n in v)]
                for y, v in sorted(years.items(), reverse=True)]
        print(f"{course.code} {course.title}: {sel.describe()}")
        print(_table(rows, ["year", "exam (use with -y)", "session (use with --session)", "parts"]))
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
        taught = {}
        for sess, entry in sorted(dept.teaching.get(course.code, {}).items()):
            for sec, who in entry.items():
                for f in who:
                    taught.setdefault(f, []).append(sess + (f"({sec})" if sec != "*" else ""))
        rows = []
        for f in sorted(set(taught) | {w for pt in sel.parts for w in bank.setters(pt)[0]}):
            n = sum(1 for pt in sel.parts if f in bank.setters(pt)[0])
            rows.append([f, n, ", ".join(taught.get(f, []))])
        print(_table(rows, ["faculty", "parts", "sessions (section)"]))
    return 0


def cmd_todo(argv):
    p = argparse.ArgumentParser(prog="tfsolve todo", description="What to add, solve and review next.")
    _bank_arg(p)
    p.add_argument("-c", "--course", action="append", default=[], help="course(s); default: all")
    p.add_argument("-f", "--faculty", action="append", default=[], help="only these teachers' papers and parts, e.g. ABC")
    p.add_argument("-n", type=int, default=15, help="max rows per list (default 15)")
    args = p.parse_args(argv)
    bank = _open_bank(args)
    courses = [bank.course(c) for c in args.course] if args.course else list(bank.courses.values())
    wanted = {f.upper() for f in args.faculty}
    for course in filter(None, courses):
        dept = bank.depts[course.dept]
        print(f"\n{course.code} {course.title}" + (f" (faculty: {', '.join(sorted(wanted))})" if wanted else ""))

        missing = []
        for sess, entry in sorted(dept.teaching.get(course.code, {}).items(), reverse=True):
            exams = [e for e in course.exams if e.session == sess]
            for sec, names in entry.items():
                if wanted and not set(names) & wanted:
                    continue
                have = [pt for e in exams for pt in e.parts if sec == "*" or pt.section == sec]
                if not have:
                    missing.append(f"  {sess}  section {sec if sec != '*' else '?'}  ({'/'.join(names)}): no paper in the bank yet")
        print("\n1. Papers to add (sessions in teaching.yaml without a transcribed paper):")
        print("\n".join(missing[:args.n]) if missing else "  none")

        def newest_first(pt):
            return (-int(pt.exam.label[:4] + pt.exam.label[5:7]), pt.sort_key)

        parts = sorted([pt for e in course.exams for pt in e.parts
                        if not wanted or set(bank.setters(pt)[0]) & wanted], key=newest_first)
        unsolved = [pt for pt in parts if not bank.solutions.get(pt.uid)]
        review = [pt for pt in parts if bank.solutions.get(pt.uid)
                  and bank.solutions_for(pt)[0].status in ("unverified", "disputed")]

        def show(title, items):
            print(f"\n{title}: {len(items)}")
            for pt in items[:args.n]:
                w = "/".join(bank.setters(pt)[0]) or "?"
                names = ", ".join(course.topics[t].name for t in pt.topics if t in course.topics)
                print(f"  {w:5} {pt.exam.label}  {pt.label:10} {names}")
            if len(items) > args.n:
                print(f"  ... and {len(items) - args.n} more (use -n)")

        show("2. Parts without a solution (newest exams first)", unsolved)
        show("3. Solutions waiting for a human check", review)
    return 0


def cmd_help(argv):
    print(GUIDE)
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


def cmd_update(argv):
    from .fetch import data_dir, update
    p = argparse.ArgumentParser(prog="tfsolve update", description="Download the latest question bank from GitHub.")
    p.add_argument("--repo", help="repository URL (default: the official tfsolve repo, or $TFSOLVE_REPO)")
    p.add_argument("--branch", default="main")
    args = p.parse_args(argv)
    try:
        path, n = update(args.repo, args.branch)
    except Exception as e:  # network errors, 404 for a private repo, bad zip
        hint = ""
        if "404" in str(e):
            hint = "\n(The repository was not found. A private repo cannot be downloaded this way; clone it instead.)"
        elif "CERTIFICATE" in str(e):
            hint = "\n(Python cannot check HTTPS certificates. Run: pip install --upgrade certifi tfsolve)"
        sys.exit(f"tfsolve update: {e}{hint}")
    print(f"downloaded {n} files to {path}")
    return 0


def cmd_doctor(argv):
    argparse.ArgumentParser(prog="tfsolve doctor").parse_args(argv)
    ok = True
    for good, msg in doctor():
        ok &= good
        print(("ok   " if good else "FIX  ") + msg)
    return 0 if ok else 1


def cmd_web(argv):
    from .web import build_site
    p = argparse.ArgumentParser(prog="tfsolve web", description="Build the static website (HTML, no server needed).")
    _bank_arg(p)
    p.add_argument("-o", "--output", default="site", help="output folder (default: site)")
    args = p.parse_args(argv)
    bank = _open_bank(args)
    try:
        n = build_site(bank, args.output)
    except BuildError as e:
        sys.exit(f"tfsolve web: {e}")
    print(f"{Path(args.output) / 'index.html'}  ({n} pages)")
    return 0


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):  # Windows consoles/pipes may not be UTF-8: never crash on a symbol
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-help", "--guide"):
        return cmd_help([])
    cmd = argv[0] if argv and argv[0] in COMMANDS else "build"
    if argv and argv[0] in COMMANDS:
        argv = argv[1:]
    return {"build": cmd_build, "help": cmd_help, "list": cmd_list, "todo": cmd_todo, "lint": cmd_lint, "check": cmd_check,
            "pages": cmd_pages, "update": cmd_update, "doctor": cmd_doctor, "web": cmd_web}[cmd](argv)


if __name__ == "__main__":
    raise SystemExit(main())
