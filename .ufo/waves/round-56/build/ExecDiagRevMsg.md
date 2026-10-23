Result: DONE — round-55 routed defect 5a fixed: under a git that is present and refuses (exit 128, dubious ownership), seven lane gates now report git's own refusal instead of claiming the revision is unknown; each carries a self-test arm that fails on the base bytes and passes on the patched bytes.

Seat: KotobaR56.ExecDiagRevMsg (executor). Sandbox clone `/fast/scratch/hyaku/kotoba-r56/ExecDiagRevMsg` at `e02f5f5d` (verifiers/ is byte-identical at the lane tip `3d8efd7`; `git diff e02f5f5d 3d8efd7 -- verifiers/` is empty). Sandbox commit **`c070b44`**. Second clone `/fast/scratch/hyaku/kotoba-r56/ExecDiagRevMsg-apply` at the lane tip `3d8efd7` used to prove the patch applies. Receipts: `/fast/scratch/hyaku/kotoba-r56/ExecDiagRevMsg/scratch/{git128-post.txt,selftest-post.txt,red-arms.txt,noregress.txt}`. No tool installs; no lane writes except this file and `ExecDiagRevMsg.patch`. Nothing in `check_assertion_floors.py` was touched.

## 1. The defect, reproduced

`CriticC2Landed` (`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-55/falsify/CriticC2Landed.md:65`) reported that under a fake `git` printing `fatal: detected dubious ownership in repository` and exiting 128, the round-55 patches gave exit 2 for all seven git-reading gates with the message `revision '<rev>' is not a commit`. Its receipt is `/fast/scratch/hyaku/kotoba-r55/CriticC2Landed-scratch/git128.txt` (7 lines, all misattributing).

My reproduction, sandbox `e02f5f5d`, shim `git` first on PATH (present, `exit 128`, stderr `fatal: detected dubious ownership in repository at '/x/y'`), valid revision `e02f5f5d` passed:

```
$ cd /fast/scratch/hyaku/kotoba-r56/ExecDiagRevMsg && PATH=scratch/bin:$PATH timeout 120 python3 -B verifiers/<gate> ...
box_proof_case_deletion.py --rev e02f5f5d          -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
check_gate_finding_delta.py --base e02f5f5d --head e02f5f5d -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
check_overlap_levers.py --rev e02f5f5d             -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
check_mcp_instructions.py --rev e02f5f5d           -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
check_description_thresholds.py --rev e02f5f5d     -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
check_correction_sweep.py --rev e02f5f5d           -> exit 2 | could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>
verify_corpus_independent.py                       -> exit 2 | could-not-evaluate: not a git repository: <sandbox>
```
(2026-10-23 02:47:43Z. The 7th line is the same refusal class, not the literal revision message; see §6 scope note.)

The misattribution is real, not cosmetic: the revision was a valid commit, and `git rev-parse --verify --quiet` exits **1 with empty stderr** for a genuinely unknown revision (measured in the sandbox: `git rev-parse --verify --quiet 0000…^{commit}` → `exit 1`, no output). A refusal is exit 128 with a diagnostic. The base code collapsed both into `returncode != 0`.

## 2. The patch

`ExecDiagRevMsg.patch` (this directory), sha256 `f328cb8c7f00f196d2a5a898b9996befd5c87c8846f7ca97cc360c09ffd30ed4`, 477 lines, 308 added lines, 7 files, +301/−9. Generated with `git diff -- verifiers/` from the sandbox commit `c070b44`; it uses the lane's `i/`…`w/` mnemonic prefixes and applies with plain `git apply` (verified in the second clone).

Per gate: one local helper plus the call site. The rule is the same everywhere:

- `returncode == 1` **and** empty stderr → the existing, correct text `revision %r is not a commit in %s`.
- anything else (a refusing git, no repository, a broken object store) → `git rev-parse %r failed in %s (exit %d): %s`, where the last field is git's own first stderr line. Exit code stays 2.

| file | helper | call site |
|---|---|---|
| `verifiers/box_proof_case_deletion.py` | `revision_error()` (before the `main` banner) | `main()` rev check |
| `verifiers/check_gate_finding_delta.py` | `revision_error()` | `validate_revision()` |
| `verifiers/check_overlap_levers.py` | `revision_error()` | `verify_rev()` |
| `verifiers/check_mcp_instructions.py` | `revision_error()` | `main()` rev check |
| `verifiers/check_description_thresholds.py` | `revision_error()` | `verify_rev()` |
| `verifiers/check_correction_sweep.py` | `revision_error()` | `verify_revision()` |
| `verifiers/verify_corpus_independent.py` | `git_unreadable()` | `analyse()` repo check |

`verify_corpus_independent` keeps `not a git repository: <repo>` when git's own stderr says `not a git repository`, so the genuine case is unchanged; every other refusal is reported with git's exit code and first stderr line.

Post-patch run under the same shim (`scratch/git128-post.txt`, 02:50:19Z):

```
could-not-evaluate: git rev-parse 'e02f5f5d' failed in <sandbox> (exit 128): fatal: detected dubious ownership in repository at '/x/y'   (x6)
could-not-evaluate: git rev-parse --git-dir failed in <sandbox> (exit 128): fatal: detected dubious ownership in repository at '/x/y'
```
All seven exit 2, none says `is not a commit`.

## 3. Self-test arms, and the red evidence

Each gate gained one arm of the same shape: a temp dir holding a `git` shim (`exit 128`, dubious-ownership stderr, mode 0755) plus a `python3` symlink, PATH pointed at it, the gate run with a **valid** revision; assertions: exit 2, `is not a commit` absent, `dubious ownership` present. The arms follow the existing arms' idioms (in-process `run_revision` for box_proof, `run_cli` for correction_sweep, `run_gate` for mcp, `st.eq` for corpus_independent, `contextlib.redirect_stderr` for overlap). The mcp arm deliberately does not pass `dir=LANE`; the pre-existing `dir=LANE` of its neighbour arm is left as the critic found it.

Red evidence (`scratch/red-arms.txt`, 02:50:31Z): the production half of each patched file was reverted by exact string substitution (the arm kept), the copy placed at `verifiers/rev_<gate>.py` inside the sandbox, and `--self-test` run:

```
rev_box_proof_case_deletion.py      -> exit 1 | FAIL refusing git does not blame the revision: got True, expected False || FAIL refusing git reports git's own refusal: got False, expected True
rev_check_correction_sweep.py       -> exit 1 | FAIL refusing git: exit 2, stderr "could-not-evaluate: revision 'HEAD' is not a commit in <sandbox>"
rev_check_description_thresholds.py -> exit 1 | FAIL refusing git names git's refusal, not the revision: got (True, False), expected (False, True)
rev_check_gate_finding_delta.py     -> exit 1 | FAIL arm/refusing-git-names-git: got (2, True, True, False), want (2, True, False, True)
rev_check_mcp_instructions.py       -> exit 1 | FAIL G refusing git does not blame the revision || FAIL G refusing git reports git's own refusal
rev_check_overlap_levers.py         -> exit 1 | FAIL refusing git names git, not the revision: stderr="could-not-evaluate: revision 'b8f0c813…' is not a commit in /tmp/tmp…"
rev_verify_corpus_independent.py    -> exit 1 | not ok 98 - cli: refusing git is not reported as a non-repository: got True want False || not ok 99 - cli: refusing git quotes git's own refusal: got False want True
```
(The red copies were deleted afterwards; they lived only in the sandbox clone.)

Green: `scratch/selftest-post.txt` (02:50:19Z) — all seven `--self-test` runs exit 0. Assertion counts, base → patched (both measured in the sandbox): box_proof 14→17, correction_sweep 13→14, description_thresholds 24→26, finding_delta 12→13, mcp 14→17, overlap_levers 53→55, corpus_independent 95→99. All stay above their `verifiers/floors-registry.json` floors (overlap_levers 51, corpus_independent 93; the other five are not in the registry).

## 4. No regression

`scratch/noregress.txt` (02:50:54Z), base bytes vs patched bytes run side by side on real revisions in the sandbox:

| gate | base | patched | last stdout line (identical) |
|---|---|---|---|
| box_proof_case_deletion.py `--rev e02f5f5d` | 0 | 0 | `killed 6 of 6` |
| check_correction_sweep.py `--rev e02f5f5d` | 0 | 0 | `correction sweep: 0 stale block(s)` |
| check_description_thresholds.py `--rev e02f5f5d` | 0 | 0 | `description thresholds backed 7 of 7 clients` |
| check_gate_finding_delta.py `--base e02f5f5d --head e02f5f5d` | 0 | 0 | `finding delta: new 0, resolved 0` |
| check_mcp_instructions.py `--rev e02f5f5d` | 0 | 0 | `mcp instructions backed 7 of 7 clients` |
| check_overlap_levers.py `--rev e02f5f5d` | 0 | 0 | `overlap levers backed 7 of 7 clients` |
| verify_corpus_independent.py | 1 | 1 | `exit 1` |

Preserved failure messages: `--rev 0000…` still exits 2 with `could-not-evaluate: revision '000…' is not a commit in <repo>` for the six revision gates, and `verify_corpus_independent.py --repo /tmp/r56-not-a-repo` still exits 2 with `could-not-evaluate: not a git repository: /tmp/r56-not-a-repo`. The round-55 C2 counter (`check_could_not_evaluate.py`) probes only unknown revisions and a git-absent PATH, so neither class changes; it was not run (counter runs belong to the L1).

Applied at the lane tip: `git -C ExecDiagRevMsg-apply apply --check <patch>` → OK, `git apply` → applied, then `box_proof_case_deletion.py --self-test` → `0 failure(s) over 17 assertions` (exit 0) and `check_overlap_levers.py --rev 3d8efd7` under the shim → exit 2 with `git rev-parse '3d8efd7' failed in <clone> (exit 128): fatal: detected dubious ownership …`.

## 5. Residual (not mine to change)

- **`check_assertion_floors.py` untouched** — defect 5b (its `git --version` preflight ignores the returncode) is another seat's item, as assigned.
- **The same misattribution survives in four counters**, which a seat may not edit: `check_agent_definitions.py` (round-56 C1, frozen v1.3), `check_explicit_invocation.py` (round-55 C1 v2), `check_could_not_evaluate.py` (round-55 C2) all print `could-not-evaluate: revision 'e02f5f5d' is not a commit in <sandbox>`, exit 2, under the refusing git (02:51:30Z). `check_agentdef_boxes.py` exits 2 with `cannot evaluate: Command '('show', 'e02f5f5d:verifiers/checklist-baseline.json')' returned non-zero exit status 128.` — it names git's exit code but not the refusal text. Fixing any of these needs an L1 decision (erratum/new frozen version), not a seat edit.
- **Scope note for the L1**: six files carry the literal revision message named in defect 5a; `verify_corpus_independent.py` is the seventh probe line of the same receipt and had the same root cause with a repo-shaped message. If the L1 reads 5a as the revision message only, drop that file's hunk; the other six stand alone.

## 6. What I did not check

- `check_assertion_floors.py` under the refusing git (other seat; the critic's `floors-git128.txt` already shows a nested timeout, not this defect).
- The full round-55 C2 counter, `verify_surfaces.py`, and any post-integration gate — the L1 owns post-integration verification. The five gates not in `floors-registry.json` were not floor-checked; only their own self-tests were run.
- No consumer greps beyond the lane: `grep -rn "is not a commit"` over the lane finds only the gates' own arms and prose (`corpus/lessons/round-11.md:24`, round-55 seat reports under `.ufo/`); no script matches on the message text, so the rewording breaks no matcher. [INFERENCE] from that grep, not from running a consumer.
