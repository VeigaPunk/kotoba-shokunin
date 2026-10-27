# E09D2D3Hygiene — r74 hygiene repairs D2 + D3 (kotoba round 77, w1)

Seat: executor, leaf. Lane base for every measurement: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (r77 freeze).
Lane tree was not written by this seat: the deliverable is a patch plus drafts under `.ufo/waves/round-77/`.
No tool was installed (nothing needed; pacman not run). Scratch clone was removed after the evidence was copied.

## 1. The ask, re-derived (not taken from the r76 drafts)

`corpus/lessons/round-74-verifier-spotcheck.md` at the r77 base:

- § 1 Conformance defects, **D2** (:38-40): "`d5aebcf` … sits between `d919179` and `2c81137` on `master` but is
  absent from the report's Landed changes table and from `LOG.md` (`grep -c d5aebcf` → 0 in both). It is an
  orchestrator snapshot, not lane work, but the 'every landed change tied to a LOG entry' contract has no line for it."
- § 5 Routed defects, item 2 (:137): "List the orchestrator snapshot `d5aebcf` in the round-74 record (**LOG appended
  correction**) as a non-landing commit (D2)."
- § 5 Routed defects, item 3 (:138): "The round-49 census entry `corpus/knowledge/sibling-overlap-census-round49.md`
  carries no forward pointer to its round-74 re-pin …; **append one** so a reader of the old entry meets the corrected
  tsukuroi class."

## 2. Facts verified at the r77 base (read-only, lane repo)

```
$ git cat-file -t d5aebcf                                  → commit        (resolves)
$ git log -1 --format='%H|%an|%ad|%s' --date=iso d5aebcf
d5aebcf51c394435e768461001a2d0cc8f67fe3a|kotoba-shokunin|2026-10-25 23:16:44 -0300|hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here
$ git show --name-only --format='' d5aebcf | grep -c .    → 394 files
$ git log -1 --format='%P' d5aebcf                        → d919179c63925e27f0d047ccccfc30b49cfe9766
$ git merge-base --is-ancestor d919179 d5aebcf            → exit 0
$ git merge-base --is-ancestor d5aebcf 2c81137            → exit 0
$ grep -c 'd5aebcf' LOG.md                                → 0 (exit 1)   (still absent at the r77 base)
$ grep -c 'round-74\|Round 74\|round74' corpus/knowledge/sibling-overlap-census-round49.md → 0 (exit 1)
$ awk 'NR==43||NR==246||NR==416||NR==466{...}' corpus/knowledge/sibling-overlap-census-round49.md
43: ## Classification rule
246: ## Round 50: precedence between `contested` and a stated split (routed…
416: ## Round 51 status of the precedence rule (routed D6)
466: are in `skill-overlap-levers-round51.md`.     (file is 466 lines)
```

The round-74 re-pin the pointer must name exists and is tracked:
`corpus/knowledge/sibling-overlap-census-round74.md` (`verified-at: 2026-10-25`; `:26` "Classes now: 10 adjacent,
10 none, 0 contested — … round 49 had 9 adjacent and 11 none"; `:29` "One class changes: tsukuroi `none` →
`adjacent` (basis kotoba)").

## 3. Form decision for D2 — FormB (tail correction section), with the reasoning

Three constraints meet here:

1. The closure's routed item 2 says **"LOG appended correction"** — the object is a correction, and it is appended.
2. `LOG.md` is append-only in this corpus (`check_r63_routed_repairs.py` conjunct 4 asserts the r62-tip `LOG.md` is a
   byte-prefix of the measured `LOG.md`); the r77 prompt names the same discipline.
3. The general listing contract D2 names ("every landed change tied to a LOG entry") is satisfied by any line that
   lists the commit; it does not require the line to sit inside § Round 74.

FormA (a bullet inserted after `LOG.md:2803`, inside § Round 74) contradicts (1) and (2): it is an insertion, and the
r76 draft measured that it breaks the base→tip byte-prefix for `LOG.md` (`starts-with b7f13f4` → False, first
difference at byte 560524). FormB satisfies all three; `LOG.md` gains the section at the tail and every existing byte
stays where it is. The r77 plan's paraphrase (touch list: "`LOG.md` (§ Round 74 `d5aebcf` line)") and the r76 plan's
("round-74 d5aebcf line") describe the content, not the position; the closure's parenthetical governs the position.
**Decision: FormB.** The draft's ordering note is preserved: the section may land before or after the round-77 entry
(the reading order differs, the append-only property does not).

## 4. Deliverable — one unified patch

`.ufo/waves/round-77/build/E09D2D3Hygiene.patch` (sha256
`e366ac06f22d2963e7962cadd563d68127f28457f251ebfc2b429185aaf63410`), generated as
`git diff 6523ace f3a2dc4` in the scratch clone:

- `LOG.md`: +4 lines, `## Round 74 correction (append-only, routed D2)` — commit facts (subject, 394 files, author,
  timestamp), position between `d919179` and `2c81137`, the "not a landing / not lane work" reading, the two commands
  that check it, and the routing trail (r74 spot-check D2 + routed item 2; drafted in round 76 as
  `.ufo/waves/round-76/build/B10RepairD2D3.formB.patch`; landed in round 77 as this appended correction).
- `corpus/knowledge/sibling-overlap-census-round49.md`: +15 lines, `## Round 74 forward pointer (append-only, routed
  D3)` — names the re-pin entry, the three line ranges it inherits (`:43-64`, `:246-295`, `:416-458`, unchanged), the
  nine-cell method, the tsukuroi `none` → `adjacent` change and the counts, then the **measured** status at the r77
  base (`rows 20 verified 20` but exit 1, 16 `FAIL` lines: 15 pinned lane commits moved since 2026-10-22 plus the
  tsukuroi class; the round-74 entry's command is 20/20 exit 0). The draft's status sentence was written at
  `4de12b6`; it was re-measured at the r77 base and the numbers are unchanged, so the text keeps them and now names
  the base revision it was measured at. Frontmatter of the census entry is untouched.

Applied at the r77 base, the patch reproduces exactly the scratch after-state (byte diffs empty for both files).

**Apply-order hazard (measured, not assumed).** The LOG hunk is anchored on the current tail (§ Round 76's last
three lines). Applied at the r77 base: `git apply --check` exit 0. Applied to a tree that already carries a later LOG
tail append (a dummy `## Round 77 — …` section): `git apply --check` exit 1 (`patch failed: LOG.md:2816`), and
`git apply --3way` also refuses (`does not match index`, because the appended tail is unstaged). **Instruction: apply
this patch before the round-77 LOG entry lands; if the round-77 entry has already landed, append the section bytes at
the tail instead of applying the hunk** (the added lines are visible verbatim in the patch). The census hunk has no
such coupling.

## 5. Measurements (scratch clone; every exit code is the gate's own, captured as `cmd > out 2>&1; echo "exit=$?" >> out`)

Harness: `git clone --shared` of the lane → `…/E09D2D3Hygiene/kotoba-shokunin`, `user.name scratch-r77`,
`user.email scratch@example.invalid`, `git rev-parse --show-toplevel` asserted equal to the clone before the first
commit; fleet-layout shim (symlinks to the fleet `.ufo`, `*-shokunin`, `PROTOCOL.md`, `AXES.md`, `CORPUS.md`,
`MISSION.md`, `SCORECARD.md`, `MANIFEST.json`, `scripts`) at the clone parent, and the clone named `kotoba-shokunin`
so `trigger.name_directory` does not fire spuriously. Base = `6523ace…`, after = scratch commit `f3a2dc4…`.
Full transcript: `.ufo/waves/round-77/build/E09D2D3Hygiene.measurements.txt`.

| measurement | base | after |
|---|---|---|
| `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` (run from the clone root, the entry's own `recheck` form) | `rows 20 verified 20`, `province rows 20 matched 4`, 16 `FAIL`, exit 1 | `rows 20 verified 20`, `province rows 20 matched 4`, 16 `FAIL`, exit 1; `diff` of the FAIL sets **identical** |
| same for `…census-round74.md` | `rows 20 verified 20`, `province rows 20 matched 20`, exit 0 | identical, exit 0 |
| `check_r63_routed_repairs.py --root <clone> --rev <rev>` (append-only conjunct) | `PASS append-only prefix=True grew_by=252`, `r62 routed defects closed 5 of 5`, exit 0 | `PASS append-only prefix=True grew_by=256`, `5 of 5`, exit 0 |
| `verify_skill_checklist.py --json --repo <clone>` | `pass 10 / fail 1 / exit 1`; `governance.citation_resolves` evaluated 1308, FAIL on `LOG.md:2818` | `pass 10 / fail 1 / exit 1`; same single FAIL, evaluated **1310** (the two new `corpus/…` subjects resolve) |
| `verify_corpus_integrity.py --json --repo <clone>` | exit 1; DRIFT `tracked_files 146/144`, `unindexed 2/0`, `report_total 102/99`, `commit_total 44/43` | exit 1; results **and** observed JSON byte-identical |
| `verify_corpus_independent.py --json --repo <clone>` | exit 1 | exit 1; results **and** observed JSON byte-identical |
| `check_desc_craft.py --repo <clone> --rev <rev> --work <scratch>` (frozen C1 counter) | `description craft backed 0 of 6`, exit 1 | `description craft backed 0 of 6`, exit 1 (only the `measured-rev:` line differs) |
| `check_r75_routed_repairs.py --repo <clone> --rev <rev> --work <scratch>` (frozen C2 counter) | `r75 routed repairs closed 0 of 4`, exit 1 | `r75 routed repairs closed 0 of 4`, exit 1 (only `measured-rev:` differs) |
| `check_gate_registry.py --rev <rev>` | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0`, exit 1 | identical, exit 1 |
| patch application | `git apply --check` exit 0; applied diff = 4 + 15 lines | applied files byte-identical to `f3a2dc4` (`diff` empty ×2) |

Byte properties of the after-state (computed from `git show`):

```
LOG.md                                    base 563287 B / 2818 lines → after 564306 B / 2822 lines; base is a byte-prefix: True
corpus/…/sibling-overlap-census-round49.md base 43202 B / 466 lines → after 44600 B / 481 lines; base is a byte-prefix: True
after LOG.md sha256 81d71b5b4b96b8a3… · after census sha256 25dba8293b92910dc57160efd26958919fdf3894b8b4d67d6371a694b7780292
census line ranges after the append: :43 `## Classification rule`, :246 `## Round 50: …`, :416 `## Round 51 status …`
```

The task's explicit acceptance check — `check_sibling_census.py` still printing `rows 20 verified 20` after the
change — holds (table row 1). The gate's exit 1 is **pre-existing at the r77 base** and is not caused by, and not
repaired by, this seat's append; the pointer text states exactly that.

## 6. Findings at the r77 base outside this seat's write scope (surfaced, not fixed)

- **F1 — gate registry 60 of 62.** `python3 -B verifiers/check_gate_registry.py --rev 6523ace…` → exit 1;
  `verifiers/check_desc_craft.py` and `verifiers/check_r75_routed_repairs.py` report "no registry rows naming it: 0
  (need 1)". The r77 plan's no-harm battery includes this gate, so it is red at the base and will stay red unless the
  two frozen counters get registry rows (a `verifiers/` edit, not in this seat's item).
- **F2 — checklist citation.** `verify_skill_checklist.py --json` is `pass 10 / fail 1` at the base:
  `LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve from <lane root>`. The r76 report exists only in
  the fleet repo (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md`), while the lane's `.ufo/reports/`
  stops at round-45; the lane-relative citation needs the `../` form (as older LOG lines use) or the report needs to
  be reachable from the lane. Pre-existing at the r77 base; the r76 plan's base battery expected `pass 11`.

## 7. Risks

- R-A: patch ordering against a later LOG tail append (§4, measured). Apply before the round-77 entry or append the
  section by hand.
- R-B: the D3 status sentence is a dated measurement (it names base `6523ace…`); a later reviewer should read it as a
  snapshot, not a live claim — the live reading is the round-74 entry, as the pointer says.
- R-C: the new `## Round 74 correction` heading reads after `## Round 76` at the tail; nothing parses LOG sections in
  numeric order (checked: `section()` in the r75 counter, the r63 append-only conjunct, the checklist), but a human
  reading LOG top-down meets it late — that is the price of append-only and is stated in the heading itself.

## 8. No-harm / cleanliness

No lane file was edited; no git/jj write was issued in the lane (read-only `log`/`show`/`cat-file`/`merge-base`
only). No registry, `SKILL.md`, index, baseline or counter byte was touched. Scratch
`/fast/scratch/hyaku/kotoba-r77/E09D2D3Hygiene/` was removed after the evidence files were copied into
`.ufo/waves/round-77/build/`. No installs (no `pacman`, none needed).

VERDICT: D2 and D3 re-derived, verified against committed bytes and the closure ask; FormB chosen (LOG append-only, "appended correction" in the routed item) and D3 tail-appended with the census recheck still `rows 20 verified 20` (16 pre-existing FAILs, identical set); one unified patch applies cleanly at the r77 base and leaves every other gate's verdict unchanged — two pre-existing base defects surfaced (gate registry 60/62, checklist citation LOG.md:2818) and left untouched as out of scope.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E09D2D3Hygiene.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/E09D2D3Hygiene.measurements.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/E09D2D3Hygiene.md
