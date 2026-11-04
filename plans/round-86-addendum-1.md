# kotoba round 86 — addendum 1 to the C1 counter (before any candidate data)

Committed before any candidate model was scored: ExecModel acknowledged a HOLD (it had scored
nothing; `.ufo/waves/round-86/w1/ExecModel/` was empty and `verifiers/verify_harness_claims.py`
unmodified when the hold was sent). Lane precedent: `plans/round-74-addendum-1.md` (amended before
any data on control-world findings). The predicate sentence, the headline, the 215 total, the 205
target, the fixture and its sha256 are **unchanged**:

    python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>
        -> prints "omp catalogue lines reproduced N of 215", exit 0 iff N >= 205
           and guards G1-G4 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

## Why: three falsifications of the frozen instrument by this round's attack seats

| finding | seat | world | frozen counter | receipt |
|---|---|---|---|---|
| F1 | Critic-2 | base model + one USER_ROOTS line `~/.zcode/cli/plugins/marketplaces/ecc/pi/core/skills` (a root omp never reads; `.zcode` occurs 0 times in the ELF) + ledger row `*<TAB>: archive has no SKILL.md` | `215 of 215`, G1–G4 PASS, exit 0 | `w1/Critic/receipts/cheapest-zcode-1line-wild.txt` |
| F2 | Sentinel-3 | `~/.omp/logs/http-400-requests/*.json` (request dumps) carry all 215 renders and were visible inside the sandbox; no `--unshare-net`, no pid namespace, env not cleared | catalogue readable in the box | `w1/Sentinel/receipts/catalogue-leak.txt` |
| F3 | ReviewerCounter-2 | an answer key split or encoded past G1's equality test, served through `preview`, with one old SKILL.md path offered for every name; also the fixture fetched over the network from the pushed freeze | `215 of 215`, exit 0 | `w1/ReviewerCounter/` |

## Amendments (all in `verifiers/check_omp_catalogue_repro.py`)

1. **G4 dot-directory rule** (`_pattern_problem`): a ledger pattern's relative part must contain at
   least one literal dot-directory segment (`.agents`, `.omp`, …); no wildcard in its first segment
   or in a dot segment; the row's quote must contain every literal dot segment verbatim.
   Kills F1 (`*` row; `.zcode` never named by any ELF string).
2. **Sandbox allowlist and namespaces** (`default_hide`, `default_rebind`, `run_module`): all of
   `~/.omp` is hidden and only `~/.omp/plugins/node_modules` and `~/.omp/agent/skills` are bound back
   read-only; `/dev/shm` and `/run/user` hidden; `--unshare-net --unshare-pid --unshare-ipc
   --new-session --clearenv` with HOME/PATH/LANG set. Kills F2 and the network half of F3.
3. **Parent-side reference** (`predict`, `ref_key`, `ref_preview`): the module contributes only
   discovery (`path`) and parsing (`desc`). The parent requires the SKILL.md's directory name to equal
   the skill name, the whitespace-collapsed description to occur in the file the path names, the
   module's `omp_key` and `preview` to equal the reference ports of omp 18.15.0 `A(e)` and `dnt`
   (`k = 100`, `E = 40`, the `o >= E` last-space test) per name, and computes the render itself
   (cache row if the reference key is cached, else the reference preview). Kills F3's answer key and
   one-path forgery.

Side finding (not a counter change): the lane's base `preview` omits omp's `o >= E` last-space test
(`(s[:s.rfind(" ")].rstrip() or s)`); no fixture line exercises that branch (base still 83 of 215,
0 `render-differs`), but under amendment 3 the candidate must match the source rule. Routed to
ExecModel as part of C1's surface.

## Controls re-run on the amended counter (receipts `.ufo/waves/round-86/receipts/*-a1.txt`)

| id | world | amended counter |
|---|---|---|
| self-test | 46 assertions incl. `*` row, dot wildcard, no-dot pattern, quote missing the dot segment, one-path forgery, base64 answer key | `0 failure(s) over 46 assertions` |
| K0 | round base | `83 of 215`, G4 FAIL (no ledger), exit 1 |
| K1 | echo forgery | `83 of 215`, exit 1 |
| K2 | literal answer key | G1 FAIL, exit 1 |
| K3 / K3b | Critic-2's F1 world / per-root zcode row | `215 of 215` but G4 FAIL (first-segment wildcard / quote does not name `.zcode`), exit 1 |
| K4 | sandbox visibility probe | logs, sessions, cache, agent DB absent; fleet and `/run/user` empty; network blocked; home not writable; 4 env vars (`c1-K4-sandbox-a1.txt`) |

**Residual bound, stated before data:** G4 checks that a located quote names the root's client
directory; whether that quote is the code that makes omp read the root (e.g. `var Gh = ".omp";` for
the plugin root) stays the reviewer's judgement (ReviewerRoots, then the closure). Kill rule
unchanged.
