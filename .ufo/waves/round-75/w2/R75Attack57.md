# R75Attack57 — attack on R75Facet57 (stale `8 of 8` figure on the `check_skill_evals.py` gate row)

Seat R75Attack57 (leaf, read-only). Target: `.ufo/waves/round-75/w1/R75Facet57.md` at lane HEAD
`65a5c7a663249e0522cc49e4a148424200d9ddfe`. All measurements below are mine, run against a throwaway
clone of the lane at that rev (`/fast/scratch/hyaku/kotoba-r75/R75Attack57/fixture`;
`git rev-parse --show-toplevel` = the fixture, asserted before use), so every verdict is anchored to
committed bytes. Scratch removed on exit. No lane file edited, no commit, no live fetch, no installs.

## 1. Verdict

**The central claim survives, reproduced in full; two minor evidence errors in the report do not
overturn it.** The `## Gate registry` row at committed `SKILL.md:503` states
`skill eval facts backed 8 of 8` at the measured rev; `check_skill_evals.py` prints
`skill eval facts backed 1 of 8`, exit 1, at HEAD and at every rev since `bf98d28`. The two pointer
surfaces (`corpus/knowledge/skill-eval-artefacts-round70.md:8`, `corpus/README.md:133`) still name v1.
The finding is in-scope under Q46/Q04 (both quoted accurately), is not a duplicate of any sibling's
central claim, and its proposed controls are non-vacuous (the red arm is real and printable today).

## 2. Reproduction (my runs, committed bytes, verbatim)

```
$ git clone <lane> fixture && git -C fixture rev-parse HEAD
65a5c7a663249e0522cc49e4a148424200d9ddfe
$ python3 -B verifiers/check_skill_evals.py --repo <fixture> --rev HEAD
measured-rev: 65a5c7a663249e0522cc49e4a148424200d9ddfe
skill eval facts backed 1 of 8
  F1..F6: S212 has no pinned snapshot
  F7: S213 has no pinned snapshot        exit=1        (single backed fact = F8/S211, as claimed)
$ … --rev bf98d28 -> backed 1 of 8, exit 1
$ … --rev 4dba3bc -> backed 8 of 8, exit 0
$ … --rev 8edeb49 -> backed 8 of 8, exit 0
$ … --rev 7d51253f… -> backed 0 of 8, "entry corpus/knowledge/skill-eval-artefacts-round70.md absent", exit 1
$ python3 -B verifiers/check_skill_evals.py --self-test
self-test: 0 failure(s) over 13 assertions        exit=0
$ python3 -B verifiers/check_skill_evals_v2.py --repo <fixture> --rev HEAD   -> verified 10 of 10, exit 0
$ … --rev bf98d28  -> 10 of 10, exit 0
$ … --rev 4dba3bc  -> verified 1 of 10, exit 1 ("SKILL.md: 0 rendered lines name the entry + S211/S212/S213")
$ python3 -B verifiers/check_instruction_authority.py --repo <fixture> --rev HEAD -> grounded 1 of 1, exit 0
$ python3 -B verifiers/check_skill_precedence.py      --repo <fixture> --rev HEAD -> backed 5 of 5, exit 0
$ python3 -B verifiers/check_province_core.py         --repo <fixture> --rev HEAD -> rows 2 of 2, exit 0
```

Committed-byte anchors re-opened directly: `git show 65a5c7a:SKILL.md:503` ends
"…`skill eval facts backed 8 of 8` at the measured rev and `0 of 8` at the pinned base…", kind `gate`;
`grep -c "at the measured rev"` on committed SKILL.md = 4 (lines 478/499/501/503);
`git show 65a5c7a:corpus/knowledge/skill-eval-artefacts-round70.md` :5-6 are the S212/S213 superseding
rows and :8 is `recheck: 90d — python3 -B verifiers/check_skill_evals.py --rev <rev> --fetch …`;
`git show 65a5c7a:corpus/README.md:133` is the round-70 index row counted by v1. `git rev-list --count
bf98d28..HEAD` = 36 and `git log --oneline bf98d28..HEAD -- <entry> <v1>` is empty: the red level holds
across the range by construction, exactly as the facet argued. The facet's §2/§5 tables reproduce
cell-for-cell; I found no counterevidence in any run.

## 3. Attack angles tried, all dead ends

1. **`--fetch` rescue.** The registry row's as-written command is `--rev <rev> --fetch`; the facet
   measured without it. Dead end: `main()` exits `0 if n == TOTAL else 1` where n is the
   pinned-snapshot count, and `live_fetch` only prints `live quotes found k of n`
   ("network is a second evidence, never the verdict", `check_skill_evals.py:190-212, 330-353`). The
   as-written command is red at HEAD with or without network. I did not run `--fetch` (no network
   needed; documented here).
2. **Row-prose reading.** Could `8 of 8` be historical? The three sibling figure rows
   (`:478/:499/:501`) all print their claimed figures at HEAD, so the column's convention is a live
   reading; `8 of 8` was true only at `8edeb49`/`4dba3bc` and carries no rev qualifier. The facet's
   Q46 reading is verbatim correct (`corpus/QUALITY.md` Q46: "the `gate` kind alone reads as a live
   claim gate"), and Q04 is verbatim correct ("Every `recheck:`/source command resolves and runs
   today").
3. **Registry gate or tip battery catch it.** Dead end: `check_gate_registry.py:46` states "The
   counter does not run verifier scripts or prove their actual exit statuses" and parses the verdict
   cell only for `<code>=<class>` pairs, so a stale figure is invisible; `grep -c check_skill_evals
   verifiers/check_tip_battery.py` = 0. The facet's blindness claim holds.
4. **Duplicate check.** Facet57 is the only w1 report whose *central* claim is this defect. Facet51
   (teaches-cell conjunct) treats v1-red as an unrelated premise; Facet52 (page-uniqueness gap +
   v2 docstring prose) records the `:503` byte fact as "Secondary risk, not judged here"; Facet02
   (equality-case advice) flags the stale `recheck:` as "Adjacent, outside this facet". Corroborating
   premises, no duplicated claim.
5. **Repair-constraint soundness.** The facet's §8.2 (keep `kind = gate`) is right: a `probe` relabel
   is rejected when the source has an active `--self-test` handler (`check_gate_registry.py` docstring;
   v1's `main()` registers `--self-test`). §8.5's Q73 sweep re-verified: byte-identity conjuncts exist
   only on `PROVINCE.md` sections (`check_province_core.py:24,45,48,108`) and six scripts +
   spotcheck lessons (`check_tip_battery.py:50,54,122,328`); nothing pins SKILL.md byte-identical, so
   the proposed in-cell annotation reddens nothing.

## 4. Defects found in R75Facet57 itself (minor; do not overturn)

1. **A stated grep result is false.** §4 claims `grep -rn "check_skill_evals"
   corpus/lessons/round-7[1-4]*.md` → no hits. Reproduced literally, it prints one hit:
   `corpus/lessons/round-71-verifier-spotcheck.md:17` (`…check_r69_routed_repairs_v2.py`,
   `check_skill_evals_v2.py`,…) — `check_skill_evals_v2.py` contains the pattern as a substring. The
   substantive conclusion survives (that line is the closure's did-not-execute disclaimer naming the
   *successors*; no round-71..74 record discloses v1's red-at-HEAD or re-points the row), but the
   evidence line as written is wrong.
2. **Small anchor noise.** v1's "has no pinned snapshot" finding is at `check_skill_evals.py:158`
   (facet: :157); SNAPSHOTS dict spans :48-59 (facet: :46-57); the registry-gate disclaimer is at :46
   (facet: :45-47); `bf98d28` is 2026-10-25 11:13:**23** -0300 (facet: 11:13:29). The committed
   README also carries a second v2 mention the facet's "three surfaces" enumeration omits
   (`README.md:136`, the round-70 spotcheck index row naming `check_skill_evals_v2.py`) — immaterial,
   it is not a live pointer to v1.

## 5. World-state caveat for the integrator

The lane working tree is dirty with in-flight round-75 integration (`M LOG.md SCORECARD.md SKILL.md
corpus/README.md corpus/knowledge/skill-eval-artefacts-round70.md`; untracked
`plans/round-75*.md`, `corpus/lessons/round-75.md`, `.ufo/waves/round-75/`). The single SKILL.md hunk
rewords the `:192` equality-case paragraph; the entry gains a Facet02-citing clarification. **None of
the in-flight edits touch `:503`'s figure, the entry's `:8` recheck line, or `README.md:133`** — the
defect stands in both committed and working-tree bytes as measured. My verdicts are committed-byte
anchored and unaffected either way.

## 6. Control non-vacuity (facet §7)

The proposed counter's red arm is real and printable today (`1 of 4` over the four figure rows, with
`:503` the only red — measured in §2); the green arm is reachable by the annotation/re-point (the
three sibling rows already demonstrate the green form); the base arm (`0 of 8`, entry absent) is
correctly flagged by the facet itself as a weak do-nothing world that must not be sold as
discrimination. The facet's one-liner falsifier (`check_skill_evals.py --rev 65a5c7a | grep backed`
must print `8 of 8`) is red exactly as stated. Calibration in §6 of the facet is honest: it refuses a
depth/freshness inflation while v2 carries the substance green (`10 of 10`).

Report trailer: `Facet 57 attack; evidence committed bytes at the cited paths/lines at 65a5c7a663249e0522cc49e4a148424200d9ddfe plus a scratch clone at the same rev (removed on exit); runs without `--fetch` justified in §3.1; no live fetch, no installs, no lane edits, no commits.`
