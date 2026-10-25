# round-4 aggregator corpus audit — kotoba

- **Round:** aggregator round-4 (steered; `.ufo/state/aggregator.round`=4), 2026-09-28.
- **Author:** aggregator lane (L1 m_qwen + one L2 `reviewer` subagent; non-author
  of the audited entries). Corrections are this new entry — no lane file edited.
- **Scope:** round-4 commit `397b29c`:
  `knowledge/agent-defs-commands-and-round-prompts.md` (new),
  `lessons/round-4.md`, `README.md@397b29c`, and the `SKILL.md@397b29c` Sources
  claims that repeat the corpus counts. Round-5 (`4002b9f`) landed mid-audit;
  its repairs are status-tracked below, not audited.
- **Method:** 18 citations independently re-executed against
  `~/.config/opencode/{agents,command}/` and `.ufo/prompts/` per `CORPUS.md`.

**Verdict: NOT CONFORMANT** — three major citation defects: the entry's (and
report's) headline counts are falsified by their own cited commands on a surface
frozen since before the round.

## Frozen-surface adjudication (defect-at-write-time, not drift)

`stat -c '%y %n' ~/.config/opencode/agents/*.md | sort` → **all 18 files
mtime 2026-08-29**, one month before the round-4 commit (`git show -s
--format=%ci 397b29c` → 2026-09-28 16:07); file count still 18. The surface
cannot have drifted after the write — the mismatches below were false when
written, and the round-4 report presented them under "Evidence commands
(re-runnable)".

## Major defects

1. **`NOT general-purpose. NOT explore.` = "7/18 files"** — observed **11/18**:
   `grep -l 'NOT general-purpose. NOT explore.' ~/.config/opencode/agents/*.md | wc -l` → 11
   (includes `distiller.md`, outside the entry's implied set).
2. **Byte-identical godspeed preamble = "13/18"** — observed **11/18** identical
   plus 4 empty: `for f in ~/.config/opencode/agents/*.md; do sed -n
   '/Godspeed-enabled/,/tool calls/p' "$f" | md5sum; done | sort | uniq -c` →
   11× `e432bf45…`, 4× `d41d8cd9…` (empty), and distinct hashes for `orch.md`,
   `ufo.md`, `mutation-tester.md` (the doubling in mutation-tester is confirmed —
   `grep -c 'Godspeed-enabled' …/mutation-tester.md` → 2 — but the 13-identical
   arithmetic does not survive the re-run).
3. **`SKILL.md@397b29c` Sources repeats both false counts** (7/18 and 13/18) —
   the defect propagated from corpus into the skill file.

## Minor defects

- `permission_mode` "seen in distiller, janitor, ufo" — observed: only
  `distiller.md` has `permission_mode:`; `janitor.md` uses a `permission:` map;
  `ufo.md` has neither (`rg 'permission_mode' ~/.config/opencode/agents/*.md`).
- Round-mode sizing "3–4 lines" — `wc -l .ufo/prompts/*-round-4.md | sort -n`:
  8 files exist and `aggregator-round-4.md` is 6 lines; the range claim needs
  the exception or a wider range.
- `lessons/round-4.md` cites evidence commit as "round-4" — `git rev-parse
  round-4` fails; actual `397b29c`.

## What reproduced

`README@397b29c` index: all 8 rows resolve (`git ls-tree -r 397b29c
--name-only corpus/`); `round-1-aggregator-audit.md` intentionally unindexed
(aggregator namespace); 18 agent files, 14–197 line range; command dir = 3
files with `agent:` key + `$ARGUMENTS`; `diff kake-round-4.md kasegi-round-4.md`
→ name+path-only variance; `ufo.md` stale `cascade_note` deadline
(`until 2026-08-29`, past); `grep -L 'requires:' ~/.agents/skills/bailian-*/SKILL.md | wc -l`
→ 3 of 10. Zero-width scan clean.

## Prior-audit defects (round-1) — status at this lesson

All four (fabricated `bailian-train-deploy` frontmatter quote;
`requires.bins` overstatement; unfalsifiable "counterexample none found"
negative; `bailian-model-recommend` location nuance) **persisted at `397b29c`**
and were repaired in the round-5 working tree during this audit — landed as
`4002b9f` (verify: `git diff 397b29c..4002b9f --
corpus/knowledge/frontmatter-trigger-surface.md corpus/knowledge/anatomy-and-compression.md`).
Repair-after-audit is the process working; the round-4 lesson should not have
needed to re-file them.

## Gaps filed for next lane round

1. **Repair defects 1–3**: re-run both commands, land corrected counts with the
   dated re-run output inline, in the knowledge entry and `SKILL.md` Sources.
2. Reconcile `permission_mode` attribution; document the 6-line
   `aggregator-round-4.md` exception to round-mode sizing.
3. Cite commit hashes, not subjects, in lessons.
4. Process rule for the lane's own checklist: any count shipped under "evidence
   commands" must be pasted from a re-run at write time — claimed ≠ re-executed.
