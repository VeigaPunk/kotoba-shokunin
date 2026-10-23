Result: HOLDS — C1's census-first 4/3 sizing rejects the recorded no-work and shortcut controls, but that discrimination establishes a sourced-location floor, not semantic depth by itself.

## Scope and evidence limits

Seat: KotobaR58.CriticC1Sizing. Axes: depth and calibration. Reviewed the sizing of C1 at content commit `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`, against freeze `3de87aad29e960c95ed35840442f424c48c29729`. This is a scoped critique, not a canonical judgment or admission.

All scores below are observations in the named existing receipts, not counter runs by me. I used local reads/searches and read-only, timeout-capped Git history/blob commands. No counter, test, client, judge, other runtime, source fetch, sandbox world, or installation was run. Only this report was written.

## 1. What the controls actually scored

Paths in this table are under `.ufo/waves/round-58/controls/`. F is live-found credit; K is grammar eligibility, not verified knowledge. Every listed control's frozen `--fetch` predicate exits 1.

| Control | Recorded live-fetch result | Evidence: command, output, exit |
|---|---|---|
| `CtlC1DoNothing`: base | F=0, K=0, G=0 | `CtlC1DoNothing.md:60-81`; command `timeout 900 python3 -B verifiers/check_command_files.py --rev f56f6e191762c27c1aa2af11a204db9e2ca4edec --fetch`; exit 1; `custom command files found on the live page 0 of 0; new ground 0` |
| `CtlC1DoNothing`: counters-only | F=0, K=0, G=0 | `CtlC1DoNothing.md:106-127`; command at :111, output :119, exit :114 |
| `CtlC1DoNothing`: exact heading/header, empty table | F=0, K=0, G=0 | `CtlC1DoNothing.md:152-173`; command at :157, output :165, exit :160 |
| `CtlC1Junk`: invented/misassigned locations and unrelated real quotes | W1 F=0, K=6, G=0; W2 F=0, K=7, G=0 | `CtlC1Junk.md:74-100,125-145`; commands at :84/:128; exits 1 at :100/:144 |
| `CtlC1Fabricated`: real locations, fabricated quotations | F=0, K=6, G=0 | `CtlC1Fabricated.md:71-90`; command at :74, output :82; exit 1 |
| `CtlC1OffTopic`: real skill/plugin/agent/settings/rule locations; second world uses a docs link | Both F=0, K=0, G=0 | `CtlC1OffTopic.md:149-169,189-226`; commands at :154/:194; exits 1 |
| `CtlC1SharedLabel`: 13 identity/sharing/entry/base-URL worlds | All exit 1; F never exceeds 1 and G never exceeds 1 | `CtlC1SharedLabel.md:44-64,188-221`; complete commands/output follow :188. The false Copilot CLI attribution is F=1, K=1, G=0; genuine narrow Cursor worlds reach F=1, G=1. |

Do not read the fabricated control's headline `BREAKS` as a C1 predicate pass. Its no-fetch run prints **backed** 6 of 6, not F=6, computes no G, and still exits 1 (`CtlC1Fabricated.md:18-25,92-110`). The mandatory live fetch rejects all six invented quotations.

For comparison, the delivered receipt is `.ufo/waves/round-58/C1-measure.txt:1-14`:

```text
python3 -B verifiers/check_command_files.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe --fetch
custom command files found on the live page 6 of 6; new ground 4
exit 0
```

That receipt and the controls identify the same instrument SHA-256 `aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c`. I did not independently re-hash or re-run it.

**Finding:** neither a table-shaped shell, seven plausible-looking rows, invented source support, nor the tested real off-topic inputs receives the claimed result. The two-client margin is not evidence that doing nothing passes.

## 2. Q45 ordering and arithmetic hold

`corpus/QUALITY.md:56` requires a no-content census before freezing a per-item target, a recorded census/command, and an explicit margin. The frozen plan records:

- `plans/round-58.md:52-64`: seven client census dispositions, six eligible, with W0 report/source pointers and fetch times 07:37–07:40Z.
- `:65-68`: F_max=6; G_max=4; the base-search command; two held forms, `.codex/prompts` and `.github/prompts`.
- Only then `:69-71`: T_F=4, margin 2; T_G=3, margin 1; conjunction F>=4 AND G>=3.

The margins are stated with the target declaration, not literally on an earlier line; the census precedes the declaration and both margins are frozen with it. That meets the sizing/order point being attacked.

Committed-byte inspection, not just present-day prose, supports the sequence:

```sh
timeout 60 git --no-optional-locks show 8db2070270147510e4729f04d657168c265229e4:plans/round-58.md
timeout 60 git --no-optional-locks show 3de87aad29e960c95ed35840442f424c48c29729:plans/round-58.md
```

Both commands completed successfully. The draft displays census `TBD` followed by targets `TBD`; the freeze displays the six/four census and four/three targets above. A read-only `git log --reverse --format='%H %cI %s'` over the base-to-content range, restricted to the plan, controls and affected content, returned this order:

```text
8db2070270147510e4729f04d657168c265229e4 2026-10-23T04:34:43-03:00  plan draft
3de87aad29e960c95ed35840442f424c48c29729 2026-10-23T04:51:33-03:00  freeze, census and targets
a39942c94027cd3875144284112422d1aa642260 2026-10-23T05:07:32-03:00  control receipts and erratum
46b4a7061c688cefd3e3ec9cbb655130ba1aafbe 2026-10-23T05:20:32-03:00  C1 content
```

Subjects above are abbreviated; hashes/timestamps are copied from output. The separately committed chronology review provides exact command/exit receipts at `.ufo/waves/round-58/build/ReviewPlanChronology.md:17-43`. The census itself is not proof of fully integrated backing; the content receipt supplies that separate observation.

## 3. Strongest sizing counterexample: an honest table need not pass

The conjunction matters more than the F margin in isolation. `verifiers/check_command_files.py:246-247,1073-1085,1933-1944` sets 4/3, requires fetch, and computes distinct new forms only from live-found rows.

[INFERENCE; arithmetic, not executed worlds]:

- Four correctly sourced rows consisting of the two held locations and two new locations yield F=4, G=2: **fail**.
- Three new locations plus one held location yield F=4, G=3: **pass**.
- All four new locations without either held location yield F=4, G=4: **pass**.
- Losing two new rows from the observed six-row result leaves F=4, G=2: **fail**, despite the nominal F margin of two.

Thus the floor requires four live-supported client locations, at least three of the four eligible unheld forms: 4/6 of eligible clients and 3/4 of eligible new forms. It permits omitting both held clients, or one held and one new client; it does not permit two arbitrary omissions. That is conservative sizing, not an automatic pass for any honest partial table.

The measured 6/6, G=4 reaches this fixed census's ceiling. It does not establish exhaustion of the domain or saturation of depth. The baseline F=0 also does not mean the corpus held zero command-file knowledge: the two held forms are explicitly excluded from G.

## 4. Remaining calibration limit and smallest safe correction

The strongest unresolved shortcut is not empty or false locations. It is **correct sourced locations with vacuous file-setting/action detail**. The existing junk control changes the locations and quotes too, so its failure does not test that shortcut. The prior static counterexample is at `.ufo/waves/round-58/build/CriticAxisFit.md:17-27`.

Direct code evidence: `verifiers/check_command_files.py:763-784` ignores the `What a file sets` cell and checks only the action's word count. The entry already admits that boundary at `corpus/knowledge/command-files-round58.md:65-68`.

[INFERENCE, not an observed successful control]: preserving the six valid location/source/quote/Gate inputs while replacing the file-setting cells with empty or generic text and actions with three meaningless words leaves F/G unchanged. No choice of a larger F target within the same census repairs that semantic blind spot. Conversely, this inference does not show that the delivered semantic cells are deficient.

**Smallest safe correction:** keep the frozen counter, target and declared axis unchanged. In claim/report wording, separate the measured location result from the independently reviewed technical distinctions and actions. Suggested bounded text:

> The pre-target census found six eligible client locations, four unheld at base; frozen thresholds were F>=4/G>=3, with margins 2/1. Recorded no-work and shortcut controls failed. The content receipt reports F=6/G=4. These counts establish sourced locations and new forms; file-setting semantics and author actions require the cited content review.

If only locator coverage survives that review, the canonical Rust judge must not substitute it for the declared depth move. If the promised technical detail is independently supported, the conservative threshold alone is no reason to reject it. No frozen-target change or round-admission decision is proposed.
