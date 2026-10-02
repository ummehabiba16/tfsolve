# tfsolve

A community question bank for **BUET term finals**. Filter past questions by **course × topic × faculty × year** and get a LaTeX PDF with solutions:

**1. A whole course, arranged:**

```bash
tfsolve -c CSE313 -topicwise     # one chapter per topic; the contents list every question under its topic
tfsolve -c CSE313 -yearwise      # one chapter per exam; the contents list every question under its exam
```

**2. One teacher (`-f`), 3. chosen years (`-y`):**

```bash
tfsolve -c CSE313 -topicwise -f ABC          # only the questions ABC set
tfsolve list years -c CSE313                 # which exam years are available
tfsolve -c CSE313 -yearwise -y 2021..2025    # exams from 2021 to 2025
```

`tfsolve help` prints a short guide. The [website](https://ummehabiba16.github.io/tfsolve) has the same choices: an **Arrange: by topic / by year** switch, then teacher and year filters, plus a Help page.

`ABC` stands for a teacher's initials; `tfsolve list faculty -c CSE313` shows the real ones.

Every solution in a PDF carries a badge: **verified**, **reviewed**, **not yet verified** (every AI solution starts here) or **disputed**.

Created and maintained by **[ummehabiba16](https://github.com/ummehabiba16)**. The code was written with [Claude](https://www.anthropic.com/claude) (Anthropic) through Claude Code; see [Credits](#credits).

## Install (Windows, macOS, Linux)

Needs Python 3.10 or newer. Pandoc comes bundled.

```bash
pip install tfsolve
tfsolve update                    # downloads the question bank (run again to get new papers)
tfsolve doctor                    # checks your LaTeX setup
tfsolve -c CSE313 -topicwise      # PDF lands in out/
```

- **PDFs need LaTeX with XeLaTeX:**
  - Windows: [MiKTeX](https://miktex.org), which installs missing packages on first use.
  - macOS: MacTeX or BasicTeX.
  - Linux: `texlive-xetex texlive-latex-extra texlive-pictures fonts-lmodern`.
- **No LaTeX?** Add `--tex`. You get a `.tex` file to upload to [Overleaf](https://www.overleaf.com), where you compile with XeLaTeX.
- **Contributors work in a clone instead:**
  1. `git clone`, then `python -m venv .venv`, then `.venv/bin/pip install -e '.[scan]'`.
  2. Inside the clone, `tfsolve` uses your local `bank/` directly.

| Command | What it does |
|---|---|
| `tfsolve -c COURSE -topicwise` / `-yearwise` | Build a PDF of the whole course, arranged topic by topic or exam by exam, with a matching table of contents. Topicwise is the default. |
| `... -f ABC`, `... -y 2025`, `-t TOPIC`, `--session 2023-24` | Narrow it down. Without `-f`, all faculty are included. Repeat a flag for OR (`-f ABC -f XYZ`); different flags combine with AND. |
| `tfsolve help` | A short guide to all of the above. |
| `tfsolve list years -c COURSE` | The exam years, exam folders and sessions in the bank, with the value to pass to `-y` or `--session`. |
| `tfsolve list courses\|topics\|exams\|faculty -c COURSE` | See what is in the bank. `list topics -f ABC` counts one teacher's topics. |
| `tfsolve todo [-c COURSE] [-f ABC]` | Missing papers, unsolved parts and unreviewed solutions, newest exams first. `-f` limits it to chosen teachers. |
| `tfsolve lint` | Check the bank for mistakes. CI runs this on every pull request. |
| `tfsolve check [-c COURSE]` | Lint, build the PDF, and name every part whose layout breaks (text off the page, missing symbols). Must end with `CHECK OK`. |
| `tfsolve pages scan.pdf` | Turn a scanned paper into page images (used when transcribing). |
| `tfsolve doctor` | Check that Pandoc and LaTeX are ready. |
| `tfsolve web [-o site]` | Build the website: plain HTML you can open from `site/index.html`, filter by topic, teacher and exam, and print. No LaTeX needed. |

Year options:
- `-y 2025` (exam year);
- `-y 2021..2025` (range);
- `-y 2025-09` (one exam, by month);
- `--session 2023-24` (as printed on the paper).

If nothing matches, tfsolve lists the years that exist.

Output options: `--solutions best|all|none|human|ai`, `--answers-at-end`, `-o file.pdf`, `--tex` (keeps the `.tex` too, e.g. for Overleaf).

## How the bank is organised

Files are stored **by exam paper**. Topics are **tags**, so a part that covers two topics is never duplicated.

```text
bank/CSE/
├── dept.yaml                 department code and name
├── faculty.yaml              initials, e.g. ABC, XYZ
├── teaching.yaml             the faculty sheet: course → session → section → teacher
└── CSE313/
    ├── course.yaml           topic tree + aliases (pagetable → paging)
    └── 2025-09/              one exam, named by the month it was held
        ├── paper.yaml        date, session, sections
        ├── q1a.md            one file per question part: front matter + Markdown/LaTeX math
        ├── q7a.md            a shared setup ("stem") for q7a-i, q7a-ii …
        └── solutions/q1a/ai.md, solutions/q1a/<github-username>.md
```

A question part looks like this; GitHub renders the math:

```markdown
---
marks: 15
topics: [bankers-safety-check, safe-vs-unsafe]
---
Consider a system with 4 processes and 3 resource types: A (9 units), B (3 units), C (6 units) …
```

Faculty are not typed into every question. Each paper has a `session`, and `teaching.yaml` says who set each section in that session.

## Adding papers with Claude Code

The repo includes Claude Code skills in `.claude/skills/`, plus a `CLAUDE.md` that every new Claude Code session reads. Open Claude Code **in this folder** (desktop app or `claude` in a terminal), attach the scanned paper, and type:

```text
/add-paper ~/Downloads/CSE313-2021.pdf
Faculty: CSE313 2021-2022 A: ABC, B: XYZ.
```

It will:
1. add the faculty list to `teaching.yaml`;
2. transcribe the paper into `bank/<DEPT>/<COURSE>/<exam month>/`, tagging each part with topics;
3. write AI solutions for the new parts (or only for the teachers you name, e.g. "solve only ABC's parts");
4. run `tfsolve check` and fix layout problems until it passes;
5. report anything it couldn't read.

Plain English works too ("add this paper"). Nothing is committed until you say so.

| Skill | Use it for |
|---|---|
| `/add-paper` | Everything at once: faculty list → questions → solutions → check |
| `/transcribe` | Only turn a scan into question files |
| `/solve` | Only write missing solutions, in `tfsolve todo` order (e.g. `/solve CSE313`, or "solve ABC's parts in CSE313") |

Afterwards, compare the new files with the scan and add your GitHub username to `transcription.checked_by` in `paper.yaml`. Rendering rules and fixes are in [rendering.md](https://github.com/ummehabiba16/tfsolve/blob/main/.claude/skills/add-paper/rendering.md).

These skills only work in **Claude Code**, because they read and write files in this repo. A regular Claude chat on the web can't write into the repo.

## Contributing

1. Fork, then add or fix files: a new paper, a solution in `solutions/<part>/<your-github-username>.md`, or a review.
2. Run `tfsolve lint`.
3. Open a pull request. A course maintainer reviews it.

Mark a solution `status: reviewed` (and add yourself to `reviewed_by`) only after working through it yourself.

## Credits

- **[ummehabiba16](https://github.com/ummehabiba16)**: project owner. Idea, requirements and design decisions; the CSE313 question data (paper transcriptions, topic tags, faculty mapping) and the first set of solutions.
- **Claude (Anthropic), via Claude Code**, working under the owner's direction:
  - wrote the `tfsolve` code (`src/tfsolve/`, `tools/`) and the Claude Code skills;
  - converted the original CSE313 material into this bank format;
  - reviewed the imported solutions; the corrections are listed in each solution file's `changes:`.
- **AI-written solutions** are marked `author: ai`. They stay *not yet verified* until a person checks them.
- Contributors of papers, solutions and reviews are credited in the files they wrote (`author`, `reviewed_by`, `transcription.by`) and in the Git history.

## Licence and notice

Code: MIT ([LICENSE](https://github.com/ummehabiba16/tfsolve/blob/main/LICENSE)). Transcriptions, tags and solutions: CC BY-NC-SA 4.0 ([LICENSE-CONTENT](https://github.com/ummehabiba16/tfsolve/blob/main/LICENSE-CONTENT)).
The original question papers belong to BUET and are reproduced here for non-commercial study. For a correction or takedown request, open an issue. Requests are handled promptly.
