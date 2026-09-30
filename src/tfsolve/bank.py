"""Load a question bank directory into memory.

    bank/<DEPT>/dept.yaml                      name, current_session
    bank/<DEPT>/faculty.yaml                   initials registry
    bank/<DEPT>/teaching.yaml                  course -> session -> {section: [initials]} (the faculty sheet)
    bank/<DEPT>/<COURSE>/course.yaml           title + topic tree
    bank/<DEPT>/<COURSE>/<YYYY-MM>/paper.yaml  one exam paper, named by exam month
    bank/<DEPT>/<COURSE>/<YYYY-MM>/q3a.md      one question part; q3.md is the shared stem of q3a, q3b ...
    bank/<DEPT>/<COURSE>/<YYYY-MM>/solutions/q3a/<author>.md
"""
from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml

_Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

STATUSES = ("verified", "reviewed", "unverified", "disputed")
STATUS_RANK = {"verified": 0, "reviewed": 1, "unverified": 2, "disputed": 3}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10}
PART_RE = re.compile(r"^q(?P<num>[1-9]\d*)(?P<letter>[a-z])?(?:-(?P<sub>i|ii|iii|iv|v|vi|vii|viii|ix|x))?$")
EXAM_RE = re.compile(r"^(?P<year>\d{4})-(?P<month>\d{2})(?:-(?P<suffix>[a-z0-9]+))?$")
SESSION_RE = re.compile(r"^(\d{4})\s*[-–/]\s*(\d{2}|\d{4})$")


@dataclass
class Issue:
    level: str  # "error" | "warning"
    path: Path | None
    message: str


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, Loader=_Loader)


def read_markdown(path):
    """Split a Markdown file into (front-matter dict, body)."""
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    start = text.find("\n") + 1
    m = re.compile(r"^---[ \t]*$", re.M).search(text, start)
    if not m:
        raise ValueError("front matter is not closed with a '---' line")
    meta = yaml.load(text[start:m.start()], Loader=_Loader) or {}
    if not isinstance(meta, dict):
        raise ValueError("front matter must be a YAML mapping")
    return meta, text[m.end():].strip("\n") + "\n"


def norm(s):
    """Normalise a typed name for matching: 'Page Table' == 'page-table' == 'pagetable'."""
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def norm_session(s):
    """'2019-2020' or '2019-20' -> '2019-20'; None if it is not a session."""
    m = SESSION_RE.match(str(s).strip())
    return f"{m.group(1)}-{m.group(2)[-2:]}" if m else None


def as_list(v):
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [str(x) for x in v]
    return [str(v)]


def is_under(child, parent):
    """q7a-ii is under q7a and q7; q10a is not under q1; q7a-ii is not under q7a-i."""
    c, p = PART_RE.match(child), PART_RE.match(parent)
    if not c or not p or c["num"] != p["num"]:
        return False
    if p["letter"] is None:
        return c["letter"] is not None
    return p["sub"] is None and c["letter"] == p["letter"] and c["sub"] is not None


# --------------------------------------------------------------------------- model

@dataclass
class Topic:
    id: str
    name: str
    parent: str | None
    aliases: list[str]
    info: dict
    children: list[str] = field(default_factory=list)


@dataclass(eq=False)
class Course:
    code: str
    dept: str
    path: Path
    meta: dict
    topics: dict[str, Topic]  # tree pre-order, as written in course.yaml
    exams: list["Exam"] = field(default_factory=list)

    @property
    def title(self):
        return self.meta.get("title", self.code)

    @property
    def display_code(self):
        m = re.match(r"^([A-Z]+)(\d+)$", self.code)
        return f"{m.group(1)} {m.group(2)}" if m else self.code

    def ancestors(self, tid):
        out, t = [], self.topics.get(tid)
        while t and t.parent:
            out.append(t.parent)
            t = self.topics.get(t.parent)
        return out

    def root(self, tid):
        chain = self.ancestors(tid)
        return chain[-1] if chain else tid

    def expand(self, tid):
        """The topic and all of its descendants."""
        out, stack = set(), [tid]
        while stack:
            t = stack.pop()
            if t in out:
                continue
            out.add(t)
            stack.extend(self.topics[t].children if t in self.topics else [])
        return out

    def resolve_topic(self, term):
        n = norm(term)
        for t in self.topics.values():
            if n in (norm(t.id), norm(t.name)) or n in (norm(a) for a in t.aliases):
                return t.id
        return None

    def suggest_topics(self, term, n=3):
        names = {}
        for t in self.topics.values():
            for key in [t.id, *t.aliases]:
                names.setdefault(norm(key), t.id)
        close = difflib.get_close_matches(norm(term), list(names), n=n * 2, cutoff=0.6)
        out = []
        for c in close:
            if names[c] not in out:
                out.append(names[c])
        return out[:n]


@dataclass
class Section:
    name: str
    questions: list[int]
    answer_any: int | None
    rule: str | None
    set_by: list[str]  # explicit override; normally comes from teaching.yaml


@dataclass(eq=False)
class Exam:
    course: Course
    label: str
    path: Path
    meta: dict
    exam_date: date | None
    session: str | None
    sections: dict[str, Section]
    parts: list["Part"] = field(default_factory=list)
    stems: dict[str, "Part"] = field(default_factory=dict)

    @property
    def uid(self):
        return f"{self.course.dept}/{self.course.code}/{self.label}"

    @property
    def year(self):
        return self.exam_date.year if self.exam_date else int(self.label[:4])

    @property
    def when(self):
        """'Sep 2025' (falls back to the folder label)."""
        y, m = int(self.label[:4]), int(self.label[5:7])
        return f"{MONTHS[m - 1]} {y}" if 1 <= m <= 12 else str(y)

    @property
    def title(self):
        return f"{self.when} ({self.session})" if self.session else self.when

    def section_of(self, num):
        for s in self.sections.values():
            if num in s.questions:
                return s.name
        return None


@dataclass(eq=False)
class Part:
    exam: Exam
    pid: str
    path: Path
    meta: dict
    body: str

    def __post_init__(self):
        m = PART_RE.match(self.pid)
        self.num = int(m.group("num"))
        self.letter = m.group("letter")
        self.sub = m.group("sub")

    @property
    def uid(self):
        return f"{self.exam.uid}/{self.pid}"

    @property
    def label(self):
        s = f"Q{self.num}"
        if self.letter:
            s += f"({self.letter})"
        if self.sub:
            s += f"({self.sub})"
        return s

    @property
    def sort_key(self):
        return (self.num, self.letter or "", ROMAN.get(self.sub or "", 0))

    @property
    def marks(self):
        return self.meta.get("marks")

    @property
    def topics(self):
        return as_list(self.meta.get("topics"))

    @property
    def section(self):
        return self.exam.section_of(self.num)

    def stem_ids(self):
        """Ids whose files, if present, hold shared context for this part (outermost first)."""
        out = [f"q{self.num}"] if (self.letter or self.sub) else []
        if self.letter and self.sub:
            out.append(f"q{self.num}{self.letter}")
        return out


@dataclass(eq=False)
class Solution:
    part_uid: str
    author: str
    path: Path
    meta: dict
    body: str

    @property
    def status(self):
        return self.meta.get("status", "unverified")

    @property
    def is_ai(self):
        return str(self.meta.get("author", self.author)) == "ai"

    @property
    def rank(self):
        return (STATUS_RANK.get(self.status, 9), 1 if self.is_ai else 0, self.author)


@dataclass(eq=False)
class Dept:
    code: str
    path: Path
    meta: dict
    faculty: dict[str, dict]
    teaching: dict[str, dict[str, dict[str, list[str]]]]  # course -> session -> section|'*' -> initials

    @property
    def current_session(self):
        return norm_session(self.meta.get("current_session", "")) or None


# ---------------------------------------------------------------------------- bank

class Bank:
    def __init__(self, root):
        self.root = Path(root)
        self.issues: list[Issue] = []
        self.depts: dict[str, Dept] = {}
        self.courses: dict[str, Course] = {}
        self.solutions: dict[str, list[Solution]] = {}
        self.orphan_solutions: list[Solution] = []
        self._load()

    # ---- queries
    @property
    def parts(self):
        return [p for c in self.courses.values() for e in c.exams for p in e.parts]

    def course(self, code):
        n = norm(code).upper()
        for c in self.courses.values():
            if norm(c.code).upper() == n:
                return c
            if any(norm(x).upper() == n for x in as_list(c.meta.get("previous_codes"))):
                return c
        return None

    def teaching_entry(self, course, session):
        dept = self.depts.get(course.dept)
        if not dept or not session:
            return {}
        return dept.teaching.get(course.code, {}).get(session, {})

    def taught_by(self, exam):
        entry = self.teaching_entry(exam.course, exam.session)
        out = []
        for names in entry.values():
            out += [n for n in names if n not in out]
        return out

    def setters(self, part):
        """(initials, how) where how is 'set' (known setter), 'taught' (only who taught) or None."""
        explicit = [x.upper() for x in as_list(part.meta.get("set_by"))]
        if explicit:
            return explicit, "set"
        sec = part.section
        if sec and part.exam.sections[sec].set_by:
            return part.exam.sections[sec].set_by, "set"
        entry = self.teaching_entry(part.exam.course, part.exam.session)
        if sec and entry.get(sec):
            return entry[sec], "set"
        taught = self.taught_by(part.exam)
        return (taught, "taught") if taught else ([], None)

    def current_faculty(self, course):
        dept = self.depts.get(course.dept)
        if not dept or not dept.current_session:
            return []
        out = []
        for names in self.teaching_entry(course, dept.current_session).values():
            out += [n for n in names if n not in out]
        return out

    def solutions_for(self, part):
        return sorted(self.solutions.get(part.uid, []), key=lambda s: s.rank)

    def stems_for(self, part):
        return [part.exam.stems[s] for s in part.stem_ids() if s in part.exam.stems]

    # ---- loading
    def _issue(self, level, path, msg):
        self.issues.append(Issue(level, path, msg))

    def _yaml(self, path, default=None):
        try:
            data = load_yaml(path)
        except (OSError, yaml.YAMLError) as e:
            self._issue("error", path, f"cannot read YAML: {e}")
            return default
        return default if data is None else data

    def _load(self):
        if not self.root.is_dir():
            self._issue("error", self.root, "bank directory not found")
            return
        for ddir in sorted(p for p in self.root.iterdir() if p.is_dir() and not p.name.startswith(".")):
            if not (ddir / "dept.yaml").exists():
                continue
            dept = self._load_dept(ddir)
            self.depts[dept.code] = dept
            for cdir in sorted(p for p in ddir.iterdir() if p.is_dir() and (p / "course.yaml").exists()):
                course = self._load_course(dept, cdir)
                if course:
                    self.courses[course.code] = course

    def _load_dept(self, ddir):
        meta = self._yaml(ddir / "dept.yaml", {})
        faculty = self._yaml(ddir / "faculty.yaml", {}) if (ddir / "faculty.yaml").exists() else {}
        raw = self._yaml(ddir / "teaching.yaml", {}) if (ddir / "teaching.yaml").exists() else {}
        teaching = {}
        for code, sessions in (raw or {}).items():
            for sess, who in (sessions or {}).items():
                s = norm_session(sess)
                if not s:
                    self._issue("error", ddir / "teaching.yaml", f"{code}: '{sess}' is not a session like 2019-20")
                    continue
                if isinstance(who, dict):
                    entry = {str(k): [x.upper() for x in as_list(v)] for k, v in who.items()}
                else:
                    entry = {"*": [x.upper() for x in as_list(who)]}
                teaching.setdefault(str(code), {})[s] = entry
        faculty = {str(k).upper(): (v or {}) for k, v in (faculty or {}).items()}
        return Dept(str(meta.get("code", ddir.name)), ddir, meta, faculty, teaching)

    def _load_course(self, dept, cdir):
        meta = self._yaml(cdir / "course.yaml", {})
        topics = {}

        def walk(items, parent):
            for t in items or []:
                if not isinstance(t, dict) or "id" not in t:
                    self._issue("error", cdir / "course.yaml", f"topic entry without an id: {t!r}")
                    continue
                tid = str(t["id"])
                if tid in topics:
                    self._issue("error", cdir / "course.yaml", f"duplicate topic id '{tid}'")
                    continue
                info = {k: v for k, v in t.items() if k not in ("id", "name", "aliases", "children")}
                topics[tid] = Topic(tid, str(t.get("name", tid)), parent, as_list(t.get("aliases")), info)
                if parent:
                    topics[parent].children.append(tid)
                walk(t.get("children"), tid)

        walk(meta.get("topics"), None)
        course = Course(str(meta.get("code", cdir.name)), dept.code, cdir, meta, topics)
        for edir in sorted(p for p in cdir.iterdir() if p.is_dir()):
            if not (edir / "paper.yaml").exists():
                self._issue("warning", edir, "folder has no paper.yaml; skipped")
                continue
            exam = self._load_exam(course, edir)
            if exam:
                course.exams.append(exam)
        course.exams.sort(key=lambda e: e.label)
        return course

    def _load_exam(self, course, edir):
        meta = self._yaml(edir / "paper.yaml", {})
        if not EXAM_RE.match(edir.name):
            self._issue("error", edir, "exam folder must be named YYYY-MM (the exam month), e.g. 2025-09")
            return None
        d = meta.get("exam_date")
        if d is not None and not isinstance(d, date):
            self._issue("error", edir / "paper.yaml", f"exam_date '{d}' is not a date like 2025-09-04")
            d = None
        sess = meta.get("session")
        session = norm_session(sess) if sess else None
        if sess and not session:
            self._issue("error", edir / "paper.yaml", f"session '{sess}' is not like 2019-20")
        sections = {}
        for name, s in (meta.get("sections") or {}).items():
            s = s or {}
            qs = s.get("questions") or []
            sections[str(name)] = Section(
                str(name), [int(q) for q in qs if str(q).isdigit()],
                s.get("answer_any"), s.get("rule"), [x.upper() for x in as_list(s.get("set_by"))])
        exam = Exam(course, edir.name, edir, meta, d, session, sections)

        found = {}
        for f in sorted(edir.glob("*.md")):
            pid = f.stem
            if not PART_RE.match(pid):
                if f.name.lower() != "readme.md":
                    self._issue("error", f, "part files must be named like q3.md, q3a.md or q7a-ii.md")
                continue
            try:
                pmeta, body = read_markdown(f)
            except (ValueError, yaml.YAMLError) as e:
                self._issue("error", f, str(e))
                continue
            found[pid] = Part(exam, pid, f, pmeta, body)
        for pid, part in found.items():
            if any(is_under(o, pid) for o in found):
                exam.stems[pid] = part
            else:
                exam.parts.append(part)
        exam.parts.sort(key=lambda p: p.sort_key)

        sdir = edir / "solutions"
        if sdir.is_dir():
            for f in sorted(sdir.glob("*/*.md")):
                pid, author = f.parent.name, f.stem
                try:
                    smeta, body = read_markdown(f)
                except (ValueError, yaml.YAMLError) as e:
                    self._issue("error", f, str(e))
                    continue
                sol = Solution(f"{exam.uid}/{pid}", author, f, smeta, body)
                if pid in found and pid not in exam.stems:
                    self.solutions.setdefault(sol.part_uid, []).append(sol)
                else:
                    self.orphan_solutions.append(sol)
        return exam


def find_bank(start=None):
    """Walk up from `start` looking for a folder with bank/<DEPT>/dept.yaml."""
    p = Path(start or Path.cwd()).resolve()
    for d in [p, *p.parents]:
        b = d / "bank"
        if b.is_dir() and any(b.glob("*/dept.yaml")):
            return b
    from .fetch import downloaded_bank
    return downloaded_bank()
