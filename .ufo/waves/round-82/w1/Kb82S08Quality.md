# Kb82S08Quality — hermetic self-test quality-bar audit

## Behavior and decision

Axes: freshness; operability. No axis after-value or score is measured here.

**Recommend one append-only criterion extending Q65, not a rewrite.** The historical mistake is already recognized by Q65, but the prevention mechanism requested this round is absent: fixture self-tests must not depend on the evolving live tree. Re-running a coupled arm and refreshing its expected live verdict is not isolation.

| Existing row | What it actually requires | Does it prohibit fixture live reads? |
|---|---|---|
| Q09, QUALITY.md:20 | Re-derive and re-pin after substrate rebuild; otherwise disclose freshness debt. | No; different substrate mechanism. |
| Q19, QUALITY.md:30 | Re-measure carried/planned before-values at round start with command and commit. | No; premise provenance, not fixture input ownership. |
| Q65, QUALITY.md:81 | Base no-harm battery, budget arithmetic, and re-run a self-test arm pinning a live verdict whenever its record changes. | No; expressly accommodates live-verdict arms and requires re-running them. Captures detection, not hermetic prevention. |

The complete opened QUALITY.md through Q75 contains no fixture/live-tree isolation requirement. Q48 covers public-main exercising, Q63 covers honest live-world placement for a lane gate, and Q72 covers post-state no-harm; none makes a fixture self-test hermetic. Q63 must not be misused to prohibit isolated fixtures: public live gates and fixture self-tests are different execution modes.

## Real red-before witness — inherited, not rerun

Opened receipt: `.ufo/waves/round-82/receipts/before-checklist-selftest.txt`, SHA256 `7bd01499ff95a5929af92677f47fb6d1ec3f31b818195330b635d9336e0c3072`.

Its exact contents:

```text
# measured branch master=47dbe8781657de563ff867caca6244d28e3db504
# command: python3 -B verifiers/verify_skill_checklist.py --self-test
self-test FAIL: governance: live round-65 corrections land, errata-excused: got ('FAIL', 1363, "SCORECARD.md:480: '.ufo/wapes' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; SCORECARD.md:482: 'corpus/lessons/round-80-verifier-spotcheck.md:30,37' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; SCORECARD.md:484: '.ufo/reports/round-81/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; SCORECARD.md:484: '.ufo/reports/round-81/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused")
1 failure(s) over 1863 assertions

exit=1
```

This is previously captured execution evidence, not this seat's execution. The receipt names its measured base; it does not establish that the receipt itself existed at that base.

## Mechanism and lesson provenance

Base `verifiers/verify_skill_checklist.py:2463-2514` already contains isolated correction fixtures, including valid registered correction, missing registration, restored stale token, and unrelated dead subject. Lines 2521-2527 then derive `live_repo = Path(__file__).resolve().parent.parent`, call the live governance checker and require PASS plus two absence/four correction counts. Lines 2531 onward also use `live_repo` for load-bearing erratum checks. Isolating only the first call would leave live coupling in the neighboring arm.

Round-72 lesson M125, lines 77-81, says this same arm went stale when an erratum retired its expected red. Its fix asserted the new live state and added guard-removal coverage. Q65 preserves that re-run obligation but not a ban on mutable live inputs. Therefore the new criterion is grounded in both a pre-existing lesson and a directly observed recurrence, not a speculative style preference.

Candidate artifact supplies an append-only lesson class and provisional Q76 row. L1 owns identifier allocation and admission. Existing criteria stay unchanged. No claim that a new round-82 lesson row is already present.

## Gates and integration acceptance

No tests, production gates, production after-scoring, binaries or other runtimes were invoked. No 6/6 tip-battery claim. No green-after or completed repair claimed.

For L1's authorized C2 verification: preserve N >= 1863; demonstrate valid correction green; missing correction, restored stale target and unrelated dead fixture subject red; prove unrelated live governance edits do not alter fixture results; disable the replacement guard and show the corresponding assertion fails; retain public live rejection of genuinely dead citations. These are requirements, not exercised results in this report.

C1 remains unchanged: current-host re-derivation/re-pin targets 3/3 pins, 7/7 surfaces, 3/3 removal ledger. This seat supplies no host extraction or C1 execution evidence.

## Commands, outcomes, and byte binding

Read tools opened operator RULES.md, godspeed skill, round-82 plan, QUALITY.md, the before receipt, relevant verifier sections, and round-72 M125. Targeted searches located the three criteria and historical live-arm lesson. Initial broad criterion search included .jj metadata; only explicit corpus/verifier/receipt reads underpin findings.

Exact shell commands executed (read-only):

```text
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/receipts/before-checklist-selftest.txt /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/QUALITY.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-72.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-82.md

git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse 47dbe8781657de563ff867caca6244d28e3db504:corpus/QUALITY.md 47dbe8781657de563ff867caca6244d28e3db504:verifiers/verify_skill_checklist.py 47dbe8781657de563ff867caca6244d28e3db504:corpus/lessons/round-72.md

git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin hash-object /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/QUALITY.md /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/lessons/round-72.md
```

All returned normally; tool output did not supply numeric exit statuses, so none is invented. Both git commands printed the same ordered object identities:

```text
f60ba1032d0209dccd42088df1c169e23c37a7dd
6aab16849bd6d71ded8f3bcb3f95668f14f6a78f
66fa75468ba90d6029d7f3db2acc0f6a03a5ef39
```

This binds the three opened source files to the named base without checkout/index mutation.

SHA256 results, in command order:

```text
7bd01499ff95a5929af92677f47fb6d1ec3f31b818195330b635d9336e0c3072 before-checklist-selftest.txt
53d28b6699383592976fe02d34b18977685b48bc9d8629fd7fdb404ac723788e corpus/QUALITY.md
b7d7b0fca8be17cfa18e75fe4d130a0d429e34f5f4e1a30fdc5fb22a70539615 verifiers/verify_skill_checklist.py
f36644f98410f44ab432b84b083e0df594c664125be2c8dadf8e418845d662ee corpus/lessons/round-72.md
d00710618e510dac17914b4a215034f271533d3dadb12fa719640c4098106f86 plans/round-82.md
```

## Touched surfaces, exclusions, conflicts

Only this report and the unique build criterion candidate were written. No production code, QUALITY, lesson, source corpus, plan, judge, index, jj state or peer output changed. No clone, scratch artifacts, installs, heavy work, cleanup, commits, push, publication or deployment. Disk guard was not needed because no heavy work ran. No tools installed or updated.

No observed peer/judgment conflict. Scope distinction for canonical judge: Q65 already captures the historical reference-drift mistake, but does not contain the newly requested isolation mechanism. The proposed row adds that mechanism; it does not claim the mistake was previously wholly uncaptured.

VERDICT: Propose append-only hermetic fixture criterion extending Q65; real red-before inherited from named base receipt; repair and green-after unmeasured.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82S08Quality.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82S08Quality-append.md
