Result: DONE — 12 single-point mutants have complete inline probes and explicit frozen-class mappings; four missing frozen-counter arms are identified honestly, and the heredoc mutant was killed by one bounded detector with exact-byte restoration.

# C2 mutation battery — REDESIGN INPUT ONLY

C2 was withdrawn before data (`plans/round-57.md:124-133`). This is not a C2 fix, a replacement counter, or evidence that the planned rule passes. Neither frozen counter was edited. No lane verifier, checklist text, or sibling source was changed.

Axis: **operability** — probes can be copied into an isolated clone and passed to the existing command-check CLI. Supporting calibration: distinguish a proposed killer from an exercised kill and identify cases the frozen generator cannot distinguish.

## Contract and evidence

Candidate rule being challenged, from `.ufo/waves/round-57/build-spec.json:127`: within an **info-less** fence, skip individual lines with a leading pipe, a leading plus border, a leading box-drawing character, an unquoted U+2192 arrow, or a first whitespace-delimited token ending in a colon. Leading means first non-whitespace character. Preserve shell-tagged behavior, the other lines of a mixed fence, and heredoc tracking. This report does not implement that rule.

Frozen vocabulary and assertions:

- `verifiers/check_infoless_fences.py:29-51`: P1 table, P2 box/tree, P3 ASCII box, P4 unquoted arrow, P5 key/value; H1 missing command, H2 missing pipeline command, H3 missing command after a table, H4 colon in an argument, H5 plain missing command in a bash-tagged fence.
- `verifiers/check_infoless_fences.py:30-44`: P cases require PASS; H cases require FAIL **and the bogus command head in detail**. FAIL from an unrelated table cell is not a kill of the command-preservation defect.
- Actual builders: `verifiers/check_infoless_fences.py:282-351`; only H5 is tagged, at `:368`.
- Existing heredoc behavior: `verifiers/verify_skill_checklist.py:1097-1108`; verdict/floor behavior: `:1724-1750`.

The planned rule does not exist at the assigned revision. Therefore every planned-rule reference/mutant outcome below is **[INFERENCE]**, except the explicitly observed M12 sandwich. The other eleven mutants were not implemented or run. No full frozen-predicate run was made by this seat.

## Mutation matrix

Each row changes one decision only; all other behavior is held fixed. `FAIL(head)` means FAIL with `r57missingcmd` in the selected check's detail. `GAP` is not an exercised survivor: it means the frozen generated inputs lack the distinguishing arm.

| ID | Single-point mutant | Concrete probe: reference → mutant | Frozen class expected to kill it / coverage reality |
|---|---|---|---|
| M01 | Remove the leading-pipe line class. | m01: PASS → FAIL on table cells. | **P1**, also P3's middle row. |
| M02 | Remove the leading-plus-border line class. | m02: PASS → FAIL on `+------+`. | **P3**. The pipe class remains enabled. |
| M03 | Remove the box-drawing line class. | m03: PASS → FAIL on box/tree heads. | **P2**. |
| M04 | Remove the unquoted-arrow line class. | m04: PASS → FAIL on arrow-line heads. | **P4**. |
| M05 | Remove the first-token-ending-colon line class. | m05: PASS → FAIL on `MODE:` / `state:`. | **P5**. |
| M06 | Shorten the inclusive box range's upper endpoint from U+257F to U+257E. | m06: PASS → FAIL on U+257F `╿`. | **P2 boundary arm needed — GAP.** Frozen P2 never emits U+257F. |
| M07 | Detect U+2192 anywhere, ignoring whether it is quoted. | m07: FAIL(head) → N/A after its only command is skipped. | **H1-family quoted-argument arm needed — GAP.** P4 only tests unquoted arrows; frozen H1–H5 contain none. |
| M08 | Treat any token containing a colon as key/value output, instead of testing the first token's suffix. | m08: FAIL(head) → N/A. | **H4**. |
| M09 | Treat any line containing a pipe as a table row, instead of testing the leading character. | m09: FAIL(head) → N/A. | **H2**. |
| M10 | Remove the info-less-only scope guard, applying the same skips to bash-tagged fences. | m10: FAIL(head) → PASS, leaving only `ls -la`. | **H5 shape-bearing arm needed — GAP.** Frozen H5's plain two-token command matches none of the skip classes. |
| M11 | Lift a matching line's skip to its entire containing info-less fence. | m11: FAIL(head) → N/A. | **H3**. If the mutation instead drops every info-less fence unconditionally, H1, H2 and H4 kill that broader defect too. |
| M12 | Disable opening-heredoc recognition while leaving ordinary scanning intact. | m12: PASS → FAIL on the heredoc body/delimiter. | **No existing P1–P5/H1–H5 arm.** H5 is the nearest preservation-control family, but needs a new PASS-expected heredoc arm; calling today's FAIL-only H5 a killer would be false. The supplemental detector below **did kill** this mutant. |

### Why the four gaps are real coverage gaps

These conclusions follow from the frozen builders, not a claimed execution of a future implementation:

1. **M06:** P2 emits U+2500, U+2502, U+250C, U+2510, U+2514, U+2518 and U+251C (`:295-300`). Dropping U+257F cannot change their classification, on any seed.
2. **M07:** P4 emits no quote characters (`:309-314`), and none of H1–H5 emits U+2192 (`:327-351`). Thus removing arrow quote-awareness changes no frozen case.
3. **M10:** H5 is only `<head> <token>` (`:349-351`), with tokens restricted to lowercase words/hyphens/digits (`:121`, `:245-258`). It has no leading pipe/plus/box character, arrow, or colon. Applying the new skips to that shell-tagged input is invisible.
4. **M12:** none of the ten builders emits `<<` or a heredoc body/delimiter. Lost heredoc state is invisible to their inputs. A PASS-expected preservation arm is necessary; the current H labels are all FAIL-expected.

These are inputs for a later redesign, **not permission to alter this round's frozen classes, targets, or predicates**.

## How to use the inline probe files

All files below are complete UTF-8 `SKILL.md` files, with a final newline. Materialize them only under the assigned sandbox, using the relative paths shown. Only m12 was materialized by this seat.

For a later candidate or one mutant at a time, use the same CLI and an empty sandbox cwd:

```sh
ROOT=/fast/scratch/hyaku/kotoba-r57/MutC2Rule
INSTRUMENT="$ROOT/verifiers/verify_skill_checklist.py"
CASE="$ROOT/probes/m01"
# Run from an empty directory under ROOT, not from the lane or fleet repo.
timeout 20s env PYTHONSAFEPATH=1 python3 -B -P "$INSTRUMENT" \
  --repo "$CASE" --skill "$CASE/SKILL.md" \
  --check trigger.command_binary_resolves --json
```

Select the exact `trigger.command_binary_resolves` record, not a substring elsewhere in stdout. Reject invalid JSON, duplicate/missing records, timeout, usage/environment exits, and N/A. PASS probes require process exit 0, PASS and a positive evaluated count; FAIL probes require exit 1, FAIL and the named unresolved head. Before use, require `ls` and `cat` to resolve and `r57missingcmd` / `r57heredocbody` not to resolve via PATH or as paths in the empty case repo. A failed prerequisite makes that run inconclusive.

For any later mutation run: retain pristine bytes, run the identical detector on pristine/mutated/restored bytes, record all exits and hashes, and restore in a finally-equivalent path. A failing pristine candidate is inconclusive, not a killed mutant. Do not use this report's future expected outcomes as measured results.

## Inline probes

### probes/m01/SKILL.md

````markdown
---
name: m01
description: Test table lines without suppressing a real command.
---

# Pipe-led table

```
| alpha | beta |
|---|:---:|
| gamma | delta |
| epsilon | zeta |
ls -la
```
````

### probes/m02/SKILL.md

````markdown
---
name: m02
description: Test ASCII borders independently of pipe-led rows.
---

# ASCII box

```
+------+
| alpha |
+------+
ls -la
```
````

### probes/m03/SKILL.md

````markdown
---
name: m03
description: Test Unicode box and tree lines.
---

# Box and tree

```
┌──────────┐
│ alpha │
└──────────┘
├── beta
└── gamma
ls -la
```
````

### probes/m04/SKILL.md

````markdown
---
name: m04
description: Test unquoted arrow output lines.
---

# Arrow output

```
alpha beta (gamma)    → delta/epsilon.json
zeta theta (iota)    → kappa/lambda.json
ls -la
```
````

### probes/m05/SKILL.md

````markdown
---
name: m05
description: Test first-token colon suffixes in output.
---

# Key value output

```
MODE: dense
state:   alpha/beta
ls -la
```
````

### probes/m06/SKILL.md

The first character of the first content line is **U+257F**, not a visually similar U+2502 or U+257E.

````markdown
---
name: m06
description: Test the inclusive upper box-drawing boundary.
---

# Upper endpoint

```
╿ alpha
ls -la
```
````

### probes/m07/SKILL.md

The arrow is inside a double-quoted argument. This is an ordinary unresolved command, not an arrow-output line. The single-quoted counterpart is an additional useful later arm, not claimed exercised here.

````markdown
---
name: m07
description: Keep commands with quoted arrow arguments visible.
---

# Quoted arrow command

```
r57missingcmd --label="alpha → beta"
```
````

### probes/m08/SKILL.md

````markdown
---
name: m08
description: Keep commands with colons inside arguments visible.
---

# Colon argument

```
r57missingcmd --opt=alpha:beta
```
````

### probes/m09/SKILL.md

````markdown
---
name: m09
description: Keep missing pipeline commands visible.
---

# Pipeline

```
ls | r57missingcmd
```
````

### probes/m10/SKILL.md

U+2192 outside quotes is an ordinary shell argument here; the fence is explicitly tagged bash. A leaked display filter would hide the second command and leave a false PASS on the first.

````markdown
---
name: m10
description: Preserve explicitly shell-tagged command checking.
---

# Tagged shell control

```bash
ls -la
r57missingcmd alpha → beta
```
````

### probes/m11/SKILL.md

````markdown
---
name: m11
description: Preserve a missing command after table output.
---

# Mixed fence

```
| alpha | beta |
|---|---|
| gamma | delta |
| epsilon | zeta |
r57missingcmd --probe
```
````

### probes/m12/SKILL.md

This file is exactly the 132-byte probe used in the observed sandwich below. The body is data; only the heredoc opener's `cat` and the tail's `ls` are command subjects. No shell commands in these examples are executed by the verifier.

````markdown
---
name: m12
description: Test heredoc body opacity.
---

# Heredoc control

```
cat <<'R57_EOF'
r57heredocbody
R57_EOF
ls -la
```
````

## One exercised mutation probe: M12

Scratch clone: `/fast/scratch/hyaku/kotoba-r57/MutC2Rule`, checked out at assigned `01312a77e36317feb6e961aba77841ddab1225ca`. No sandbox commit was made. Clone/checkout command exited 0, with no output:

```sh
env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 90s git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57/MutC2Rule && env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE timeout 30s git -C /fast/scratch/hyaku/kotoba-r57/MutC2Rule checkout -q 01312a77e36317feb6e961aba77841ddab1225ca
```

**Mutant:** one scratch-only statement at `verifiers/verify_skill_checklist.py:1106` changed from `hm = heredoc_delimiter(line)` to `hm = None`. This removes recognition of a heredoc opener. It is deliberately regressive, not a proposed C2 fix. The exact statement was restored immediately after the mutant run, including after its nonzero exit.

**Expected detector:** the same `detect_m12.py` below runs the CLI with a 15-second child timeout and a 20-second subprocess backstop, and requires PASS with exactly two live command subjects. Each outer invocation was `timeout 25s python3 -B -P detect_m12.py`, cwd the scratch clone. It asserts only the inherited heredoc invariant; it does not classify info-less display lines.

### Actual outputs and exits

| State | Detector exit | Instrument exit | Selected-check output | Verdict |
|---|---:|---:|---|---|
| Pristine | 0 | 0 | PASS, evaluated 2, `2 segments; 2 command subject(s) resolve` | Baseline valid. |
| Mutated | 1 | 1 | FAIL, evaluated 4; exact detail below. | **KILLED by supplemental heredoc detector**, not by a claimed frozen-counter run. |
| Restored | 0 | 0 | PASS, evaluated 2, `2 segments; 2 command subject(s) resolve` | Behavior restored. |

All three instrument stderr values were `''`. Pristine and restored stdout were identical:

```json
{
  "checks": [
    {
      "detail": "2 segments; 2 command subject(s) resolve",
      "evaluated": 2,
      "id": "trigger.command_binary_resolves",
      "status": "PASS"
    }
  ],
  "exit_code": 0,
  "fail": 0,
  "na": 0,
  "pass": 1
}
```

Mutant stdout:

```json
{
  "checks": [
    {
      "detail": "4 segments; line 10: 'r57heredocbody' (fenced, segment 'r57heredocbody') does not resolve; line 11: 'R57_EOF' (fenced, segment 'R57_EOF') does not resolve",
      "evaluated": 4,
      "id": "trigger.command_binary_resolves",
      "status": "FAIL"
    }
  ],
  "exit_code": 1,
  "fail": 1,
  "na": 0,
  "pass": 0
}
```

The detector's final output was respectively:

```text
detector PASS expected PASS with exactly two live command subjects
detector FAIL expected PASS with exactly two live command subjects
detector PASS expected PASS with exactly two live command subjects
```

### Hashes and restoration evidence

Hashes were printed by the identical detector and by `timeout 15s sha256sum ...`; the initial hash command exited 0. After restoration the command was `timeout 25s python3 -B -P detect_m12.py && timeout 15s sha256sum verifiers/verify_skill_checklist.py verifiers/check_infoless_fences.py verifiers/check_plugin_manifests.py detect_m12.py probes/m12/SKILL.md`, exit 0.

| Bytes | SHA-256 |
|---|---|
| Instrument before | `629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab` |
| Instrument mutated | `18b7ab72ba57a4184d95694ec887871e803398ba1203ee006becb9f6d79a5715` |
| Instrument restored | `629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab` |
| M12 probe, all three runs | `6eff200ff0e59f841b0a7843bde729393d371e886427cb34642064687b26273d` |
| Unchanged detector source | `c3e913340573c02f13938b9e139cb422d00f24a351f7ce70946efa156e9a809c` |
| Frozen C2 counter, before/after | `b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac` |
| Frozen C1 counter, before/after | `bf11a4efc1c7589a2a057040cc2d5026b54d4f4e2d24c6455b4c50f12f3ea37e` |

Matching before/restored instrument hashes establish exact-byte restoration, not merely a reversal that appears equivalent. No counter was mutated. One initial edit attempt was refused because the scratch anchor had not been displayed; the exact scratch range was then read and the single-line edit applied. That refusal changed no bytes.

### detect_m12.py — complete exercised detector

```python
#!/usr/bin/env python3
"""One read-only heredoc regression detector; does not implement a fence rule."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent
instrument = root / "verifiers/verify_skill_checklist.py"
case = root / "probes/m12"
empty = root / "probe-cwd"
empty.mkdir(exist_ok=True)
print("instrument sha256", hashlib.sha256(instrument.read_bytes()).hexdigest(), flush=True)
print("probe sha256", hashlib.sha256((case / "SKILL.md").read_bytes()).hexdigest(), flush=True)
for executable in ("python3", "timeout", "cat", "ls"):
    if shutil.which(executable) is None:
        print("INCONCLUSIVE missing prerequisite", executable)
        sys.exit(2)
if shutil.which("r57heredocbody") is not None:
    print("INCONCLUSIVE payload unexpectedly resolves")
    sys.exit(2)
argv = ["timeout", "15s", "python3", "-B", "-P", str(instrument),
        "--repo", str(case), "--skill", str(case / "SKILL.md"),
        "--check", "trigger.command_binary_resolves", "--json"]
print("command", " ".join(argv), flush=True)
try:
    result = subprocess.run(argv, cwd=empty, env={**os.environ, "PYTHONSAFEPATH": "1"},
                            capture_output=True, text=True, timeout=20)
except subprocess.TimeoutExpired:
    print("INCONCLUSIVE detector subprocess timeout")
    sys.exit(2)
print("instrument exit", result.returncode)
print("stdout:\n" + result.stdout, end="" if result.stdout.endswith("\n") else "\n")
print("stderr:", repr(result.stderr))
try:
    document = json.loads(result.stdout)
    check, = [row for row in document["checks"]
              if row["id"] == "trigger.command_binary_resolves"]
except (ValueError, KeyError, TypeError):
    print("INCONCLUSIVE invalid JSON/check cardinality")
    sys.exit(2)
if result.returncode not in (0, 1):
    print("INCONCLUSIVE instrument environment/usage failure")
    sys.exit(2)
ok = (result.returncode == 0 and check["status"] == "PASS"
      and check["evaluated"] == 2 and "r57heredocbody" not in check["detail"])
print("detector", "PASS" if ok else "FAIL", "expected PASS with exactly two live command subjects")
sys.exit(0 if ok else 1)
```

## Handoff boundaries

- Battery deliverable: 12 complete probe files inline; all requested mutant types covered.
- Exercised result: M12 killed; pristine/restored detector exits 0, mutant exit 1; exact restoration hashes above.
- Other 11 mutant verdicts: unrun, expected only. Four frozen coverage gaps are not silently assigned fictional killers.
- Later-round use requires a separately controlled/frozen redesign before scoring a C2 fix. No fix or counter change is supplied here.
- Tool installs/updates: none. Existing git, Python 3, timeout and sha256sum sufficed; no pacman transaction or other runtime/agent dispatch occurred.
