---
name: solve
description: Write AI solutions for tfsolve question parts that have none, current teachers' questions first. Use for "/solve CSE313", "/solve bank/CSE/CSE313/2025-09" or "/solve bank/CSE/CSE313/2025-09/q5a.md".
---

# Solve question parts

Writes `solutions/<part>/ai.md` next to the question. Follow the formatting rules in `.claude/skills/add-paper/rendering.md`. Every AI solution starts as `status: unverified`. **Never** set `reviewed` or `verified`, and never edit a solution written by a person (any file other than `ai.md`).

## Which parts

- Given a single part file: solve that part.
- Given an exam folder or a course: run `.venv/bin/tfsolve todo -c <COURSE> -n 200`. Solve the listed parts without a solution **in that order**; lines marked `*` are set by this term's teachers and come first. Skip parts that already have an `ai.md` unless the user asks for a redo.
- Work one exam at a time and report between exams (usage limits).

## For each part

1. Read the part file, its stem(s) (`q5.md`, `q5a.md` for `q5a-ii.md`), `paper.yaml`, the course's `course.yaml` (topic names and any slide references), and the solutions of **similar parts in other years** (same topic). Faculty repeat questions, so match the conventions of earlier answers (notation, assumptions, level of detail). If a hint in the paper defines a notation (e.g. the clock-hand `*`), follow it.
2. **Numerical questions**: compute the answer with a short script (Banker's safety check, scheduling Gantt charts, page-replacement simulation, table sizes) before writing it, and make the written steps match the computation. If the paper is ambiguous (priority direction, RR queue order, average vs. maximum seek), state the assumption you used and, if cheap, the result under the other reading.
3. Write the solution at exam length, as a student would write it for full marks: steps, units, the final answer in bold, a table or ```` ```gantt ```` block where the question asks for one (`P1 0 30` per line, `# caption` optional). Refer to the course textbook where it helps (CSE313: Tanenbaum *MOS* for Section A, OSTEP for Section B).
4. Front matter:

   ```yaml
   author: ai
   via: claude-code
   model: <the model id you are running as>
   prompt: solve-v1
   created: <YYYY-MM-DD>
   status: unverified
   summary: "<one-line final answer>"
   sources: ["<slides / textbook section>"]
   ```
5. Run `.venv/bin/tfsolve check -c <COURSE>` and fix every problem it reports (see `rendering.md`) until **CHECK OK**.
6. Report back:
   - which parts you solved;
   - any answer you are unsure of, and why.

   Remind the user that these need a human check before they count as `reviewed`.
