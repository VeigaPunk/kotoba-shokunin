verdict: PARTIAL — OC-2 (`verifiers/verify_surfaces.py` 376–382, 457–467) on the real frozen opencode-1.19.3 dump: anchor removal/corruption holds (19/19 killed); liveness and census-gate mutants survive (9/37); equivalent quote/variable/resolve/optional-chain forms false-red (5/37).

Pinned: 7ad7fadfc09354b74fb66605dfb0c1182c115a2f (scratch clone `/fast/scratch/kotoba-r47/w2/W2DropOC2-2/kotoba-shokunin`, HEAD verified). Line numbers below are at 7ad7fad unless marked "candidate".

## Setup and controls

- Frozen dump copied to scratch; sha256 `f4d8f34a…97bc3` = SHA256SUMS. Reproduces from the snapshot binary: `strings -n 4 bin/opencode-1.19.3 | sha256sum` → `f4d8f34a…`; binary sha `179ca421…` = SHA256SUMS.
- Both OC-2 anchors occur exactly once, on dump line 443993: `X.join(r.config,"AGENTS.md")` at byte 10893058 and `X.join(r.home,".claude","CLAUDE.md")` at byte 10893118. `.config,"AGENTS.md"` also occurs at line 445482 as OC-6's `jX(L.config,"AGENTS.md")`, which is not a `.join(` match and is correctly not counted by OC-2.
- Verifier: `python3 verifiers/verify_surfaces.py --opencode-strings <mutant> --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` (all default checks). Control on the unmodified frozen dump: exit 0, all 7 PASS, `opencode extraction 9/9 declared class(es) from 7/7 rules`.
- `--self-test` at 7ad7fad: exit 0, `0 failure(s) over 99 assertions`.
- Harness: `mutate_oc2.py` (saved as `W2DropOC2.mutate_oc2.txt`). 37 one-at-a-time mutants of the real dump, 4 workers, about 45 s, exit 0.

## Results (37 mutants)

| group | ids | observed | count |
|---|---|---|---|
| removal | A1 drop config anchor, A2 drop home anchor, A3 drop both | exit 1, `FAIL surfaces.opencode_extract`, owned classes named | 3 KILLED |
| config corruption | B1 `.concat`, B2 receiver `cfgdir`, B3 `.mdx`, B4 `.MD`, B5 `AGENTS_.md`, B6 embedded space, B7 Cyrillic homoglyph | exit 1, named | 7 KILLED |
| home corruption | C1 `.concat`, C2 `homedir`, C3 `.claud`, C4 no dot, C5 `.mdx`, C6 `.MD`, C7 `CLAUDE_CODE.md` | exit 1, named | 7 KILLED |
| additions | D1 undeclared `config/CLAUDE.md` at EOF, D2 undeclared `codex-home/AGENTS.md` at EOF | exit 1, undeclared id named | 2 KILLED |
| renamed-equivalent | E1 receiver `Zq`, E2 receiver `$r`, E3 whitespace | exit 0 | 3 ACCEPTED |
| equivalent forms | E4 single quotes, E5 template literals, E6 literal via variable, E7 `join`→`resolve`, E8 `r?.config` | exit 1 | 5 FALSE-RED |
| liveness/textual | L1 dead `!1&&` (config), L2 dead `!1&&` (home), L3 config commented out, L4 both dead, L5 config moved to EOF, L6 home moved to EOF | exit 0 | 6 SURVIVED |
| gate | G2 home gate removed, G3 home gate inverted | exit 0 | 2 SURVIVED |
| gate, adjacent OC-1 | G1 OC-1 gate removed from the priority array | exit 0 | 1 SURVIVED |
| control | unmodified | exit 0 | ACCEPTED |

Across all 37 runs the only FAIL lines are `surfaces.opencode_extract` (24 lines = 19 kills + 5 false-reds). No other check reacts to any OC-2 mutation.

## Findings

### F1 — SURVIVED (L1–L6): the rule is a presence test, so dead, commented, or relocated anchors pass (too wide)

Exit 0 with `PASS surfaces.opencode_extract: opencode extraction 9/9 … 7/7 rules`. Mutant deltas (dump line 443993):
- L1: `n=[X.join(r.config,"AGENTS.md"),` → `n=[!1&&X.join(r.config,"AGENTS.md"),` (offset 10893055). `!1&&` short-circuits, so the candidate is never evaluated.
- L2: `?[X.join(r.home,".claude","CLAUDE.md")]:[]` → `?[!1&&X.join(r.home,".claude","CLAUDE.md")]:[]`.
- L3: `X.join(r.config,"AGENTS.md")` → `/*X.join(r.config,"AGENTS.md")*/void 0`.
- L4: L1 + L2.
- L5: the config call deleted in place and an identical call appended at EOF.
- L6: the home call deleted in place and an identical call appended at EOF.

Cause: `extract_opencode_classes` uses `OC_CONFIG_JOIN_RE.findall(dump)` and `OC_HOME_DIR_JOIN_RE.findall(dump)` over the whole 67 MB dump (`verify_surfaces.py:376–382`, `:458–459`). `matched` is `bool(cfg) and bool(home)` (`:465`). No liveness, containment, or provenance is checked. The header limit at `:40–41` disclaims runtime firing for call shapes generally, but census row `:311` (`governed (OC-2)`, anchor count `1`) is backed only by this presence test.

### F2 — SURVIVED (G2, G3): OC-2 does not verify the gate the census asserts for the home candidate (too wide)

- G2: `!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]` → `[X.join(r.home,".claude","CLAUDE.md")]` (offset 10893090). Exit 0.
- G3: same span with the gate polarity inverted (`t.disableClaudeCodePrompt?…`). Exit 0.

The census states the home candidate is "gated by `disableClaudeCodePrompt`" (`corpus/knowledge/instruction-surface-census-round13.md:253`; also `:330–331`, adjudicated as correct at `:333`). The OC-2 anchors (`verify_surfaces.py:466–467`) do not include the gate, and the `matched` expression (`:465`) does not test it. Anchor presence therefore certifies a class whose load condition is unchecked.

### F3 — SURVIVED (G1, adjacent to OC-2 in OC-1): the OC-1 gate check is a tautology

`verify_surfaces.py:450`: `gated = m is not None and (OC_GATE not in m.group(0) or OC_GATE in dump)`. Because `m.group(0)` is a substring of `dump`, the disjunction is true whenever `m` matched, so `gated ≡ m is not None`. G1 (`!t.disableClaudeCodePrompt?["CLAUDE.md"]:[]` → `["CLAUDE.md"]` in the priority array) exits 0. The census claims that element is gated (`:250`). The anchor is listed at `:455` but never enforced.

### F4 — FALSE-RED (E4–E8): too narrow for equivalent forms

- E4 single-quoted literals, E5 template literals: exit 1, both rule anchors unmatched.
- E6 file literal held in a variable (`Pq="AGENTS.md",n=[X.join(r.config,Pq)`): exit 1. OC rules do no identifier resolution; the omp path does (`verify_surfaces.py:21–28`).
- E7 `join`→`resolve`, E8 `X.join(r?.config,…)`: exit 1.

Not too narrow for identifier renames (E1 `Zq`, E2 `$r`) or whitespace (E3): all exit 0. Regexes at `:376–382` require double quotes, a bare `IDENT.config` receiver, and literal `,`/`"` adjacency.

### F5 — Diagnostic calibration: the failure message names both anchors and drops the vanished class from `owns`

`verify_surfaces.py:441` `missing = [] if matched else list(anchors)` lists both anchors whenever the rule fails. `:462–463` derive `owns` only from surviving halves. A1 (config anchor removed only) reports:

`OC-2 (owns opencode:claude-home/CLAUDE.md; missing X.join(<v>.config,"AGENTS.md") + X.join(<v>.home,".claude","CLAUDE.md"))`

The vanished `opencode:config/AGENTS.md` appears only in the separate "produced by no rule" clause. The check still fails and names the classes, but the per-anchor diagnosis is wrong.

### F6 — Self-test does not exercise OC-2 single-anchor or corruption cases

The only OC-2 fixture in the `(oc)` loop (`verify_surfaces.py:1038`) is `strings-opencode-drop-oc2.txt`. Diffing it against the clean fixture shows it replaces line 9 (the whole `n=[…]` line) with a comment. So both anchors vanish together. No single-anchor, corruption, addition, or gate fixture exists. The 19 kills above come only from the real-dump probe, not from `--self-test`.

### F7 — Candidate tightening (scratch only, NOT landed) closes F1–F3 with no new false-red on the 37-set

Diff against 7ad7fad: `W2DropOC2.candidate-verifier.txt` (3 hunks):
- add `OC_CANDIDATE_ARRAY_RE` pinning OC-2's full array expression `n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]]`, with generic identifiers and `\s*`;
- OC-2 `matched` additionally requires that match (candidate line 475);
- OC-1 `gated = m is not None and OC_GATE in m.group(0)` (candidate line 460).

Results: self-test 99/99 exit 0. 37-set: 19 KILLED (unchanged); L1–L6 and G1–G3 now exit 1 with `FAIL surfaces.opencode_extract` naming the rule and its owned classes (e.g. G1: `rule(s) matched nothing: OC-1 (… missing ["AGENTS.md" … "CONTEXT.md"] + disableClaudeCodePrompt)`); E1–E3 still accepted; E4–E8 still false-red; control exit 0.

Trade-off [INFERENCE, untested]: the candidate hardcodes the literals and the array order and polarity. Benign refactors (e.g. reordering the spread, or `!(t.gate)`) would likely false-red. That is the price of closing F1–F3.

### F8 — Production write (my error, disclosed and restored)

At about 14:05 my candidate edit used the relative path `kotoba-shokunin/verifiers/verify_surfaces.py`. That resolves against the session cwd `/home/vgpnk/Projects/shokunin`, not the scratch clone. Three hunks landed in `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_surfaces.py`: a 10-line insert after line 382, a rewrite of line 450, and a rewrite of line 465.

I detected it because the "candidate" run was byte-identical to baseline (same verifier sha `e44bf34b…`). I then confirmed with `diff` against `git show 7ad7fad:verifiers/verify_surfaces.py` that the production delta was exactly those hunks. I restored production with `cp` from the 7ad7fad blob. No git or jj command was run inside production; the only git contact with that path was a read-only `git clone` source at setup, and nothing was written there. Result: production sha256 `e44bf34b1a52c0e5…`, 60048 bytes, `cmp`-identical to the blob. Its mtime is now 14:06. The transient state existed for about one minute. If a jj snapshot ran in that window, its op log will show it. The restored bytes equal 7ad7fad. All later writes use absolute paths.

## Holds (verified)

- Anchor presence: 19/19 removal, corruption, and addition mutants exit 1 with `FAIL surfaces.opencode_extract` naming the owned or undeclared class(es). The harness checks the names for every kill.
- Control: 7/7 PASS. Self-test at 7ad7fad: 99/99, exit 0.
- Frozen dump reproduces from the snapshot binary via `strings -n 4`.

## Commands run (exit codes)

- `git clone --no-hardlinks … && git checkout --detach 7ad7fad…`: exit 0; HEAD = 7ad7fad.
- `sha256sum` on frozen dump and snapshot binary: match SHA256SUMS.
- `strings -n 4 …/bin/opencode-1.19.3 | sha256sum`: `f4d8f34a…` (matches dump).
- Control verifier on frozen dump: exit 0, 7/7 PASS.
- `verify_surfaces.py --self-test`: exit 0, `0 failure(s) over 99 assertions`.
- `python3 mutate_oc2.py` (baseline): exit 0, 19 KILLED / 9 SURVIVED / 5 FALSE-RED / 4 ACCEPTED.
- Candidate (scratch only, after applying `W2DropOC2.candidate-verifier.txt` to the scratch clone): self-test exit 0 (99/99); `W2_PREFIX=W2DropOC2.candidate python3 mutate_oc2.py` exit 0, 19 KILLED / 9 now exit 1 / 5 FALSE-RED / 4 ACCEPTED.
- L1 repro (below): exit 0, `PASS surfaces.opencode_extract`.
- `grep` over `W2DropOC2.run.log`: only `surfaces.opencode_extract` FAIL lines (24).
- Production `cmp` against the 7ad7fad blob after restore: identical.

## Counterexample repro (survivor L1)

```
python3 - <<'EOF'
import pathlib
d = pathlib.Path('/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings').read_bytes()
o = b'n=[X.join(r.config,"AGENTS.md"),'
assert d.count(o) == 1
pathlib.Path('/tmp/L1.strings').write_bytes(d.replace(o, b'n=[!1&&X.join(r.config,"AGENTS.md"),'))
EOF
cd /fast/scratch/kotoba-r47/w2/W2DropOC2-2/kotoba-shokunin && python3 verifiers/verify_surfaces.py --opencode-strings /tmp/L1.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings; echo $?
```

Expected: `PASS surfaces.opencode_extract: … 7/7 rules`, exit 0. Full battery: `cd /fast/scratch/kotoba-r47/w2/W2DropOC2-2 && python3 mutate_oc2.py`.

## Adjacent observation (not verified)

`verify_surfaces.py:130` sets the default opencode binary to `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, an npx-cache path rather than the frozen snapshot. Default-resolution results therefore depend on cache state. I did not check that path's existence or sha (C1 scope).

## Not checked

- OC-1 (other than G1), OC-3 through OC-6, and every omp rule: no mutation run.
- Liveness and reachability: static only, no parser. Only the textual anchor shape was tested.
- Candidate's false-red risk on benign reorders: predicted, not run.
- The `--json` output mode and `--check` subsets.
- Multi-occurrence anchors: the real dump has one occurrence of each, so "remove one of N" was not exercised.
- Whether the census's "gated" wording reflects runtime behaviour.
- jj op log for the one-minute production-write window (F8); no jj or git command was run in production.
- Labrat probe: none spawned.

## Tools

None installed or upgraded. Used the system python3 (3.14.8), binutils `strings`, and git (scratch clone only).

## Artifacts (`.ufo/waves/round-47/falsify/`)

- `W2DropOC2.mutants.json`: baseline results, 37 rows, with mutant sha256, edit windows, and verdicts. Full stdout is in `W2DropOC2.run.log`.
- `W2DropOC2.run.log`: full verifier output per baseline mutant.
- `W2DropOC2.patch`: windowed before/after diffs per baseline mutant.
- `W2DropOC2.candidate.mutants.json`, `W2DropOC2.candidate.run.log`, `W2DropOC2.candidate.patch`: candidate run.
- `W2DropOC2.candidate-verifier.txt`: candidate verifier diff against 7ad7fad (not landed).
- `W2DropOC2.mutate_oc2.txt`: harness source (repro).
- `W2DropOC2.selftest.baseline.txt`, `W2DropOC2.selftest.candidate.txt`: self-test outputs.
