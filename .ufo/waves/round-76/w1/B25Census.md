# B25Census — sources census at base (round 76, wave 1)

Seat: `B25Census` (executor, leaf). Scope: measure the corpus registry census at
the round-76 base, land the receipt, report only. No claim data was written.

**Verdict: census clean at base — `exit 0`, `kotoba ok`, 151 rows, 20 W04
duplicate-URL warnings, 0 E-code findings. One land-ordering constraint measured
for C1: the S213 `used-by` cell and the new entry file must land in the same
commit or the census flips to `E11` / exit 1.**

## What was run

All commands run read-only against the lane; the only write is the named receipt
and this report. No git/jj mutation was performed anywhere.

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git log --oneline -3
4de12b6 round-76: wave w1 spec + dispatch (64 seats, v2 band, 34% attack share)
abd8e5c round-76: plan — C1 depth description-craft (sourced), C2 consistency r75 routed repairs; base battery
b7f13f4 round-75 verifier spot-check (integrator, hyaku): non-author admit/reject
```

Base revision (the plan's frozen base): `b7f13f4b39cbd43076a85568adca763a6f674e7a`.

### 1. The specified command

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S207 duplicate url opencode.ai/docs/skills across scopes
kotoba	W04	S208 duplicate url learn.microsoft.com/en-us/agent-framework/agents/skills across scopes
kotoba	W04	S212 duplicate url agentskills.io/skill-creation/evaluating-skills.md across scopes
kotoba	W04	S213 duplicate url agentskills.io/skill-creation/optimizing-descriptions.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

### 2. Row count (the plan's exact grep)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
151
```

### 3. W04 warning count

```
$ grep -c 'W04' <validate stdout>
20
$ grep -oE 'W[0-9]+' <validate stdout> | sort -u
W04
$ grep -cE '	E[0-9]+	' <validate stdout>
0
```

W04 id set: `S018 S019 S021 S054 S055 S056 S065 S086 S103 S104 S106 S110 S111
S114 S115 S118 S207 S208 S212 S213` (20 ids, no repeats).

## Base identity — the census's only input is byte-stable base→tip

The census reads `corpus/SOURCES.md` (plus the on-disk `used-by` paths). The
plan's touch list edits only the S213 `used-by` cell, so at base the registry is
unchanged between the base revision, the tip HEAD and the working tree:

```
$ git show b7f13f4b39cbd43076a85568adca763a6f674e7a:corpus/SOURCES.md | sha256sum
4176098c8976114161c29a4b3fbe4dea94202cc6ce58aed8a11d9c91b9c6ff57  -
$ git show 4de12b61f75c73e3675ef0e422cc2be0f7da8960:corpus/SOURCES.md | sha256sum
4176098c8976114161c29a4b3fbe4dea94202cc6ce58aed8a11d9c91b9c6ff57  -
$ sha256sum corpus/SOURCES.md
4176098c8976114161c29a4b3fbe4dea94202cc6ce58aed8a11d9c91b9c6ff57  corpus/SOURCES.md
$ git diff --stat b7f13f4b39cbd43076a85568adca763a6f674e7a HEAD -- corpus/
(no output — corpus/ is byte-identical base..tip)
```

## Independent base-pinned re-run (does not read the working tree)

Extracted the base revision into scratch with `git archive` and re-ran the
census against that tree with its own `shokunin.conf` root, so the measurement
does not depend on the live lane's working copy:

```
$ git archive b7f13f4b39cbd43076a85568adca763a6f674e7a | tar -x -C <scratch>/baseroot/kotoba-shokunin
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root <scratch>/baseroot kotoba
<same 20 W04 lines, same ids, same order>
kotoba	ok	<scratch>/baseroot/kotoba-shokunin/corpus/SOURCES.md
exit=0
$ diff <(grep -v '	ok	' base-tree-validate.out) <(grep -v '	ok	' live-validate.out)
(no output — ALL-FINDINGS-IDENTICAL)
```

## Census mode totals (same tree, read-only)

```
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh census --root /home/vgpnk/Projects/shokunin kotoba
kotoba	rows	151
kotoba	tier.A	134
kotoba	tier.B	16
kotoba	tier.C	1
kotoba	status.mined	143
kotoba	status.queued	7
kotoba	status.rejected	1
FLEET	rows	151
FLEET	tier.A	134
FLEET	tier.B	16
FLEET	tier.C	1
FLEET	tier.invalid	0
FLEET	status.queued	7
FLEET	status.mined	143
FLEET	status.rejected	1
FLEET	status.invalid	0
FLEET	missing	0
exit=0
```

The census's own `rows` counter agrees with the plan's grep at 151 — the two
counters do not drift apart at base.

## Freshness / carry-forward

| measure | round-74 receipt | round-76 base | delta |
|---|---|---|---|
| rows (grep) | 148 | 151 | +3 |
| W04 count | 20 | 20 | 0 |
| W04 id set | S018…S213 | S018…S213 | identical |
| E-code findings | 0 | 0 | 0 |

The round-74 receipt is a *before* census (148 rows at r74's base). The +3 is
round 74's own landing, not round 75's: r74's data commit `2c81137`
("round-74: C1 and C2 data — entries, S223-S225") brought the registry to 151,
and round 75 added no registry row. Verified by walking every commit that
touched `corpus/SOURCES.md`:

```
$ for r in $(git log --format=%H --all -- corpus/SOURCES.md); do
    n=$(git show $r:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|')
    echo "$n  $(git log -1 --format='%h %s' $r)"; done
151  2c81137 round-74: C1 and C2 data — entries, S223-S225, snapshots, SKILL.md body-craft rows and description, PROVINCE Adjacent re-pin, lesson, QUALITY Q70-Q72
151  ab3a69e
151  bcf11ce
151  dcd2419
148  0f3e8ad round-73 C1 data: Chinese-vendor skill-surface entry, rows S217-S222, …
148  cb61111
```

`diff` of the two sorted W04 id sets: no output. The duplicate-URL warning set
is unchanged since round 74; it is a standing structural property of the
registry (many pages are admitted under two scopes), not a regression. The plan's
base-battery note "W04 duplicate-url warning set as at r75" is confirmed by
measurement: it is the same set r74 recorded.

## Finding (F-B25-1) — C1 land-ordering constraint on the S213 `used-by` cell

The plan's C1 conjunct (e) requires row S213's `used-by` to name
`corpus/knowledge/description-craft-round76.md`. The census resolves every
`used-by` path on disk and reports a dangling one as **E11**, an E-code finding
that makes `validate` exit 1. Measured on a scratch copy of the base tree (no
lane file touched):

```
(i) S213 used-by patched to add `corpus/knowledge/description-craft-round76.md`,
    that file absent:
      kotoba	E11	S213 missing used-by corpus/knowledge/description-craft-round76.md
      exit=1
(ii) same patched row, a placeholder file present at that path:
      kotoba	ok	.../corpus/SOURCES.md
      exit=0
```

So the registry edit and the entry file must land together — the
`corpus/knowledge/description-craft-round76.md` file has to exist in the same
commit (or an earlier one) as the S213 `used-by` cell. If C1's build seat
lands the SOURCES.md cell before the entry file, the census goes red and the
no-harm battery fails at the tip. This is a land-ordering fact for the L1, not a
defect in the plan.

Secondary note: the used-by edit does not change the row count — grep stays 151
and census `rows` stays 151 — so the tip's expected census figures are
**151 rows, 20 W04, 0 E-codes, exit 0**, provided the entry file lands with the
cell.

## Consistency with the plan and with the other no-harm consumers

- Plan base battery (`plans/round-76.md` § Base battery) says census "exit 0,
  `kotoba ok` (151 rows; W04 duplicate-url warning set as at r75)" — reproduced
  exactly: exit 0, `kotoba ok`, 151 rows, W04 set unchanged since r74/r75.
- `verifiers/check_author_rules.py --census-check` runs the same census against
  a `git archive` of the measured revision; it agrees with this receipt:
  ```
  $ python3 -B verifiers/check_author_rules.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a \
      --census /home/vgpnk/Projects/shokunin/scripts/sources-census.sh --census-check
  measured-rev: b7f13f4b39cbd43076a85568adca763a6f674e7a
  author-facing rules in SKILL.md 4 of 4
  census validate: conformant
  exit=0
  ```
  That path uses `--file` mode, whose `used-by` resolution is relative to the
  extracted tree's root; the E11 arm behaves identically there (confirmed:
  patching S213's used-by and deleting the placeholder turns `--file` mode to
  `file E11 …`, exit 1).
- `check_report_pointers.py` treats a bare `census-before.txt` as a
  pointer resolved against the round's receipts dir, so the receipt's canonical
  name matters: it is `census-before.txt` in this round's receipts dir, matching
  the round-74 precedent.
- This report's own pointers were checked with that gate (read-only):
  ```
  $ python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-76/w1/B25Census.md --repo . --rev 4de12b61f75c73e3675ef0e422cc2be0f7da8960 --round 76
  report pointers resolved 9 of 13; unresolved 4
  pointer objects: blob 9, directory 0
  exit=1
  ```
  The four unresolved tokens are all *not yet committed*: this report itself,
  this round's `census-before.txt` receipt, and the two mentions of
  `corpus/knowledge/description-craft-round76.md` (C1's entry, which does not
  exist until C1 lands). The counter reads committed bytes only, so this is the
  expected pre-landing state, not a broken pointer; the same run at base
  revision additionally reported `plans/round-76.md` unresolved because the
  plan itself landed after base.
- Cross-lane `shared` mode: the agentskills.io URLs are not shared with another
  lane, so the C1 admission of S213 creates no fleet-wide duplicate-URL churn.

## Files changed by this seat

| path | kind |
|---|---|
| `.ufo/waves/round-76/receipts/census-before.txt` | new — the required receipt (stdout + exit codes + row count + W04 count + the F-B25-1 measurement) |
| `.ufo/waves/round-76/w1/B25Census.md` | new — this report |

Nothing else in the lane repo was written. No git/jj mutation, no index change,
no commit. The lane working tree at the time of this report has
`corpus/SOURCES.md` byte-identical to base.

## Tooling

No tool was installed or upgraded by this seat. `gawk` (used by the census
script) and `git`/`python3` were already present in the image and were used from
their existing locations.

## Scratch

All temporary work lived in `/fast/scratch/hyaku/kotoba-r76/B25Census/` (base
`git archive` extraction, patched-row probe, captured stdout). The directory was
removed after the last measurement, before this seat yielded.

## Risks / blockers

- **None blocking.** The census is green at base and the wave's data phase
  cannot break it as long as F-B25-1's land-ordering is honoured.
- The census reads the *working tree* when run with `--root <fleet>`; a
  mid-wave land by another seat that edits `corpus/SOURCES.md` will change what
  a re-run reports. The tip re-run (no-harm battery) must be taken against the
  tip tree, not against a stale working copy.
- `check_report_pointers.py` resolves `census-before.txt` by bare name against
  the round's receipts dir; if a same-named receipt from another round is
  present and this round's is missing, that gate would still read green. Worth
  an integrator eye at the tip.
