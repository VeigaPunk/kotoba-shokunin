# Kb79MT02TemplateCounter — seat report (kotoba round 79, wave w1)

Mutation probe of the template counter the round-79 C2 counter is built from:
`verifiers/check_cn_vendor_surfaces.py` (r73, frozen). 40 single-point mutants of a scratch
copy, each judged by the counter's own `--self-test` (56 fixture worlds / 161 assertions,
isolated scratch git repos, no lane or network touched). Kill ratio **42% (17/40)**.
Survivors (23) are coverage findings for seat Kb79X01CounterBuild:
`build/Kb79MT02.survivors.md`. This seat modified nothing in the lane tree.

## 1. Provenance

- Probe target bytes: blob `89b8f8f027181337898fe095226cb6de0a2818a6`, verified identical at
  base `b10bcbc6b00f8f56b202ccbadca311007b5b463c` and plan commit F1 `2c56622375641193a03bb97c0624e6536f3dffba`
  (`git rev-parse <rev>:verifiers/check_cn_vendor_surfaces.py` -> same blob both).
- Scratch clone per the recipe; `git rev-parse --show-toplevel` printed the clone dir (`TOPLEVEL_OK`).
- Pristine copy sha256 `7177a7f6923789f5b180534c5cba71b08a4f04f052e358d7d750379eda5e22f9`;
  `--print-self-sha` printed `5772c06cc6fcdfdbd3da19a62c1c2d8e82d4394166991b5b26ad62e2322c93eb`
  = the file's frozen `SELF_SHA` constant (blanked-sha match: the copy is the frozen bytes).
- Host: Python 3.14.8, git 2.56.0, linux x64. No tools installed or upgraded (none needed);
  pacman untouched. Disk-guard checked before the pass: /fast/scratch/hyaku 27% use, 592.4G free.

## 2. Commands (exact)

```
S=/fast/scratch/hyaku/kotoba-r79/Kb79MT02TemplateCounter
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/clone"
git -C "$S/clone" checkout -q 2c56622375641193a03bb97c0624e6536f3dffba      # rc 0
test "$(git -C "$S/clone" rev-parse --show-toplevel)" = "$S/clone"          # rc 0 (TOPLEVEL_OK)
cp "$S/clone/verifiers/check_cn_vendor_surfaces.py" "$S/pristine/"
python3 -B "$S/pristine/check_cn_vendor_surfaces.py" --print-self-sha       # rc 0, 5772c06c...
# battery: TMPDIR=$S/tmp, cwd=$S/run, driver = $S/mutate.py (in scratch, removed after):
python3 -B "$S/mutate.py"                                                   # rc 0, 14.5 s wall
#   per mutant: python3 -B $S/mutants/mutNN.py --self-test   (<=4 concurrent; each 1.1-1.2 s)
```

Each mutant applies exactly one textual edit, asserted to occur the expected number of times
(39 singles, 1 double: `host == h.lower()` -> `h.lower() in host`, both `host_ok` branches).
Mutant file sha256s and per-mutant raw outputs: `build/Kb79MT02.mutants.log`,
`build/Kb79MT02.verdicts.tsv`.

## 3. Baseline (pristine)

`python3 -B pristine/check_cn_vendor_surfaces.py --self-test` -> **rc 0**,
`self-test: 0 failure(s) over 161 assertions`, 56 PASS / 0 FAIL, 1.0 s.
Baseline healthy, so every mutant verdict below is conclusive.

## 4. Results: 17 killed / 23 survived / 0 inconclusive = kill ratio 42% (17/40)

Killed (17) — the arm is guarded by an existing fixture world (killing world quoted; full
output in `build/Kb79MT02.mutants.log`):

| id | arm | killing world |
|---|---|---|
| mut03 | ws() collapse -> strip-only | "(d) quote wrapped across a line break is still found" |
| mut05 | vendor_of() lookahead dropped | "(a) vendor row named by a longer client name" |
| mut06 | duplicate vendor row allowed | "(a) two rows name the same vendor" |
| mut07 | cited-ids-subset check dropped | "(a) cited id absent from the source: lines" |
| mut08 | 11-cell shape check dropped | "(b) cited row has 12 cells" |
| mut09 | status `mined` filter dropped | "(b) cited row is queued, not mined" |
| mut10 | tier A/B filter dropped | "(b) cited row is tier C" |
| mut11 | used-by filter dropped | "(b) cited row's used-by omits the entry" |
| mut12 | page binding host-only | "(b) a pin of a different page on the same vendor host is not the cited page" |
| mut13 | manifest escape check dropped | "(c) manifest path escapes the snapshot directory" (exit 0, wanted 2) |
| mut14 | snapshot sha-vs-pin dropped | "(c) tampered snapshot (manifest hash left)" (exit 0, wanted 2) |
| mut15 | opened-this-round date dropped | both "(e) … not the capture date" worlds (exit 0, wanted 2) |
| mut16 | anchor sha == pin dropped | "(e) anchor sha256 not the snapshot pin fails that vendor" |
| mut17 | MIN_QUOTE_WORDS 5->2 | "(d) located quote under 5 words" |
| mut18 | MAX_QUOTE_WORDS 25->500 | "(d) located quote over 25 words" |
| mut19 | held-at-base zeroed | "vendor hosts already in the base registry read held 4" + "held at base: 1" |
| mut20 | entry_problems short-circuit dropped | 4 worlds: "no vendor table", "without verified-at:", "without recheck:", "cited id absent" |

Survived (23) — ordered list with the one-line fixture each needs:
`build/Kb79MT02.survivors.md` (items 1-20; items 21-23 structural). Headlines for X01:

- mut24 host equality -> substring: `docs.trae.cn.evil.io` passes; no hostile-host world exists.
- mut25 path segment -> bare prefix: `…/moonshotai/kimi-cli-docs/…` passes its pin — this is the
  round-79 C6 sibling-host control (`raw.githubusercontent.com/badlogic/pi-mono-evil`); the
  template battery does not have it, so the NEW counter must ship it, not inherit it.
- mut26 dot-segment guard dropped: `/pin-path/../evil` passes; no world.
- mut28 located quote in ANY cited snapshot passes: quote laundering; round-79 (d) freezes
  "its own snapshot" — X01 must add the cross-snapshot world.
- mut27 manifest duplicate-digest conflict accepted; mut37 `HTTP 404` anchor accepted; mut34
  two named pins resolve to the first silently.
- mut01/mut02 (predicted kills): comment/fence stripping is NOT pinned — the hidden row lands
  as a header-only table block either way. Fixture needed: two rows hidden in one
  comment/fence, expecting "0 vendor-table row(s)".
- mut04 (predicted kill): the CJK word-boundary world is masked by the existential token read
  (the root token also occurs in the row's other snapshot). Keep ASCII boundaries; fixture must
  make the CJK page the only carrier of the token.
- mut40 `_INTERNAL_SELFTEST` default flip survives by construction: a self-test can never see a
  dead drift guard. Process consequence: only the L1's `--print-self-sha` vs
  `receipts/freeze-shas.txt` check covers drift; do not cite `--self-test` for it.

No mutant produced a do-nothing pass of the full predicate beyond the mutated arm's own
weakening (baseline `0 of 4` do-nothing world stayed exit 1 everywhere), and no survivor was
"repaired" — per role, survivors are reported as coverage findings, not fixed by narrowing.

## 5. Restoration evidence

All mutants ran on scratch copies under `$S/mutants/` (40 files, sha256s in the log). The lane
file was never opened for writing. After the battery and after `rm -rf -- $S`:

- `sha256sum verifiers/check_cn_vendor_surfaces.py` ->
  `7177a7f6923789f5b180534c5cba71b08a4f04f052e358d7d750379eda5e22f9` (identical before and after).
- `git status --porcelain -- verifiers/` -> empty (0 lines); no commit/add/checkout in the lane.
- Scratch dir removed: `test -d $S` fails -> `SCRATCH_REMOVED`. Receipts copied to build/ first.

## 6. Deliverables and verdict

- `build/Kb79MT02.survivors.md` — 23 numbered survivors, one-line fixture each, for the C2
  counter builder (Kb79X01CounterBuild).
- `build/Kb79MT02.mutants.log` — per-mutant: sha256, verdict, rc, exact killing/failing world output.
- `build/Kb79MT02.verdicts.tsv` — machine-readable verdict table + baseline line.
- `build/Kb79MT02.baseline-selftest.txt` — pristine self-test output (56 PASS, rc 0).
- Seat report: this file.

VERDICT: 40-mutant probe of the r73 template counter killed 17/40 (42%); 23 survivors are coverage gaps the new C2 counter must close with the listed fixtures (host-substring, unanchored path prefix, dot-segments, cross-snapshot quotes, manifest conflicts, non-200 anchors, pin ambiguity, styled/ordered/shaped-tree arms), including three battery worlds that looked like kills but pin nothing; template bytes untouched.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79MT02.survivors.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79MT02.mutants.log /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79MT02.verdicts.tsv /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79MT02.baseline-selftest.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79MT02TemplateCounter.md
