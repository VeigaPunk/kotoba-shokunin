# ExecOC5 — OC-5 re-derivation on opencode v2.1.4 (round 72, wave 1 build)

**Verdict: OC-5 is honestly re-derivable on the opencode v2.1.4 bytes — the
resolution-switch behavior is witnessed in a new shape. Replacement rule written
in scratch and delivered; same-token decoys rejected; nothing loosened.**

Deliverables: `.ufo/waves/round-72/w1/build/ExecOC5/verify_surfaces.py`
(scratch copy), `.ufo/waves/round-72/w1/build/ExecOC5/rule.diff` (46-line
unified diff against `verifiers/verify_surfaces.py`).

## 1. Committed OC-5 as run on the v2.1.4 dump (step 1)

Command:

```
python3 -B - <<'EOF'
import importlib.util, json
spec = importlib.util.spec_from_file_location("vs", "verifiers/verify_surfaces.py")
vs = importlib.util.module_from_spec(spec); spec.loader.exec_module(vs)
dump = open("/tmp/k72-oc-strings.txt", encoding="utf-8", errors="replace").read()
ids, report = vs.extract_opencode_classes(dump)
print("CLASS IDS:", sorted(ids))
print(json.dumps(report, indent=1))
EOF
```

Observed output (relevant row):

```
"rule_id": "OC-5", "owns": [], "matched": false,
"missing": ["OPENCODE_DISABLE_PROJECT_CONFIG",
            "globUp(<v>.directory,<v>.worktree)",
            "globUp(<v>.config,<v>.config)"]
```

Full CLI (same result as the plan's Q19 baseline row):

```
timeout 280 python3 -B verifiers/verify_surfaces.py --opencode-strings /tmp/k72-oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
```

Observed output (verbatim, byte-exact from the run):

```
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: ... OC-5 (owns no class id (shape witness); missing OPENCODE_DISABLE_PROJECT_CONFIG + globUp(<v>.directory,<v>.worktree) + globUp(<v>.config,<v>.config)); OC-6 ...
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=1
```

(Full untruncated `opencode_extract` detail captured in artifact 43314.)

## 2. The v2.1.4 witness of what OC-5 was written to see (step 2)

The rule witnesses *the resolution switch that decides where OC-1's names are
read from — project walk-up versus config-only*. In v2.1.4 that behavior lives
in two places:

**(a) Env gate read** — dump line **702021** (found with
`grep -n -F "OPENCODE_DISABLE_PROJECT_CONFIG" /tmp/k72-oc-strings.txt`).
The config object folds both env names into a `.project` flag. Located quote
(≤25 words, copied from the fetched bytes):

```
project:!D(process.env.OPENCODE_CONFIG_PROJECT_DISABLE??process.env.OPENCODE_DISABLE_PROJECT_CONFIG)
```

Dropped bytes: preceding `config:{directory:process.env.OPENCODE_CONFIG_DIR,` and
following `,claude:!(D(process.env.OPENCODE_DISABLE_CLAUDE_CODE)…`. The two
env literals also appear side by side in the env-name table at dump lines
**671290 (OPENCODE_CONFIG_PROJECT_DISABLE)** and **671291
(OPENCODE_DISABLE_PROJECT_CONFIG)**.

**(b) The match switch** — dump line **708687** (found with
`grep -n -F "globUp" /tmp/k72-oc-strings.txt`), inside the
`ConfigInstructionPlugin.match` registration (the only `globUp(` call in the
whole dump; two other `globUp` occurrences are the `FileSystem.globUp`
service-name strings at lines 662143/662146 and the service definition at
701613). Located quote (≤25 words, copied from the fetched bytes):

```
if(C)return yield*l.globUp(Ae,T,N);if(!a.global)return[];return yield*l.scan(Ae,{...ye,cwd:r.config})
```

Dropped bytes: enclosing `ee=c("ConfigInstructionPlugin.match")(function*(we){let Ae=…` and trailing `.pipe(Qe(()=>[]))})`. The `C` gate is bound earlier in the same chunk as `C=a.project&&Ce.contains(N,T)` where `T=yield*l.resolve(_.directory)` (project directory) and `N=yield*l.resolve(_.project.directory)` (worktree) — i.e. project-config enablement AND inside the project. That is the walk-up-vs-config-only contrast the old `globUp(<v>.directory,<v>.worktree)` vs `globUp(<v>.config,<v>.config)` anchors used to carry.

## 3. Replacement rule (step 3)

The replacement keeps OC-5 fail-closed (absent anchor → unmatched → FAIL) and
keeps `owns []` (shape witness). It re-anchors on:

- env gate canonical literal `OPENCODE_CONFIG_PROJECT_DISABLE` (the v2.1.4
  name; the legacy `OPENCODE_DISABLE_PROJECT_CONFIG` alias is still read in the
  same expression and noted in the comment, but is no longer the gate name), and
- the switch shape anchored on the `"ConfigInstructionPlugin.match"` label, so a
  same-token shape in a *non-instruction-loading* role cannot satisfy it:
  `ConfigInstructionPlugin.match` → `globUp` call → `if(!<v>.global)return[];`
  guard → `scan(...,{cwd:<v>.config})` fallback.

## 4. Decoy rejection (same tokens, no instruction-loading role)

All tested by running the scratch `extract_opencode_classes` on dumps carrying
the same tokens (env literals + full witness body) with one property changed:

| decoy | change | OC-5 matched |
|---|---|---|
| exact witness fragment | none | **True** |
| A: label swapped | `"ConfigInstructionPlugin.match"` → `"FormatterPlugin.match"` (identical body) | False |
| B: reordered | config-scan before globUp, `.global` guard moved after | False |
| C: cwd not config | `cwd:r.config` → `cwd:td.dirname(Ae)` | False |
| D: guard dropped | `if(!a.global)return[];` removed | False |

Decoy A was additionally shown rejected on the **real** dump (label replaced in
the 28 MB dump): OC-5 unmatched with both anchors in `missing`. Decoy B/D also
fail on the real-dump basis by construction (the regex requires the exact
sequence).

## 5. Scratch verifier run, per-check (step 4)

Command:

```
timeout 280 python3 -B verify_surfaces.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --opencode-strings /tmp/k72-oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
```

(ran from `.ufo/waves/round-72/w1/build/ExecOC5/`; `--repo` needed because the
scratch copy's default repo resolution is its own grandparent). Observed output:

```
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: vacuity: ... OC-1 ...; OC-2 ...; OC-3a ...; OC-3b ...; OC-4 ...; OC-6 ...   [OC-5 NO LONGER in the unmatched list]
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=1
```

OC-5 report row from the scratch module on the real dump:

```
{"rule_id": "OC-5", "owns": [], "matched": true,
 "anchors": ["OPENCODE_CONFIG_PROJECT_DISABLE",
             "ConfigInstructionPlugin.match: globUp walk-up vs scan(cwd:config)"],
 "missing": []}
```

The remaining `opencode_extract` FAIL is the expected vacuity plus the other six
rules (OC-1/2/3a/3b/4/6), which are other seats'/L1 scope. So of the 7 OC
rules, on v2.1.4 this seat's honest count is **1 of 7** (OC-5).

## 6. Risks / notes for the L1

- **The shared dumps vanished during wave 1.** `/tmp/k72-oc-strings.txt` and
  `/tmp/k72-omp-strings.txt` existed at my start (sha256 `020fb253…` /
  `953b19df…`, both verified then) and were gone by ~18:39 local. All evidence
  above was captured before removal. Wave-2 seats that need a dump must
  re-dump with `strings -n 4` from `/home/vgpnk/.opencode/bin/opencode` and
  `~/.local/bin/omp.real`; if the re-dump's fingerprint differs, line numbers
  may shift — re-locate anchors before trusting them.
- The scratch OC-5 anchors are structural and label-bound; if a later rebuild
  renames the `ConfigInstructionPlugin.match` service label, the rule will fail
  closed (correct behavior) and must be re-derived.
- No tools installed; no git writes; no lane/committed files modified; process
  bounds respected (single long command run alone with wall time recorded;
  parallel batches otherwise). Scratch dir `/tmp/k72w1-ExecOC5` removed before
  return.
