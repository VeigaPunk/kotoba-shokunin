# ExecInstancesA1 — frozen E2e instances (A1 guarded key form)

Date: 2026-10-23. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only; only this assigned report was written in the lane). Measurement revision: `a745411c66d4765e9ac0ce48f1d96c34f425dab4` (round-62 plan's r61 close tip). The probe obtains both the counter source and each page/SOURCES blob using `git show <revision>:<path>`; it imports that committed counter byte string and calls its functions. No counter or snapshot file was changed.

## Frozen instance literals and required verdicts

Canonical keys were derived by the committed counter's `canonical_scope_keys()` from the committed `corpus/SOURCES.md` at the same revision: Claude Code `paths`, VS Code `applyTo`, Copilot CLI `applyTo`, Cursor `globs`.

The two fresh instances are formed by appending one synthetic line to a copy of the committed S103 page. They are new A1 test inputs, not claims that those lines occur in the vendor snapshot.

```python
E2E_INSTANCES = [
    {
        "id": "E2e-bold-only-value",
        "client": "Claude Code",
        "key": "paths",
        "snapshot": ".ufo/waves/round-60/snapshots/S103.page",
        "append_line": "paths: **",
        "expected": "REJECT",
        "reason_substring": (
            "A1: scope key 'paths' is not in key form with a path-like glob"
        ),
    },
    {
        "id": "E2e-negated-key-within-60",
        "client": "Claude Code",
        "key": "paths",
        "snapshot": ".ufo/waves/round-60/snapshots/S103.page",
        "append_line": "Do not use paths: src/legacy/**/*.ts",
        "expected": "REJECT",
        "reason_substring": (
            "A1g: key 'paths' has no clean colon-form site with a path-like value "
            "at S103:665"
        ),
    },
]
```

The second reason substring is the expected A1g rejection form in the MutA1 §5 guarded proposal, with the actual fixture line number (665). The negator `not` begins 11 characters before `paths`, well inside the specified 60-character window. Both cases are canonical Claude Code keys; the first isolates the bold-marker value and the second isolates key polarity while retaining a path-like glob.

Benign controls requested, including both clients that use `applyTo`:

```python
BENIGN_CONTROLS = [
    {
        "id": "Claude-S103-198-199",
        "client": "Claude Code", "key": "paths", "line": 198,
        "line_text": "paths:",
        "next_line_text": '  - "src/api/**/*.ts"',
        "expected": "ACCEPT", "reason_substring": "none",
    },
    {
        "id": "Cursor-globs-mdc",
        "client": "Cursor", "key": "globs",
        "append_line": "globs: **/*.mdc",
        "expected": "ACCEPT", "reason_substring": "none",
    },
    {
        "id": "VS-Code-applyTo-S105-164",
        "client": "VS Code", "key": "applyTo", "line": 164,
        "line_text": "applyTo: '**/*.py'",
        "expected": "ACCEPT", "reason_substring": "none",
    },
    {
        "id": "Copilot-CLI-applyTo-S106-66",
        "client": "Copilot CLI", "key": "applyTo", "line": 66,
        "line_text": '   applyTo: "app/models/**/*.rb"',
        "expected": "ACCEPT", "reason_substring": "none",
    },
]
```

The Claude, VS Code, and Copilot inputs above are verbatim lines from the committed snapshots. Cursor's `globs: **/*.mdc` is a positive synthetic line appended to the committed S108 snapshot. The Claude test uses the real immediately following quoted YAML list value, exercising the key-line block lookahead rather than relocating the citation to the value line.

## Exact scratch probe and command

Scratch path: `/fast/scratch/hyaku/kotoba-r62/ExecInstancesA1/probe.py` (not a lane artifact). Full source used:

```python
from datetime import datetime, timezone
import hashlib
import subprocess
import types
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
REV = "a745411c66d4765e9ac0ce48f1d96c34f425dab4"

def git_show(path):
    return subprocess.check_output(["git", "show", f"{REV}:{path}"], cwd=ROOT)

counter_bytes = git_show("verifiers/check_scoped_rules.py")
mod = types.ModuleType("committed_check_scoped_rules")
mod.__file__ = f"{ROOT}/verifiers/check_scoped_rules.py@{REV}"
exec(compile(counter_bytes, mod.__file__, "exec"), mod.__dict__)

snapshots = {
    "S103": git_show(".ufo/waves/round-60/snapshots/S103.page").decode("utf-8").splitlines(),
    "S105": git_show(".ufo/waves/round-60/snapshots/S105.page").decode("utf-8").splitlines(),
    "S106": git_show(".ufo/waves/round-60/snapshots/S106.page").decode("utf-8").splitlines(),
    "S108": git_show(".ufo/waves/round-60/snapshots/S108.page").decode("utf-8").splitlines(),
}
sources = git_show("corpus/SOURCES.md").decode("utf-8")
keys = mod.canonical_scope_keys(sources)

print("date_utc=" + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
print("revision=" + REV)
print("counter_sha256=" + hashlib.sha256(counter_bytes).hexdigest())
for sid in ("S103", "S105", "S106", "S108"):
    blob = git_show(f".ufo/waves/round-60/snapshots/{sid}.page")
    print(f"{sid}_sha256=" + hashlib.sha256(blob).hexdigest())
print("canonical_keys=" + repr({k: sorted(v) for k, v in sorted(keys.items())}))


def assess(name, client, key, lines, line_no, value_probe, expected, reason):
    line = lines[line_no - 1]
    raw = None
    for _i, j in mod.key_occurrences(line, key):
        m = mod.KEY_SUFFIX_RE.match(line, j)
        if m is not None:
            raw = mod.value_after(lines, line_no, line[m.end():])
            if raw is not None:
                break
    membership = mod.a1_conjunct(client, key, keys)
    site_reasons = mod.scope_conjunct(lines, key, line_no)
    reasons = membership + site_reasons
    actual = "REJECT" if reasons else "ACCEPT"
    print(f"\n{name}")
    print("  client/key=" + repr((client, key)))
    print("  line=" + repr(line))
    print("  following_line=" + repr(lines[line_no] if line_no < len(lines) else None))
    print("  bound_value=" + repr(raw))
    print("  path_value(" + repr(value_probe) + ")=" + repr(mod.path_value(value_probe)))
    print("  path_site=" + repr(mod.path_site(lines, line_no, key)))
    print("  a1_conjunct=" + repr(membership))
    print("  scope_conjunct=" + repr(site_reasons))
    print("  combined_reasons=" + repr(reasons))
    print("  actual_verdict=" + actual)
    print("  expected_verdict=" + expected)
    print("  expected_reason_substring=" + repr(reason))


# Fresh mutant 1: append a bold-only value to the committed Claude snapshot.
s103_bold = list(snapshots["S103"])
bold_line = len(s103_bold) + 1
s103_bold.append("paths: **")
assess(
    "E2e-fresh-1-bold-marker",
    "Claude Code", "paths", s103_bold, bold_line, "**", "REJECT",
    "A1: scope key 'paths' is not in key form with a path-like glob",
)

# Fresh mutant 2: append a canonical key explicitly negated within 60 chars.
s103_negated = list(snapshots["S103"])
negated_line = len(s103_negated) + 1
s103_negated.append("Do not use paths: src/legacy/**/*.ts")
assess(
    "E2e-fresh-2-negated-within-60",
    "Claude Code", "paths", s103_negated, negated_line,
    " src/legacy/**/*.ts", "REJECT",
    f"A1g: key 'paths' has no clean colon-form site with a path-like value at S103:{negated_line}",
)

# Benign real Claude key plus its quoted block-list glob on the immediately following line.
s103 = snapshots["S103"]
claude_value = '  - "src/api/**/*.ts"'
assess(
    "control-claude-S103-198-199",
    "Claude Code", "paths", s103, 198, claude_value, "ACCEPT", "none",
)

# Benign Cursor key with requested glob; appended to the committed S108 bytes.
s108_cursor = list(snapshots["S108"])
cursor_line = len(s108_cursor) + 1
s108_cursor.append("globs: **/*.mdc")
assess(
    "control-cursor-globs-mdc",
    "Cursor", "globs", s108_cursor, cursor_line, " **/*.mdc", "ACCEPT", "none",
)

# Benign real VS Code and Copilot CLI applyTo key sites from committed snapshots.
assess(
    "control-vscode-S105-164",
    "VS Code", "applyTo", snapshots["S105"], 164, " '**/*.py'", "ACCEPT", "none",
)
assess(
    "control-copilot-S106-66",
    "Copilot CLI", "applyTo", snapshots["S106"], 66,
    ' "app/models/**/*.rb"', "ACCEPT", "none",
)
```

Executed (read-only):

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'; python3 -B /fast/scratch/hyaku/kotoba-r62/ExecInstancesA1/probe.py; rc=$?; printf 'python_exit=%s\n' "$rc"
```

Exact terminal output, 2026-10-23T20:52:03Z; Python exit code 0:

```text
2026-10-23T20:52:03Z
date_utc=2026-10-23T20:52:03Z
revision=a745411c66d4765e9ac0ce48f1d96c34f425dab4
counter_sha256=5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
S103_sha256=82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
S105_sha256=a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f
S106_sha256=00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
S108_sha256=884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
canonical_keys={'Claude Code': ['paths'], 'Copilot CLI': ['applyTo'], 'Cursor': ['globs'], 'VS Code': ['applyTo']}

E2e-fresh-1-bold-marker
  client/key=('Claude Code', 'paths')
  line='paths: **'
  following_line=None
  bound_value=' **'
  path_value('**')=False
  path_site=False
  a1_conjunct=[]
  scope_conjunct=["A1: scope key 'paths' is not in key form with a path-like glob at line 665"]
  combined_reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 665"]
  actual_verdict=REJECT
  expected_verdict=REJECT
  expected_reason_substring="A1: scope key 'paths' is not in key form with a path-like glob"

E2e-fresh-2-negated-within-60
  client/key=('Claude Code', 'paths')
  line='Do not use paths: src/legacy/**/*.ts'
  following_line=None
  bound_value=' src/legacy/**/*.ts'
  path_value(' src/legacy/**/*.ts')=True
  path_site=True
  a1_conjunct=[]
  scope_conjunct=[]
  combined_reasons=[]
  actual_verdict=ACCEPT
  expected_verdict=REJECT
  expected_reason_substring="A1g: key 'paths' has no clean colon-form site with a path-like value at S103:665"

control-claude-S103-198-199
  client/key=('Claude Code', 'paths')
  line='paths:'
  following_line='  - "src/api/**/*.ts"'
  bound_value='  - "src/api/**/*.ts"'
  path_value('  - "src/api/**/*.ts"')=True
  path_site=True
  a1_conjunct=[]
  scope_conjunct=[]
  combined_reasons=[]
  actual_verdict=ACCEPT
  expected_verdict=ACCEPT
  expected_reason_substring='none'

control-cursor-globs-mdc
  client/key=('Cursor', 'globs')
  line='globs: **/*.mdc'
  following_line=None
  bound_value=' **/*.mdc'
  path_value(' **/*.mdc')=True
  path_site=True
  a1_conjunct=[]
  scope_conjunct=[]
  combined_reasons=[]
  actual_verdict=ACCEPT
  expected_verdict=ACCEPT
  expected_reason_substring='none'

control-vscode-S105-164
  client/key=('VS Code', 'applyTo')
  line="applyTo: '**/*.py'"
  following_line='---'
  bound_value=" '**/*.py'"
  path_value(" '**/*.py'")=True
  path_site=True
  a1_conjunct=[]
  scope_conjunct=[]
  combined_reasons=[]
  actual_verdict=ACCEPT
  expected_verdict=ACCEPT
  expected_reason_substring='none'

control-copilot-S106-66
  client/key=('Copilot CLI', 'applyTo')
  line='   applyTo: "app/models/**/*.rb"'
  following_line='   ---'
  bound_value=' "app/models/**/*.rb"'
  path_value(' "app/models/**/*.rb"')=True
  path_site=True
  a1_conjunct=[]
  scope_conjunct=[]
  combined_reasons=[]
  actual_verdict=ACCEPT
  expected_verdict=ACCEPT
python_exit=0
```

## Result, limit, handoff

The first hostile instance is rejected by the committed functions, and all four benign controls are accepted (including Claude's real two-line case). The second hostile instance is **not rejected**: `a1_conjunct=[]`, `path_site=True`, `scope_conjunct=[]`, hence the current combined verdict is `ACCEPT` and no rejection reason is emitted. This is an observed E2e absorption gap: the committed `a1_conjunct`/`scope_conjunct`/`path_site` implementation does not contain the MutA1 G7 negation guard. The expected G7 reason is included above as a test oracle, not represented as output from the frozen code. This evidence does not support calling E2e absorbed; the L1 integration must account for the surviving instance or an authorized later counter change. This seat made no counter change and ran no build, lint, test suite, or formatter.

**Files changed:** `.ufo/waves/round-62/w1/ExecInstancesA1.md` only. Scratch probe: `/fast/scratch/hyaku/kotoba-r62/ExecInstancesA1/probe.py`.

Installs: no installs.
Blockers: frozen counter accepts the specified negated-key instance, contrary to E2e's expected guarded behavior.
Produced: two concrete hostile E2e instances and four benign controls, measured against revision `a745411c66d4765e9ac0ce48f1d96c34f425dab4`.
