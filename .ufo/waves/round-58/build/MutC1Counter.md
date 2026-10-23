Result: MIXED — 20 single-point mutants probed: 10 killed, 10 survived; every pristine/restored self-test passed and every mutant was restored byte-for-byte.

## Scope and method

- Axes: sensitivity to the new grammar/backing conjuncts; demonstrated survivor behavior; exact-byte restoration.

- Read-only lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Only this requested report was written there. All mutations and execution were in `/fast/scratch/hyaku/kotoba-r58/MutC1Counter`, cloned and checked out at frozen commit `3de87aad29e960c95ed35840442f424c48c29729`. No sandbox commits, pushes, subagents, source fetches or client model calls.

- Target: `verifiers/check_command_files.py`. All line references below are to its frozen bytes. Every mutant changes one behavior-bearing source line only; no self-test or contract changes.

- Detector for every pristine, mutated and restored stage (60 actual runs), cwd = sandbox above:

```sh
timeout 120 python3 -B verifiers/check_command_files.py --self-test
```

- Child environment removed `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`; set `TMPDIR=/fast/scratch/hyaku/kotoba-r58/MutC1Counter/.probe-tmp` and `PYTHONDONTWRITEBYTECODE=1`. Parent subprocess deadline was 125 seconds. All runs finished normally: no timeouts or baseline failures.

- Expected detector: `--self-test` should exit nonzero on each non-equivalent defect. Verdict uses that detector alone, not the auxiliary witness. Every witness also ran on pristine/mutated/restored bytes with the same Python executable under `timeout 15`; all 60 witness commands exited 0 and each demonstrated a behavior change that disappeared on restoration.

- These are self-test coverage findings against the frozen counter, not changes to the claim, population, targets or rules. No live `--fetch` predicate or measured F/G claim was run. C2 was not evaluated.

- Tooling: existing `python3 --version` printed `Python 3.14.8` (exit 0). No tool installed or updated.

## Restoration and provenance

`H0 = aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c` is the original frozen target SHA-256. Each per-mutant section records pristine/mutated/restored before/after hashes. The detector did not change its input in any stage. All 20 restored files matched the complete original byte string, not just a selected region.

Final independent commands and observed outputs (each exit 0):

```text
$ timeout 30 sha256sum verifiers/check_command_files.py
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  verifiers/check_command_files.py
$ timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git --no-optional-locks show 3de87aad29e960c95ed35840442f424c48c29729:verifiers/check_command_files.py | timeout 30 sha256sum
aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c  -
```

## Surviving mutants: concrete coverage gaps

### M04 — Permit a single dot-led segment

At-least-two segments (spec 78-80, 90-95; tests 1209-1216). Admits `.commands`, a single segment. Existing one-segment negatives also fail the leading-dot or final-word check, so they do not isolate segment count.

### M06 — Omit plural plugins from banned words

Every banned segment word (spec 96-99; tests 1227-1240). Admits `.claude-plugins/commands/`. The existing plugin negative uses singular `plugin`, not plural `plugins`.

### M07 — Omit singular skill from banned words

Every banned segment word (spec 96-99; tests 1227-1240). Admits `.claude/skill/commands/`. Existing skill negatives use plural `skills`, not singular `skill`.

### M08 — Check banned words only in non-final segments

Ban words in every segment, including final (spec 96-99). Admits `.claude/skill-commands/`. Existing banned-word negatives put the banned word in a non-final segment.

### M09 — Skip the first segment in the E7 dot check

E7 applies to the first non-final segment too (spec 100; tests 1241-1246). Admits `.claude.local/commands/`. The host-shaped first-segment negative `opencode.ai/docs/commands/` also fails leading-dot, so it does not isolate this E7 case.

### M11 — Allow a digit directly after a quoted/page token

Quote/page right boundary excludes digits (spec 142-145, 164-169; tests 1306-1311, 1684-1693). Finds `.claude/commands` inside `.claude/commands1`: quote span becomes [31,47] and page_found becomes true. Existing quote/page right-boundary negatives cover letters, hyphen and underscore, not a digit.

### M14 — Drop word boundaries from the outside command-word regex

Outside-span keyword must be a whole word (spec 144-145; tests 1288-1299, 1486-1493). Accepts `Keep .claude/commands/ files for commanders to reuse` as having an outside command/prompt word, because `command` is found inside `commanders`. The 8-word quote has no standalone outside keyword.

### M16 — Ignore token-sharing rows with an empty client name

E5 includes any client cell (spec 13-15, 137-138; implementation 666-674; tests 1563-1580). An otherwise-backed Claude Code row is now backed despite a second row with an empty client cell using `.claude/commands/`. Pristine/restored judge returns a sharing rejection. The existing unlisted-client case uses non-empty `Zed`.

### M19 — Admit a hyphen as a held left boundary

Held left boundary is an explicit allow-list (spec 174-178; tests 1697-1715). Wrongly treats `x-.claude/commands` as held. This is a false-held result: it can suppress new ground, not inflate it. The separate page-boundary hyphen test does not exercise HELD_PREV.

### M20 — Lowercase instead of casefold the held text

Held text must be casefolded (spec 173-179; tests 1716-1723). Misses a held `.claude/commandſ` (last letter U+017F LATIN SMALL LETTER LONG S): pristine/restored held=true and new_ground=0; mutant held=false and new_ground=1. The ASCII command token remains valid. Existing case tests distinguish ASCII case only, where lower() and casefold() agree.

## Per-mutant receipts

All detector stdout below is verbatim; stderr was empty for all 60 runs. `P` = pristine, `M` = mutated, `R` = restored. `H0` is the full hash above; P/R before and after were independently hashed on every run. All P/R outputs were `self-test: 0 failure(s) over 244 assertions`; the full emitted counter hash is included below as well.

### M01 — KILLED — Omit singular command from the final word set

- Mutation point: `verifiers/check_command_files.py:290`.

- Expected detector assertions: `verifiers/check_command_files.py:1189-1190: green singular word`.

- Exact one-line substitution:

```python
# original
COMMAND_WORDS = ("command", "commands", "prompt", "prompts")
# mutant
COMMAND_WORDS = ("commands", "prompt", "prompts")
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `f9ee73865abd7a1f8149f4f440398a4eaa1248dc854b9dcf91a0fe6317428f5d`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:10:26.940455+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:12:01.118606+00:00; exit 1:

```text
counter sha256 f9ee73865abd7a1f8149f4f440398a4eaa1248dc854b9dcf91a0fe6317428f5d
FAIL green: the singular word counts: got False, expected True
self-test: 1 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:12:06.759671+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.cursor/command/')
```


Witness P/M/R (all exit 0):

```text
pristine: true
mutated: false
restored: true
```

### M02 — KILLED — Admit commanders as a final word

- Mutation point: `verifiers/check_command_files.py:290`.

- Expected detector assertions: `verifiers/check_command_files.py:1223-1224: red commanders`.

- Exact one-line substitution:

```python
# original
COMMAND_WORDS = ("command", "commands", "prompt", "prompts")
# mutant
COMMAND_WORDS = ("command", "commands", "prompt", "prompts", "commanders")
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `53065d55e91c7ce50c9f1c407dbf915511cef23bcaf5320c89dd0e08bc6c1678`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:12:06.902597+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:12:16.134910+00:00; exit 1:

```text
counter sha256 53065d55e91c7ce50c9f1c407dbf915511cef23bcaf5320c89dd0e08bc6c1678
FAIL red final segment: .claude/commanders/ is not the word: got True, expected False
self-test: 1 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:12:22.181987+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude/commanders/')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M03 — KILLED — Search any segment, not just the final segment

- Mutation point: `verifiers/check_command_files.py:587`.

- Expected detector assertions: `verifiers/check_command_files.py:1225-1226: final segment only`.

- Exact one-line substitution:

```python
# original
    if not any(w in COMMAND_WORDS for w in seg_words(parts[-1])):
# mutant
    if not any(w in COMMAND_WORDS for seg in parts for w in seg_words(seg)):
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `e188c0ea431d89d011a41e908aa0855066d9515b928c7639acf69fa354155346`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:12:22.323931+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:12:27.463592+00:00; exit 1:

```text
counter sha256 e188c0ea431d89d011a41e908aa0855066d9515b928c7639acf69fa354155346
FAIL red final segment: .claude/commands/plan.md (the word is not final): got True, expected False
self-test: 1 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:12:37.801806+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude/commands/plan.md')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M04 — SURVIVED — Permit a single dot-led segment

- Mutation point: `verifiers/check_command_files.py:583`.

- Expected detector assertions: `verifiers/check_command_files.py:1209-1216: segment-count red cases`.

- Exact one-line substitution:

```python
# original
    if len(parts) < 2 or not parts[0].startswith("."):
# mutant
    if len(parts) < 1 or not parts[0].startswith("."):
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `4b209061919a3fc2bb193736bc488f12871f20ec6cf52cd18835f3cc29de3700`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:12:37.958669+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:12:43.196635+00:00; exit 0:

```text
counter sha256 4b209061919a3fc2bb193736bc488f12871f20ec6cf52cd18835f3cc29de3700
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:12:48.310331+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.commands')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M05 — KILLED — Drop the leading-dot requirement

- Mutation point: `verifiers/check_command_files.py:583`.

- Expected detector assertions: `verifiers/check_command_files.py:1217-1220: leading-dot red cases`.

- Exact one-line substitution:

```python
# original
    if len(parts) < 2 or not parts[0].startswith("."):
# mutant
    if len(parts) < 2:
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `20aac7b217e8c346691b943e346e42f8c489d85d4aa866bb21df3ec0527ac966`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:12:48.453559+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:12:57.430722+00:00; exit 1:

```text
counter sha256 20aac7b217e8c346691b943e346e42f8c489d85d4aa866bb21df3ec0527ac966
FAIL red first segment: commands/prompts does not start with a dot: got True, expected False
FAIL red first segment: claude/commands does not start with a dot: got True, expected False
self-test: 2 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:13:03.077679+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('claude/commands')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M06 — SURVIVED — Omit plural plugins from banned words

- Mutation point: `verifiers/check_command_files.py:292`.

- Expected detector assertions: `verifiers/check_command_files.py:1227-1240: banned segment words`.

- Exact one-line substitution:

```python
# original
                               "rules", "plugin", "plugins", "extension",
# mutant
                               "rules", "plugin", "extension",
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `c65dbc4078ee10ca85fb7d0769d0f814d3422995683c3eea8e25fadf94ee8ff4`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:13:03.201608+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:13:08.389467+00:00; exit 0:

```text
counter sha256 c65dbc4078ee10ca85fb7d0769d0f814d3422995683c3eea8e25fadf94ee8ff4
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:13:13.627582+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude-plugins/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M07 — SURVIVED — Omit singular skill from banned words

- Mutation point: `verifiers/check_command_files.py:291`.

- Expected detector assertions: `verifiers/check_command_files.py:1227-1240: banned segment words`.

- Exact one-line substitution:

```python
# original
NOT_COMMAND_WORDS = frozenset(("skill", "skills", "agent", "agents", "rule",
# mutant
NOT_COMMAND_WORDS = frozenset(("skills", "agent", "agents", "rule",
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `795113943962c4d1a0a34d950640db1afbc2b1159b8fe0aa12722e7a4abb8b8f`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:13:13.800904+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:13:19.162254+00:00; exit 0:

```text
counter sha256 795113943962c4d1a0a34d950640db1afbc2b1159b8fe0aa12722e7a4abb8b8f
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:13:25.368006+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude/skill/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M08 — SURVIVED — Check banned words only in non-final segments

- Mutation point: `verifiers/check_command_files.py:589`.

- Expected detector assertions: `verifiers/check_command_files.py:1227-1240: banned segment words`.

- Exact one-line substitution:

```python
# original
    return not any(w in NOT_COMMAND_WORDS for seg in parts for w in seg_words(seg))
# mutant
    return not any(w in NOT_COMMAND_WORDS for seg in parts[:-1] for w in seg_words(seg))
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `59ce0a6bdf0521c045ae7847f1a0ace2b045b1ffa693206508fd62c4d2eb2dc7`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:13:25.505329+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:13:38.305894+00:00; exit 0:

```text
counter sha256 59ce0a6bdf0521c045ae7847f1a0ace2b045b1ffa693206508fd62c4d2eb2dc7
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:13:46.949299+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude/skill-commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M09 — SURVIVED — Skip the first segment in the E7 dot check

- Mutation point: `verifiers/check_command_files.py:585`.

- Expected detector assertions: `verifiers/check_command_files.py:1241-1246: E7 red cases`.

- Exact one-line substitution:

```python
# original
    if any("." in seg[1:] for seg in parts[:-1]):
# mutant
    if any("." in seg[1:] for seg in parts[1:-1]):
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `25309a2cb777116051679464ad6a6f9620029e0de00f33cb30feb96db7000e9b`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:13:47.080354+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:13:56.629987+00:00; exit 0:

```text
counter sha256 25309a2cb777116051679464ad6a6f9620029e0de00f33cb30feb96db7000e9b
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:14:02.037597+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_well_formed('.claude.local/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M10 — KILLED — Use substring lookup for a quote span

- Mutation point: `verifiers/check_command_files.py:624`.

- Expected detector assertions: `verifiers/check_command_files.py:1306-1309: quote path boundaries`.

- Exact one-line substitution:

```python
# original
        i = first_boundary(text, form)
# mutant
        i = text.find(form)
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `ba9b8f361a8b5c9c3557ff1c635e261041ce7168b4d4e03b87748e0b8fb6354e`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:14:02.185293+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:14:07.282968+00:00; exit 1:

```text
counter sha256 ba9b8f361a8b5c9c3557ff1c635e261041ce7168b4d4e03b87748e0b8fb6354e
FAIL a token inside a longer path is not spanned (left boundary): got (1, 18), expected None
FAIL a token followed by a word is not spanned (right boundary): got (0, 16), expected None
self-test: 2 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:14:13.672562+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_span('x.claude/commands/ here', '.claude/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: null
mutated: [1, 18]
restored: null
```

### M11 — SURVIVED — Allow a digit directly after a quoted/page token

- Mutation point: `verifiers/check_command_files.py:876`.

- Expected detector assertions: `verifiers/check_command_files.py:1306-1311 and 1684-1693: quote/page right boundary`.

- Exact one-line substitution:

```python
# original
        right_ok = j >= len(text) or not (text[j] in ASCII_ALNUM or text[j] in "_-")
# mutant
        right_ok = j >= len(text) or not (text[j] in string.ascii_letters or text[j] in "_-")
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `35261698018f91ab347c3e58564ca6be1a3c79b7c6d441dac3b78184671a32f1`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:14:13.826771+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:14:19.364580+00:00; exit 0:

```text
counter sha256 35261698018f91ab347c3e58564ca6be1a3c79b7c6d441dac3b78184671a32f1
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:14:24.809986+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
{'quote_span': m.token_span('These custom command files use .claude/commands1 today', '.claude/commands'), 'page_found': m.found_on_page('<p>These custom command files use .claude/commands1 today</p>', 'These custom command files use .claude/commands1 today', '.claude/commands')}
```


Witness P/M/R (all exit 0):

```text
pristine: {"page_found": false, "quote_span": null}
mutated: {"page_found": true, "quote_span": [31, 47]}
restored: {"page_found": false, "quote_span": null}
```

### M12 — KILLED — Casefold the quote-token lookup

- Mutation point: `verifiers/check_command_files.py:624`.

- Expected detector assertions: `verifiers/check_command_files.py:1300-1302: case-sensitive quote token`.

- Exact one-line substitution:

```python
# original
        i = first_boundary(text, form)
# mutant
        i = first_boundary(text.casefold(), form.casefold())
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `fab8f33dc4ced946ecac8a4935044c43b24afcc3311d25a0a23991f034baaedc`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:14:24.942993+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:14:30.474098+00:00; exit 1:

```text
counter sha256 fab8f33dc4ced946ecac8a4935044c43b24afcc3311d25a0a23991f034baaedc
FAIL the token match is case-sensitive: got (0, 17), expected None
self-test: 1 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:14:36.260573+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.token_span('.Claude/Commands/ is used', '.claude/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: null
mutated: [0, 17]
restored: null
```

### M13 — KILLED — Use end instead of start for the outside-word left limit

- Mutation point: `verifiers/check_command_files.py:635`.

- Expected detector assertions: `verifiers/check_command_files.py:1296-1299 and 1486-1493: token-only command word`.

- Exact one-line substitution:

```python
# original
        if m.end() <= start or m.start() >= end:
# mutant
        if m.end() <= end or m.start() >= end:
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `8419e8d85e712619d257ccc21c2633b9276f7a3706d549adbdb89579f12dd62b`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:14:36.391711+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:14:41.813001+00:00; exit 1:

```text
counter sha256 8419e8d85e712619d257ccc21c2633b9276f7a3706d549adbdb89579f12dd62b
FAIL only the token carries the command word: got True, expected False
FAIL a quote with only the token's own command word is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
self-test: 2 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:14:48.266617+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
outside('The folder lives at .claude/commands/ for reuse')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M14 — SURVIVED — Drop word boundaries from the outside command-word regex

- Mutation point: `verifiers/check_command_files.py:298`.

- Expected detector assertions: `verifiers/check_command_files.py:1288-1299 and 1486-1493: outside keyword`.

- Exact one-line substitution:

```python
# original
COMMAND_WORD_RE = re.compile(r"\b(?:commands?|prompts?)\b", re.IGNORECASE)
# mutant
COMMAND_WORD_RE = re.compile(r"(?:commands?|prompts?)", re.IGNORECASE)
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `4fdee19a1146a798f3dc9cc274104ad7a9aaced6e40c0a27e5f2df34bf5de842`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:14:48.392826+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:14:53.157222+00:00; exit 0:

```text
counter sha256 4fdee19a1146a798f3dc9cc274104ad7a9aaced6e40c0a27e5f2df34bf5de842
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:00.183552+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
outside('Keep .claude/commands/ files for commanders to reuse')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M15 — KILLED — Require three token sharers instead of two

- Mutation point: `verifiers/check_command_files.py:779`.

- Expected detector assertions: `verifiers/check_command_files.py:1563-1575: shared tokens`.

- Exact one-line substitution:

```python
# original
                if len(sharers) >= 2:
# mutant
                if len(sharers) >= 3:
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `968dcb1f84b5255f3e90de2634cea7a101889c3cdd581db3380b26c2fa1ed266`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:15:00.311529+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:15:05.553572+00:00; exit 1:

```text
counter sha256 968dcb1f84b5255f3e90de2634cea7a101889c3cdd581db3380b26c2fa1ed266
FAIL E5: a token shared with another client disqualifies both rows: got [], expected ['Gemini CLI', 'Cursor']
FAIL E5: the sharing disqualifies the otherwise-backed row: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
FAIL E5: sharing is judged on casefold(normalise()): got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL E5: a row of an unlisted client name also counts as a user: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code']
self-test: 4 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:10.831058+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
world('Cursor', '.claude/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Cursor"]}
mutated: {"backed": true, "why": []}
restored: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Cursor"]}
```

### M16 — SURVIVED — Ignore token-sharing rows with an empty client name

- Mutation point: `verifiers/check_command_files.py:673`.

- Expected detector assertions: `verifiers/check_command_files.py:1563-1580: any client cell`.

- Exact one-line substitution:

```python
# original
        if spans:
# mutant
        if spans and client_name(r[0]):
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `6c69b32881d1c09a65ff11f093ff972994fb3ab961ec4ab38605e3bd39cfda42`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:15:10.962228+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:15:15.958007+00:00; exit 0:

```text
counter sha256 6c69b32881d1c09a65ff11f093ff972994fb3ab961ec4ab38605e3bd39cfda42
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:21.072833+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
world('', '.claude/commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows , Claude Code"]}
mutated: {"backed": true, "why": []}
restored: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows , Claude Code"]}
```

### M17 — KILLED — Drop casefold when collecting E5 users

- Mutation point: `verifiers/check_command_files.py:674`.

- Expected detector assertions: `verifiers/check_command_files.py:1570-1572: E5 casefold(normalise())`.

- Exact one-line substitution:

```python
# original
            users.setdefault(normalise(spans[0]).casefold(), set()).add(client_name(r[0]))
# mutant
            users.setdefault(normalise(spans[0]), set()).add(client_name(r[0]))
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `b7a42dc3bc65ec07ba27264ba2016e0c8af286738f063ef041682ea8c945828a`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:15:21.204704+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:15:26.323507+00:00; exit 1:

```text
counter sha256 b7a42dc3bc65ec07ba27264ba2016e0c8af286738f063ef041682ea8c945828a
FAIL E5: sharing is judged on casefold(normalise()): got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
self-test: 1 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:32.232841+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
world('Codex', '~/.Claude/Commands/')
```


Witness P/M/R (all exit 0):

```text
pristine: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Codex"]}
mutated: {"backed": true, "why": []}
restored: {"backed": false, "why": ["SKILL.md command token '.claude/commands/' is shared by rows Claude Code, Codex"]}
```

### M18 — KILLED — Use slash instead of dot for the held right-suffix exclusion

- Mutation point: `verifiers/check_command_files.py:1028`.

- Expected detector assertions: `verifiers/check_command_files.py:1724-1737: held dot-word suffix`.

- Exact one-line substitution:

```python
# original
    if c == "." and j + 1 < len(line) and line[j + 1] in ASCII_ALNUM:
# mutant
    if c == "/" and j + 1 < len(line) and line[j + 1] in ASCII_ALNUM:
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `2fe25a3ee644d05c8fdd94231e2c78dfee3b8da812a3ac70806136df7b796685`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/1/0`.


pristine; started UTC 2026-10-23T08:15:32.386643+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:15:39.576981+00:00; exit 1:

```text
counter sha256 2fe25a3ee644d05c8fdd94231e2c78dfee3b8da812a3ac70806136df7b796685
FAIL held: the round-56 memory-file analogue does not hold it: got True, expected False
FAIL held: a .md suffix does not hold the bare token: got True, expected False
FAIL held: a dot before a letter does not hold it: got True, expected False
self-test: 3 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:45.161286+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.held_in_text('.claude/commands.md', '.claude/commands')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M19 — SURVIVED — Admit a hyphen as a held left boundary

- Mutation point: `verifiers/check_command_files.py:303`.

- Expected detector assertions: `verifiers/check_command_files.py:1697-1715: held left boundary`.

- Exact one-line substitution:

```python
# original
HELD_PREV = frozenset("`\"'([</~=")
# mutant
HELD_PREV = frozenset("`\"'([</~=-")
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `d8446cd4301463a2a93037f2c4eca39f1742c95fbe636f235797e07e8af755a4`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:15:45.320065+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:15:50.452811+00:00; exit 0:

```text
counter sha256 d8446cd4301463a2a93037f2c4eca39f1742c95fbe636f235797e07e8af755a4
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:15:55.813750+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
m.held_in_text('x-.claude/commands', '.claude/commands')
```


Witness P/M/R (all exit 0):

```text
pristine: false
mutated: true
restored: false
```

### M20 — SURVIVED — Lowercase instead of casefold the held text

- Mutation point: `verifiers/check_command_files.py:1007`.

- Expected detector assertions: `verifiers/check_command_files.py:1716-1723: held case folding`.

- Exact one-line substitution:

```python
# original
    for line in text.casefold().splitlines():
# mutant
    for line in text.lower().splitlines():
```

- Hashes: P-before = P-after = R-before = R-after = `H0`; M-before = M-after = `7c10f0ddbd9bd4e774978d4012970aedbe03ec4e667f87b0e6965a32f0a8c2c6`. Restored bytes equal original: yes.

- Exit codes P/M/R: `0/0/0`.


pristine; started UTC 2026-10-23T08:15:55.946350+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


mutated; started UTC 2026-10-23T08:16:00.939803+00:00; exit 0:

```text
counter sha256 7c10f0ddbd9bd4e774978d4012970aedbe03ec4e667f87b0e6965a32f0a8c2c6
self-test: 0 failure(s) over 244 assertions
```


restored; started UTC 2026-10-23T08:16:11.437305+00:00; exit 0:

```text
counter sha256 aae12d36e974cda3882016f001fa54b6d004cfc1fcd8810ebde2beafc6fb4d4c
self-test: 0 failure(s) over 244 assertions
```


Auxiliary witness expression (see exact shared prefix below):

```python
{'held': m.held_in_text('.claude/commandſ', '.claude/commands'), 'new_ground': m.new_ground(['.claude/commands'], {'.claude/commands': m.held_in_text('.claude/commandſ', '.claude/commands')})}
```


Witness P/M/R (all exit 0):

```text
pristine: {"held": true, "new_ground": 0}
mutated: {"held": false, "new_ground": 1}
restored: {"held": true, "new_ground": 0}
```

## Witness reproducibility

Actual witness subprocess argv was `["timeout", "15", "python3", "-B", "-c", prefix + "\nprint(json.dumps(" + expression + ", ensure_ascii=False, sort_keys=True))\n"]`, with the same sandbox cwd/environment. `expression` is pasted in each receipt; the exact shared `prefix` was:

```python
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location('mutation_target', Path('verifiers/check_command_files.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
def outside(q):
    span = m.token_span(q, '.claude/commands/')
    return m.command_word_outside(q, *span)
def world(other, other_token):
    skill = ('### Custom command files by client\n\n| Client | Command files | What a file sets | Action |\n|---|---|---|---|\n'
             '| Claude Code | `.claude/commands/` | a reusable prompt | read it before the skill |\n'
             + '| ' + other + ' | `' + other_token + '` | a reusable prompt | read it before the skill |\n')
    quote = 'Claude reads a custom slash command from a .claude/commands/ file'
    entry = '| Client | Command files | Source | Quote |\n|---|---|---|---|\n| Claude Code | .claude/commands/ | S900 | "' + quote + '" |\n'
    sources = '| S900 | Claude Code docs — https://code.claude.com/docs/en/slash-commands.md | docs | A | the command folder | § commands | the command folder | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |\n'
    lesson = '## Gate\n\n' + quote + '\n'
    row = m.judge(skill, entry, sources, lesson, '')[0]
    return {'backed': row['backed'], 'why': row['why']}
```

## Disposition

Stopped after the assigned 20 probes. The frozen counter and its contract are unchanged; its source is restored exactly. Ten surviving mutants are coverage findings, including both false acceptance and the explicitly identified false-held case. No repair, integration or claim adjudication was attempted.
