---
name: transcribe
description: Transcribe a scanned BUET term-final paper (PDF or photos) into tfsolve bank files - paper.yaml plus one Markdown file per question part, tagged with topics. Use when the user gives a question-paper scan to add to the bank, e.g. "/transcribe ~/scans/cse313-2021.pdf CSE313".
---

# Transcribe a paper into the bank

Input: a scan (PDF or images) and usually a course code. Output: a new exam folder `bank/<DEPT>/<COURSE>/<YYYY-MM>/` that passes `.venv/bin/tfsolve lint`. **Never write solutions here**. Solving is a separate step (`/solve`).

Before starting, read `.claude/skills/add-paper/rendering.md` (formatting rules), one existing exam folder in the same course (for example `bank/CSE/CSE313/2025-09/`) and the course's `course.yaml`. Copy their conventions exactly. (To add a paper *and* a faculty list *and* solutions in one go, use `/add-paper`.)

## Steps

1. **Read every page of the scan.** For a PDF, run `.venv/bin/tfsolve pages <file.pdf>` (`--dpi 200` for small print) and read each PNG it prints; photos can be read directly. From the header, collect: course code and title, level/term and the students' department (`L-3/T-1/CSE`), session as printed (`2019-2020` → `"2019-20"`), exam date, full marks, time, and each section's questions and rule ("answer any THREE").
2. **Folder name = exam month** from the printed date: `2025-09`. Use `YYYY-00` if only the year is known. If the course already has a paper that month for another students' department, add a suffix (`2025-09-eee`). If the course folder or `course.yaml` does not exist yet, stop and ask the user. A new course needs a topic tree first.
3. **Write `paper.yaml`** like the existing ones: `schema`, `course`, `kind: term-final`, `exam_date`, `session`, `level_term`, `students_dept`, `full_marks`, `duration`, `sections` (with `questions`, `answer_any`, `rule`), `source: {file: <scan file name>}`, and `transcription: {by: [], checked_by: []}`. Do **not** put faculty here. Faculty come from `teaching.yaml` through the session. If the user says who taught, add or extend that session's line in `bank/<DEPT>/teaching.yaml` (and any new initials in `faculty.yaml`).
4. **One file per part**, named `q5a.md`, or `q5.md` when a question has no parts:
   - Shared text that several parts depend on goes in the stem `q5.md` (no `topics`), and the parts go in `q5a.md`, `q5b.md` ...
   - Split a part into `q5a-i.md`, `q5a-ii.md` (with the stem `q5a.md`) only when its sub-parts are on different topics or carry separate marks worth filtering. Otherwise keep `(i) (ii)` inside the part.
   - Front matter: `marks` (for that part) and `topics` (ids from `course.yaml`; the first one is where the part is filed). Optional fields: `kind` (numerical / conceptual / diagram / code / analysis), `mandatory: true`, `note` (transcription remarks).
5. **Transcription rules**:
   - Keep the paper's wording, including typos. Mention a typo in `note:` ("Printed as 'ivolved'"); never silently fix it.
   - Math in `$...$`; display math on its own lines as `$$...$$`. Use only KaTeX-compatible commands; no `\input`, `\def` and the like.
   - Tables as pipe tables. Code as fenced blocks with a language (```` ```c ````). Keep marks breakdowns like `(6+3+3=12)`.
   - Sub-items `(i)`, `(ii)` and `(a)`, `(b)` each start their own paragraph (blank line between them), with no indentation. GitHub shows indented lines as code.
   - Figures you cannot express as a table or code: save a crop as `figures/q5b-1.png` if you can. Otherwise add `![Figure for Q5(b)](figures/q5b-1.png)` and a `note:` saying the figure still needs cropping.
6. **Topics**: choose from `course.yaml`. If a part needs a topic that does not exist, do not invent an id in the part. Propose the addition (id, name, parent, aliases) to the user, and add it to `course.yaml` only if they agree.
7. Run `.venv/bin/tfsolve check -c <COURSE>` and fix every error, warning and `layout:` line using `rendering.md`. Repeat until **CHECK OK**.
8. Report back:
   - the folder and the files written;
   - anything illegible or uncertain (quote it);
   - the topic tags you chose.

   Ask the user (or a friend) to check the files against the scan. When they confirm, add their GitHub username to `transcription.checked_by`.
