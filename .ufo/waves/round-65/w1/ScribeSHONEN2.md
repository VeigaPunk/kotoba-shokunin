# ScribeSHONEN2 — round 65, wave 1 — SHONEN box-1 re-run at `0e104f49`

Seat: scribe (`ScribeSHONEN2`), leaf member, no subagent dispatch.
Assignment: re-run the SHONEN box-1 counting commands at `0e104f49` (the 18-row Sources count,
the gate registry 42-of-42 run), verify the refreshed evidence lines name real revs, verify the
box-2/box-3 pointers still resolve.

**Behavior:** re-derived both counts from the landed bytes at the wave base; resolved every rev
named in the refreshed line; re-measured every number the line attributes to a rev; walked the
box-2 and box-3 pointer chains line by line. Wrote nothing except this file.

## Method (read-only, out of the lane worktree)

The lane worktree is at round-66 `2a8eba5`, past the wave base, and the lane's jj/git state is
out of bounds. All measurement was done on byte-identical copies:

```
git archive --format=tar 0e104f49 | tar -x -C /tmp/shonen2            # exit 0, 142 MB
git clone --quiet --shared --no-checkout <lane> /tmp/r65clone         # exit 0
git -C /tmp/r65clone checkout -q 0e104f49                             # exit 0
git -C /tmp/r65clone rev-parse HEAD
→ 0e104f498b3df1466284074c5b3a6e5b523420cd
git -C /tmp/r65clone status --porcelain | wc -l
→ 0
```

`--shared` uses the lane's object store read-only (alternates in the destination); no lane
object, ref, index or worktree byte was written. Instrument bytes match the wave base exactly:

```
sha256sum /tmp/shonen2/verifiers/check_gate_registry.py /tmp/r65clone/verifiers/check_gate_registry.py
→ 01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce  (both)
```

Tooling: GNU Awk 5.4.1 (`/usr/bin/gawk`), Python 3.14.8. No installs, no upgrades.

## 1. Box-1 command A — § Sources count

Command byte-exact from `SHONEN.md:6` (`awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md | wc -l`):

```
$ cd /tmp/r65clone            # HEAD = 0e104f49
$ set -o pipefail; awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md | wc -l
18
pipefail-exit=0
```

The line's other rev-attributed counts, same command against `git show <rev>:SKILL.md`:

| rev | `§ Sources` `^- ` bullets | line's claim |
|---|---|---|
| `0e104f49` (wave base) | **18** | — |
| `c019919c` | **18** | "18 … at `c019919c`" ✅ |
| `cbbee56e` | **18** | "18 at `cbbee56e`" ✅ |
| `c63ccc68` | **20** | "20 at `c63ccc68`" ✅ |
| `07c33d73` | **33** | "33 at `07c33d73`" ✅ |
| `80bb8921` | **18** | "18 at `80bb8921` (re-count this round)" ✅ |
| HEAD `2a8eba5` (lane worktree) | **18** | post-base drift: none |

At `0e104f49` the same rule over *all* bullets (`^[[:space:]]*- `) also prints **18** — § Sources
has no nested bullets, so "18 top-level entries" is an exact descriptor of the measured rule.

## 2. Box-1 command B — gate registry

Command byte-exact from `SHONEN.md:6`:

```
$ cd /tmp/r65clone
$ python3 -B verifiers/check_gate_registry.py --rev 80bb89211841289bc802fa7b55057f0ef266d19e
verifiers/box_proof_case_deletion.py         OK
verifiers/check_agent_definitions.py         OK
…  (all 42 rows OK; zero non-OK lines — asserted programmatically)
verifiers/verify_surfaces.py                 OK
gate registry rows conformant 42 of 42 lane verifiers; phantom 0
exit=0
```

**42 of 42, phantom 0, exit 0 — reproduces.** Non-OK set computed as
`[l for l in out.splitlines() if not l.endswith('OK ')]` → only the summary line.

Control on the superseded pin (the rev the line named before the round-65 refresh):

```
$ python3 -B verifiers/check_gate_registry.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
gate registry rows conformant 42 of 42 lane verifiers; phantom 0
exit=0
$ python3 -B verifiers/check_gate_registry.py --rev 0e104f498b3df1466284074c5b3a6e5b523420cd
gate registry rows conformant 42 of 42 lane verifiers; phantom 0
exit=0
```

## 3. The refreshed line names real revs

`SHONEN.md` diff `c98d137..0e104f49` is exactly one line (`--stat`: 1 insertion, 1 deletion) —
box 1's evidence line, 790 → 830 chars. Two semantic deltas only: appended
"; 18 at `80bb8921` (re-count this round)", and the gate pin moved
`c019919c97ab5fe98e87a7754b4449ea4e699c99` → `80bb89211841289bc802fa7b55057f0ef266d19e`.
Diff `0e104f49..HEAD` on `SHONEN.md`: **empty** (blob `66781a68b82450b95759b012401fc6894e95474b`,
sha256 `c42f6bff13563f39bcec3d255b78cb23fbded6bf0446e082179768725838dee8`).

Every rev named anywhere in the file resolves as a commit:

```
0e104f49 → 0e104f498b3df1466284074c5b3a6e5b523420cd  round-65: frontier step (S121 row + snapshot, g7-span-closure entry, …)
80bb8921 → 80bb89211841289bc802fa7b55057f0ef266d19e  round-65: C1 closing package (7 package arms + 4 new judge-lane arms, …)
5253b281 → 5253b28174a17dccba8db391b2a5b9bc6470472a  round-65: measurement receipts at 80bb8921 …
c019919c → c019919c97ab5fe98e87a7754b4449ea4e699c99  round-64: wave-1 integration — C1 G7 span_missing pinning arms (223 …)
cbbee56e → cbbee56e9a3589b0b46736ad36f1b77701def80e  round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32)
c63ccc68 → c63ccc6823e1f6a8577acbb43d19551eadbbee9a  round-59: C1 content — SKILL § Hook files by client …
07c33d73 → 07c33d73ddce769d9cea2846a6313164401b5478  round-57: C1 measured (4 of 4; …)
078eec4  → 078eec4a1f6a41c64ff8806f58b46a67cd413bfc  round-63 verifier spot-check (integrator, hyaku) …
c98d137  → c98d1378236bae56d9d2ecacd5db59a4cc142e1e  round-64 verifier spot-check (integrator, hyaku) …
```

The full 40-hex pin in the command matches `rev-parse 80bb8921` byte for byte.

Secondary claims inside the refreshed line, each re-measured:

- `.ufo/round-46/scouts/B2.md` exists at `0e104f49` (10,049 B); line 44 (516 chars) carries the
  claimed inventory: "41 checklist items (15/9/9/8), seven anatomy-table data rows, five
  decision-table data rows, and 38 Sources entries", plus `SKILL.md` SHA-256
  `0404fdc0ee6e1b16c765b7dd7dc78aef92c5758bfb980dbbbaf2212ab3c2b09f`, 521 lines.
- "the 5 decision-shape rows are `corpus/knowledge/anatomy-and-compression.md:102-108`":
  lines 102/103 are the header + separator, 104–108 are **5** data rows;
  `git diff` of lines 102–108 between `c019919c` and `0e104f49` → identical.
- "pointer `SKILL.md:241` (both unchanged at `c019919c`)": line 241 text is identical at
  `c019919c`, `0e104f49`, `80bb8921` (decision-table shape / action-cell rule).
- "SKILL.md carries the round-64 gate-registry row for `check_r64_routed_repairs.py`":
  present at `SKILL.md:493` at `c019919c` (1 match), `0e104f49`, `80bb8921`.
- "38 Sources entries" is a *round-46-tree* figure, not a rev-pinned one. It reproduces under the
  same rule against the blob B2.md pinned: rev `e8a81acf86bb5921ab105b94bee3687c11b42645`
  (2026-10-19) has `SKILL.md` sha256 `0404fdc0ee6e1b16…` — the exact sha B2.md records — 521 lines,
  § Sources 38 bullets. See F4.

## 4. Box-2 pointer — resolves

`SHONEN.md:8` (`[~]` end-to-end domain task):

```
git cat-file -e 0e104f49:corpus/knowledge/cold-run-round11.md  → exists, 21056 B
git show 078eec4:LOG.md   287:   ids. Non-author cold run (`corpus/knowledge/cold-run-round11.md`): runner
git show 078eec4:LOG.md   294:   `corpus/knowledge/cold-run-round11.md`, `corpus/lessons/round-11.md`,
git show 078eec4:LOG.md   342:   37). Both repairs are declared in `corpus/knowledge/cold-run-round11.md` §7, which now
git show 0e104f49:LOG.md  287:   ids. Non-author cold run (`corpus/knowledge/cold-run-round11.md`): runner   # line numbers stable past the pin
```

All three anchors at the named rev (`078eec4`) land on the cold-run record — record line, artifact
list, §7 repair declaration. Anchor and file both resolve.

## 5. Box-3 pointer — resolves, one anchor offset

`SHONEN.md:10`, file `corpus/lessons/round-8-aggregator-box3-coldrun.md` exists at `0e104f49`
(14,193 B). Line-by-line:

| anchor | claimed in SHONEN | measured | verdict |
|---|---|---|---|
| `:36` | B1 newest-block recipe under-determined | B1 row: newest-mtime session file "carries 0 `<skills>` blocks and 0 `session_init` records … names no selection rule" | ✅ exact |
| `:37` | B2 unlabeled mutating harness | B2 row: "`fault_injection_corpus.sh` sits in the runnable-verifier list with no mutating-gate warning … discoverable only by opening the script" | ✅ exact |
| `:78` | records that with the gate counted "the recipe gap stands" | 385-char line ends: "the refusal is credited, **the recipe gap stands**." Quoted phrase is verbatim at :78 | ✅ exact |
| `:100` | round-13 pass "presentational only — no verdict, count, or quotation above was changed" | :100 is the heading `## kotoba reconciliation (round 13, 2026-09-28)`; the quoted sentence is at **:102** | ⚠️ anchor is the section heading, quoted bytes 2 lines below (F3) |
| prose | "`corpus/knowledge/` holds one cold-run record" | `git ls-tree 0e104f49 corpus/knowledge/ \| grep -c cold-run` → **1** (`cold-run-round11.md`) | ✅ |

## 6. Findings

**F1 — pass (both mandated commands).** At `0e104f49`, box 1's two counting commands reproduce:
§ Sources **18** (pipefail exit 0) and gate registry **42 of 42, phantom 0, exit 0**. Supports the
plan's C1 landing: the registry stays fully conformant at the implementation rev `80bb8921`.
Note the registry counter is structural (row/flag/path conformance) — it says nothing about v32's
assertion count.

**F2 — pass (rev resolution / number re-derivation).** Every rev the refreshed line names is a
real commit, and every count it attributes to a rev (18/18/18/20/33/18) reproduces exactly.
Nothing in the line over-claims a revision.

**F3 — minor (pointer precision, box 3).** `:100` names a section heading; the quoted sentence is
at `:102`. The quotation is genuine and the section is the right one; only the line number is off
by two. Calibration cost: a reviewer grepping `:100` for the quote gets a miss. Fix belongs in
`SHONEN.md:10` → `:102` (not edited by this seat).

**F4 — minor (pin strength, box 1).** "38 Sources entries" is attributed to "the round-46 tree",
not to a rev. It is reproducible only transitively: B2.md's `SKILL.md` SHA-256
`0404fdc0…` identifies blob `0404fdc0…`, which I located at `e8a81acf` (521 lines, 38 bullets).
The six other numbers in the same line are rev-pinned; this one is blob-pinned at best and its
unit ("entries") differs from today's 18 top-level bullets. Not falsified — but it is the
weakest link in the line and would be the first thing a hostile reader attacks.

**F5 — informational (the refresh is a pin move, not a result change).** The gate registry prints
42 of 42 / exit 0 at `c019919c`, `0e104f49` and `80bb8921`. [INFERENCE] The refresh moves the
measurement onto the round's implementation rev for provenance; it does not change the verdict.

**F6 — calibration hazard, measured.** Box-1's line is 830 chars. Any layer that truncates
display at 768 bytes cuts it at `prints \`gate …`, which reads exactly like a truncated or missing
result. The file bytes are complete: line 6 ends
``… rows conformant 42 of 42 lane verifiers; phantom 0`, exit 0``. I initially mis-read the
truncated view as a defect and had to re-read the line through Python to clear it. Rule for the
next seat: never call an evidence line truncated from a capped display; read the line's bytes.

**F7 — state (no post-base drift).** `SHONEN.md` is byte-identical from `0e104f49` to the current
round-66 tip `2a8eba5`, and § Sources is still 18 at the tip. The refreshed line is the landed
line, not a superseded one.

Supports: the round-65 C1 evidence chain (gate-registry conformance at the implementation rev) and
the promotion file's own reproducibility at the wave base.
Falsifies: nothing. F3/F4 are precision defects in `SHONEN.md:10` / `SHONEN.md:6`, not
contradictions of the counts.

## 7. Limits / not run

- Both counting commands were run in a `--shared` clone checked out at `0e104f49` and against
  `git show` blobs; `check_gate_registry.py` reads *all* of its inputs through git at `--rev`, so
  the run is rev-faithful. Not run inside the lane worktree (it is at `2a8eba5`; mutating it is
  out of bounds).
- Out of scope, not verifiable here: the "7 anatomy rows" and "41 checklist boxes 15/9/9/8" figures
  (round-46-tree inventory; I measured only the 38 Sources and 5 decision rows from that chain),
  box 4 (`PROVINCE.md` / sibling census), v32 self-test, floors registry, checklist 11/11, census —
  those are other lanes' commands and are not re-run to decorate this report.
- No verifier exists for box 2/box 3; "resolves" above means anchor-and-file resolution, not a
  gate pass.
- No gate regressed or moved as a side effect: nothing was written outside this file.
- Contention: ≤2 concurrent processes, all commands completed well inside the 120 s cap; no
  timeouts, no installs.

## 8. Artifacts

- Report: `.ufo/waves/round-65/w1/ScribeSHONEN2.md` (this file)
- Byte source A: `/tmp/shonen2` (`git archive 0e104f49`, 142 MB)
- Byte source B: `/tmp/r65clone` (`--shared` clone, HEAD `0e104f49`, clean)
- Raw outputs pasted above; no scratch files retained under the lane repo.
