# RowTameshiR50: falsify attack on the tameshi adjacency ruling

**Verdict: HOLDS-BOUNDED.** Applies to tameshi's `adjacent` class at kotoba `PROVINCE.md:55` and to the round-50 ruling at `corpus/knowledge/sibling-overlap-census-round49.md:277-281`, judged at kotoba `956ee1676e4c18480bce8ac3993541462be76e11` and tameshi pin `3b20f073c7305a582562cd323982991464c324f3`. The class `adjacent` holds on the bytes. The row's clause "kotoba owns the SKILL-checklist instrument" FAILS its cited basis. The ruling's firing step and its basis label need repair.

Scope: the adjacency row for tameshi only. C1, C2, D1 to D6, S024 to S029 and Q26 belong to other seats; I touch them only where they bear on this row.

## 1. Are the quotes verbatim at the cited lines?

- "every lane's gate remains its own": tameshi `PROVINCE.md:14`. Verbatim (check T1).
- "Never edits a sibling's gate code": `PROVINCE.md:16-17`, split by a line break. Verbatim (T2).
- Core names "kagi `corpus/surface-census.sh` and `corpus/checklist-run.sh`": `PROVINCE.md:31-32`. Verbatim (T5).
- Ledger "kotoba `verifiers/*` — file existence is O, their gate-ness is U until a survey admits them": `corpus/knowledge/fleet-kill-rate-ledger.md:127-128`. Verbatim (T7). The ledger has no ownership word for kotoba (see F1).
- Ruling's "reads kagi's SKILL.md checklist": accurate but incomplete. `checklist-run.sh:4` calls it the "Credential-hygiene checklist", and the default read is `SKILL="$ROOT/SKILL.md"` at line 68. kagi `SKILL.md:425` holds the heading (G1, G2, D).
- Row's "kotoba owns the SKILL-checklist instrument": NOT in any tameshi file outside `.ufo/` (grep B), and NOT in kotoba base `a5adc146` (check A). It first appears at `f3046466:55`, which is this row (K5).
- Row's path "tameshi corpus `fleet-kill-rate-ledger.md:125-128`": no such file at the pin. The file is `corpus/knowledge/fleet-kill-rate-ledger.md` (path check).

## 2. Does the ruling's reasoning hold on the bytes?

a. **"The arm fires literally."** Holds only under the broad text. The classification rule (census `:45-46`) says "or the instruments over them". The precedence section (census `:253-255`) narrows a claim to craft and excludes "a credential checklist item, or the kill rate of the owner's gate". `checklist-run.sh` runs kagi's credential checklist, and tameshi's only measurement of it is the kill rate of the gate's selftest (`mutation-case-kagi-checklist.md:47-52`; U1 at `:347-349`: the live mode "was never run"). Under the narrow text there is no claim, so the arm does not fire. The ruling cites neither exclusion. **FAILS as stated.**
b. **"That instrument is kagi's."** Holds. The sha256 of `checklist-run.sh` at kagi `899c50b` starts `7e5ec98b9e1d0afa`, matching the ledger pin. Ownership alone does not place a Core element, though; the exclusion does.
c. **"Not an element of kotoba's § Core."** Holds on the named list. Kotoba `PROVINCE.md:14` names eight verifiers, and `checklist-run.sh` is not one of them. The bullet's generic words "Executable instruments over those surfaces" are not addressed by the ruling.
d. **"Tameshi measures it read-only."** Holds. `tools/mutate-and-run.sh:36-37` and `:63` say every mutant is a fresh copy and the target is only read (sha before and after). `:119` says the fleet trees are never written.
e. **"Tameshi's own split assigns the element."** Holds, but the cited range is the weakest. `PROVINCE.md:18` ("Credential material (→ kagi)") lies outside the cited 14-17 (T4 false, T4b true). `PROVINCE.md:44-45` repeats it ("credential material (kagi)"). Those are the specific assignments.
f. **"Basis sibling."** Contested. The fact seat (`RuleTameshi.md` §2) says the split is "on kotoba's side only". The census says the round-50 description edit "adds kotoba's side for ... tameshi" (census `:261-262`), yet the basis list still reads "tameshi sibling" (`:264`). Kotoba `SKILL.md:13-14` now says "tameshi owns the fixture and mutation method" (K1), and the ruling does not cite it.

## 3. Would claim-always-wins change the row?

- **Yes**, under the broad text the ruling itself uses. Current rule: the claim exists but the sibling's split assigns it to kagi, so the row is `adjacent`. Claim-always-wins: the row becomes `contested`. Counts go from 9 adjacent / 11 none / 0 contested to 8 / 11 / 1 (the critic seat's table also moves kama: 7 / 2, `CriticPrecedence.md:33`). Kotoba `PROVINCE.md:17` ("names the 9 lanes classed adjacent") would become false.
- **No**, under the narrow text: no claim exists, so the precedence is inert and the row stays `adjacent` under either precedence, provided a split exists (it does, §2e and §2f).
- **The guard cannot tell these apart.** Mutant M2 flips both census and PROVINCE to `contested` and exits 0. Mutant M1 flips only PROVINCE and exits 1. The guard checks consistency between the two files, not the ruling.

## 4. Findings

- **F1 HIGH (boundary text, Q26 spirit).** The clause "kotoba owns the SKILL-checklist instrument" has three cited sources, and none states it: the ledger lines say kotoba verifiers are "sightings" that are "not queued" with unknown gate-ness; the "kotoba base" line is the row itself; the phrase is absent from `a5adc146`. The clause may be true of kotoba's own `verifiers/verify_skill_checklist.py`, but nothing cited shows it. The census guard does not read boundary text: mutant M3 deletes the clause and exits 0 (the PROVINCE intro says so).
- **F2 MEDIUM (firing step).** The ruling says the arm "fires literally", which conflicts with the census's own narrow definition (`:253-255`). The exclusion "a credential checklist item, or the kill rate of the owner's gate" is the actual reason and is not cited.
- **F3 MEDIUM (basis label and range).** "Basis sibling" cites `PROVINCE.md:14-17`, which omits line 18, the most specific assignment. The kotoba-side split (`SKILL.md:13-14`) is not cited. The label should read "both", or the seat disagreement should be recorded.
- **F4 MEDIUM (two definitions of contested).** Classification rule `:45-46` is unamended ("or the instruments over them"), while the precedence section `:253-260` narrows the term. The ruling's "fires" uses one and its "not a claim" uses the other. Under the current exit rule, any generic sibling line (here `PROVINCE.md:44-45`, "every sibling gate's code ... (owner lane)") clears a gate claim, so for tameshi the contested arm cannot bind. That is a policy question for the integrator; it does not change this row's class.
- **F5 LOW (ambiguous referent).** "The SKILL-checklist instrument" fits kagi's `checklist-run.sh` literally, since it reads a SKILL.md checklist section. The row never names kotoba's file. Naming `verifiers/verify_skill_checklist.py` (kotoba `PROVINCE.md:14`) removes the collision that the residual in `RuleTameshi.md:113-117` describes.
- **F6 LOW (paraphrase).** "Reads kagi's SKILL.md checklist" drops "credential-hygiene", the word that makes the exclusion apply.
- **F7 LOW (path).** The row's ledger path is wrong (see §1).
- **F8 LOW (dangling pointer).** `corpus/lessons/round-50.md:123` says "see `## D3 precedence ruling` below". No such heading exists; the ruling is at census `:246-295`.
- **F9 INFO (non-independent basis).** Kotoba's description tameshi clause is this round's own output (C1 counts it), so it cannot corroborate the row independently of the census.

## 5. Suggested repairs (not applied; the lane is read-only for me)

1. Row 55 boundary: replace the ownership clause with "kotoba owns `verifiers/verify_skill_checklist.py` (PROVINCE.md:14)"; cite sibling `PROVINCE.md:18, :44-45`, kotoba `SKILL.md:13-14`, and ledger `corpus/knowledge/fleet-kill-rate-ledger.md:127-128` (kotoba verifiers not queued). Basis: both. Drop the self-citation.
2. Census `:45-46`: narrow to the `:253-255` definition. Rewrite the tameshi ruling to say "no claim: a credential checklist item and the owner's gate kill rate (`:254-255`)", and drop "fires literally".
3. Lesson `round-50.md:123`: point to census `:246`.

## 6. Residual risk and verification gaps

- I read only the pinned bytes. Tameshi HEAD now differs from the seat's quoted tip (`2227d83`); this does not change the pin claims.
- I did not check kotoba's "four fidelity checklists" location; the statement that they are craft checklists is [INFERENCE].
- I did not run C1, C2, D1 to D6 or S024 to S029; those belong to other seats.
- The claim that the SCORECARD's "0 contested" wording would change is from the critic seat and is unverified by me.

## 7. Evidence (commands and exit codes)

- Quote checks T1 to T10, NC1, K1 to K5, G1 to G3, C1 to C3 (python `git show` plus exact substring test, scratch cell): all `ok=True`. NC1 (falsified quote) found=False, so the check can fail. T4 (cited range 14-17) found=False; T4b (line 18) found=True.
- `git -C tameshi-shokunin grep -n -i kotoba 3b20f07… -- PROVINCE.md SKILL.md AGENTS.md corpus README.md` → exit 0; hits only at ledger `:127`, `:233` and `fleet-suite-census.md:625`.
- `git -C tameshi-shokunin grep -n -i -E "kotoba owns|SKILL-checklist" 3b20f07… -- corpus/knowledge/fleet-kill-rate-ledger.md` → exit 1.
- `git -C kotoba-shokunin grep -n -i "SKILL-checklist" a5adc146 -- PROVINCE.md SKILL.md corpus` → exit 1.
- `git -C kagi-shokunin grep -n -E "^## .*[Cc]redential-hygiene checklist" 899c50b… -- SKILL.md` → exit 0 (`SKILL.md:425`).
- `git -C kotoba-shokunin grep -n -E "^## .*D3 precedence ruling" 956ee… -- corpus/lessons/round-50.md` → exit 1; the pointer at `:123` → exit 0.
- Census guard, scratch clone at 956ee (`/fast/scratch/hyaku/kotoba-r50/falsify/RowTameshiR50/lane`): `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → "rows 20 verified 20", "province rows 20 matched 20", exit 0. With `--skill SKILL.md` → "skill description names 9 of 9 non-none lanes", "skill description length 1008 of 1024", exit 0.
- Mutants in `/fast/scratch/hyaku/kotoba-r50/falsify/RowTameshiR50/mut-M1…M5`: M1 PROVINCE row to contested: exit 1 ("province rows 20 matched 19"). M2 census and PROVINCE to contested: exit 0. M3 delete the ownership clause: exit 0. M4 tameshi commit changed: exit 1. M5 census only to contested: exit 1.
- Ledger line count at pin: 437 (`wc -l`).

## Tooling

No installs or upgrades. Used git, python3 and bash only. Writes: this report, its directory, and the scratch clone and mutants. The lane checkout is otherwise untouched.

Check labels: T1 to T10, K1 to K5, G1 to G3, C1 to C3 and NC1 are the scratch quote checks (python cell: `git show` plus exact substring test; NC1 is the negative control). A (SKILL-checklist at a5adc146), B (kotoba mentions at the tameshi pin), grep C (ledger "kotoba owns" or "SKILL-checklist"), D (kagi heading), E and F (lesson heading and pointer) are the bash greps in §7. M1 to M5 are the mutants.
