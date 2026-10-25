# ExecAuthorCounter — round 72, wave 1 (build): the C1 frozen counter

**Verdict.** `check_author_rules.py` is drafted, frozen and exercisable:
`.ufo/waves/round-72/w1/build/ExecAuthorCounter/check_author_rules.py` (843 lines,
blanked `SELF_SHA = ce86a966…`, sha self-check green). `--self-test` drives `main()` over
**16 isolated local git worlds / 47 assertions, 0 failures**; the base run prints
`author-facing rules in SKILL.md 0 of 4` and exits **1** (the do-nothing control the plan froze at
`plans/round-72.md:98`); a real-data rehearsal built from the *scribes' own box prose* reaches
`4 of 4` exit 0 once the A4 id is real and its pin slot is filled, and exits **2** (never a pass)
while the slot is empty. Three integration items are the L1's and are named in §5; none is a blocker
for this seat. No committed lane file was touched (`git status --porcelain` shows only untracked
`.ufo/...` paths), no tool was installed, and every scratch dir (`/tmp/k72w1-ExecAuthorCounter.*`)
is deleted.

The frozen predicate is carried verbatim in the counter's docstring and implemented as one sentence:

```
plans/round-72.md:76
python3 -B verifiers/check_author_rules.py --rev <rev>  ->  prints "author-facing rules in SKILL.md N of 4", exit 0 when N == 4
```

## 1. What the counter checks (conjuncts exactly as frozen, no reinterpretation)

Per rule `Ai` (A1 name uniqueness, A2 authority level, A3 install-path trust, A4 rung), over committed
bytes only, no instrument of the measured tree executed:

- **(a)** rendered `SKILL.md` (HTML comments + fenced blocks stripped, the r71 `check_skill_evals_v2`
  shape) holds **exactly one** `- [ ] ` box inside `## Trigger-fidelity checklist` (`SKILL.md:253`, up
  to the next `## ` at `:328`) whose text carries the frozen token set as whole words and ends with
  `(sourced: S###[, S###…]; entry: <frozen entry path>)`, the cited ids being a **subset** of that
  entry's own `source:` ids;
- **(b)** each cited id is exactly one **11-cell** registry row at `--rev`, status `mined`, tier `A`
  or `B`, `used-by` listing the cited entry path as an exact comma-separated item;
- **(c)** the entry exists at `--rev`, opens with `source:` lines naming every cited id, then
  `verified-at:` and `recheck:`;
- **(d)** A4 only — the located quote (5–25 words) is found word-bounded in a committed, sha256-pinned
  snapshot under `.ufo/waves/round-72/snapshots/`; an empty slot, an absent snapshot or a sha mismatch
  is **exit 2**.

Two readings are deliberately stricter than the naive one and are named in the docstring so a critic
can attack them rather than discover them: the token set is matched **with the tail removed** (two of
the four entry paths contain a rule token — `client-trust-gates-round68` carries `trust`,
`instruction-authority-ladder-round67` carries `authority` — so matching the whole joined box would let
the citation supply the token the prose must carry); and the located quote is the `located quote "…"`
span (the lane's r67/r68/r69 convention), not any quoted span on the line. Both are proved
load-bearing by worlds 6 and 12 below.

Exit codes: **0** iff `N == 4`; **1** otherwise; **2** when the counter cannot evaluate (no `--rev`,
not a commit, not a lane worktree, counter sha drift, missing/tampered/unfilled snapshot, unreadable
box map).

## 2. Self-test — 16 worlds, 47 assertions, 0 failures

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecAuthorCounter/check_author_rules.py --self-test
PASS honest world scores 4 of 4: exit 0
PASS (a) box hidden in an HTML comment: exit 1
PASS (a) box hidden in a fenced block: exit 1
PASS (a) box moved outside the checklist section: exit 1
PASS (a) tail cites an id the entry never names: exit 1
PASS (a) rule tokens supplied only by the tail's entry path: exit 1
PASS (a) two boxes carry the same rule: exit 1
PASS (b) cited row is queued, not mined: exit 1
PASS (b) cited row's used-by omits the entry: exit 1
PASS (b) cited id resolves in no registry row: exit 1
PASS (c) entry without verified-at:: exit 1
PASS (d) A4 quote absent from its snapshot: exit 1
PASS (d) tampered snapshot: exit 2
PASS (d) unfilled pin slot: exit 2
PASS (d) snapshot not committed at the measured rev: exit 2
PASS section heading absent reads 0 of 4: exit 1
self-test: 0 failure(s) over 47 assertions
EXIT=0
```

Every world is a fresh `mktemp -d` repo (`git init -q`, toplevel verified equal to the dir before the
first commit, throwaway identity passed per call, dir removed in `finally`) — Q48: no lane, fleet or
shared index is touched. Each broken world asserts **three** things: the exit code, the exact frozen
line (`… 3 of 4` / `… 0 of 4`), and the finding text that names the broken conjunct, so a world cannot
pass for the wrong reason.

## 3. Base run — the do-nothing control

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecAuthorCounter/check_author_rules.py \
      --repo . --rev c69711ee08279609374d895bb0f3c8c18ccf15c9
measured-rev: c69711ee08279609374d895bb0f3c8c18ccf15c9
author-facing rules in SKILL.md 0 of 4
  A1: 0 checklist box(es) carry tokens ['name', 'unique', 'precedence'] + a tail naming corpus/knowledge/skill-name-precedence-round69.md (want exactly 1; 15 box(es) in the section)
  A2: 0 checklist box(es) carry tokens ['authority', 'level', 'body'] + a tail naming corpus/knowledge/instruction-authority-ladder-round67.md (want exactly 1; 15 box(es) in the section)
  A3: 0 checklist box(es) carry tokens ['install', 'trust', 'command'] + a tail naming corpus/knowledge/client-trust-gates-round68.md (want exactly 1; 15 box(es) in the section)
  A4: 0 checklist box(es) carry tokens ['prompt', 'always-on', 'skill', 'index'] + a tail naming corpus/knowledge/resident-index-and-rungs-round72.md (want exactly 1; 15 box(es) in the section)
EXIT=1
```

`15 box(es) in the section` is an independent cross-check of the extractor: the section's own prose
says "Eight of the fifteen boxes", and `verify_skill_checklist.py` reads `section_boxes 15` (the
ScribeBoxesB report measured the same number). The counter finds the same 15 and no tail, so `0 of 4`
is the section's real state, not a parsing artifact.

Exit-2 paths, each observed:

```
$ python3 -B … --repo . --rev deadbeef
environment error: --rev deadbeef is not a commit                              EXIT=2
$ cp … /tmp/k72-drift.py && printf '\n# drift\n' >> /tmp/k72-drift.py && python3 -B /tmp/k72-drift.py --repo . --rev c69711e
environment error: counter drifted — the running file is not the frozen counter EXIT=2
$ python3 -B … --repo . --rev c69711e --census-check
… author-facing rules in SKILL.md 0 of 4 … census validate: conformant         EXIT=1
```

`--census-check` is second evidence only (never the verdict): `sources-census.sh validate --file` over
the revision's extracted registry reads `conformant` at the base, so the registry the (b) conjunct
reads row by row is also census-clean.

## 4. Real-data rehearsal — the scribes' own prose, in a `--shared` clone

Sandbox: `D=$(mktemp -d /tmp/k72w1-ExecAuthorCounter.XXXX)`; `git clone --shared -q <lane> $D/lane`;
every commit inside `$D/lane` only. Boxes were extracted **verbatim** from the wave-1 scribe drafts
(`.ufo/waves/round-72/w1/ScribeBoxesA.md`, `ScribeBoxesB.md`), not retyped.

| world (commit in the sandbox) | command | observed |
|---|---|---|
| A1+A2+A3 drafted boxes spliced before `## Agent-definition fidelity checklist` | `check_author_rules.py --repo $D/lane --rev HEAD` | `author-facing rules in SKILL.md 3 of 4`; only `A4: 0 checklist box(es) … (18 box(es) in the section)`; exit 1 |
| + the A4 draft **verbatim**, tail `(sourced: S2XX; entry: corpus/knowledge/resident-index-and-rungs-round72.md)` | same | `3 of 4`; `A4: 0 checklist box(es) … (19 box(es) in the section)`; exit 1 |
| + `S261` in place of `S2XX`, an A4 entry, an 11-cell `S261` row, a committed snapshot | same, delivered pins | `environment error: SNAPSHOT_PINS['S261'] is an unfilled slot ('', '') …`; exit **2** |
| same tree, counter copy with the slot filled `("S261-letta-skills.md", 0067268a…)` | same | `author-facing rules in SKILL.md 4 of 4`; exit **0** |

So the counter is **satisfiable on the real lane**, not only on its own fixture: the drafted A1/A2/A3
prose (including A1's tail split across a line break, `(sourced: S203,` / `S204, …`) and the drafted A4
prose both parse, and the A4 placeholder `S2XX` is rejected by the `S\d{3,}` shape exactly as
ScribeBoxesB predicted. The empty pin slot turns a complete-looking landing into exit 2 — it can never
read 4 by accident.

`--box-proof` (added for the checklist map; the gate's `delegated_box_proof` runs
`<instrument> --box-proof --map <map>` and takes the first stdout line as its detail):

```
$ python3 -B … --box-proof --map verifiers/checklist-baseline.json
box proof: the map delegates 0 box(es) to check_author_rules.py (want 4)      EXIT=1
$ python3 -B … --box-proof --map /tmp/k72-map.json     # map with 4 boxes delegated to this file
boxes proven 4                                                                EXIT=0   (wall 0.34 s)
```

It reuses the same 16-world table, so the proof is the self-test's evidence: each delegated rule is
held by the satisfying world and dropped by a world that breaks one of its conjuncts.

## 5. Integration items for the L1 (measured, not inherited)

1. **Line budget.** `wc -l SKILL.md` → `600`; the base receipt reads
   `PASS trigger.line_budget: evaluated 600 — 600 lines within budget 600 (from box at line 320)`
   (`.ufo/waves/round-72/receipts/base-outputs/verify_skill_checklist.out`). In the sandbox the three
   4-line drafted boxes added **+13** lines and the A4 box **+4** — **+17** for four boxes at the
   drafts' shape (600 → 617). Landing needs ≥17 lines freed first (or a ≤2-line box shape).
2. **Checklist map.** `verifiers/checklist-baseline.json` is `boxes[]` of
   `{box_id, section, text_sha256, disposition}` plus `box_total`; adding four boxes needs four entries
   and `box_total 41 → 43` (ScribeBoxesA already recorded the same requirement for its two). If the
   boxes are mapped `delegated:verifiers/check_author_rules.py`, this counter's `--box-proof` keeps
   `checklist.box_map_complete` green; otherwise use `unexecuted:<reason>` (the gate then reports "no
   --box-proof support, not run" and stays green).
3. **Pin slots and the gate row.** `SNAPSHOT_PINS` ships eight named empty slots —
   `S248, S254, S255, S256, S261, S262, S263, S264` — each `("", "")`; the L1 fills
   `(filename under .ufo/waves/round-72/snapshots/, sha256)`. The lane's snapshot dir now holds 23
   files for exactly those ids, with `.sha256` sidecars for six (`ls .ufo/waves/round-72/snapshots/*.sha256 | wc -l`
   → `6`; S254/S255 have no sidecar yet, so their sha256 must be computed). A cited id with **no** slot
   is also exit 2, so an unlisted A4 citation cannot pass. Separately,
   `grep -c check_author_rules verifiers/check_gate_registry.py` → `0`: the L1 must add the gate row
   (the registry is already red at base, `conformant 51 of 53`).

## 6. Risks a wave-2 seat should attack

- **Token-without-tail reading.** Matching tokens against the box minus its tail is my reading of "(a)
  … carries the rule's token set"; it is stricter than the literal sentence and is proved by world 6
  (`trust` in `client-trust-gates-round68.md` cannot supply A3). If the L1 prefers the literal reading,
  the change is one line in `rule_holds` — and it must be made **before** data, never after (Q28).
- **Located-quote reading.** `located quote "…"` wins over any other quoted span on the same line; with
  no such phrase the `source:` line's single quoted span is used. An entry that quotes two different
  located quotes for one row fails as ambiguous rather than passing on one of them.
- **Not machine-checked, by construction:** whether the box prose actually *means* the rule it cites
  (semantic agreement stays a named non-author spot-check duty, unchanged from r71's boundary), and
  whether the snapshot is the right page (sha pinning proves identity of bytes, not provenance).
- **`--box-proof` runs 16 git worlds in ~0.34 s**; it writes only under `mktemp -d`. If a future
  `BOX_PROOF_TIMEOUT` in the checklist gate is tighter than that, the delegation note degrades to "not
  run", not to a false pass.

## 7. Evidence index

| claim | command / file |
|---|---|
| counter exists, sha-frozen | `.ufo/waves/round-72/w1/build/ExecAuthorCounter/check_author_rules.py`; `_blanked_sha(src) == SELF_SHA` → `True` |
| 16 worlds / 47 assertions | `--self-test` output in §2 |
| base 0 of 4, exit 1 | §3, `--rev c69711ee08279609374d895bb0f3c8c18ccf15c9` |
| real prose reaches 4 of 4 | §4 table, sandbox commits in a deleted `mktemp -d` clone |
| empty slot is exit 2 | §4 row 3; §2 worlds 14–16 |
| 15 boxes in the section | §3 output; `SKILL.md:253`, `SKILL.md:328`; `verify_skill_checklist.py` receipt |
| nothing landed | `git status --porcelain` → only `?? .ufo/waves/round-72/…` |
