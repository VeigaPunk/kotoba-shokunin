# Kb80S15FreezeShas — round-80 freeze receipt, assembled

Seat: `Kb80S15FreezeShas` (scribe, round-80 w1). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (lane HEAD at assembly `c2f69d4f7b5887c409d7c3975d6aebc2e312c406`; base is an ancestor — receipt blocks `lane HEAD`, `base is an ancestor of lane HEAD`).
Format source: `.ufo/waves/round-79/receipts/freeze-shas.txt` (9 lines: one `base=` line, eight `<sha256>  <path>` lines; receipt block `r79 freeze-shas.txt (format source, whole file; 9 sha256 + base= line)`).

**State at assembly: 26 of 26 value lines filled, 0 pending** — counted from the block itself (§1).
Nothing is pending: the last three values (the C2 counter and patches P1/P3) were filled from the L1's
committed freeze (`5599193`) and re-hashed against the worktree bytes before substitution. The L1's
`receipts/freeze-shas.txt` is now the canonical file; this assembly is its corroboration, and it adds
the one thing the L1's receipt does not carry: § 6 F23, that the artifacts it names are not yet
committed at the freeze rev.

What is filled: part 0 (9/9, sha256 of the base tree — a pre-state, never an after-value), part 4
(5/5, the r79 drafts the repairs port from), part 1 (E06's published amended counter), part 1b (the two
composed instrument blobs, re-derived here from the published stack’s gate hunks), and the part-3
digests for P2, P4 and P6. What is pending: the C2 counter (part 2 — blocked by C-f, not by absence) and patches P1 and P3 (not
published as standalone files; both are carried inside the P5 landing patch, so landing that patch
supersedes them — see C-a).

**One fork the L1 must close before freezing.** Two counter byte streams are published and they are
mutually exclusive: E06's patch (part 1 carries its result, `15cc1761…`) and the counter hunk inside the
`Kb80Y01-simplified.patch` bundle (`ae29fc7b…`, cap 60, same two pins). They conflict on
`verifiers/check_tip_battery.py` — apply E06 on top of Y01 and git refuses at line 103. Landing Y01 also
means P5 *is* Y01 and P6 does not apply; landing E06 requires a class-only patch from E05, which is not
published. Finding F16; the freeze must record the decision, not both.

Two rules make a filled value safe to hand to the L1: every filled line is recomputable by the command
in §2/§3, and the freeze self-check (§4.3) re-measures **every** line at F2 — so a seat that revises an
artifact after this assembly shows up as a `MISMATCH`, never as a silently stale pin. The receipt file
itself is `.ufo/waves/round-80/build/Kb80S15FreezeShas-receipts.txt` (36 blocks, each with its
command's own exit status); pending lines carry `{{MARKER}}` plus a source and a command (§2).

---

## 0. Freeze semantics this receipt implements

1. **Frozen = the bytes the claim is *counted by*, not the tree it counts.** Part 1 pins the amended
   C1 counter, part 1b the two instrument pins that counter's `INSTRUMENT_PINS` table must carry,
   part 2 the C2 counter. Data files the counters *read* (the entry, snapshots, `corpus/README.md`,
   `SKILL.md`, `PROVINCE.md`, the refreshed baseline) are measured surfaces: they are written by
   seats after the freeze and are recorded as after-values in a companion receipt (§4.3), never here.
2. **Write-once.** The file is committed at F2 together with the two counters and the control
   receipts, and is not edited afterwards. Anything discovered later goes to the companion
   after-receipt or to the report, so a reviewer can always distinguish "declared before data" from
   "recorded after".
3. **Two hash grammars, one line shape.** `sha256sum` lines are `<64-hex>  <path>` (parts 0, 1, 2, 3,
   4). `INSTRUMENT_PINS` values are git **blob** ids (`git rev-parse <rev>:<path>`, 40 hex) and cannot
   be checked by `sha256sum`; they live in their own part (1b) under a header that says so.
4. **Comments are safe.** No verifier and no fleet script reads this file: `grep -rln freeze-shas
   verifiers/` → no match, exit 1; `grep -rln freeze-shas /home/vgpnk/Projects/shokunin/scripts/` → no
   match, exit 1 (receipt blocks `no verifier parses freeze-shas.txt` and `the lane has no scripts/ dir; ...`). r79's file had no comments because it needed none; the section
   headers below exist so a reviewer can tell which value binds which claim, and they change no
   machine-readable line.
5. **Two path families, one content set.** The L1's committed `receipts/freeze-shas.txt` names the
   *input* artifacts under `build/`; this assembly names the **landed** tree paths (`verifiers/…`) because
   those are the bytes the counter reads at the tip. At F2 the two must agree — and F23 records that, as
   of the L1's freeze commit, the `build/` inputs are not committed at all, so only the landed form is
   resolvable from a clone.
6. **Scope of "instrument".** Counter code + the pin table + the baseline those counters compare
   against. `verifiers/baseline.json` is **not** in that set — the corpus gate never opens it. The
   gate reads `verifiers/corpus-baseline.json` (`verify_corpus_integrity.py` `BASELINE_NAME`), which
   the r79 freeze file omitted; part 0 line 8 corrects that (finding F1).

---

## 1. The file to write — `.ufo/waves/round-80/receipts/freeze-shas.txt`

Byte-for-byte, with the `{{...}}` markers substituted per §2. The first line and every value line use
the r79 grammar exactly; `#` lines are section headers only.

```
base=398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
# part 0 — pre-state: the tree the C1 predicate's base figure is measured on (sha256 at the base; NOT an after-value)
e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a  verifiers/check_tip_battery.py
3e600f4b70e4664048c0c09b06bf6a28cb00ff37fbb8c78f597a1f1452c03748  verifiers/verify_corpus_integrity.py
c9cef5b3ecca5e9cfdac26b77702ac39186049ed782ce4a250776939a06e7ff2  verifiers/verify_corpus_independent.py
01b8ad1b1a2d9f7568dc6b970cd5c9ec621bf58af411973f001fa3ad0c35ddce  verifiers/check_gate_registry.py
84458c057eef2bff8d7c76e4fdc029428688e3920deb0b69f948387433061f21  verifiers/check_assertion_floors.py
b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615  verifiers/verify_skill_checklist.py
df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f  verifiers/check_correction_sweep.py
22d5f0bb6458abd63592f57e2230ea989860350f8b4b0723332ef743453374d7  verifiers/corpus-baseline.json
7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a  SKILL.md
# part 1 — C1 frozen bytes at F2: the erratum-E5 counter AND the refreshed baseline (C-g)
#   THE ROUND-80 COUNTER IS 20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276 -- one
#   stream only: the E5 amendment republished on E05's canonical pins (68ccce1c.../e887de7..., F22).
#   Superseded and NOT to be substituted: 15cc1761... (E06's first stream, Y01 pins) and ae29fc7b...
#   (the Y01 bundle's own counter hunk). Pinned to the deterministic tree a207fafb... (rev fc91d8d2...).
20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276  verifiers/check_tip_battery.py
9f2d3ef51e7cef8fb6971c7c8adaf04d4f2322c4cd024b90b0b85995c2a7d537  verifiers/corpus-baseline.json
# part 1b — INSTRUMENT_PINS at F2: git BLOB ids (40 hex) — E05's class composed with E04; NOT sha256
68ccce1c152c915e16893a5157c9d5878df779fb  verifiers/verify_corpus_integrity.py
e887de71892ecfc6be5b3f47e362ce8a766c5c89  verifiers/verify_corpus_independent.py
# part 2 — C2 frozen bytes at F2: the counter the depth claim is counted by
a12921bee0433e88b04dd0ff5779cb0cd2bbdd3671d5faa574bfd5928e19f08e  verifiers/check_allowed_tools.py
# part 3 — the C1 repair patches as published (sha256 of the build artifacts)
dde6d91e888d4d6f41073bf985615927d16fdf67f547303127233cccc90a0b94  .ufo/waves/round-80/build/Kb80E01Registry.patch
0f3202409299e0ef2e29242d80c8816f23f9cf04502a370925142d27564bf35b  .ufo/waves/round-80/build/Kb80E02Symlink.patch
54e43309e05af3f98d23b030f811d9a729aa865b2dea6a9dc8dc778cf9d796f9  .ufo/waves/round-80/build/Kb80E03IndexBaseline.patch
d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78  .ufo/waves/round-80/build/Kb80E04DeadPointer.patch
a4345d34d3a8e35d7697b5abc05d077c2bb43e49e636edd6937590b1b223a2d3  .ufo/waves/round-80/build/Kb80E05GrammarFix.patch
# P5b withdrawn: E05's single patch carries both gates' class.
# superseded composition artifacts (kept for the record, NOT to be landed with E05):
#   938ee8df50df1094bf7a169790bb5b6242de0b11827d046bbabbb15294a3f4b6  Kb80E06CounterErratum.Y01bundle-minus-counter.patch (embeds Y01's class)
#   5c163cebb0c4ea57660bad5ee10d64315fccc1ba2d297d153d374798ea7cde9d  (the PREVIOUS recipe, Y01 stack; superseded by the line below)
#   Y01 stream, archived under build/Kb80E06CounterErratum/superseded-y01-pins/: counter 15cc1761..., patch f94f7e04...,
#   pins cc182613.../89f392da..., rev 0c730880..., tree dde9e843..., baseline 1058c8da...
# f94f7e04... (the Y01-pin patch) is superseded; the re-issued patch is below.
fcd886870d3689468c8fa2a5f9aad27b4e0b25e9a4ca06dcf89d7fe297b80382  .ufo/waves/round-80/build/Kb80E06CounterErratum.patch
b13ce13c03ca25bb6072308dd361cf2272c6c31ba2bee52383b4774e97c68ea7  .ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh
# part 4 — port provenance: the r79 reviewed drafts these repairs start from (inputs, not claim surfaces)
c411106e1ce60f14a87840b42906642d3bfe1dee1f37d8f60042143d2c95c611  .ufo/waves/round-79/build/Kb79E01Registry.patch
0f3202409299e0ef2e29242d80c8816f23f9cf04502a370925142d27564bf35b  .ufo/waves/round-79/build/Kb79E02LogCitation.patch
d7169dd8f9db17a908f00c1e62a668d73c7ca96cca75626807fb81889f4a5d78  .ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch
8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a  .ufo/waves/round-79/build/refresh-corpus-baseline.py
74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6  .ufo/waves/round-79/build/check_allowed_tools.py
```

Line counts of the block above (measured, not estimated): 26 value lines, 1 `base=` line, 6 section
headers, 34 non-empty lines (two legacy lines are withdrawn and therefore a comment, not a value). Part 3 carries **six slots** P1–P6; P5 is one repair published as two
files (one per gate). If E05 publishes a single combined patch instead, delete the P5B line, retitle
P5A's path to that single file, and say so in the report — six slots, six patch digests, file count 6
or 7.

---

## 2. Markers — source, recompute command, blocking status

`<lane>` = `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; `<F2>` = the freeze commit; run every
command from `<lane>`.

| Marker | Value comes from | Recompute command | Blocks |
|---|---|---|---|
| ~~`{{SHA_TIP_BATTERY_R80}}`~~ **filled** | `build/Kb80E06CounterErratum.sha256` (E06) | `sha256sum build/check_tip_battery.amended.py`; `git -C <lane> show <F2>:verifiers/check_tip_battery.py \| sha256sum` after landing | filled in §1 |
| ~~`{{BLOB_INTEGRITY_R80}}`~~ **filled** | the composed stack’s gate hunks (`Kb80Y01-simplified.patch`, which embeds E04’s hunk); E05 never published | `git apply Kb80Y01-simplified.patch` on a clone at 398cbe1, then `git hash-object verifiers/verify_corpus_integrity.py` → `cc182613…` (re-derived here; receipt block `composed instrument blobs re-derived`) | filled in §1 |
| ~~`{{BLOB_INDEPENDENT_R80}}`~~ **filled** | same composed stack | `git hash-object verifiers/verify_corpus_independent.py` → `89f392da…`; then `git -C <lane> rev-parse <F2>:<path>` must equal it | filled in §1 |
| `{{SHA_ALLOWED_TOOLS_R80}}` | `build/check_allowed_tools.py` (E07) | `git -C <lane> show <F2>:verifiers/check_allowed_tools.py \| sha256sum` | F2 |
| `{{SHA_PATCH_P1_REGISTRY}}` | `build/Kb80E01Registry.patch` (E01) | `sha256sum .ufo/waves/round-80/build/Kb80E01Registry.patch` | F2 record |
| ~~`{{SHA_PATCH_P2_SYMLINK}}`~~ **filled** | `build/Kb80E02Symlink.patch` (E02) | `sha256sum .ufo/waves/round-80/build/Kb80E02Symlink.patch` | filled in §1 |
| `{{SHA_PATCH_P3_INDEX}}` | `build/Kb80E03IndexBaseline.patch` (E03) | `sha256sum .ufo/waves/round-80/build/Kb80E03IndexBaseline.patch` | F2 record |
| ~~`{{SHA_PATCH_P4_DEADPOINTER}}`~~ **filled** | `build/Kb80E04DeadPointer.patch` (E04) | `sha256sum .ufo/waves/round-80/build/Kb80E04DeadPointer.patch` | filled in §1 |
| `{{SHA_PATCH_P5A_GRAMMAR_INTEGRITY}}` | `build/Kb80E05GrammarFix-integrity.patch` (E05) | `sha256sum .ufo/waves/round-80/build/Kb80E05GrammarFix-integrity.patch` | F2 record |
| `{{SHA_PATCH_P5B_GRAMMAR_INDEPENDENT}}` | `build/Kb80E05GrammarFix-independent.patch` (E05) | `sha256sum .ufo/waves/round-80/build/Kb80E05GrammarFix-independent.patch` | F2 record |
| ~~`{{SHA_PATCH_P6_COUNTER_ERRATUM}}`~~ **filled** | `build/Kb80E06CounterErratum.patch` (E06) | `sha256sum .ufo/waves/round-80/build/Kb80E06CounterErratum.patch` | filled in §1 |

**Six constraints the marker values must satisfy — check them before substituting, not after:**

- **C-a Ordering.** E04 and E05 both patch `verifiers/verify_corpus_integrity.py`. E04-only blob is
  `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` (published `build/Kb80E04DeadPointer.blob`; the patch is
  17 insertions / 0 deletions, `git apply --numstat`, receipt block `r79 E04 patch line counts`). The frozen pin must be the
  **E04∘E05 composed** blob. Applying E06's pin from `Kb80E04DeadPointer.blob` instead would fail
  `instrument-pin` at the integrated tip — finding F2.
  Guard: `git -C <lane> rev-parse <F2>:verifiers/verify_corpus_integrity.py` must **differ** from
  `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f`. If it does not, E05's integrity hunk was lost.
  **P5 is E05's class, and the pins moved with it (F22).** `Kb80E05GrammarFix.patch`
  (sha256 `a4345d34…`) is the reviewed official class: E04-free, applies to the bare base and on top of
  E04 in either order, and composed with E04 it hashes to `68ccce1c…` (integrity) / `e887de7…`
  (independent) — re-derived here (receipt block `E05 composed with E04`). The six-instrument numstat is
  **60 added / 8 deleted**, exactly at `LINE_CAP` with **zero headroom** (C-b). E06's published counter
  `15cc1761…` pins Y01's blobs (`cc182613…`/`89f392da…`), so it is **stale**: two reviewed
  implementations of the class exist in this wave, exactly one may land, and the counter must be
  republished with the landed one's pins. The Y01 bundle (`938ee8df…`) and its landing recipe
  (`5c163ceb…`) are superseded for the same reason and kept only as a record.
  **A class-only patch is pinnable — the pin is on composed content.** Measured: E04-applied
  `verify_corpus_integrity.py` is `051b8c5f…`; a class-only diff (E04-applied → composed, 27/4,
  sha256 `4f0663b7…`) applied on top yields exactly `cc182613…` (receipt block `class-only + E04
  reproduces the pinned blob`). So E05 may publish a class-only patch; what the pin requires is that
  E04 lands in the same tree. The world seat's W5b `instrument-pin` failure (blob `67a668ce…`) is the
  class applied **without** E04, not evidence that a class-only path cannot be pinned.
  **The two streams conflict on the counter itself, and the recipe is how that is avoided, not
  whether it matters:** E06's patch does not apply to a tree that
  already carries Y01's counter hunk (`error: patch failed: verifiers/check_tip_battery.py:103`, exit 1,
  receipt block `E06 patch on the Y01 bundle: conflict`). The L1 therefore lands **one** stack, and the
  freeze receipt's part-1 line must name that stack's counter bytes (`15cc1761…` for E06's stream,
  `ae29fc7b…` for the Y01 bundle).
- **C-b Cap arithmetic.** The `LINE_CAP` the amendment sets (60) must cover the six instruments'
  total additions *and* deletions against the counter's **pinned** base, `BASE =
  072048fa8e8a52c707d25f7079772fa317244eb7` — the guard diffs from that constant, never from the
  measured rev's own ancestor:
  `git -C <lane> diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 <F2> -- verifiers/check_gate_registry.py verifiers/check_assertion_floors.py verifiers/verify_skill_checklist.py verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py verifiers/check_correction_sweep.py | awk '{a+=$1; d+=$2} END {printf "added %d deleted %d (each must be <= 60)\n", a, d}'`
  Measured now, pinned base → r80 base: `22 3 verifiers/check_assertion_floors.py`, total **22 added /
  3 deleted** (receipt block `pinned-base instrument delta (what the guard measures)`). Diffing
  `398cbe1..<F2>` instead — the obvious mistake, and the one this receipt exists to prevent —
  under-reports by 22 and makes a diff that fails `instrument-size` look budget-clean. With E04's +17
  the running total is 39, so the grammar class has 60 − 39 = **21 added lines across BOTH gates**.
  **E05's class spends 20 of them (28/2 on integrity, 10/3 on independent) and the total is exactly 60 —
  zero headroom:** any further instrument edit fails `instrument-size`, and the freeze must assert the
  per-file numstat, not merely the sum (`--expect-numstat`, §4.3).
- **C-c No post-freeze counter edits.** From the tip:
  `git -C <lane> diff --quiet <F2> <TIP> -- verifiers/check_tip_battery.py verifiers/check_allowed_tools.py`
  must exit 0. A non-zero exit means an after-value was measured on bytes that are not the frozen ones —
  the freeze defect this file exists to make visible. C-c also fixes **which** counter (part 1's single
  declared stream): a tree whose `verifiers/check_tip_battery.py` hashes to `15cc1761…` or
  `ae29fc7b…` is a different round-80 counter, not a stale variant of this one.
  **Republish acceptance test — now executable without any archive.** Compare the **base** counter with
  the **final** one, both derivable from committed/reviewed bytes:
  `diff <(git -C <lane> show 398cbe1:verifiers/check_tip_battery.py) .ufo/waves/round-80/build/check_tip_battery.amended.py`
  → **30 added / 12 deleted** (re-measured here), and the semantic content is exactly: the two docstring
  cap mentions 40→60; the `LINE_CAP` constant and its erratum comment; the two pin rows each gaining one
  member (`68ccce1c…` / `e887de7…`); the size-world fixture and its expected string re-anchored to
  `LINE_CAP`; the stub-world padding and its expected string re-anchored; and the pin-arm edit widened
  from 2 to 41 lines with its comment. Measured on the bytes: `68ccce1c…` twice, `e887de7…` twice,
  **Reviewer's supersession delta (Kb80V01C1's re-diff, accepted):** against the superseded `15cc1761…`
  stream the change is **two pin values plus one comment line** (the E5 rationale now names the canonical
  E05 blobs) — no guard logic, no self-test arm change; the republished patch applies at base and its
  `--self-test` reads 0 failures / 69 assertions. That delta and the 30/12 base→final numstat describe the
  same bytes from two directions, which is why both are recorded.
- **C-d The external-commit class is line-scoped- **C-d The external-commit class is line-scoped- **C-d The external-commit class is line-scoped, or C1 stays red.** Measured at the base in both
  gates' own JSON: the only two `commit_unresolvable` tokens are `corpus/SOURCES.md:171` and `:172`,
  both the bare hex `7bb48f213ac677f943d5c791199ed3dddf302f00` with the third-repository name
  (`badlogic/pi-mono`) separate on the same line; the plan § Trigger's named `451a02ff` /
  `cfb894a5` are `commit_quoted` code-span exclusions, never unresolvable (receipt blocks `base
  commit classification, gate 1` and `gate 2`). A P5 keyed only on the in-token `owner/repo@<hex>`
  grammar therefore leaves both tokens unresolvable and the tip reads 5 of 6 — only the plan's
  "(or otherwise an explicit third-repository citation)" clause, applied at line scope, clears them.
  Check before substituting P5a/P5b: on a scratch tree with P4 + P5 applied, **both** gates print
  `commit_unresolvable = 0` and neither `corpus/SOURCES.md:171` nor `:172` reappears in a detail list.
  A **third** token arrives with the C2 entry: `corpus/knowledge/allowed-tools-surfaces-round80.md`
  carries a full-hex commit citation on a line whose only repository hint is the bare name
  `mistral-vibe` (no `owner/repo` token, no `owner/repo` URL on that line). Under an arm shaped "an
  unmarked absent token keeps the red path" that line reads unresolvable and landing the entry makes
  the gates red again. Measured since on the published entry draft
  (`build/allowed-tools-surfaces-round80.md`, 159 lines): exactly one backticked hex token,
  `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` — the **lane** base, which resolves — and zero
  `owner/repo@<hex>` matches (receipt block `C2 entry: commit-shaped tokens in the published draft`),
  so the entry as drafted adds no unresolvable token. Keep the assertion anyway: it is the arm that
  would catch a re-introduced third-repo digest, and a lane token that stopped resolving would be a
  regression the class must *not* excuse.
- **C-e If the grammar class cannot fit 21 lines, C1 stops — and the cap is never raised again.**
  The plan's kill rule fixes 22 + 17 + grammar ≤ 21 = 60 as an honest-stop boundary. Measured here on
  the published candidate (`Kb80S07Quality-world.patch`, sha256 `f4263274…`):
  `75 4 verifiers/verify_corpus_independent.py` + `96 1 verifiers/verify_corpus_integrity.py` =
  **171 added / 5 deleted**, which projects a guard total of 22 + 17 + 171 = **210 added against a cap
  of 60** — `instrument-size` fails by 150 lines (210 − 60)
  (receipt block `the grammar candidate E10Battery cites, measured here`). So that candidate cannot be
  P5; a class whose arms live in the two gates' own self-tests is the reason. E05 must either produce a
  class within 21 added lines across both gates or C1 ends as an honest stop: freeze this receipt with
  the P5 slots withdrawn, record the measured overshoot, and do not edit `LINE_CAP` a second time.

- **C-g The refreshed baseline is not a pure function of the tree.** `corpus-baseline.json` records the
  commit it was refreshed at (`head`/`note`), so a run whose commit ids differ produces different
  baseline bytes, a different tree and a different rev — the cascade that made the first two recipes
  non-reproducible while their *content* looked identical. Mechanically (measured by E06, reproduced
  here): `0e5a3ab` is the recipe's **pre-refresh** commit and `0c73088…` the refresh commit the recipe
  prints, so the baseline quotes the tree it was refreshed *from* — correct semantics, but it means the
  **baseline file is not reproducible from the tree alone**: the freeze must pin its bytes
  (`1058c8da…`, receipt block `refreshed baseline bytes at the deterministic recipe tree`) beside the
  tree id (`dde9e843…`), and a hand refresh with anyone's own clock yields different bytes from an
  identical tree. The chain is inputs → commit ids (themselves a function of the dates) → baseline
  bytes → tree → rev, so the dates sit **upstream of every hash in it**, not beside them: drop them and
  a recomputation from the same inputs still diverges. Four runs agree — two of E06's, one of mine and
  E06's fourth — on rev, tree and baseline digest (their `cross-verification.txt`, read here; my three
  are primary). The pinned recipe's fixed `GIT_*_DATE` plus the seven input digests is the complete
  recipe; the citable unit is the triple (inputs, dates, tree).
- **C-f Do not freeze part 2 while the C2 counter's quote locator rejects a single-occurrence page.**
  The draft counter's `quote_location()` accepts a located quote only after the first heading-like
  line. On `S229-msaf.html` the field name occurs **exactly once** (raw line 818, measured, receipt
  block `S229 (msaf) page: the field name occurs exactly once`), and the first `#`-prefixed line in the
  text view is a Python comment inside a code sample, not a heading — so every admissible quote starts
  before the locator's bound and is rejected. Freezing such a counter freezes a predicate whose best
  possible value is 5 of 6 for a reason no data can fix, and the pin would have to be re-cut after
  measurement — the defect a freeze exists to prevent. Substitute `{{SHA_ALLOWED_TOOLS_R80}}` only from
  a counter whose locator handles the HTML text view (or whose Q70 arm is re-declared in the plan), or
  record C2 as an honest stop with the part-2 line withdrawn. **Scope:** this blocks the C2 column
  only — `verifiers/check_allowed_tools.py` is not one of the six battery instruments, so C1's
  predicate, its guards and its `6 of 6` are untouched by it; the failure belongs to the C2 scorecard
  row (confirmed against the counter's `BATTERY` tuple, which names the six, and by Kb80V01C1
  independently).

---

## 3. Recompute every filled value (part 0, the filled part-3 digests, part 4)

Per line, from the base (a pre-state, not an after-value):

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
B=398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
for p in verifiers/check_tip_battery.py verifiers/verify_corpus_integrity.py \
         verifiers/verify_corpus_independent.py verifiers/check_gate_registry.py \
         verifiers/check_assertion_floors.py verifiers/verify_skill_checklist.py \
         verifiers/check_correction_sweep.py verifiers/corpus-baseline.json SKILL.md; do
  git show "$B:$p" | sha256sum      # must equal the part 0 line for $p
done
sha256sum .ufo/waves/round-80/build/Kb80E02Symlink.patch \
          .ufo/waves/round-80/build/Kb80E04DeadPointer.patch \
          .ufo/waves/round-79/build/Kb79E01Registry.patch \
          .ufo/waves/round-79/build/Kb79E02LogCitation.patch \
          .ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch \
          .ufo/waves/round-79/build/refresh-corpus-baseline.py \
          .ufo/waves/round-79/build/check_allowed_tools.py
```

Base git blob ids (the values `INSTRUMENT_PINS` carries at the base; receipt blocks `base git blob sha <path>`):
`check_gate_registry.py` `95ffed389f483c3d6f93db3c08dcfdb9a2240576`;
`check_assertion_floors.py` `9cb860bda21ef8d24fcb0603aa85372b96f3ac41`;
`verify_skill_checklist.py` `6aab16849bd6d71ded8f3bcb3f95668f14f6a78f`;
`verify_corpus_integrity.py` `e470eaaea5ef11c582b8353c9344ddf730c1a57a`;
`verify_corpus_independent.py` `edac0df79324ba62ee25ff10a6a4d422ef59da61`;
`check_correction_sweep.py` `c94b771fa7d798ef45fc3bb640422ee7910f81a6`.

Base `verifiers/corpus-baseline.json` expectations the repair must re-record (not free): 
`tracked_files 144`, `unindexed 0`, `report_total 99`, `report_dead 0`, `commit_total 43`,
`commit_unresolvable 0` (receipt block `corpus-baseline.json expectations at base`). The observed base tree is 152 / 1 / 109 / 1 / 46 / 2
(plan § Trigger), so the refresh at the pre-report commit must read the plan's expected values with
every zero class at 0 — that is the W3 control's job, not this file's.

If E05 publishes late, derive the two blobs yourself and say so:

```
S=/fast/scratch/hyaku/kotoba-r80/freeze; mkdir -p "$S"; export TMPDIR=$S/tmp; mkdir -p "$TMPDIR"
git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin "$S/clone"
git -C "$S/clone" checkout -q 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93
test "$(git -C "$S/clone" rev-parse --show-toplevel)" = "$S/clone" || { echo SCRATCH-NOT-TOPLEVEL; exit 2; }
git -C "$S/clone" apply /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E04DeadPointer.patch
git -C "$S/clone" apply <E05 integrity patch> <E05 independent patch>
git -C "$S/clone" hash-object verifiers/verify_corpus_integrity.py    # part 1b line 1
git -C "$S/clone" hash-object verifiers/verify_corpus_independent.py   # part 1b line 2
```

---

## 4. Substitution and verification (L1, in this order)

0. **Land the tree first, if the L1 takes the composition route.** One command —
   `bash .ufo/waves/round-80/build/Kb80E06CounterErratum.landing-recipe.sh <work-dir>` — applies the
   pinned landing patch, writes the amended counter, inserts the C2 counter, its registry row, the
   snapshots manifest and the entry with its coverage row, then commits and refreshes. Its inputs are
   seven artifacts whose digests the receipts file records under `recipe inputs` (the recipe and its
   six inputs); pin them with the recipe at F2, or the recipe's output is not reproducible. Pin
   **content and the deterministic rev**: the recipe now exports fixed `GIT_AUTHOR_DATE`/
   `GIT_COMMITTER_DATE`, and two from-scratch runs here produce the same rev and the same tree
   (`0c73088…` / tree `dde9e843…`, receipt block `determinism of the recipe, verified by two
   from-scratch runs`). The earlier runs did not: their *trees* differed, not just metadata, in
   `verifiers/corpus-baseline.json` `head`/`note` — see C-g. Pin both the rev and the seven inputs.
1. **Substitute** all 9 pending markers from §2, from the published build artifacts — never from a
   seat report or from memory; a patch digest recomputed from the file the patch names is the only
   acceptable source.
2. **No leftovers:** `grep -n '{{' .ufo/waves/round-80/receipts/freeze-shas.txt; echo rc=$?` → rc=1.
   Any rc=0 is an unsubstituted freeze and the commit stops.
3. **One command for the whole check** (published, so it is recomputable rather than described):
   `python3 -B .ufo/waves/round-80/build/Kb80S15FreezeShas-checkfilled.py --rev <F2>`
   `--repo <lane> --rev <F2>` → `checked 26 line(s), deferred 0 tip-side, skipped 0 pending, 0 failure(s)`, exit 0 once every line is filled (the `base=` line is checked
   separately by the same script and not counted in that number — it prints `MISMATCH base=` if wrong).
   As published, with no `--rev`, the same script prints `checked 17 line(s), deferred 3 tip-side,
   skipped 5 pending, 0 failure(s)`, exit 0: part 1 and part 1b describe bytes that are not in the tree
   until the freeze commit, so they are reported *deferred* rather than silently passed. `--repo <path>`
   moves only the git reads (useful when probing a scratch stack), never the part-3/4 workspace paths.
3b. **Assert the per-file numstat, not only the cap** (C-b: zero headroom):
   `python3 -B .ufo/waves/round-80/build/Kb80S15FreezeShas-checkfilled.py --repo <lane> --rev <F2> --expect-numstat "check_assertion_floors.py=22/3,verify_corpus_independent.py=10/3,verify_corpus_integrity.py=28/2"`
   → per-file match, `six-instrument numstat 60 added / 8 deleted (cap 60)`. Any extra line anywhere in
   the six reads `NUMSTAT MISMATCH` before the counter ever runs. Note that on a tree that has not had
   the baseline refreshed, part 1's baseline pin will report `MISMATCH` — that is correct: it pins the
   refreshed bytes (C-g), so it only matches the deterministic freeze tree.
4. **Per-part verification by hand**, if the script is unavailable (never `sha256sum -c` on the whole
   file — part 1b is 40-hex and part 3 paths are build artifacts):
   - part 0, at the base: the loop in §3, all nine digests equal.
   - part 1 and part 2, at F2: `git show <F2>:<path> | sha256sum` equals the line, for each of the two
     counters, and `git show <F2>:verifiers/check_allowed_tools.py | sha256sum` equals part 2.
   - part 1b, at F2: `git -C <lane> rev-parse <F2>:<path>` equals the line, and the C-a guard holds.
   - part 3: `sha256sum` of each file in `build/` equals its line (build/ is tracked in this lane —
     `.ufo/waves/round-79/build/` is 201 tracked files, so round-80's will be too).
   - C-b arithmetic and C-c (no post-freeze counter edits) hold.
5. **After-receipt (companion, written later, never merged into this file):**
   `.ufo/waves/round-80/receipts/after-shas.txt`:
   ```
   # post-freeze values the report cites; NOT freeze inputs
   {{SHA_CORPUS_BASELINE_TIP}}  verifiers/corpus-baseline.json
   {{SHA_SKILL_TIP}}  SKILL.md
   {{SHA_PROVINCE_TIP}}  PROVINCE.md
   {{SHA_ENTRY_TIP}}  corpus/knowledge/allowed-tools-surfaces-round80.md
   {{SHA_SYMLINK_TARGET_TIP}}  .ufo/reports/round-76/kotoba.md  # sha256 of the FOLLOWED link's bytes, not of a regular file
   ```
   The last line is checked with
   `sha256sum "$(readlink -f .ufo/reports/round-76/kotoba.md)"` → `a025051d389368ea3a1078b7a64d3847c1e6ff25328fc1645a7be34f30e3f78f`
   (the fleet file, tracked in the fleet repo; receipt blocks `fleet round-76 report sha256`, `fleet round-76 report is tracked in the fleet repo`). `sha256sum` on the link path
   itself would hash the target *string*, not the bytes — do not.

---

## 5. Erratum E5 — justification (one sentence, per the plan's kill rule)

Erratum E5's only **semantic** change is the two constants it declares — `LINE_CAP` from 40 to 60 and
one reviewed composed blob added to each of the two `INSTRUMENT_PINS` rows (`cc182613…` for
`verify_corpus_integrity.py`, `89f392da…` for `verify_corpus_independent.py`) — declared before any
after-value is measured and justified once, because the pin guard and not the size bound carries the
anti-laundering load (every one of the six instruments' bytes at the measured rev must equal the
round-72 base blob or a reviewed pin, so a weakened instrument is caught blobbily while a two-line stub
still fails under any cap at +2/−~1000), and because the declared repair arithmetic — 22 lines already
spent at the base, plus 27 for the E04+grammar composition of `verify_corpus_integrity.py`, plus 10 for
the grammar class in `verify_corpus_independent.py`, totals 59 against the new bound with one line of
headroom — would otherwise fail the reviewed repairs themselves, while the five guards' checks remain
semantically identical.

**Byte-level truth (measured, because the plan's "changes only" speaks about guard semantics, not about
hunks):** E06's shipped `Kb80E06CounterErratum.patch` is **29 added / 12 deleted**
(`git apply --numstat`); its other hunks only re-anchor the counter's own self-test fixture constants to
`LINE_CAP` and widen the existing `instrument-pin` arm's edit from 2 to 41 lines so the arm still
exercises the new cap, and a literal cap-and-pins-only edit leaves `--self-test` at **4 failed
assertions, exit 1** (E06's `selftest-cap60-naive.txt`), so "only the cap" was never a shippable E5.

Mapping to the kill rule's clauses: the two changed constants (guard semantics only); declared before
data; the pin guard as the load-bearing check with the size bound secondary; the cap arithmetic
22 + 27 + 10 = 59 ≤ 60, one line of headroom. A repair needing a guard's *logic* edited is still an
honest stop.

---

## 6. Findings

- **F1 (high, calibration).** The r79 freeze file pins `verifiers/baseline.json`; the corpus gate
  never opens that file — it reads `verifiers/corpus-baseline.json` (`BASELINE_NAME`), whose base
  digest is `22d5f0bb…` with expectations 144 / 0 / 99 / 0 / 43 / 0. r79's pin therefore guarded
  nothing, exactly as `Kb79SN01Sentinel` F9 recorded. Part 0 line 8 fixes the subject; `baseline.json`
  is deliberately dropped rather than carried for symmetry.
- **F2 (high, operability).** E04's published blob `051b8c5f…` is the E04-only instrument. E05 patches
  the same file, so an E06 that pins `051b8c5f…` (the value a reader of `Kb80E04DeadPointer.blob`
  would reach for) turns `instrument-pin` red at the integrated tip and the wave reads 5 of 6 for a
  bookkeeping reason. The freeze receipt states the composition rule (C-a) and pins only the composed
  blob.
- **F3 (medium, provenance).** The plan and the seat briefing name
  `.ufo/waves/round-79/build/Kb79E04DeadPointer.patch`; that path does not exist (`ls` → exit 2, no
  such file). The reviewed bytes are at
  `.ufo/waves/round-79/build/Kb79E04DeadPointer/Kb79E04DeadPointer.patch`, sha256 `d7169dd8…` (the
  digest the plan quotes, on the subdirectory path). Part 4 names the real path so the pin is
  recomputable.
- **F4 (low, freshness).** The E07 seat brief calls the r79 draft counter "1,6xx lines"; the file is
  2,288 lines, sha256 `74e067cc…`. Harmless to the claim, but a reviewer checking "read the file"
  against the brief would think they had the wrong artifact.
- **F5 (low, consistency).** The `Kb80S02Log` brief specifies the wave shape as "attack share
  18/64 = 28.1 %". The dispatched spec carries 17 attack seats — critics 6 + reviewers 6 +
  mutation-testers 4 + sentinel 1 — i.e. 17/64 = 26.6 %, which is what the plan prints (receipt block `round-80 w1 role census (attack share)`).
  The LOG entry must carry 17 (or the L1 must say why 18); the plan's threshold (≥ 25 %) holds either
  way, so this is a wording defect, not a claim defect.
- **F6 (low, design).** r79's freeze file is a flat list of nine lines with no statement of which
  value binds which claim, plus a "part 2" that its own LOG draft expected and that never landed
  (`Kb79A04LogScoreDraft` line 37 cites `receipts/freeze-shas.txt` part 2 for `{{SHA_CTR}}`). Round 80
  sections by role, keeps after-values out (companion receipt), and labels the blob grammar; the
  premise that headers are safe is measured, not assumed (no parser, receipt blocks `no verifier parses freeze-shas.txt` and `the lane has no scripts/ dir`).
- **F7 (self, low, fixed).** My first receipt pass wrapped `git show base:SKILL.md | wc -l` inside a
  `run` helper, so the pipeline's status was recorded and 590 lines of `SKILL.md` were written into
  the receipt. Regenerated with one command per block and each command's own exit status — the M80-1
  class of error, caught in the seat that documents how to avoid it. The regenerated file is the only
  receipts file published.

- **F8 (positive, provenance).** Both patches published by E02 and E04 are **byte-identical** to the
  r79 reviewed drafts they port: `Kb80E02Symlink.patch` = `Kb79E02LogCitation.patch` (sha256
  `0f320240…`) and `Kb80E04DeadPointer.patch` =
  `Kb79E04DeadPointer/Kb79E04DeadPointer.patch` (sha256 `d7169dd8…`) — receipt block
  `part-3 digests now filled (P2, P4) and their byte-identity with the r79 drafts in part 4`. So the
  part-3 lines for P2/P4 and the corresponding part-4 lines are the same digests by construction: a
  reviewer reading the freeze file can see that the "new" repair is the reviewed byte stream, not a
  re-derivation, and `git apply --numstat` shows the shapes the review measured (P4: 17 insertions in
  `verifiers/verify_corpus_integrity.py`; P2: 1 insertion in `.ufo/reports/round-76/kotoba.md`).
- **F9 (low, evidence, routed to E02/L1).** `build/Kb80E02-sym-tipbattery.txt` is **0 bytes**
  (`wc -c` → 0). An empty receipt named after a battery run is evidence of nothing; if the C1 report
  cites it for the symlink-only world (plan W2: "expect ≤3 of 6, per the r79 receipt
  `Kb79E02-sym-tipbattery.txt`"), the citation must move to the r79 receipt or the artifact must be
  regenerated. It does not move any number in this freeze file.

- **F11 (high, calibration).** The plan § Trigger names the wrong blockers: it says the two
  `commit_unresolvable` tokens are `google-gemini/gemini-cli@451a02ff` and
  `zed-industries/zed@cfb894a5`. Both gates, measured at the base, report
  `commit_unresolvable = 2` with detail `corpus/SOURCES.md:171` and `:172`, both
  `7bb48f213ac677f943d5c791199ed3dddf302f00`, while `451a02ff` and `cfb894a5` sit in
  `commit_quoted` (6 exclusions, receipt blocks `base commit classification, gate 1`/`gate 2`).
  A repair-5 implemented to the plan's literal wording (in-token grammar) clears nothing; the
  parenthetical clause is the operative one (C-d). The plan text is L1-frozen and not mine to edit —
  the correction belongs in the round-80 lesson and the LOG.
- **F12 (medium, freshness — direction corrected).** The two blocking rows cite the *same* hex
  `7bb48f213ac677f943d5c791199ed3dddf302f00`, and the fetch records say whose it is:
  `S230.fetch.json` (pi-mono) records `main` at fetch time = `bb65e3e49710fbd14f10c7792d0eaa6e2b2c5923`
  (blob sha1 `19d2bf28…`, last path commit `25cc5c7b…`), while `S231.fetch.json` (vibe) records
  `main` = `7bb48f21…`. So the defective row is **S230**, the pi-mono row citing **vibe's** commit;
  S231's hex is its own and correct. My first draft of this finding said the reverse (S231 wrong) on the
  plausible but insufficient ground that it looked like a copy of S230 — the fetch records contradict
  that reading and this is the correction; `Kb80E08C2Entry` reached the same conclusion independently
  (receipt block `which repository does each blocking hex belong to?`). Neither hex is in lane or fleet
  (`7bb48f21…` → exit 128 both; the correct `bb65e3e4…` is also absent, exit 128, and is not
  cited), so the external-citation class remains the right disposition for the text actually present;
  the row error itself is a lesson item, since the plan allows only `used-by` changes in S226–S231.

- **F13 (self, high, fixed).** The C-b command I first wrote diffed `398cbe1..<F2>` for the
  instrument-size budget. The guard diffs from the counter's **pinned** base
  `072048fa8e8a52c707d25f7079772fa317244eb7`, so that command would have under-reported by 22 lines
  and passed a diff that fails `instrument-size`. Corrected in C-b, with the pinned-base measurement
  recorded (22 added / 3 deleted, all in `verifiers/check_assertion_floors.py`). This is the same
  class of error as F7 — a plausible command that answers a neighbouring question — and the reason the
  freeze receipt carries its own checkable commands rather than prose.
- **F14 (high, calibration — superseded reading).** With E05's official class the composed stack is
  **60 added / 8 deleted**, exactly at the cap with zero headroom (28/2 on integrity, 10/3 on independent,
  22/3 already spent at the base). Earlier readings in this receipt — the 171-line standalone candidate
  and the 59/10 Y01 composition — are now history: the class that can land is E05's, and it fills the
  budget to the line.
- **F15 (high, structural).** The C2 counter's quote locator cannot admit any msaf quote: the page
  names the field once (raw line 818, measured) while the locator requires the quote to start after the
  first heading-like line, and the first `#`-prefixed line on that page is a Python comment inside a
  code sample. So the counter's maximum for a fully documented msaf surface is 5 of 6 whatever the
  documentation says, which makes part 2 of the C1/C2 freeze meaningless unless the counter changes
  (C-f). Reported by `Kb80E08C2Entry`; the occurrence count is re-measured here.

- **F16 (high, operability — the stack fork, re-opened by E05).** Two reviewed implementations of the
  same class exist: Y01's (bundled, embeds E04, pins `cc182613…`/`89f392da…`) and E05's
  (class-only, E04-free, pins `68ccce1c…`/`e887de7…`). Exactly one may land. E06's published
  counter and its landing recipe are built on Y01's, so they must be rebuilt on E05's before the freeze
  — otherwise the counter pins blobs no landed tree carries and `instrument-pin` reds at the tip.
- **F17 (self, medium, fixed).** My E5 sentence said the amendment "changes exactly two things … and
  nothing else". Measured against the shipped patch that is false (29/12, fixture re-anchors, arm
  widened from 2 to 41 lines). The sentence now states the semantic change and carries the byte-level
  truth beside it — the plan's wording is about guard semantics, and a freeze receipt that repeats it as
  a hunk count would be the exact misreading the receipt exists to prevent.

- **F18 (medium, calibration — conditional on the fork).** The two counter streams enforce the same
  guard semantics (cap 60, the same two pins) and differ only in self-description and one fixture: the
  Y01 stream keeps the guard docstring saying the instruments "gain at most 40 … lose at most 40" and
  the erratum comment "(# stays 40)" while `LINE_CAP = 60` (verified on the Y01-applied tree, receipt
  block `Y01 counter variant: enforces 60, documents 40`), and keeps the 2-line pin fixture; E06's
  stream updates that prose and widens the fixture to 41 lines. If the L1 lands Y01, the instrument
  misdescribes its own bound — a calibration defect that belongs in the lesson, and one a reader of
  `--help`/docstring would trip over when a 45-line instrument change passes a document that says 40.

- **F19 (high, calibration — CLOSED by the recipe's second revision).** The first landing recipe's tree
  had no `verifiers/check_allowed_tools.py`, so its `6 of 6` was a C1-only reading; adding the C2 counter
  without its registry row made `check_gate_registry.py` read
  `verifiers/check_allowed_tools.py   no registry rows naming it: 0 (need 1)`, `62 of 63`, exit 1. The
  recipe now composes four extra pieces — (i) the C2 counter, (ii) its gate-registry row (S09's text
  extracted, not applied: the bundle moved `SKILL.md`), (iii) `snapshots/MANIFEST.sha256` with six
  digests verified against the committed snapshot bytes, (iv) the entry plus its coverage-map row in the
  COVERAGE MAP table (inserting after the last `| ` line lands it in the Frontier table and the gate
  still reads `unindexed = 1`) — and commits before refreshing, because the refresh reads worktree
  bytes while recording at `HEAD`. **Re-run here (primary):** rev `6bf9a31…`, counter `15cc1761…`,
  blobs `cc182613…` / `89f392da…`, numstat `22/3 + 10/3 + 27/4` = 59 added / 10 deleted,
  `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`, `post-refresh: 9/9 checks pass,
  exit 0` (receipt block `full landing recipe re-run here`). The battery itself was **not** run by this
  seat — that is the claim's after-value and belongs after the freeze.

- **F21 (self, medium, corrected).** My reproducibility finding was right about the symptom and shallow
  about the cause: I read "different revs" as "commit metadata" and advised pinning content only. The
  **trees** differed, in `verifiers/corpus-baseline.json` `head`/`note`, because the refresh embeds the
  commit it ran at — the cascade is baseline → tree → rev. E06 found that, pinned the dates and
  measured two identical runs; I reproduced it (`0c73088…`, tree `dde9e843…`, twice). The practical
  advice survives (pin the inputs) but the reason and the status of the rev changed: it is now
  reproducible and may be cited (C-g).

- **F22 (high, calibration — the pins moved, twice).** E05's canonical class fixed the pin values
  (`68ccce1c152c915e16893a5157c9d5878df779fb` / `e887de71892ecfc6be5b3f47e362ce8a766c5c89`) and E06 then
  re-issued the counter on them: **counter `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`**,
  patch `fcd88687…`, recipe `b13ce13c…`, landing patch unchanged `938ee8df…`. Re-run here: rev
  `fc91d8d2…`, tree `a207fafb…`, refreshed baseline `9f2d3ef5…`, `63 of 63`, `9/9 checks pass`,
  six-instrument numstat 60 added / 8 deleted (receipt block `re-issued recipe run`). The whole Y01 stream
  — counter `15cc1761…`, patch `f94f7e04…`, recipe `5c163ceb…`, pins `cc182613…`/`89f392da…`,
  rev `0c730880…`, tree `dde9e843…`, baseline `1058c8da…` — is superseded, kept visible in
  part 3 and archived by E06 under `superseded-y01-pins/`, because it was true of a stream that was
  reviewed and then not landed.

- **F23 (high, operability — the freeze is not recomputable from its own rev).** The L1's committed
  `receipts/freeze-shas.txt` (`5599193`) pins `build/check_tip_battery.amended.py`, `build/Kb80E06CounterErratum.patch`,
  `build/check_allowed_tools.py` and the integration patches — but `git ls-tree -r 5599193
  .ufo/waves/round-80` lists **no** `build/` path and `git ls-files .ufo/waves/round-80/build` is empty
  (0 files, against 201 tracked in r79). `git show 5599193:build/check_tip_battery.amended.py` returns
  nothing, so every pinned input exists only in the worktree. The *numbers* are right — I hashed the
  worktree and they match the receipt exactly (counter `20e496…`, patch `fcd886…`, C2
  `a12921be…`, E01 `dde6d91e…`, E03 `54e43309…`, E05 `a4345d34…`, S05 `5cec8585…`, S10
  `6f342703…`, entry `caadf57d…`, S08 `10117e66…`, S09 `9ad16e05…`) — so this is a
  *location* defect, not a value defect. **Two tiers, because only one of them is fixable by the
  landing itself.** For the counter and the two pins, F23 is a citation problem the integration commit
  resolves by construction — from the landed tip, `git show <tip>:verifiers/check_tip_battery.py |
  sha256sum` → `20e496…`, `git rev-parse <tip>:verifiers/verify_corpus_integrity.py` → `68ccce1c…`,
  `… verify_corpus_independent.py` → `e887de7…`. What the tree can never recover are the *process*
  artifacts that do not land in `verifiers/`: the counter patch (`fcd88687…`), the landing recipe
  (`b13ce13c…` — the reproducible way to rebuild the stack, existing nowhere else), the
  bundle-minus-counter patch (`938ee8df…`), and the round's receipts and seat reports. If `build/` is
  never committed and the worktree is discarded those are **lost, not merely unreadable** — the sharper
  form of this finding, put to the L1 by `Kb80E06CounterErratum` independently. Remedy stays the same and
  follows the r79 precedent: commit `build/` (201 tracked files there). General form worth carrying past
  this round: *a freeze is only as strong as the retrievability of what it names* — hashing a worktree
  file proves its value now, not its availability later, and only a commit gives the second property.
  **Severity, aligned:** this receipt graded F23 high from the outset and the C1 reviewer of record has
  since aligned their report to **High** on the same ground — tier 2 is irreversible: an unreadable
  citation is a nuisance, losing the landing recipe and the counter patch as reviewed bytes is not. The
  L1 owns the fix (track `build/` inputs in the integration commit, r79's 201-file precedent), and it is
  the only open item either seat tracks.

---

## 7. Out of scope of this seat (stated, not implied)

No after-value was measured: I did not run `check_tip_battery.py`, either corpus gate, or the C2
counter. I did not build, edit or re-derive any patch; no lane file outside
`.ufo/waves/round-80/build/` was touched; nothing was committed, staged or checked out in the lane.
The `Kb80E04DeadPointer.blob` value is read as published, not recomputed from a patched tree (the
E04 seat owns that measurement; the recompute command is given in §3).

**Touch surface:** `.ufo/waves/round-80/build/Kb80S15FreezeShas.md` (this file),
`.ufo/waves/round-80/build/Kb80S15FreezeShas-receipts.txt` (41 command blocks, each with its
command's own exit status — never a pipeline's),
`.ufo/waves/round-80/build/Kb80S15FreezeShas-checkfilled.py` (the freeze self-check; sha256
`a2f65641…`), `.ufo/waves/round-80/w1/Kb80S15FreezeShas.md` (seat report). Scratch
`/fast/scratch/hyaku/kotoba-r80/Kb80S15FreezeShas/` was used only for a temporary prompt dump and a
grep capture, holds no clone, and is removed before yielding.
