# Round-49 falsify — C1 census row `kagi` (seat KotobaR49.RowKagi, leaf)

HOLDS — applies to the C1 `kagi` row in `corpus/knowledge/sibling-overlap-census-round49.md`
(line 67) and its matching row in `PROVINCE.md` § Adjacent (line 41), at judged commit
`c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`, against pinned sibling commit
`899c50b42634a3a4ad0b28ab7509786315e2fc2b` in `/home/vgpnk/Projects/shokunin/kagi-shokunin`.
No finding flips the row; two residual risks recorded.

## Findings

None that defeat the row. All five assigned checks verified at byte level; details below.
Two residual risks (R-a, R-b) do not change the classification under the entry's stated rule.

## Check evidence (commands verbatim; kagi repo = /home/vgpnk/Projects/shokunin/kagi-shokunin)

1. Commit exists, branch cell right — PASS.
   - `git -C <kagi> rev-parse master` → `899c50b42634a3a4ad0b28ab7509786315e2fc2b`, exit 0.
   - `git -C <kagi> rev-parse 899c50b…^{commit}` → same hash, exit 0 (commit exists).
   - `git -C <kagi> branch --contains 899c50b…` → `* (no branch)` and `master`, exit 0 —
     master's tip is the pin; checked out detached at the same commit. Cell `master` is a true
     statement and the census Limits section scopes all claims to the pinned bytes.
   - `git log -1 --format='%ci %an %s' 899c50b…` → `2026-10-21 15:23:29 -0300 kagi-shokunin
     round-28: measured outcomes, strict receipt audit and honest frozen-fixture conformance`.
   - Skill-file cell `SKILL.md`: `git ls-tree --name-only 899c50b` lists it (exit 0).

2. Scope quote verbatim at `PROVINCE.md:3` — PASS.
   - `git show 899c50b:PROVINCE.md | sed -n 3p` → `**Domain:** secrets & vault ops — the-janitor
     flows, credential hygiene evidence` (line 3; lines 1–8 read, ±2 satisfied).
   - `git show 899c50b:PROVINCE.md | sed -n 3p | grep -cF 'secrets & vault ops — the-janitor
     flows, credential hygiene evidence'` → `1`, exit 0 (row quote is a contiguous substring,
     whitespace intact; entry header allows collapsed whitespace only).

3. Classification `adjacent` under the entry's § Classification rule — PASS.
   - Rule (census lines 36–48): `contested` = sibling's committed scope surfaces claim part of
     kotoba's core (writing or auditing other lanes' SKILL.md, prompts or AGENTS.md-class files,
     or the instruments over them); `adjacent` = either side's committed scope surfaces state a
     split of one artifact, function or trigger area between the sibling and kotoba.
   - Adjacent arm satisfied by kagi's own committed bytes at the pin: `corpus/adjacency.tsv:84`
     (`$HOME/.agents/AGENTS.md  kotoba  shared-read  declared … byte-pinned here; kotoba is the
     sole fleet claimant of the file's checklist/shape reading (read-only for both lanes)`),
     `corpus/README.md:96-97` (opencode group unresolved; AGENTS.md split "no adjudication
     needed, both are read-only"), `corpus/surface-census.tsv:55`, `corpus/knowledge/
     drift-gate.md:96`. That is a stated split of one artifact — the adjacent arm, not weaker.
   - Contested arm not met: full-tree sweep `git grep -in kotoba 899c50b -- . ':(exclude).ufo'`
     (54 hits, all reviewed) — every hit is (a) kagi stating the split (corpus files above,
     LOG.md:181, SCORECARD.md), (b) kagi mapping kotoba's verifiers as adjacent/different-unit
     (lessons round-11…16), or (c) citation-defect records (SKILL.md:297). No kagi surface
     claims writing or auditing any lane's SKILL.md, prompts, or AGENTS.md-class content, nor
     instruments over them. Second sweep `git grep -inE 'always-?on|alwayson|checklist' …
     ':(exclude).ufo'` → only kagi's own credential-hygiene checklist machinery (checklist-run.sh,
     checklist.tsv, its own SKILL.md section); AGENTS.md-only sweep (hits not naming kotoba) shows
     integrity-level observation only: drift-baseline.tsv:14 `mode 600, 75 lines, sha -`,
     tac-evidence-integrity.md:5 "(existence/mode only)".
   - The kagi-vs-kake contested musketeer row (adjacency.tsv:82) is between kagi and kake —
     irrelevant to kotoba under this rule.

4. Mechanical columns re-derived from `git show 899c50b:SKILL.md` — PASS.
   - Description (frontmatter line 3): `Domain specialist — secrets & vault ops — the-janitor
     flows, credential hygiene evidence, vault lifecycle. Rank: shonen.`
   - `git show 899c50b:SKILL.md | sed -n 3p | grep -ioE '\b(kotoba|audio|chousa|game-dev-2d|
     game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|
     souji|tabi|tameshi|tsukuroi)\b' | sort | uniq -c` → empty output (zero matches; no sibling
     or kotoba token, whole-token, case-insensitive). Row cells `no | no` are correct.
   - Census row (line 67) fields cross-checked: commit/skill file/classification/quote all match
     the pinned bytes; PROVINCE.md:41 carries the same commit and classification.

5. `PROVINCE.md:41` boundary note, statement by statement — PASS.
   - "secrets and vault ops" ← kagi PROVINCE.md:3 (verbatim, check 2).
   - "shared read of `$HOME/.agents/AGENTS.md`" ← kagi adjacency.tsv:84 status `shared-read`.
   - "kagi pins the bytes" ← cited line `corpus/README.md:97` verbatim at the pin: "kagi pins its
     bytes; kotoba owns the checklist/shape reading — no adjudication needed, both are read-only";
     also adjacency.tsv:84 "byte-pinned here" and surface-census.tsv:55 "bytes pinned here".
     Citation line number exact (README:96 = opencode row, :97 = AGENTS.md row).
   - "kotoba owns the checklist and shape reading" ← same cited line, verbatim.
   - "the opencode config group owner is unresolved and stays with the integrator" ← kagi
     adjacency.tsv:81 (`integrator`, `unresolved`, "Ruling still owed to the integrator") and
     README.md:96 ("**`unresolved`** … ruling owed to the integrator").
   - Guard exercised end-to-end in scratch (lane itself untouched):
     `git clone -q …/kotoba-shokunin k && git -C k checkout -q c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`
     then `python3 -B verifiers/check_sibling_census.py
     corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` →
     `rows 20 verified 20` / `province rows 20 matched 20`, exit 0. The kagi row joins and its
     quote re-reads at the pinned commit.

## Residual risk

- R-a: "kagi pins the bytes" is kagi's committed self-description, faithfully cited; kagi's own
  drift policy withholds the content hash (`drift-pins.sh` NOHASH list, drift-baseline.tsv sha `-`,
  LOG.md at pin: "pinned by mode+lines only"), so no committed hash lets a third party re-verify
  the byte pin. Kotoba's note only reports kagi's claim ("report, don't absorb"), so the note is
  accurate as written; the classification does not hinge on hash presence (the split is stated
  by kagi regardless).
- R-b: the contested/adjacent line rests on reading byte/mode/line observation as not-"auditing".
  A stricter reading of the rule's contested arm over kagi's drift-gate.md:96 and
  tac-evidence-integrity.md (existence/mode + a quoted janitor section) could argue contested;
  kagi's explicit cession ("kotoba is the sole fleet claimant of the file's checklist/shape
  reading (read-only for both lanes)") and the entry's own override precedent (kotodama,
  description-level) both support `adjacent`. Judgment call, documented, not a defect.
- Pins move: kagi master may have advanced since 2026-10-21; every claim here is pin-scoped
  (census § Limits states the same).

## Verification gaps

- kagi's `scope-gate.sh` not executed (host-state dependent; row truth does not depend on it).
- No tool installed or upgraded; no web sources opened; no LSP server involved (byte/git-level
  markdown/tsv checks only). Other 19 rows and C2 are other seats' scope, untouched.
