# tfsolve: notes for Claude

A Git-backed bank of BUET term-final questions and solutions, plus a CLI that compiles filtered PDFs. Design and decisions: `PROJECT_PLAN.md` (local only, not in Git). Owner: ummehabiba16.

## Adding content

- **A question paper (PDF or photos), with or without a faculty list** → follow `.claude/skills/add-paper/SKILL.md`. Do this even if the user doesn't type `/add-paper`.
- Only transcribing → `.claude/skills/transcribe/SKILL.md`. Only solving → `.claude/skills/solve/SKILL.md`.
- Formatting rules and fixes for rendering problems: `.claude/skills/add-paper/rendering.md`.

## Commands (use the project venv)

```bash
.venv/bin/tfsolve check -c CSE313        # lint + PDF build; must end with CHECK OK
.venv/bin/tfsolve pages scan.pdf         # scanned PDF -> PNG pages you can read
.venv/bin/tfsolve todo -c CSE313         # what to add/solve/review, current teachers first
.venv/bin/tfsolve -c CSE313 -f current   # build a PDF
```

If `.venv` is missing: `python3 -m venv .venv && .venv/bin/pip install -e '.[scan]'`.

## Rules

- Layout: `bank/<DEPT>/<COURSE>/<YYYY-MM exam month>/` holds `paper.yaml`, `q5a.md` and `solutions/q5a/<author>.md`. Faculty live only in `bank/<DEPT>/teaching.yaml` (by session), never in paper files.
- Transcribe faithfully: keep typos and note them in `note:`.
- AI solutions: `author: ai`, `status: unverified`. Never mark anything reviewed or verified, and never edit a person's solution.
- When fixing an existing solution, add a dated line to its `changes:` list saying what changed and why.
- Don't re-run `tools/import_legacy.py`; its output has been hand-edited.
- Don't commit or push unless the user asks.
