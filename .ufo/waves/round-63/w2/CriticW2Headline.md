# CriticW2Headline — a five-check score is not five routed obligations

role: UFO-FSD critic; leaf; advisory, not the canonical judge
item: CriticW2Headline — falsify `r62 routed defects closed 5 of 5`; trace every original §6 obligation
measured revision: `cbbee56e9a3589b0b46736ad36f1b77701def80e`

**Axes named:** calibration / consistency — denominator honesty, completeness of self-assessment, and provenance. No other axis is scored here.

## Finding and review verdict on the committed bytes

**The semantic headline is falsified; the five computed PASS results reproduce.** The committed counter has five arms, not one arm for each of the spot-check's five routed items. They comprise four content/linkage checks and one frozen-LOG-prefix-plus-growth guard. Its code does not read the H1 bound in Q57, require a correction of the false post-report-child assertion, inspect Cursor's rejection reason, or assess SHONEN ownership. Naming the no-harm tokens does not require the words saying their defects were fixed at tip. See `verifiers/check_r63_routed_repairs.py:80-178` and the original route `corpus/lessons/round-62-verifier-spotcheck.md:159-177`.

The executed counterexample is a **real scratch commit**, `4cb52f68d4221f1ac38411b74c23517a8cdf015d`, parented by the real r62 base. It changes only three paths: adds the genuine late report, adds the byte-identical committed counter, and appends six lines to LOG. Both historical receipts, the entry, Q57, the old lesson and SHONEN remain byte-identical to r62. **All five checks pass, exit 0, while §6.1's required H1 absorption and §6.2's child-claim correction are absent.** The append also never says the two no-harm failures were fixed. This requires neither a forged receipt nor a constant-output substitute instrument.

This does **not** establish that every omitted obligation is still open at the actual `cbbee56e` tip. Substantive repairs exist elsewhere: **Q57:68** learns the named H1-variant limitation (not an edit to the unchanged r62 entry), **LOG:2572** withdraws the false sweep claim, and **LOG:2573** names the interim no-harm failures **and** their repair. Cursor's rules-URL correction is in the **r63 Gate**, although the two-endpoint disposition and its URL-identity explanation remain incomplete. The crosswalk below distinguishes these committed repairs from missing explicit sub-items; the five-check score alone establishes neither.

These qualifications must remain visible:

1. `LOG.md:2572` correctly withdraws the claimed sweep but overreaches with “nothing else descends from `e53b6e5c`.” At the measured tip the actual chain includes `e53b6e5c → 35d44b4b → 8c4cefa8 → cbbee56e`. Scope that sentence to the missing sweep/report-time claim; do not substitute a false genealogy for a false child claim.
2. The original `corpus/lessons/round-62.md:19` still calls both Cursor `.md` URLs dead, with no local supersession pointer. `corpus/lessons/round-63.md:26-34` and `corpus/SOURCES.md:221-235` correct the rules URL, but do not explicitly absorb the plugins endpoint. Both endpoints' Accept-dependent results exist in the committed wave evidence (`ScoutS049.md:24-36`, `ExecSourceProbe.md:8-10`); S088 already mines the plugins URL and its 30,324 B body. The specifically planned r62 Gate repair has not landed in that file.
3. The later rules errata's “at the same URL” explanation is itself false: S049's source is `https://cursor.com/docs/rules.md` (`SOURCES.md:62`), whereas S108/S115 use `https://cursor.com/docs/rules` (`:120,127`). The hold is a documented re-open/alias decision and canonical fetch choice, not literal URL equality. Correct that phrase in the errata's appended interpretation, not the historical rows.
4. Q57 names M-a/M-b/M-e/M-f/M-j but does not explicitly spell out the lane's own `**not**` false negative from the adopted report:65-75. The general honest-fixture bound is learned there; the routed emphasis-specific sub-item is still explicit only in the seat report, not in the entry/Q57 wording. The smallest completion is the explicit entry-bound sentence below, not a claim that the regexes were repaired.

This is a fixable measurement-description/disposition defect. Keeping the frozen output as historical evidence is legitimate; treating it as complete routed closure or as an independent/general calibration rate is not an innocuous tradeoff. Admission and axis judgments remain with the canonical judge.

## Attacks run — commands and verbatim process output

All execution used a detached, revision-pinned `/tmp` clone. No lane production file, lane Git index/ref, jj state, or fleet file was mutated. Transport notices are not process output.

### Pin the evidence

```sh
git clone --shared --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba-r63-CriticW2Headline && git -C /tmp/kotoba-r63-CriticW2Headline checkout --detach cbbee56e9a3589b0b46736ad36f1b77701def80e
```

```text
Cloning into '/tmp/kotoba-r63-CriticW2Headline'...
done.
HEAD is now at cbbee56 round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
```

Exit 0. All following relative commands use cwd `/tmp/kotoba-r63-CriticW2Headline`.

### Re-run the declared counter, before and after, and its controls

```sh
python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
```

```text
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
```

Exit 1. This is the E1 predicate, including growth; the pre-E1 prefix-only definition is not substituted for it.

```sh
python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
```

```text
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
```

Exit 0.

```sh
python3 -B verifiers/check_r63_routed_repairs.py --self-test
```

```text
self-test: 0 failure(s) over 15 assertions
```

Exit 0. Passing these constructed controls does not refute the omitted-obligation attack.

### Execute the counterexample tree

I wrote the following new scratch script to `/tmp/kotoba-r63-CriticW2Headline-attack.py` and ran `python3 -B /tmp/kotoba-r63-CriticW2Headline-attack.py`. It writes objects and a separate index **only in `/tmp`**, does not check out its attack, and does not alter the pinned evidence files. Full construction source is retained here so the scratch pathname is not the only reproduction evidence.

```python
#!/usr/bin/env python3
"""Build a real counterexample commit only in the /tmp clone's object store."""
import os
from pathlib import Path
import subprocess
import sys

root = Path('/tmp/kotoba-r63-CriticW2Headline')
base = '35d44b4b4dcdda234b5dbff7af37e432fec55f05'
tip = 'cbbee56e9a3589b0b46736ad36f1b77701def80e'
late = '.ufo/waves/round-62/w2/FalsifyC2HonestH1.md'
verifier = 'verifiers/check_r63_routed_repairs.py'
entry = 'corpus/knowledge/erratum-absorption-round62.md'
receipt = '.ufo/waves/round-62/C2-successor-measure.txt'
noharm = '.ufo/waves/round-62/noharm-tip.txt'
env = dict(os.environ, GIT_INDEX_FILE='/tmp/kotoba-r63-CriticW2Headline-attack.index')

def git(*args, data=None):
    return subprocess.run(['git', '-C', str(root), *args], input=data,
                          capture_output=True, check=True, env=env).stdout

# The real r62 base keeps the original Q57/entry and uncorrected child-commit
# report disposition. Add only the real late report, the unmodified counter,
# and the tokens its five arms read. Historical receipts are untouched.
git('read-tree', base)
for path in (late, verifier):
    oid = git('rev-parse', f'{tip}:{path}').decode().strip()
    git('update-index', '--add', '--cacheinfo', f'100644,{oid},{path}')
entry_bytes = git('show', f'{base}:{entry}')
receipt_bytes = git('show', f'{base}:{receipt}')
receipt_rev = next(line.split(b'=', 1)[1].decode()
                   for line in receipt_bytes.splitlines()
                   if line.startswith(b'receipt_rev='))
log_extra = (
    '\n### Round-63 minimal token-only append (counterexample)\n\n'
    f'- receipt_rev={receipt_rev}\n'
    f'- {entry}: {len(entry_bytes.splitlines())} lines / {len(entry_bytes.split())} words\n'
    '- FAIL reg_gate 36 of 38; FAIL corpus-idx\n'
).encode()
log = git('show', f'{base}:LOG.md') + log_extra
log_oid = git('hash-object', '-w', '--stdin', data=log).decode().strip()
git('update-index', '--cacheinfo', f'100644,{log_oid},LOG.md')
tree = git('write-tree').decode().strip()
env.update(GIT_AUTHOR_NAME='CriticW2Headline scratch',
           GIT_AUTHOR_EMAIL='critic-scratch@example.invalid',
           GIT_COMMITTER_NAME='CriticW2Headline scratch',
           GIT_COMMITTER_EMAIL='critic-scratch@example.invalid',
           GIT_AUTHOR_DATE='2026-10-23T23:30:00+00:00',
           GIT_COMMITTER_DATE='2026-10-23T23:30:00+00:00')
attack = git('commit-tree', tree, '-p', base,
             data=b'Counterexample: five checks without complete routed closure\n').decode().strip()
print(f'attack_commit={attack}')
print(f'attack_tree={tree}')
print('changed paths versus real r62 base:')
print(git('diff-tree', '--no-commit-id', '--name-only', '-r', base, attack).decode(), end='')
print('verifier_equals_cbbee=' + str(git('rev-parse', f'{attack}:{verifier}') == git('rev-parse', f'{tip}:{verifier}')))
for path in (receipt, noharm, entry, 'corpus/QUALITY.md', 'corpus/lessons/round-62.md', 'SHONEN.md'):
    print(f'unchanged_from_r62[{path}]=' + str(git('show', f'{attack}:{path}') == git('show', f'{base}:{path}')))
print('appended LOG bytes:')
print(log_extra.decode(), end='')
print('committed semantic checks:')
q57 = next(line for line in git('show', f'{attack}:corpus/QUALITY.md').decode().splitlines()
           if line.startswith('| Q57 |'))
print('Q57_has_H1_bound=' + str('honest variants' in q57 or 'H1' in q57))
print('entry_has_H1_bound=' + str(b'H1' in entry_bytes or b'M-a/M-b' in entry_bytes))
print('LOG_has_child_commit_correction=' + str(b'Defect 2c' in log or b'No such sweep commit exists' in log))
print('LOG_has_fixed_at_tip_disposition=' + str(b'fixed' in log_extra.lower()))
print('counter invocation:')
command = [sys.executable, '-B', str(root / verifier), '--root', str(root), '--rev', attack]
print(' '.join(command))
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout, end='')
print(result.stderr, end='')
print(f'counter_exit={result.returncode}')
if result.returncode:
    raise SystemExit(result.returncode)
```

Verbatim output:

```text
attack_commit=4cb52f68d4221f1ac38411b74c23517a8cdf015d
attack_tree=0f52ad26612364e00a1915a42da1dca83b04c651
changed paths versus real r62 base:
.ufo/waves/round-62/w2/FalsifyC2HonestH1.md
LOG.md
verifiers/check_r63_routed_repairs.py
verifier_equals_cbbee=True
unchanged_from_r62[.ufo/waves/round-62/C2-successor-measure.txt]=True
unchanged_from_r62[.ufo/waves/round-62/noharm-tip.txt]=True
unchanged_from_r62[corpus/knowledge/erratum-absorption-round62.md]=True
unchanged_from_r62[corpus/QUALITY.md]=True
unchanged_from_r62[corpus/lessons/round-62.md]=True
unchanged_from_r62[SHONEN.md]=True
appended LOG bytes:

### Round-63 minimal token-only append (counterexample)

- receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a
- corpus/knowledge/erratum-absorption-round62.md: 64 lines / 1044 words
- FAIL reg_gate 36 of 38; FAIL corpus-idx
committed semantic checks:
Q57_has_H1_bound=False
entry_has_H1_bound=False
LOG_has_child_commit_correction=False
LOG_has_fixed_at_tip_disposition=False
counter invocation:
/usr/bin/python3 -B /tmp/kotoba-r63-CriticW2Headline/verifiers/check_r63_routed_repairs.py --root /tmp/kotoba-r63-CriticW2Headline --rev 4cb52f68d4221f1ac38411b74c23517a8cdf015d
PASS late-write-tracked   tracked at 4cb52f68d4221f1ac38411b74c23517a8cdf015d
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=6 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
counter_exit=0
```

Script exit 0. The four semantic booleans are transparent narrow substring observations, not a new semantic gate. The missing H1 fold additionally follows from byte equality with the frozen pre-repair Q57/entry; the complete appended LOG is shown, so its lack of a child correction or fixed-at-tip disposition is inspectable without trusting the booleans.

### Independently resolve the actual entry, tracking and history

```sh
wc -l -w corpus/knowledge/erratum-absorption-round62.md
```

```text
  64 1044 corpus/knowledge/erratum-absorption-round62.md
```

```sh
git ls-tree -r cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/w2/FalsifyC2HonestH1.md corpus/knowledge/erratum-absorption-round62.md corpus/QUALITY.md SHONEN.md
```

```text
100644 blob f48861bff4a44d9501b8519f54a53b2c850bd5c9	.ufo/waves/round-62/w2/FalsifyC2HonestH1.md
100644 blob 969834ef38eb9a650318dc314e931afbe2f5acc0	SHONEN.md
100644 blob 7a94bff852c0f56df6077e37ec645567d802bf61	corpus/QUALITY.md
100644 blob db0e08d70f16b0618f0496d2373b99f55ad3969f	corpus/knowledge/erratum-absorption-round62.md
```

```sh
git show --no-patch --format='%H %P %s' 35d44b4b4dcdda234b5dbff7af37e432fec55f05 cbbee56e9a3589b0b46736ad36f1b77701def80e
```

```text
35d44b4b4dcdda234b5dbff7af37e432fec55f05 e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02 round-62 verifier spot-check (integrator, hyaku): non-author admit/reject
cbbee56e9a3589b0b46736ad36f1b77701def80e 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8 round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
```

```sh
git show --no-patch --format='%H %P %s' 8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
```

```text
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8 35d44b4b4dcdda234b5dbff7af37e432fec55f05 round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
```

```sh
git log --format='%H %s' e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02..cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/w2/FalsifyC2Mutants.md
```

No output, exit 0.

```sh
git log -1 --format='%H %s' cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/w2/FalsifyC2Mutants.md
```

```text
d519047cb895d84e5a6518215a75d94f3b30d20c round-62: fourth sweep — FalsifyC2Mutants final wording (G-c coverage bound; split-evaluator dies on the landed CLI dependency arm)
```

```sh
git diff --numstat 35d44b4b4dcdda234b5dbff7af37e432fec55f05 cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-62/C2-successor-measure.txt .ufo/waves/round-62/noharm-tip.txt corpus/knowledge/erratum-absorption-round62.md corpus/lessons/round-62.md SHONEN.md
```

No output, exit 0. The historical receipts and these original files were not rewritten by wave 1.

The disposition pointers below were opened with the read tool in the pinned checkout, including the complete raw Q57 row; they are not inferred from report-seat attestations. Historical probe/gate outputs cited there were **read**, not re-executed by this seat.

## Smallest safe correction — exact report-bound wording

Keep the frozen command and its literal stdout as the declared measurement. Do not retroactively rename its historical receipt or silently expand its frozen predicate. Use this honest headline and interpretation in the round report:

```markdown
### C2 — r62 reconciliation checks passed 5 of 5; routed dispositions audited separately

At `cbbee56e9a3589b0b46736ad36f1b77701def80e`,
`python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e`
prints the frozen legacy label `r62 routed defects closed 5 of 5`, exit 0;
at the frozen r62 base `35d44b4b4dcdda234b5dbff7af37e432fec55f05` it prints
`0 of 5`, exit 1 under pre-data erratum E1.

The denominator is five reconciliation checks: four content/linkage checks
and one frozen-LOG-prefix-plus-growth guard. It is not the spot-check's five
routed obligations, five independently new repairs, or an accuracy estimate.
In particular, the counter does not test H1 finding absorption, the false
post-report-child claim, Cursor's source disposition, or SHONEN ownership;
its no-harm arm names tokens without establishing repaired-at-tip semantics.
Those obligations require the separate committed-byte crosswalk below.
CriticW2Headline's unchanged-instrument scratch tree passed all five checks
without the H1 fold or child-claim correction. This is bounded, in-sample
reconciliation prompted by known outside findings, not general calibration,
independent receipt authentication, or history-wide append-only enforcement.
No numeric calibration-axis increase follows from this five-check fraction.
```

### Full original §6 crosswalk — exact report-bound text

```markdown
#### Round-62 spot-check §6: routed item/sub-item → committed disposition

All pointers in this table are lane-relative and are read at
`cbbee56e9a3589b0b46736ad36f1b77701def80e`. The routing authority is
`corpus/lessons/round-62-verifier-spotcheck.md:159-177`.

| Routed item/sub-item | Committed disposition and evidence | Relation to the five-check count |
| --- | --- | --- |
| §6.1a — commit or revert the late write | Committed, not reverted: `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md`, blob `f48861bff4a44d9501b8519f54a53b2c850bd5c9`; LOG:2574 explicitly adopts it as r63 wave evidence, not evidence retroactively counted in r62. | `late-write-tracked` establishes a tracked nonempty blob, not absorption. |
| §6.1b — if committed, absorb H1 narrowness in entry/Q57 or repair with a receipt | **General bound learned, no regex fix:** `corpus/QUALITY.md:68`, Q57's appended bound, names H1, M-a/M-b/M-e/M-f/M-j and R-c/ancestry false negatives; it says `honest passed 2 of 2` is not an honest-acceptance rate and population claims need held-out honest variants. LOG:2574 points there. The adopted report:60-130 supplies the period, two-line-window, ancestry-comment and own-`**not**` specifics, but Q57 does not explicitly mention that last emphasis case. The original `corpus/knowledge/erratum-absorption-round62.md:1-64` is unchanged and has no H1 bound. Thus the named-variant bound is in Q57; explicit absorption of the own-`**not**` sub-item in entry/Q57 is not claimed complete. | Not counted; append the explicit entry bound below for the missing sub-item. |
| §6.2a — correct C2 receipt revision | `LOG.md:2570` gives the exact authoritative `receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`, re-recorded at `e424f2a4`; compare `.ufo/waves/round-62/C2-successor-measure.txt:2`. This appended correction supersedes stale r62 receipt citations; the old report and LOG record remain historical text. | `receipt-rev-named` establishes token linkage. |
| §6.2b — correct entry size | `LOG.md:2571`; the actual committed `corpus/knowledge/erratum-absorption-round62.md` is 64 lines / 1044 words (`wc -l -w` in the pinned checkout). 50 lines / 723 words describes the older `e6da78bb` version, not the r62 close. | `entry-size-named` recomputes this entry's current size and finds a LOG line naming it. |
| §6.2c — withdraw false post-report sweep-child assertion | `LOG.md:2572` says no such sweep exists. The last change to `.ufo/waves/round-62/w2/FalsifyC2Mutants.md` is `d519047cb895d84e5a6518215a75d94f3b30d20c`; the `e53b6e5c..cbbee56e` path history is empty. **Qualification:** the same correction's unqualified “nothing else descends” sentence is false at r63 and needs the scoped addendum below; absence of that sweep does not imply absence of later descendants. | Not counted. |
| §6.2 method — prefer appended corrections, not rewriting already committed records | `LOG.md:2568-2575` is the appended corrections block. The counter reports `prefix=True grew_by=9 line(s)` relative to `35d44b4b`. Original receipt blobs, the r62 entry and r62 lesson are unchanged. This establishes frozen-prefix preservation plus growth, not that every intervening parent→child transition was append-only. | `append-only` occupies one of the five slots; it is a guard, not another original routed defect. |
| §6.3a — rules URL's request-profile-dependent rejection | Rules reason corrected elsewhere in `corpus/lessons/round-63.md:26-34`, `LOG.md:2575`, and `corpus/SOURCES.md:221-235`: `Accept: text/markdown` yields 404/389 B, wildcard/default yields 200 markdown/17,252 B. **Planned local correction absent:** `corpus/lessons/round-62.md:19` retains the unqualified “dead URLs” sentence; append its local correction rather than claiming it landed. | Not counted; source freshness/disposition is separate. |
| §6.3a, plugins sub-item — same old rejection sentence's second endpoint | `.ufo/waves/round-63/w1/ScoutS049.md:32-36` and `ExecSourceProbe.md:9,95-170` record plugins 200/30,324 B under wildcard/default and 404/389 B under markdown Accept. `corpus/SOURCES.md:101` S088 already mines that exact `.md` URL at the same 30,324 B / `3bbf36f3…` digest. The r63 Gate and SOURCES errata discuss only the rules URL; the plugins correction has probe evidence but is not explicitly absorbed there. | Not counted; the proposed r62 Gate appendix covers both endpoints. |
| §6.3b — re-open minability or justify canonical `/docs/rules` | The rules `.md` URL is minable under wildcard/default. S108 explicitly re-opens S049 and S115 re-opens S108; `ScoutS049.md:38-42` explains why extensionless `/docs/rules` remains the canonical fetch spelling under the seat header. Historical S049 size/hash stay dated, not overwritten. **False explanatory sub-claim:** r63 lesson:34, LOG:2575 and SOURCES:234-235 call this “the same URL,” but S049 `:62` is `.md` and S108/S115 `:120,127` are extensionless. The duplicate decision can stand on the documented alias/re-open evidence, not URL identity. | Not counted; append the exact URL-identity correction below. |
| §6.4a — name interim `reg_gate` red and its revision/count | `LOG.md:2573` names `FAIL reg_gate`, `36 of 38`, revision `3e7aed9b`; original `.ufo/waves/round-62/noharm-tip.txt:1,12-15` identifies the two unregistered instruments. | `noharm-arms-named` checks the token and count, not final repair. |
| §6.4b — name interim `corpus-idx` red and affected lesson | `LOG.md:2573` names `FAIL corpus-idx` and the round-61 spot-check; original no-harm receipt:17 names `corpus/lessons/round-61-verifier-spotcheck.md`. | Part of the same `noharm-arms-named` arm, not a second counted check. |
| §6.4c — say both interim defects were fixed at tip, with evidence | LOG:2573 explicitly says both were fixed by `e6da78bb`/`e424f2a4`. The committed r62 re-check `.ufo/waves/round-62/w2/FalsifyGateRegress.md:13,26,39` records registry `39 of 39` and `corpus-idx` PASS at `e6da78bb`; `SKILL.md:488-490,493` contains the four r62 gate rows and `corpus/README.md:108` indexes the affected lesson. These repair facts are historical committed evidence, not gates re-run by this headline seat. | Fixed-at-tip wording and evidence are not enforced by the five-check arm. |
| §6.4 receipt bound — do not convert the historical battery into a complete pass | `.ufo/waves/round-62/noharm-tip.txt:23` still records `Battery exit code: 124`, and the historical receipt is unchanged. Naming later arm repairs does not establish an uninterrupted full-battery pass. | Not an additional PASS inferred from 5/5. |
| §6.5 box 1 — preserve `[~]` and a resolvable evidence pointer | `SHONEN.md:5-6`: `[~]`; `.ufo/round-46/scouts/B2.md` exists, and the moved decision-table pointer resolves at `corpus/knowledge/anatomy-and-compression.md:102-108`. The dated inventory is not promoted to a fresh outside verification. | Not counted; retained boundary, not an earned r63 repair. |
| §6.5 box 2 — preserve `[~]` and a resolvable task pointer | `SHONEN.md:7-8`: `[~]`; `corpus/knowledge/cold-run-round11.md` exists. SHONEN explicitly qualifies this as a lane-dispatched run; the entry:19-28 also discloses its historical reachability limitation. | Not counted; no non-author promotion inferred. |
| §6.5 box 3 — preserve `[~]` and outside-review limitation | `SHONEN.md:9-10`: `[~]`; `corpus/lessons/round-8-aggregator-box3-coldrun.md` exists and records the old outside run/defects; SHONEN says no fresh non-author rerun since. | Not counted; no new executable-independence claim. |
| §6.5 box 4 and ownership — preserve `[~]`, province pointers, and no author-written `[x]` | `SHONEN.md:11-12`: `[~]`; `PROVINCE.md:35-44` is the resolving Adjacent section and names its round-49 census and older connector evidence. All four SHONEN boxes remain `[~]`, no `[x]`; promotion stays with the operator/non-author gate, not this lane-dispatched review. | Not counted; unchanged ownership boundary. |
```

### Minimal appended disposition corrections — exact proposed text

For the existing LOG correction (append; do not edit LOG:2572):

```markdown
- **r63 addendum to Defect 2c (scope of the child-commit correction).** The
  preceding correction withdraws the r62 report's claimed post-report sweep
  of `.ufo/waves/round-62/w2/FalsifyC2Mutants.md`; it does not deny later lane
  history. At `cbbee56e`, the actual chain is `e53b6e5c → 35d44b4b →
  8c4cefa8 → cbbee56e`. The phrase “nothing else descends from `e53b6e5c`”
  is therefore withdrawn. The last change to that mutants report remains
  `d519047c`, and its `e53b6e5c..cbbee56e` path history is empty.
```

For the r62 lesson Gate (append a dated correction after the old rejection bullet; preserve its historical bytes):

```markdown
- **Appended r63 correction to the Cursor rejection above.** The blanket
  “dead URLs” statement is superseded: the committed r63 probes of both
  `https://cursor.com/docs/rules.md` and
  `https://cursor.com/docs/reference/plugins.md` returned HTTP 404/389 B
  under `Accept: text/markdown`, but HTTP 200 `text/markdown` under
  `Accept: */*` (17,252 B and 30,324 B respectively). See
  `.ufo/waves/round-63/w1/ScoutS049.md:24-42` and
  `corpus/lessons/round-63.md` § Gate, S049 errata. The rules `.md` route
  is minable under the wildcard profile; minting a distinct rules row remains
  rejected on the documented re-open/alias evidence: S108 re-opens S049 and
  S115 holds `/docs/rules` as the canonical fetch spelling. These are not
  literally identical URLs. S088 already mines the plugins `.md` URL at
  the same 30,324 B / `3bbf36f3…` digest seen in the r63 wildcard probe.
  This changes the rejection reasons, not the dated source receipts.
```

For the later r63 rules errata (append a correction to LOG, the r63 Gate and the SOURCES errata note; retain dated originals):

```markdown
- **r63 URL-identity correction.** “At the same URL” in the earlier S049
  errata is withdrawn. S049 names `https://cursor.com/docs/rules.md`;
  S108 and S115 name `https://cursor.com/docs/rules`. S108 explicitly
  re-opens S049, S115 re-opens S108, and the committed `ScoutS049.md:24-42`
  records the representation/alias evidence for retaining `/docs/rules`
  as the canonical fetch spelling. The no-new-distinct-row decision stands
  on that evidence, not literal URL equality. The plugins `.md` URL is
  separately held by S088; its current wildcard probe matches S088's
  30,324 B / `3bbf36f3…` receipt. Both endpoints' 404s depend on the
  `Accept: text/markdown` request profile, not dead-URL status.
```

For the r63 entry's Limits (an explicit bound, not a successor-repair claim):

```markdown
- **H1 honest-acceptance bound (r62 late report).** Besides the Q57
  variants M-a/M-b/M-e/M-f/M-j, the lane's actual r62 R-c wording uses
  `**not**` and fails the successor's denial regex, which requires
  whitespace immediately after `not`; the adopted
  `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md:65-75,123-130` records the
  emphasis and sentence-final-period failures. The regexes are not
  repaired here. One chosen H1 fixture passing does not establish
  acceptance of honest repair prose generally or an honest-acceptance rate.
```

No additional counter arms or changed historical predicate are necessary to make this report honest. If a stronger automated *semantic closure* claim is desired, it is a different predicate requiring separately frozen controls; this seat does not introduce it.

## Scope, tooling and handoff

Only this report was written in the lane. All counter execution, scratch Git index/object writes, and constructed commits stayed under `/tmp`; no lane commit/index/ref or jj operation, no fleet write, no service action, no judge/admission/runtime delegation, and no tool install/update occurred. Pacman was not used. The checks actually exercised are the C2 before/after CLI, its 15-assertion self-test, the unchanged-instrument scratch attack, and the read-only history/size commands above. No broader build, lint, no-harm battery, C1 check, or live source fetch was run by this seat.

L1 owns any integration and final-revision verification. Preserve the literal declared receipt, use the bounded headline, and carry this full sub-item crosswalk with its stated qualifications rather than equating five token/guard checks to five routed obligations.

Report: `.ufo/waves/round-63/w2/CriticW2Headline.md`
