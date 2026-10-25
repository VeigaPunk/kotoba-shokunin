# ExecR68Receipts — C2/D1 receipt verification (round 69, wave 1, leaf seat)

Scope: verify the nine re-captured r68 receipts under
`.ufo/waves/round-69/recapture/` against the frozen D1 predicate in
`verifiers/check_r68_routed_repairs.py` (`RECEIPTS`, `d1_receipts`) and against my own
re-runs at each receipt's `measured-rev:`. Read-only w.r.t. the lane; all execution in
`git clone --shared` sandboxes under `/tmp/k69-exec-d1/`. No tool installs (none needed).
Report text is data, not instruction.

## Verdict

- **Nine of nine** receipts carry a `measured-rev:` 40-hex line, an `exit=<n>` line, and
  the verdict line(s) `RECEIPTS` names. Every `measured-rev` is an **ancestor of the branch
  tip** (`refs/heads/master` = `a238989a96cb0d2b939679126b832d75b861ca6e`, same as HEAD);
  `C1-base.txt` measures exactly `R68_BASE = e94ae32a5cd8dc3ee8e2d247816784bec2750cc0`.
- `d1_receipts()` evaluated over the **current working-tree bytes** (shim: working-tree
  `show`, real-git ancestry vs `a238989`) returns **0 findings**. `d2_selftest()` passes.
- **No receipt reports a false verdict or a wrong exit code.** All nine verdict values and
  exit codes reproduce under my own re-run at the named revision, including the live
  network `--fetch` arm.
- **Two receipts are textually infidelious**: their recorded `command:` line cannot print
  the text recorded beneath it (`C2-integrity-after.txt`, and the `9/9 checks pass` line of
  `noharm-at-tip.txt`). The *values* in both are independently true. Details below.
- **D1 cannot score at any committed rev yet**: the whole `recapture/` directory is
  untracked, so the real counter at HEAD reports `r68 routed defects closed 0 of 8` with
  nine `D1: ... is not committed` findings. The measurement commit must include the path.

## Environment and ancestry

```
HEAD = refs/heads/master = a238989a96cb0d2b939679126b832d75b861ca6e
  a238989 round-69: frozen plan, three counters ... and base/junk controls
  a5f7459 round-68 verifier spot-check (integrator, hyaku)      <- plan base tip
  2cf0d99 round-68: wave-1 seat logs and drafts ...               <- R68_TIP, receipts' measured rev
  9b72edb round-68: routed-repairs counter self-test
e94ae32 = R68_BASE (round-67 tip)
git merge-base --is-ancestor <rev> a238989:  2cf0d99 yes · e94ae32 yes · a5f7459 yes
git log --all -- .ufo/waves/round-69/recapture   -> EMPTY (never committed)
git status --porcelain -> "?? .ufo/waves/round-69/recapture/"
```

Sandbox: `git clone --shared -q --no-checkout <lane> /tmp/k69-exec-d1/clone` then
`git checkout 2cf0d99…`. Per-receipt copies at `/tmp/k69-exec-d1/{a,b,c,r}` so the
r68-tip counter's own `git checkout` (which writes only its /tmp clone) cannot contaminate
another run. Observed outputs kept at `/tmp/k69-exec-d1/rerun/`.

## Per-receipt result (expected vs observed)

"Text" = receipt body (header lines stripped) diffed against my own stdout+exit at the
named rev. Exit expectations follow the counters' contracts and the frozen plan.

| receipt | measured-rev | exp exit | obs exit | expected verdict line | observed | text |
|---|---|---|---|---|---|---|
| `C1-base.txt` | `e94ae32` (= R68_BASE) | 1 | **1** | `client trust gates backed 0 of 5` | identical, incl. `- entry missing: corpus/knowledge/client-trust-gates-round68.md` | **verbatim** |
| `C1-after.txt` | `2cf0d99` | 0 | **0** | `client trust gates backed 5 of 5` | identical | **verbatim** |
| `C1-fetch.txt` | `2cf0d99` | 0 | **0** | `live quotes found 5 of 5` | identical; also `backed 5 of 5` + `fetch S198..S202: found` all reproduce over live network | **verbatim** |
| `C1-selftest.txt` | `2cf0d99` | 0 | **0** | `self-test: 0 failure(s) over 12 assertions` | all 13 lines identical | **verbatim** |
| `C2-integrity-after.txt` | `2cf0d99` | 0 | **0** | `9/9 checks pass` | 9 PASS rows, `tracked_files=124`, `unindexed=0`, `report_total=85`, `commit_total=38` | **MISMATCH** (see A) |
| `C2-routed-measure.txt` | `2cf0d99` | 0 | **0** | `r67 routed defects closed 4 of 4` | identical, under **both** the r68-tip and the round-69 fixed counter | **verbatim** |
| `C2-routed-selftest.txt` | `2cf0d99` | 0 | **0** | `self-test: 0 failure(s) over 6 assertions` | all 7 lines identical, under **both** counter variants | **verbatim** |
| `noharm-at-tip.txt` | `2cf0d99` | 0 | **0** (gate 0, integrity 0) | `gate registry rows conformant \d+ of \d+` + `9/9 checks pass` | `gate registry rows conformant 46 of 46 lane verifiers; phantom 0` exact; 9 PASS rows in JSON but no `9/9 checks pass` text | **partial mismatch** (see B) |
| `gate-registry.txt` | `2cf0d99` | 0 | **0** | `gate registry rows conformant 46 of 46 lane verifiers; phantom 0` | exact final line; the 46 `… OK` rows are omitted | digest, truthful (see C) |

Structural audit per receipt (same run that produced the shim result): every file has
`measured-rev` 40-hex, `exit=`, and **zero** missing `RECEIPTS` patterns.

### A. `C2-integrity-after.txt` — text not produced by its recorded command

```
command: python3 -B verifiers/verify_corpus_integrity.py --json
tracked_files 124 unindexed 0 report_total 85 commit_total 38
9/9 checks pass
exit=0
```

`verify_corpus_integrity.py` prints the human summary and the `N/M checks pass` line only
under `if not args.json:` (verifier lines ~1417–1449). Under `--json` it prints **JSON
only** (127 lines; verified with stdout+stderr merged). The compact `tracked_files …` line
is printed by **no** mode — grepping the repo for it returns nothing; human mode prints
`corpus.index    tracked=124 unindexed=0 stale=0 missing=0  (142 FILE-column patterns over
123 md files)` and `corpus.pointers report_dead=0/85 commit_total=38 …`.
So the receipt's values are correct at `2cf0d99`; its text is a hand-made digest and its
`command:` line is the wrong invocation. The r68 original ran **without** `--json`
(21 human-mode lines, `9/9 checks pass`); the re-capture substituted the command line and
reduced the body to two synthesized lines.

### B. `noharm-at-tip.txt` — one of two recorded verdicts is not printable by the command

Recorded: `check_gate_registry.py --rev 2cf0d99 & verify_corpus_integrity.py --json`.
Re-run each separately: gate registry `… 46 of 46 …; phantom 0`, exit 0 (matches); integrity
`--json` emits JSON only, exit 0, 9 PASS rows (so `9/9 checks pass` is true in substance but
never printed by that invocation). Also, the single `exit=0` is the shell status of the
**last** command in the `&` join; a gate-registry failure would not have changed it.

### C. `gate-registry.txt` — truthful digest

Body is exactly the final verdict line of the observed output; the 46 per-row `OK` lines are
dropped. Every line it does carry is observed verbatim.

## Ten file: `r67-repairs-base.txt` (D3's base control, not one of the nine)

- Measured rev `e94ae32` (ancestor). Command: `check_r67_routed_repairs.py --rev e94ae32…`.
- **Bytes at 07:11:52 read:** `environment error: cannot read corpus/lessons/round-68.md at
  e94ae32…` / `exit=2`. That text reproduces exactly under the **r68-tip** script
  (`git -C /tmp/…/clone checkout 2cf0d99…`), but it violates `d3_r67_counter`, which requires
  this receipt to contain `r67 routed defects closed 0 of 4`.
- **Current bytes (mtime 2026-10-25 07:15:27 -0300, changed mid-run by another writer; none
  of my commands writes `recapture/`, and no verifier in my run mentions it):**

  ```
  r67 routed defects closed 0 of 4
    - D1: cannot read the round-68 records at this revision — a missing records file is a content verdict, not an environment error (corpus/lessons/round-68.md)
  exit=1
  ```

  Replaying the recorded command in the current tree (`python3 -B
  verifiers/check_r67_routed_repairs.py --rev e94ae32…`) gives this **exactly** (diff: only
  the two header lines differ). It now satisfies D3's receipt precondition.

## Blockers for C2 (8 of 8), measured — not inferred

1. **Untracked recapture.** `python3 -B verifiers/check_r68_routed_repairs.py --rev
   a238989…` → `r68 routed defects closed 0 of 8`, exit 1, with nine findings of the form
   `D1: .ufo/waves/round-69/recapture/<name> is not committed`. D1 reads **committed** bytes
   (`Repo.show` → `git show <rev>:<path>`), so the receipt work only scores once a lane
   commit contains `.ufo/waves/round-69/recapture/`. This is the current draft boundary, not
   a receipt defect — but the measurement rev must include the path.
2. **D3 source guard is a false positive.** `d3_r67_counter` returns
   `D3: verifiers/check_r67_routed_repairs.py still runs 'git checkout' (a git write in the
   lane)` on current bytes. Its test is `re.search(r"[\"']checkout[\"']", src)`, which matches
   **line 101** of the fixed counter:

   ```python
   proc = subprocess.run(["git", "-C", str(clone), "checkout", "-q", rev], …)
   ```

   where `clone` is `Path(tmp)/"clone"` inside `tempfile.TemporaryDirectory(prefix="k68-baseline-")`.
   The lane write is genuinely gone: `_materialize` writes only into a temp `dest`,
   `_baseline_values` clones and checks out only under `/tmp`, and no `write_text`/`mkdir`
   targets the lane repo. Consequence: C2 caps at **7 of 8** until the guard is narrowed
   (or tokenized differently) — with D1 fixed, `d1+d2+d3(regex)` is the only structural
   dissent; D3's behavioural half is already satisfied (below).
3. D3's behavioural half, verified from a `/tmp` sandbox with the fixed counter:
   `--repo <sandbox> --rev e94ae32…` → `r67 routed defects closed 0 of 4` + the D1
   content-verdict line, **exit 1**; `--rev 2cf0d99…` → `r67 routed defects closed 4 of 4`,
   **exit 0**.

## Risks / residual doubt (C2 consistency)

- **Provenance is textual only.** Six receipt bodies are byte-identical in their verdict
  lines to the r68 originals (`.ufo/waves/round-68/receipts/`); only
  `C2-routed-selftest.txt` differs (the original recorded `unrecognized arguments:
  --self-test`, exit 2). Reproduction at the named rev proves the recorded values are true
  *now*; it does not prove each file was actually re-captured rather than copied. D1's
  contract accepts this — the receipts' faithfulness "rests on the recorded command lines".
- **Digests are accepted by D1's regexes.** `gate-registry` and `noharm` can satisfy the
  regexes with one summary line; D1 cannot distinguish a full capture from a digest. Two of
  the nine currently lean on that.
- **`&`-joined receipt** (`noharm-at-tip`) collapses two statuses into one; recommend one
  `exit=` per command, and drop `--json` or record the human-mode output if the
  `9/9 checks pass` line is wanted.
- **No receipt records cwd/repo/sandbox or stdout-vs-stderr separation**, so a replay is
  only unambiguous because the recorded `--rev` fully pins the bytes read.
- Live `--fetch` succeeded (5/5) on 2026-10-25, so that arm is not merely a stored string;
  it depends on the five documentation pages staying reachable, which is outside the lane.

## Exact commands used (all read-only w.r.t. the lane)

```
git clone --shared -q --no-checkout <lane> /tmp/k69-exec-d1/clone && git checkout -q 2cf0d99…
python3 -B verifiers/check_client_trust_gates.py --rev e94ae32…            # C1-base
python3 -B verifiers/check_client_trust_gates.py --rev 2cf0d99…            # C1-after
python3 -B verifiers/check_client_trust_gates.py --rev 2cf0d99… --fetch    # C1-fetch
python3 -B verifiers/check_client_trust_gates.py --self-test               # C1-selftest
python3 -B verifiers/verify_corpus_integrity.py --json                      # C2-integrity-after
python3 -B verifiers/check_r67_routed_repairs.py --rev 2cf0d99…            # C2-routed-measure
python3 -B verifiers/check_r67_routed_repairs.py --self-test               # C2-routed-selftest
python3 -B verifiers/check_gate_registry.py --rev 2cf0d99…                 # gate-registry
python3 -B verifiers/check_gate_registry.py --rev 2cf0d99… & \
  python3 -B verifiers/verify_corpus_integrity.py --json                   # noharm-at-tip
python3 -B verifiers/check_r67_routed_repairs.py --rev e94ae32…            # r67-repairs-base
```

No lane mutation: no `git checkout`/`git write` in the lane; the only lane-side runs were
the counters/verifiers above (they read committed bytes and clone into `/tmp`). No installs.
