# E05R3R4Repair — C2 repairs R3 and R4 (round 77, w1)

Seat: `E05R3R4Repair` (leaf). Scope: C2 routed repairs **R3** (w2 registry note) and **R4** (LOG.md
§ Round 75 closing line) + the R2/R3 LOG citation sentences. No lane file outside
`.ufo/waves/round-77/` was written; no git/jj write in the lane repo; counters untouched.

Counter bytes re-verified against the plan's pins before use (`verifiers/check_r75_routed_repairs.py`
`989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`,
`verifiers/check_desc_craft.py` `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`).

## 1. Numbers recomputed from `.ufo/waves/round-75/` (not trusted from the r76 draft)

All commands ran at the lane root `/home/vgpnk/Projects/shokunin/kotoba-shokunin` at lane HEAD
`6523aced1ee0ebe07dca996213bdc645a6acbd1e`; each exit status captured for its own command.

| quantity | command | result |
|---|---|---|
| results bytes | `sha256sum .ufo/waves/round-75/w2-results.json` | `e4ce0f6d3be78fa6db5da230ca6ec5e388c08e5f0196ebe66600e39da17bcf5c`, 70 722 bytes, blob `25870e72…` |
| seats / entries / unique names / empty outputs | `jq -r '[.seats,(.results|length),([.results[].name]\|unique\|length),([.results[]\|select((.output//"")=="")]\|length)]\|@tsv'` | `64	64	64	0` → 0 dead |
| dispatch declaration | `jq -c '.counts' .ufo/waves/round-75/w2-dispatch.json` | `{"spawn":64,"resume":0,"total":64}` |
| report files | `ls .ufo/waves/round-75/w2/*.md \| wc -l` / `grep -cE '^R75Attack[0-9]+\.md$'` | `63` / `63` |
| dir entries | `ls -1 .ufo/waves/round-75/w2 \| wc -l` | `64` (`63` `.md` + `swarm-registry.json`) |
| absent report | `for n in $(jq -r '.results[].name' …); do [ -e .ufo/waves/round-75/w2/$n.md ] \|\| echo MISSING $n; done` | `MISSING R75Attack28` only |
| R75Attack28 entry shape | `jq -c '.results[]\|select(.name=="R75Attack28")\|{name,agent,has_report_field:has("report"),note}'` | `{"name":"R75Attack28","agent":"reviewer","has_report_field":false,"note":null}` |
| entries with a `report` field | `jq -c '[.results[]\|select(has("report"))\|.name]\|length'` | `0` — **no** entry has one; key set is `{agent,name,note,output}` for all 64 |
| add-commit of results file | `git log --all --oneline --diff-filter=A -- .ufo/waves/round-75/w2-results.json` | `d118a3b` (ancestor) + two non-ancestor adders of the same blob (`8adfe33`, `b94f123`, empty subjects) |
| modified since? | `git log --oneline d118a3b..HEAD -- .ufo/waves/round-75/w2-results.json` | empty |
| phantom ever committed? | `git log --all --oneline --diff-filter=A -- .ufo/waves/round-75/w2/R75Attack28.md` | empty |
| untracked leftover? | `git status --porcelain -- .ufo/waves/round-75/w2` | empty (clean) |
| named-but-absent sweep | python over all `w2/R75Attack<nn>.md` references | 61 of 64 entries name a path; **exactly one** named path is absent (`R75Attack28`) |
| registry | `swarm-registry.json` | 64 `members`, `reportDir` only, 0 per-member report paths |

Reconciliation: **64 of 64 seats settled, 0 dead, 63 of 64 report files**; the single gap is the
`R75Attack28` phantom (its `output` names `w2/R75Attack28.md`; no commit on any ref adds it; no
untracked copy remains → never written, unrecoverable by design).

### Draft defects found in the r76 draft (`build/w2-registry-note.md`) and corrected

1. **False claim:** the draft says the entry has no `report` field "unlike sibling seats `R75Attack08`,
   `R75Attack13`, `R75Attack51`, …, which do". No entry in the file carries `report` (count `0`); all
   64 share one key set. The final note drops the claim and states the measured fact.
2. **Missing detail:** 3 of the 61 path-naming entries (`R75Attack34`, `R75Attack38`, `R75Attack62`)
   name no report path although their files exist — not gaps, but the draft's "single gap" sentence
   was under-qualified. The final note records it.
3. Draft's "measured at lane HEAD `4de12b61…`" was stale; the final note records the rev actually
   measured (`6523aced…`) and states that the C2 counter re-derives both counts at its own rev.

## 2. Deliverables

- `…/round-77/build/E05R3R4Repair.w2-registry-note.md` — final R3 note text, sha256
  `07d72021e0369e6247525a4f6551f496e922467346bcef821ab9b9e7b0f19503`. **Lands at**
  `.ufo/waves/round-76/w2-registry-note.md` (the only path the frozen counter reads).
- `…/round-77/build/E05R3R4Repair.LOG.md.patch` — unified diff against lane HEAD `6523aced…`, sha256
  `b309250214f0771fec813238d0c856eda2141ba1cf396b846a291c0932e5ad21`. Applies at the lane root
  (`git apply`, mnemonic `i/`–`w/` prefixes), **verified**: `git apply --check -v … ; exit=0`. Two
  bullets inserted after the existing `- **Pointer:** … w2 falsify results pending; …` line inside
  `## Round 75` (hunk `@@ -2808,6 +2808,8 @@`; `## Round 76` heading untouched; nothing appended at
  end of file, which is 563 KB and was never read whole):
  - `- **Correction (appended; r76 routed repairs R2/R3):** the r75 final-tip no-harm receipt is
    `.ufo/waves/round-76/receipts/noharm-at-tip.txt`; the `R75Attack28` phantom report reference — its
    `output` names `w2/R75Attack28.md`, which no commit on any ref ever added — is recorded in
    `.ufo/waves/round-76/w2-registry-note.md`.`
  - `- **Closing (appended; r76 routed repair R4):** w2 settled 64 of 64 seats, 0 dead, 63 of 64
    report files; R75Attack28 is a phantom per `.ufo/waves/round-76/w2-registry-note.md`, so the
    results file and the wave dir reconcile.`

## 3. Counter evidence (scratch clone, own exit status per command)

Clone: `git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/clone`,
`rev-parse --show-toplevel` → `$S/clone`, `user.name scratch-r77` / `user.email scratch@example.invalid`
set before the first scratch commit; every git call `-C`. Fixture commit **`65414b28`** adds the note at
the counter path and applies the LOG patch. Runs use
`python3 -B verifiers/check_r75_routed_repairs.py --repo $S/clone --work $S/work --rev <rev>` with
`cmd > out 2>&1; echo "exit=$?" >> out` (no pipeline status anywhere).

| world | rev | printed | exit | open arms |
|---|---|---|---|---|
| base (lane HEAD) | `6523aced` | `r75 routed repairs closed 0 of 4` | 1 | R1, R2, R3, R4 (all) |
| **R3+R4 fixture** | `65414b28` | **`r75 routed repairs closed 2 of 4`** | 1 | **R1, R2 only** (R3 closed, R4 closed) |
| control: note pair forged to `64 of 64` | `e5d7f3ca` | `closed 1 of 4` | 1 | R1, R2, R3 — `R3: the note records no '63 of 64' report-file/seat pair` |
| control: R4 closing count forged to `64 of 64` | `402717c3` | `closed 1 of 4` | 1 | R1, R2, R4 — `R4: … no '63 of 64' report-file/seat pair after the 'w2 falsify results pending' text` |
| control: LOG reverted, note kept | `dd322455` | `closed 0 of 4` | 1 | R1, R2 (+R2 citation), R3 (citation only), R4 (all three) |
| control: verbatim excerpt block removed | `6219f896` | `closed 2 of 4` | 1 | R1, R2 — **R3 still closed** (see § 4) |

In the fixture run the only remaining findings are
`- R1: corpus/lessons/round-75.md carries no appended correction`,
`- R1: .ufo/waves/round-76/receipts/r1-folded-render.txt is not committed at the measured revision`,
`- R2: .ufo/waves/round-76/receipts/noharm-at-tip.txt is not committed at the measured revision` — i.e.
R1/R2 stay open with E03/E04 stand-ins absent, as required. Note that the R2 **citation** arm is already
green from my LOG line (it no longer reports the LOG citation finding), so E04 only has to add the
receipt bytes.

Receipts: `.ufo/waves/round-77/receipts/E05R3R4Repair.c2-base-6523aced.txt`,
`…c2-after-r3r4.txt`, `…c2-control-pair-forged.txt`, `…c2-control-r4-count-forged.txt`,
`…c2-control-log-reverted.txt`, `…c2-control-excerpt-removed.txt`, `…c2-control-paraphrase-only.txt`,
`…E05R3R4Repair.digests.txt`.

## 4. Counter observation (reported, not acted on — counters are frozen)

R3's excerpt arm ("a ≥ 20-character verbatim window of the entry's `output`") is **shadowed by R3's own
mandatory path token**: the note must contain `w2/R75Attack28.md`, and the entry's `output` contains
`kotoba-shokunin/.ufo/waves/round-75/w2/R75Attack28.md`, so any note that satisfies the path arm also
satisfies the excerpt arm — the substring `.ufo/waves/round-75/w2/R75Attack28.md` (54 chars) matches.
Measured: with the 774-character verbatim block deleted and the path rewritten to a paraphrase that
still carries the required 18-character token (`control-paraphrase-only`, rev `6f660257`), R3 remains
**closed**; 19 of the entry's 20-char windows still match, all inside the path token. The excerpt arm
therefore cannot fail independently unless the path arm fails too. Two consequences:
(a) my note quotes the whole entry verbatim, so the excerpt is real, not incidental; (b) if the parent
wants a falsifiable excerpt arm, the counter needs a different shape (e.g. exclude windows overlapping
the path token) — that is an r78 counter change, not an r77 edit.

## 5. Risks / notes

- The note and the patch are **drafts**: the L1 lands them (note → `.ufo/waves/round-76/w2-registry-note.md`,
  patch → `LOG.md`). Until both land in one commit, C2 cannot print 4 of 4.
- Order does not matter for R3/R4 (independent arms), but R2's LOG citation is already satisfied by this
  patch; E04 must not rewrite those bullets, only add the receipt file.
- `git apply` (not `patch -p1`) is required: the repo emits mnemonic `i/`–`w/` prefixes.
- No tool installed, no package manager touched (pacman paused host-wide, never invoked). No scratch
  leftovers: `/fast/scratch/hyaku/kotoba-r77/E05R3R4Repair` removed after the receipts were filed.

VERDICT: R3 note finalized (64/64 seats, 0 dead, 63/64 report files, phantom R75Attack28 proven from commits) and R4 LOG closing patch delivered; scratch fixture closes R3+R4 only (`closed 2 of 4`, exit 1, R1/R2 open as designed), with controls showing the forged pair, forged closing count and reverted LOG each reopen their arm.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E05R3R4Repair.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E05R3R4Repair.w2-registry-note.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E05R3R4Repair.LOG.md.patch /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-base-6523aced.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-after-r3r4.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-control-pair-forged.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-control-r4-count-forged.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-control-log-reverted.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-control-excerpt-removed.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.c2-control-paraphrase-only.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/receipts/E05R3R4Repair.digests.txt
