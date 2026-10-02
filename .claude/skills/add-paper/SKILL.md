---
name: add-paper
description: One-stop workflow to add BUET term-final papers to the tfsolve bank. Takes a scanned question paper (PDF or photos) and optionally a faculty list; updates the faculty sheet, transcribes the paper into the right exam folder, writes AI solutions for the new questions (or only the teachers the user names), and checks that everything renders. Use when the user uploads or points to a question paper, e.g. "/add-paper ~/Downloads/CSE313-2021.pdf" or "add this paper, faculty list attached".
---

# Add a paper (faculty list → questions → solutions → check)

The whole job ends only when `.venv/bin/tfsolve check` prints **CHECK OK**. Work from the repository root. The Python environment is `.venv/`; if it is missing, run `python3 -m venv .venv && .venv/bin/pip install -e '.[scan]'`.

Read these before starting:
- `.claude/skills/add-paper/rendering.md`: the formatting rules and the fix for every known rendering problem;
- one existing exam folder of the same course (for example `bank/CSE/CSE313/2025-09/`), to copy its conventions.

## 1. Understand what you were given

- **The paper**: a PDF path, an attached PDF, or photos.
  - For a PDF, render it with `.venv/bin/tfsolve pages <file.pdf>` (`--dpi 200` for small print) and read every PNG it lists. Do not rely on the PDF's text layer: scans have none, or a bad one.
  - Photos can be read directly.
- **The faculty list** (optional): any format, e.g. `2019-2020 ABC, XYZ`, a table, a photo of a sheet. It says who taught a course in which session, and sometimes which section each person set.
- **Several papers at once**: handle them one at a time. Finish steps 2 to 6 for each before starting the next.

## 2. Faculty sheet → `bank/<DEPT>/teaching.yaml`

- Add every initial to `bank/<DEPT>/faculty.yaml` (uppercase, `XYZ: {}`).
- Add each course and session to `teaching.yaml`:
  - `"2019-20": {A: [ABC], B: [XYZ]}` when the sheet says which section each teacher set;
  - `"2019-20": [ABC, XYZ]` when it does not. Never guess sections.
- Sessions are written `YYYY-YY`.
- Do not overwrite an existing line that disagrees with the new list. Show the user both versions and ask which is right.

## 3. Transcribe

Follow `.claude/skills/transcribe/SKILL.md` (steps 1-6). The result is `bank/<DEPT>/<COURSE>/<YYYY-MM>/` with `paper.yaml` and one `qN<letter>.md` per part, tagged with topics.

- If the **course has no `course.yaml` yet**, create it before transcribing:
  - copy the structure of `bank/CSE/CSE313/course.yaml`;
  - give it a topic tree (5-12 top-level topics with children and aliases), built from the course syllabus if the user gives it, else from this paper's questions plus the standard textbook chapter structure;
  - show the tree to the user and continue once they accept it.
- If the department folder is new, also create `dept.yaml`, `faculty.yaml` and `teaching.yaml` there.
- If a paper for that course and month already exists, stop and ask. It may be the same paper.

## 4. Solve

Following `.claude/skills/solve/SKILL.md`, solve the parts of the new paper that have no solution.

- If the user named teachers ("solve only ABC's parts"), run `.venv/bin/tfsolve todo -c <COURSE> -f ABC -n 200` and solve just those. The other parts stay unsolved in their exam folder and show up in `todo` later.
- If the user said not to solve, skip this step.

## 5. Check and fix until clean

Run `.venv/bin/tfsolve check -c <COURSE>`.

- Fix every lint error and warning, and every `layout:` line, using `rendering.md` (each problem named there has a known fix). Run the check again. Repeat until it prints **CHECK OK**.
- If a problem cannot be fixed without changing the meaning of a question, leave the text faithful and tell the user.
- Then look at the new paper's pages yourself:
  1. `.venv/bin/tfsolve -c <COURSE> -y <YYYY-MM> -o out/new-paper.pdf`
  2. `.venv/bin/tfsolve pages out/new-paper.pdf --dpi 70`
  3. Read the PNGs. Tables, lists, code, math and Gantt charts should look like the scan.

## 6. Report to the user

Keep it short:
- the folder and part count;
- which parts were solved and which were left for later;
- any illegible text, assumptions or uncertain answers (quote them);
- changes made to `teaching.yaml` and `course.yaml`.

Then remind them:
- to compare the files with the scan and add their GitHub username to `transcription.checked_by`;
- that every AI solution stays "not yet verified" until a person reviews it.

Do not commit. The user decides when to commit.
