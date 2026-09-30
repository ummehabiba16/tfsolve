"""Select question parts by course, topic, faculty and year."""
from __future__ import annotations

import re
from dataclasses import dataclass

from .bank import norm, norm_session


class QueryError(Exception):
    pass


@dataclass
class Selection:
    course: object
    parts: list
    topics: list[str]       # resolved topic ids, as requested
    faculty: list[str]      # initials; 'current' already expanded
    years: list[str]
    sessions: list[str]
    current: bool = False   # -f current was used

    def describe(self):
        bits = []
        if self.topics:
            bits.append("Topic: " + ", ".join(self.course.topics[t].name for t in self.topics))
        if self.faculty:
            who = ", ".join(self.faculty)
            bits.append(f"Faculty: {who}" + (" (teaching now)" if self.current else ""))
        if self.years:
            bits.append("Year: " + ", ".join(self.years))
        if self.sessions:
            bits.append("Session: " + ", ".join(self.sessions))
        return " · ".join(bits) or "All questions"

    def slug(self):
        bits = [self.course.code, *self.topics, *self.faculty, *self.years, *self.sessions]
        return "_".join(re.sub(r"[^A-Za-z0-9-]+", "-", b) for b in bits)


def _year_test(v):
    v = v.strip()
    if m := re.fullmatch(r"(\d{4})\.\.(\d{4})", v):
        lo, hi = int(m[1]), int(m[2])
        return lambda e: lo <= e.year <= hi
    if re.fullmatch(r"\d{4}", v):
        return lambda e: e.year == int(v)
    if re.fullmatch(r"\d{4}-\d{2}(-[a-z0-9]+)?", v):
        return lambda e: e.label == v or e.label.startswith(v + "-")
    raise QueryError(f"-y {v}: use a year (2021), a range (2016..2023) or an exam folder (2021-03). "
                     f"For a session use --session 2019-20.")


def resolve_faculty(bank, course, names):
    known = set(bank.depts[course.dept].faculty) if course.dept in bank.depts else set()
    for sessions in bank.depts[course.dept].teaching.get(course.code, {}).values() if course.dept in bank.depts else []:
        for who in sessions.values():
            known.update(who)
    out, current = [], False
    for f in names:
        if norm(f) == "current":
            cur = bank.current_faculty(course)
            if not cur:
                raise QueryError(f"nobody is listed as teaching {course.code} in the current session. "
                                 f"Set current_session in dept.yaml and add it to teaching.yaml.")
            out += [x for x in cur if x not in out]
            current = True
            continue
        F = f.upper()
        if known and F not in known:
            raise QueryError(f"unknown faculty '{f}' for {course.code}. Known: {', '.join(sorted(known))}")
        if F not in out:
            out.append(F)
    return out, current


def select(bank, course_code, topics=(), faculty=(), years=(), sessions=(), batches=()):
    course = bank.course(course_code)
    if not course:
        have = ", ".join(sorted(bank.courses)) or "none yet"
        raise QueryError(f"unknown course '{course_code}' (the bank has: {have})")

    tids = []
    for t in topics:
        tid = course.resolve_topic(t)
        if not tid:
            sugg = course.suggest_topics(t)
            hint = f" Did you mean: {', '.join(sugg)}?" if sugg else ""
            raise QueryError(f"no topic '{t}' in {course.code}.{hint} See: tfsolve list topics -c {course.code}")
        if tid not in tids:
            tids.append(tid)
    fac, current = resolve_faculty(bank, course, faculty)
    tests = [_year_test(y) for y in years]
    sess = []
    for s in sessions:
        n = norm_session(s)
        if not n:
            raise QueryError(f"--session {s}: expected a session like 2019-20")
        sess.append(n)
    wanted = set().union(*(course.expand(t) for t in tids)) if tids else None

    parts = []
    for exam in course.exams:
        if tests and not any(t(exam) for t in tests):
            continue
        if sess and exam.session not in sess:
            continue
        if batches and str(exam.meta.get("batch")) not in {str(b) for b in batches}:
            continue
        for part in exam.parts:
            if wanted is not None and not set(part.topics) & wanted:
                continue
            if fac and not set(bank.setters(part)[0]) & set(fac):
                continue
            parts.append(part)
    return Selection(course, parts, tids, fac, list(years), sess, current)
