# ReviewerBaseValues — Round 73 Wave 1 Report

## Verdict

**CONDITIONAL PASS (3 minor plan/addendum defects identified before Freeze 2; all primary table counts and C1/C2/C3 base verdicts MATCH).**

All 6 rows of `plans/round-73.md` § Before-values, the non-table base claims in `plans/round-73.md`, the `m127-l1-repro.txt` root-cause diagnosis, and the `plans/round-73-addendum-1.md` C2 base reading (`own-description rules held 1 of 3`, exit 1: R1 fails, R2 fails, R3 passes) were independently re-derived from `072048fa8e8a52c707d25f7079772fa317244eb7` and verified.

Three plan/addendum defects require correction or alignment before Freeze 2:
1. **[DEFECT-1 / Addendum-1 C2 R1 character count & delimiter boundary]:** `plans/round-73-addendum-1.md:39-40` defines R1's first sentence as *"the text before the first `. ` or `: ` followed by an uppercase letter, else the first 99 characters"*, and lines 24 and 51–52 state that at base `072048f` *"the first sentence is 151 characters"*. On the folded description `D` (`len(D) = 1019`), the text **strictly before** the first `. ` (`Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density`) is **150 characters**, while including the trailing `.` (matching `omp`'s `s.match(/^.*?[.!?](?=\s|$)/)` in `corpus/knowledge/render-mechanism-round7.md:18`) is **151 characters**. Regardless (150 > 99 and 151 > 99), R1 fails at base (`1 of 3` holds), but `check_own_description.py` and the addendum text must agree on whether the delimiter character is included (151) or excluded (150) when printing the first sentence length.
2. **[DEFECT-2 / Addendum-1 line 15 premature past-tense claim on `.ufo/l0-questions.md`]:** `plans/round-73-addendum-1.md:15-16` states *"an L0 question is appended (`kotoba | round-73 | …`, fleet `.ufo/l0-questions.md`) asking whether a pointer registry would be acceptable."* At the current state, `grep -c 'kotoba | round-73' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` returns `0` (last line is line 169, `kama | round-42`). The L1 must append this line before round close as promised.
3. **[DEFECT-3 / Plan line 149 vs line 19 path shorthand]:** `plans/round-73.md:19` correctly locates receipts under `.ufo/waves/round-73/receipts/`, whereas lines 139 and 149 write bare `receipts/c3-base-battery-counter.txt` and `receipts/census-before.txt`. Because `plans/round-73.md:154-156` specifies a new gate `verifiers/check_report_pointers.py` that resolves every backticked `receipts/…` token against the lane tree, the r73 report must cite `.ufo/waves/round-73/receipts/…` (or `check_report_pointers.py` must resolve `receipts/…` under `.ufo/waves/round-73/receipts/`).

---

## 1. Summary Table of Base-Value Re-measurements at `072048fa8e8a52c707d25f7079772fa317244eb7`

| # | Surface / Item | Plan / Addendum Statement | Independent Command | Observed Reading | Status |
|---|---|---|---|---|---|
| 1a | Census validate (`plans/round-73.md:24`) | `exit 0; 20 W04 duplicate-URL warnings` (`receipts/census-before.txt`) | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | `exit=0`, `20` `W04` lines, `kotoba ok …/SOURCES.md` | **MATCH** |
| 1b | `corpus/SOURCES.md` row count (`plans/round-73.md:24`, `base-sweeps.txt:14`) | `142 rows` | Pattern 1 (plan regex): `git show 072048f…:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`<br>Pattern 2 (`awk` field 2): `git show 072048f…:corpus/SOURCES.md \| awk -F'\|' '$2 ~ /^[[:space:]]*S[0-9]+[[:space:]]*$/ {c++} END{print c}'` | Pattern 1: `142`<br>Pattern 2: `142` | **MATCH** |
| 2a | Tip battery counter with `--repo .` (`plans/round-73.md:25`, `c3-base-battery-counter.txt`) | `tip battery exit 0: 2 of 6`, exit 1 — floors exit 1, checklist exit 1, corpus integrity exit 1, corpus independent exit 1, gate registry exit 0, correction sweep exit 0; guard `instrument-size` FAIL (`76 > 40`, base `c69711e`); guarded paths `568`, deleted `0`, floors `15`, spotcheck base files `26` | `python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --repo .` (run alone) | `tip battery exit 0: 2 of 6`, `exit 1`; `FAIL guard instrument-size: instruments gain 76 lines > 40`; `guarded paths 568, deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 40); spotcheck base files 26`; registry `0`, floors `1`, checklist `1`, integrity `1`, independent `1`, sweep `0` | **MATCH** |
| 2b | M127 cause verification (`m127-l1-repro.txt`) | `check_tip_battery.py:610` `fleet = Path(args.fleet) if args.fleet else repo.parent` resolves `Path(".").parent` to `Path(".")` when `--repo .` is passed, symlinking lane files instead of fleet root; without `--repo .` (or with absolute repo path), floors and checklist exit 0 (`4 of 6`) | `python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7` (omitting `--repo .`, using `_default_lane()`) | `tip battery exit 0: 4 of 6`, `exit=1`; `check_assertion_floors.py exit 0`, `verify_skill_checklist.py exit 0` (only `verify_corpus_integrity.py` and `verify_corpus_independent.py` exit 1 due to unindexed r72 spotcheck) | **MATCH** |
| 3 | Checklist by hand in lane & fleet-shaped sandbox (`plans/round-73.md:26`) | `python3 -B verifiers/verify_skill_checklist.py` in the lane and in a fleet-shaped `git clone --shared` sandbox of `072048f` → `exit 0 in both` | `python3 -B verifiers/verify_skill_checklist.py` in `$P/kotoba-shokunin` (`072048f` fleet sandbox) and `/home/vgpnk/Projects/shokunin/kotoba-shokunin` | `sandbox_checklist_exit=0` and `lane_checklist_exit=0` (all 11 PASS lines identical: 45 boxes, 1019 chars, 568 lines, 187 trigger citations, 1280 governance citations) | **MATCH** |
| 4a | `SKILL.md` weight & registry block (`plans/round-73.md:27`, `base-sweeps.txt:10-12`) | `568 lines, 72,715 B; the registry block is 65 lines, 21,288 B (29% of bytes); 56 registry rows` | `git show 072048f…:SKILL.md \| wc -lc`; `git show 072048f…:SKILL.md \| awk '/^## Gate registry/{p=1} /^## Sources/{p=0} p' \| wc -lc`; `git show 072048f…:SKILL.md \| awk '/^## Gate registry/{p=1} /^## Sources/{p=0} p && /^\| \`/{c++} END{print c}'` | `568` lines, `72715` B; registry block `65` lines, `21288` B (`21288 / 72715 = 29.276%`); `56` registry rows | **MATCH** |
| 4b | `SKILL.md` boxes & `## ` sections (`plans/round-73.md:107-108`) | `45` `- [ ]` boxes matching `verifiers/checklist-baseline.json`; `S` `## ` headings | `git show 072048f…:SKILL.md \| grep -cE '^\s*- \[ \]'`; `git show 072048f…:SKILL.md \| grep -cE '^## '` | `45` boxes; `12` `## ` headings | **MATCH** |
| 5 | C1 vendor surfaces absence sweep (`plans/round-73.md:28`, `base-sweeps.txt:4-8`) | `1 hit: a host config path in corpus/knowledge/opencode-offer-trace-round8.md:84 (not a skill-surface row); registry rows naming docs.trae.cn, codebuddy.ai, kimi.com/code, moonshotai/kimi-cli, docs.bigmodel.cn: 0` | `git grep -niE 'trae\|codebuddy\|kimi code\|kimi-code\|zhipu\|bigmodel\|moonshot' 072048f… -- corpus SKILL.md PROVINCE.md`; `git show 072048f…:corpus/SOURCES.md \| grep -ciE 'docs\.trae\.cn\|codebuddy\.ai\|kimi\.com/code\|moonshotai/kimi-cli\|docs\.bigmodel\.cn'` | `1` hit (`corpus/knowledge/opencode-offer-trace-round8.md:84: parts of /home/vgpnk/.kimi-code/config.toml (merge_all_available_skills = true),`); `0` registry rows | **MATCH** |
| 6 | Package ID collisions (`plans/round-73.md:29`, `assimilation/{reg-ids,staged-ids,collisions}`) | `lane 142 ids, package 188, 14 collisions S203–S216` | Independent Python extraction from `072048f:corpus/SOURCES.md` and `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` | `reg_ids=142`, `staged_ids=188`, `collisions=14`: `['S203', 'S204', 'S205', 'S206', 'S207', 'S208', 'S209', 'S210', 'S211', 'S212', 'S213', 'S214', 'S215', 'S216']` | **MATCH** |
| 7a | Addendum-1 C2 base verdict (`plans/round-73-addendum-1.md:51-52`) | `own-description rules held 1 of 3 (R3 only; R1: the first sentence is 151 characters; R2: no quoted trigger in the first 99), exit 1` | Recomputed from `git show 072048f…:SKILL.md` using `description_of` from `verifiers/check_sibling_census.py` | `1 of 3` (R1 FAIL, R2 FAIL, R3 PASS), `exit 1`. **Note (DEFECT-1):** text strictly before `. ` is **150** chars; including `.` is **151** chars | **MISMATCH (150 vs 151 boundary)** |
| 7b | Addendum-1 C2 R2 (`plans/round-73-addendum-1.md:41-42, 52`) | First 99 chars contain whole words `skill` and `prompt` and ≥1 double-quoted string in `Triggers:` list; at base: `no quoted trigger in the first 99` | Python regex on `D[:99]` (`'Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / syste'`) | `skill` = `True`, `prompt` = `True`, double-quoted strings in `D[:99]` = `[]` (0 quoted triggers) → R2 FAIL | **MATCH** |
| 7c | Addendum-1 C2 R3 (`plans/round-73-addendum-1.md:43-45, 51`) | `len(D) <= 1024` (`1,019/1,024 chars`) and `check_sibling_census.py … --province PROVINCE.md --skill SKILL.md` exits 0 in fleet-shaped sandbox of `072048f` | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` in `$P/kotoba-shokunin` (`072048f`) | `len(D) = 1019 <= 1024`; `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, `skill description length 1019 of 1024`, `exit=0` → R3 PASS | **MATCH** |
| 7d | Addendum-1 C2 frontmatter line count (`plans/round-73-addendum-1.md:47-49`) | Frontmatter keeps its line count (`git diff --numstat <base> <rev> -- SKILL.md` inside frontmatter) | `git show 072048f…:SKILL.md \| sed -n '1,20p' \| grep -n '^---$'` | Closing `---` at line `19` (`19` lines total, lines 1..19) | **MATCH** |
| 8a | Non-table claim: `no earlier attempt` (`plans/round-73.md:6-7`) | `.ufo/watchdog.log` shows one `launch kotoba round=73` line and no `lane-dead-no-report kotoba round=73` line | `grep kotoba /home/vgpnk/Projects/shokunin/.ufo/watchdog.log \| tail -4` | Exactly 1 `launch kotoba round=73 pgid=2013243 driver=hyaku-inline attempt=1` line; 0 `lane-dead-no-report` lines | **MATCH** |
| 8b | Non-table claim: `the r72 spot-check is unindexed` (`plans/round-73.md:25`) | `corpus/lessons/round-72-verifier-spotcheck.md` added at `072048f` is unindexed in `corpus/README.md` | `git show 072048f…:corpus/README.md \| grep -c round-72-verifier-spotcheck` | `0` | **MATCH** |
| 8c | Non-table claim: inherited routed defects (`plans/round-73.md:31-43`) | `corpus/SOURCES.md:209-215` split note; `resident-index-and-rungs-round72.md:45` `"format's,."`; r72 report cites `tip-check_*`; SHONEN boxes `[~]` | Inspected at `072048f` via `read` / `git show` | All 4 verified byte-for-byte at `072048f` | **MATCH** |
| 8d | Non-table claim: quarantine slice (`plans/round-73.md:162-164`) | 13 rows at `assimilation/quarantine-slice` holds no row any admitted entry cites (staged C1 entry cites S214, S216, S217, S218, S219, S221) | Read `assimilation/quarantine-slice` and `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md:4-9` | Quarantine holds `S151, S167, S168, S169, S172, S176, S180, S185, S236, S237, S238, S239, S243` (13 rows); intersection with `{S214, S216, S217, S218, S219, S221}` is `∅` | **MATCH** |
| 8e | Non-table claim: L0 question appended (`plans/round-73-addendum-1.md:15-16`) | *"an L0 question is appended (`kotoba \| round-73 \| …`, fleet `.ufo/l0-questions.md`) asking whether a pointer registry would be acceptable"* | `grep -n 'kotoba \| round-73' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` | `0` hits (last line of `.ufo/l0-questions.md` is line 169: `kama \| round-42`) | **MISMATCH (not yet appended)** |

---

## 2. Detailed Verification & Exact Command Outputs

### 2.1 Addendum-1 C2 Base Readings (`072048fa8e8a52c707d25f7079772fa317244eb7:SKILL.md`)

**Command (frontmatter inspection):**
```sh
git show 072048fa8e8a52c707d25f7079772fa317244eb7:SKILL.md | sed -n '1,20p'
```
**Observed output:**
```yaml
---
name: kotoba-shokunin
description: >
  Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density.
  Triggers: "skill file", "SKILL.md", "frontmatter description", "trigger
  words", "prompt craft", "write a skill", "audit this skill", "skill quality".
  Anti-triggers: general prompt engineering for model outputs (not skill
  files), runtime code changes, and domain content inside a skill's
  reference/ tree. Sibling boundary: kagi, kake, kasegi, kengaku and kumitate
  own their own SKILL.md content — this skill audits and reports; fixes route
  to the owning lane. chousa owns the research method; kama owns endpoint
  verification; kengaku owns measured capability effects of prompt format;
  tameshi owns the fixture and mutation method. NOT kotodama-shokunin:
  kotodama owns naming and language for fictional worlds despite the similar
  name. Note:
  shokunin files sit outside the omp skill discovery roots, so this text
  never reaches the omp router — craft here is audit-side.
---
```

**Command (recomputing `D`, R1, R2, R3 length):**
```python
import re, subprocess
rev = "072048fa8e8a52c707d25f7079772fa317244eb7"
repo = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
skill_text = subprocess.check_output(["git", "-C", repo, "show", f"{rev}:SKILL.md"], text=True)
front = skill_text.split("\n---", 1)[0]
match = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
folded = re.sub(r"\A[>|][+-]?\s*", "", re.sub(r"\s+", " ", match.group(1)).strip()).strip()
m_sent = re.search(r"[.:] (?=[A-Z])", folded)
print("len(D):", len(folded))
print("first 99 chars:", repr(folded[:99]))
print("first sentence (before `. `):", len(folded[:m_sent.start()]), repr(folded[:m_sent.start()]))
print("first sentence (including `.`):", len(folded[:m_sent.start() + 1]), repr(folded[:m_sent.start() + 1]))
print("has_skill in first 99:", bool(re.search(r"\bskill\b", folded[:99], re.I)))
print("has_prompt in first 99:", bool(re.search(r"\bprompt\b", folded[:99], re.I)))
print("quoted strings in first 99:", re.findall(r'"([^"]+)"', folded[:99]))
```
**Observed output:**
```text
len(D): 1019
first 99 chars: 'Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / syste'
first sentence (before `. `): 150 'Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density'
first sentence (including `.`): 151 'Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts / system prompts for trigger fidelity and decision density.'
has_skill in first 99: True
has_prompt in first 99: True
quoted strings in first 99: []
```

**Command (R3 sibling census in a fleet-shaped sandbox of `072048f`):**
```sh
P=$(mktemp -d /tmp/k73fleet-ReviewerBaseValues.XXXX)
# symlink fleet entries except kotoba-shokunin, clone --shared and checkout 072048f
cd "$P/kotoba-shokunin" && python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md; echo "sandbox_sibling_census_exit=$?"
```
**Observed output:**
```text
rows 20 verified 20
province rows 20 matched 20
skill description names 9 of 9 non-none lanes
skill description length 1019 of 1024
sandbox_sibling_census_exit=0
```

**Finding on Addendum-1 C2 (DEFECT-1):**
- **R1:** Fails at base (`150 > 99` without the period; `151 > 99` with the period). However, `plans/round-73-addendum-1.md:39` writes *"the text before the first `. ` or `: ` followed by an uppercase letter"* (which is 150 chars: `m.start()`), whereas lines 24 and 52 state *"the first sentence is 151 characters"* (which includes the `.` character: `m.start() + 1`, matching `omp`'s `s.match(/^.*?[.!?](?=\s|$)/)` in `corpus/knowledge/render-mechanism-round7.md:18`). If a candidate rewrite is exactly 40 chars with the period (39 without) or 100 chars with the period (99 without), the two definitions disagree. Recommendation before Freeze 2: ensure `verifiers/check_own_description.py` and the addendum agree on whether the punctuation character is included in the slice `D[:m.start() + 1]` (151 chars at base) or excluded `D[:m.start()]` (150 chars at base).
- **R2:** Fails at base (`skill` and `prompt` are present in `D[:99]`, but 0 double-quoted trigger strings occur in `D[:99]`; `"Triggers:"` starts at index 152). **MATCH.**
- **R3:** Passes at base (`len(D) = 1019 <= 1024` and `check_sibling_census.py` exits 0 with `9 of 9 non-none lanes`). **MATCH.**
- **Overall base reading:** `own-description rules held 1 of 3`, exit 1. **MATCH.**

---

### 2.2 Census & `corpus/SOURCES.md` Row Count (`plans/round-73.md:24`, `receipts/census-before.txt`)

**Commands:**
```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba; echo "exit=$?"
git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md | awk -F'|' '$2 ~ /^[[:space:]]*S[0-9]+[[:space:]]*$/ {c++} END{print c}'
```
**Observed output:**
```text
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
[... 18 more W04 lines identical to receipts/census-before.txt ...]
kotoba	W04	S213 duplicate url agentskills.io/skill-creation/optimizing-descriptions.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
142
142
```
**Verdict:** **MATCH** (exit 0, 142 rows by both patterns, 20 W04 duplicate-URL warnings, byte-for-byte match with `.ufo/waves/round-73/receipts/census-before.txt`).

---

### 2.3 Tip Battery Counter & M127 Root-Cause Verification (`plans/round-73.md:25`, `receipts/c3-base-battery-counter.txt`, `receipts/m127-l1-repro.txt`)

**Command A (exact plan table invocation with `--repo .`, run alone):**
```sh
python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --repo .
```
**Observed output:**
```text
measured rev 072048fa8e8a52c707d25f7079772fa317244eb7 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 40); spotcheck base files 26
INFO spotcheck added at 072048fa8e8a52c707d25f7079772fa317244eb7 (not a base file): corpus/lessons/round-72-verifier-spotcheck.md
guard no-deletions PASS
guard floors PASS
FAIL guard instrument-size: instruments gain 76 lines > 40
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.6s
gate verifiers/check_assertion_floors.py exit 1 wall 67.0s
gate verifiers/verify_skill_checklist.py exit 1 wall 1.6s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 71.4s
tip battery exit 0: 2 of 6
Command exited with code 1
```

**Command B (invocation without `--repo .`, so `args.repo` uses `_default_lane()` which is `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):**
```sh
python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7; echo "exit=$?"
```
**Observed output:**
```text
measured rev 072048fa8e8a52c707d25f7079772fa317244eb7 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 40); spotcheck base files 26
INFO spotcheck added at 072048fa8e8a52c707d25f7079772fa317244eb7 (not a base file): corpus/lessons/round-72-verifier-spotcheck.md
guard no-deletions PASS
guard floors PASS
FAIL guard instrument-size: instruments gain 76 lines > 40
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.5s
gate verifiers/check_assertion_floors.py exit 0 wall 49.0s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.5s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 52.6s
tip battery exit 0: 4 of 6
exit=1
```

**Independent confirmation of M127 cause (`verifiers/check_tip_battery.py:609-610`):**
At `verifiers/check_tip_battery.py:609-610`:
```python
    repo = Path(args.repo)
    fleet = Path(args.fleet) if args.fleet else repo.parent
```
Because `Path(".")` is not resolved (`Path(args.repo).resolve()`), `Path(".").parent` evaluates to `Path(".")` (the lane directory itself). `build_sandbox` then symlinks the entries of `kotoba-shokunin` into the sandbox parent `$TMPDIR/k72-tip-…/`, leaving `../.ufo/` absent from the sandbox parent. Consequently, `verify_skill_checklist.py` (and `check_assertion_floors.py`, which runs `verify_skill_checklist.py --self-test`) fail on `../.ufo/reports/round-7/kotoba.md` not resolving. When `--repo` is resolved (or omitted so `_default_lane()` supplies the resolved path), `repo.parent` is `/home/vgpnk/Projects/shokunin`, and both `check_assertion_floors.py` and `verify_skill_checklist.py` exit `0` (`4 of 6`). **MATCH — L1's M127 diagnosis is independently confirmed.**

---

### 2.4 Checklist by Hand (`plans/round-73.md:26`)

**Command:**
```sh
P=$(mktemp -d /tmp/k73fleet-ReviewerBaseValues.XXXX)
for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
  [ -e "$e" ] || continue
  b=$(basename "$e")
  [ "$b" = "kotoba-shokunin" ] && continue
  ln -s "$e" "$P/$b"
done
git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
git -C "$P/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
(cd "$P/kotoba-shokunin" && python3 -B verifiers/verify_skill_checklist.py; echo "sandbox_checklist_exit=$?")
(cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_skill_checklist.py; echo "lane_checklist_exit=$?")
rm -rf "$P"
```
**Observed output:**
Both runs print 11 `PASS` lines and exit `0` (`sandbox_checklist_exit=0`, `lane_checklist_exit=0`). **MATCH.**

---

### 2.5 `SKILL.md` Weight and Registry Block (`plans/round-73.md:27`, `receipts/base-sweeps.txt:9-12`)

**Command:**
```sh
git show 072048fa8e8a52c707d25f7079772fa317244eb7:SKILL.md | wc -lc
git show 072048fa8e8a52c707d25f7079772fa317244eb7:SKILL.md | awk '/^## Gate registry/{p=1} /^## Sources/{p=0} p' | wc -lc
git show 072048fa8e8a52c707d25f707d25f7079772fa317244eb7:SKILL.md | awk '/^## Gate registry/{p=1} /^## Sources/{p=0} p && /^\| `/{c++} END{print c}'
```
**Observed output:**
```text
    568   72715
     65   21288
56
```
**Verdict:** **MATCH** (568 lines, 72,715 bytes; registry block 65 lines, 21,288 bytes = 29.28%; 56 registry rows).

---

### 2.6 C1 Vendor Surfaces Absence Sweep (`plans/round-73.md:28`, `receipts/base-sweeps.txt:3-8`)

**Command:**
```sh
git grep -niE 'trae|codebuddy|kimi code|kimi-code|zhipu|bigmodel|moonshot' 072048fa8e8a52c707d25f7079772fa317244eb7 -- corpus SKILL.md PROVINCE.md
git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md | grep -ciE 'docs\.trae\.cn|codebuddy\.ai|kimi\.com/code|moonshotai/kimi-cli|docs\.bigmodel\.cn' || true
```
**Observed output:**
```text
072048fa8e8a52c707d25f7079772fa317244eb7:corpus/knowledge/opencode-offer-trace-round8.md:84:  parts of `/home/vgpnk/.kimi-code/config.toml` (`merge_all_available_skills = true`),
0
```
**Verdict:** **MATCH** (1 hit at `corpus/knowledge/opencode-offer-trace-round8.md:84`; 0 registry rows naming any of the 5 vendor host strings).

---

### 2.7 Package ID Collisions (`plans/round-73.md:29`, `.ufo/waves/round-73/assimilation/`)

**Command:**
```sh
python3 -c '
import re, subprocess
reg_text = subprocess.check_output(["git", "-C", "/home/vgpnk/Projects/shokunin/kotoba-shokunin", "show", "072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md"], text=True)
with open("/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md") as f:
    staged_text = f.read()
reg_ids = [m.group(1) for line in reg_text.splitlines() if (m := re.match(r"^\s*\|\s*(S\d+)\s*\|", line))]
staged_ids = [m.group(1) for line in staged_text.splitlines() if (m := re.match(r"^\s*\|\s*(S\d+)\s*\|", line))]
collisions = sorted(set(reg_ids) & set(staged_ids), key=lambda s: int(s[1:]))
print(f"reg_ids={len(reg_ids)} (unique={len(set(reg_ids))}), staged_ids={len(staged_ids)} (unique={len(set(staged_ids))}), collisions={len(collisions)}: {collisions[0]}..{collisions[-1]} -> {collisions}")
'
```
**Observed output:**
```text
reg_ids=142 (unique=142), staged_ids=188 (unique=188), collisions=14: S203..S216 -> ['S203', 'S204', 'S205', 'S206', 'S207', 'S208', 'S209', 'S210', 'S211', 'S212', 'S213', 'S214', 'S215', 'S216']
```
**Verdict:** **MATCH** (142 lane IDs, 188 staged IDs, 14 collisions `S203`–`S216`, matching `.ufo/waves/round-73/assimilation/{reg-ids,staged-ids,collisions}`).

---

### 2.8 Non-Table Base Claims (`plans/round-73.md` & `plans/round-73-addendum-1.md`)

1. **`no earlier attempt` (`plans/round-73.md:6-7`):**
   - Command: `grep kotoba /home/vgpnk/Projects/shokunin/.ufo/watchdog.log | tail -4`
   - Output:
     ```text
     2026-10-25T11:19:08-03:00 complete kotoba round=71; hyaku-inline attempt=1
     2026-10-25T17:43:21-03:00 launch kotoba round=72 pgid=2089970 driver=hyaku-inline attempt=1
     2026-10-25T19:31:41-03:00 complete kotoba round=72; hyaku-inline attempt=1
     2026-10-25T19:36:06-03:00 launch kotoba round=73 pgid=2013243 driver=hyaku-inline attempt=1
     ```
   - Also verified: `git ls-tree 072048fa8e8a52c707d25f7079772fa317244eb7 .ufo/waves/round-73` is empty (`.ufo/waves/round-73/` was first created in plan commit `b337035fedc2a776fb84c5e885834fe77ed3df98`).
   - Status: **MATCH**.

2. **`the r72 spot-check is unindexed` (`plans/round-73.md:25`):**
   - Command: `git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/README.md | grep -c round-72-verifier-spotcheck || true`
   - Output: `0`
   - Status: **MATCH**.

3. **Inherited routed defects (`plans/round-73.md:35-42`):**
   - `corpus/SOURCES.md:209-215`: Verified at `072048f:corpus/SOURCES.md:209-217` — the round-64 placement-correction note is split mid-sentence by the round-72 assimilation entry at line 212, with stray `## Leads (unopened)\`` lines at 214 and 217. **MATCH.**
   - `corpus/knowledge/resident-index-and-rungs-round72.md:45`: Verified at `072048f` — line 45 reads `- **Check the harness's house standard before the format's,.**`. **MATCH.**
   - `.ufo/reports/round-72/kotoba.md` receipt pointers: Verified at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-72/kotoba.md:70,103` — cites `tip-check_tip_battery.txt` and `tip-check_substrate_repin_v2.txt`, while `ls .ufo/waves/round-72/receipts/` holds `tip-tip_battery.txt` and `tip-substrate_repin_v2.txt`. **MATCH.**
   - `SHONEN.md`: Verified at `072048f:SHONEN.md:5,9,12,14` — all 4 boxes are `- [~]`. **MATCH.**

4. **L0 question in `.ufo/l0-questions.md` (`plans/round-73-addendum-1.md:15-16`):**
   - Statement: *"an L0 question is appended (`kotoba | round-73 | …`, fleet `.ufo/l0-questions.md`) asking whether a pointer registry would be acceptable."*
   - Command: `grep -c 'kotoba | round-73' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md || true`
   - Output: `0`
   - Status: **MISMATCH (DEFECT-2)** — the addendum writes this in present/completed tense before the line has been appended to `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Must be appended before round close.
