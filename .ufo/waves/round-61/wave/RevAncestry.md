# RevAncestry — R-f (controls-ancestry) integration verification spec

Seat: `kotoba-r61-wave-RevAncestry` (reviewer, leaf)
Report path: `.ufo/waves/round-61/wave/RevAncestry.md`
Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated; read-only to seat except this report)
Date: 2026-10-23 (measurements stamped below)
Assignment: define the exact R-f verification the L1 must perform at integration — commit C_ctl
(carrying `.ufo/waves/round-61/receipts/C1-worlds.txt`) and commit C_data (carrying the C1
`--fetch` measurement); `git merge-base --is-ancestor C_ctl C_data` must exit 0; both must be
lane-identity commits, ancestors of the branch tip. Deliver the receipt template with checks
enumerated and failure modes named.

No LSP server/device is available to this seat (the `lsp` device is not in this seat's tool
inventory), so all code/definition evidence below is text-read from committed files — recorded as
required.

---

## 1. Ground verified (read-only; commands, outputs, date -u, exit codes)

### 1.1 The frozen checker defines R-f as a two-substring grep (committed bytes)

Read: `verifiers/check_routed_repairs.py` (frozen at plan-freeze commit `7827628`). The R-f arm:

```python
    ancestry = blobs.get(".ufo/waves/round-61/receipts/controls-ancestry.txt")
    rf = (
        ancestry is not None
        and "merge-base --is-ancestor" in ancestry
        and "exit 0" in ancestry
    )
```

Consequences (frozen, immutable):
- The receipt file must contain the **literal** substrings `merge-base --is-ancestor` and `exit 0`
  (single space). `exit=0` does NOT match `exit 0`. Case-sensitive.
- The counter greps the blob at the measured rev; the receipt must be committed before the `--rev <rev>`
  run that is expected to score it.
- The counter cannot judge honesty (Q31): a receipt containing the two literal substrings but no real
  runs would pass the grep. The enumerated checks below are the substantive verification the L1 (and
  any reader) must be able to re-derive from the receipt's pasted output.

Self-test arm (same file) pins the same contract: `ancestry = "$ git merge-base --is-ancestor $CTL $DATA\nexit 0\n"` — i.e., the expected receipt shape is a pasted command line followed by a line `exit 0`.

### 1.2 C2 base control re-confirmed live (unrun checks have not passed; these ran)

Command and output (run in the lane repo, read-only), date -u: 2026-10-23T19:12:01Z:

```
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
exit=1
```

Matches committed `.ufo/waves/round-61/controls/C2-base.txt` (`0 of 6`, `base-exit=1`).

```
$ python3 -B verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test: 0 failure(s)
exit=0
```

Note the self-test's `without-controls-ancestry.txt` arm: damaged content ("no proof\n") drops the count to 5 of 6 — a receipt file that exists but does not carry the two literal substrings fails R-f.

### 1.3 Lane identity definition (grounded in tooling, not assumed)

`scripts/hyaku/jj-lane.sh` (committed at fleet root) enforces on every lane commit:
- Identity is set per-command as `user.name=<id>-shokunin`, `user.email=<id>@shokunin.local`.
- `candidate_has_identity()` requires exactly `%an|%ae|%cn|%ce` = `<id>-shokunin|<id>@shokunin.local|<id>-shokunin|<id>@shokunin.local` — i.e., **author AND committer**.
- Push preflight rejects any pushed range containing a foreign committer email (`git log --format='%an|%ae|%cn|%ce' origin..branch`).
- Pushes are fast-forward only; nothing is rewritten; the only citable hash line is `landed <hash>`, printed after remote verification.

For this lane id = `kotoba`, so a lane-identity commit is exactly:
`kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local`

Verified live:

```
$ git log -1 --format='%an|%ae|%cn|%ce' master
kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local
$ git log -1 --format='%an|%ae|%cn|%ce' f3246d1493b60ea1c0d947a19c39f9e08e92f326
protocol-shokunin|protocol@shokunin.local|protocol-shokunin|protocol@shokunin.local
```

The base commit `f3246d1` is an ancestor of the tip and carries corpus files, but is **not** a
lane-identity commit (protocol identity). This is the concrete counterexample proving that
"exists + ancestor of tip" alone is insufficient — the identity check is a separate, required gate.

### 1.4 Lane branch/tip state at verification time

```
$ git rev-parse master origin/master
c630c4cbc01ff5e5438ab0033cfadd6e19382ab1
c630c4cbc01ff5e5438ab0033cfadd6e19382ab1
$ git log -3 --format='%h %an <%ae> %s' master
c630c4c kotoba-shokunin <kotoba@shokunin.local> round-61: erratum E1 — C3 withdrawn as a counted claim before data (CriticC3Axis hollow-counterexample); curation continues as frontier work, class mined as M92
7827628 kotoba-shokunin <kotoba@shokunin.local> round-61: plan freeze (3 claims, frozen predicates), C2 routed-repairs counter + base control, census-before, v2 wave spec+dispatch (68 seats, 46 attack)
f3246d1 protocol-shokunin <protocol@shokunin.local> round-60 verifier spot-check (integrator, hyaku): non-author admit/reject
```

- `master` == `origin/master` == `c630c4c` (plan-freeze commit `7827628` + L1 erratum E1 landed and pushed).
- The lane's `HEAD` is detached (`git branch --show-current` prints empty); the canonical tip ref is `refs/heads/master` — the C2 checker's default measured rev is `master` (`git rev-parse --verify master`), so "ancestor of the branch tip" means ancestor of `refs/heads/master`.
- `.ufo/waves/round-61/receipts/controls-ancestry.txt` does not exist at `master` yet (`git show master:...` → fatal, exit 128) — expected pre-integration; R-f lands later.
- `.ufo/waves/round-61/` currently commits `census-before.txt`, `controls/C2-base.txt`, `wave-dispatch.json`, `wave-spec.json`, `wave/swarm-registry.json`.
- Committable-path gate (`repo_path_allowed` in `jj-lane.sh`): only `.git`, `.jj`, `.ufo`, `.ufo/state`, `.ufo/state/*`, `.ufo/watchdog.log` are rejected. `.ufo/waves/round-61/receipts/*` and `C1-measure.txt` are committable — confirmed by the already-committed `.ufo/waves/round-61/controls/C2-base.txt`.

### 1.5 `git merge-base --is-ancestor` edge semantics (live demos)

```
$ git merge-base --is-ancestor master master; echo exit=$?
exit=0
$ git merge-base --is-ancestor master f3246d1493b60ea1c0d947a19c39f9e08e92f326; echo exit=$?
exit=1
$ git merge-base --is-ancestor f3246d1493b60ea1c0d947a19c39f9e08e92f326 master; echo exit=$?
exit=0
```

- A commit is an ancestor of itself (`exit 0`) — so `--is-ancestor C_ctl C_data` alone does NOT prove
  a strict controls-before-data split; the two hashes must also be distinct (V2 below).
- Reversed arguments change the verdict — the receipt must paste the invocation in the exact
  `C_ctl C_data` order.
- Topology, not timestamps, is the proof: author/committer dates can be forged (same declared limit
  as C1 arm A4), the DAG cannot. Wall-clock probe order is enforced operationally (phase ordering,
  §3) and recorded, then verified by topology.

### 1.6 Receipt-shape precedents (committed)

- `.ufo/waves/round-60/C1-measure.txt`: header line (what/where/when), command blocks, `exit N`
  lines, predicate sentence, counter sha256 line — the pasted-output receipt shape.
- `.ufo/waves/round-60/receipts/freeze2-selftest.txt`, `.ufo/waves/round-59/receipts/base-r59-a975cbbf.txt`: rev/date/seat header + `== command` blocks + `exit N` lines.
- No committed `controls-ancestry.txt` precedent exists in the lane (round 59/60 receipts are base/data/no-harm only); the R-f receipt is a new shape, defined below.
- Wave spec (committed, `wave-spec.json` item ExecReceiptsDesign) independently asks for the same three files: `receipts/C1-worlds.txt` (one line per world `W<n> <name> exit <code>` plus command block), `receipts/controls-ancestry.txt` (two hashes, exact invocation, `exit 0` line), and `.ufo/waves/round-61/C1-measure.txt` (counter sha256 + frozen predicate sentence). This spec aligns with that design.

---

## 2. The R-f verification the L1 must perform at integration

### 2.1 Commit/phase order (prerequisites for R-f to be true)

1. **Phase 0 (already true)** — plan-freeze commit `7827628` landed: plan, checker, C2-base control,
   census-before, wave spec. C2 base control re-confirmed 0 of 6 / exit 1 (§1.2).
2. **Phase 1 — controls first (M90).** The L1 commits the C1 counter v3 + fixtures + the control
   receipts (including `.ufo/waves/round-61/receipts/C1-worlds.txt`) via
   `jj-lane.sh commit <lane> --as kotoba -m ... -- <paths>`, then pushes. Capture the helper's
   `landed <hash>` line — that is **C_ctl**. **Nothing of the C1 `--fetch` measurement may be
   dispatched, run, or committed before this `landed` line exists.**
3. **Phase 2 — measure.** In a scratch/read-only context, run the frozen C1 predicate at tip and the
   base control (`--rev f3246d14…` must exit 1); write `.ufo/waves/round-61/C1-measure.txt` with the
   counter sha256 line and the frozen predicate sentence echoed (format per ExecReceiptsDesign).
4. **Phase 3 — data commit.** Commit `C1-measure.txt` (+ any data-side receipt artifacts) via the
   helper, push, capture `landed <hash>` — that is **C_data**.
5. **Phase 4 — verify + write receipt.** Run checks V1–V9 below in the lane repo; write
   `.ufo/waves/round-61/receipts/controls-ancestry.txt` from the template (§4); commit it (together
   with census-after and the other repair artifacts) via the helper and push.
6. **Phase 5 — final counter run.** After the receipt commit lands: `python3 -B verifiers/check_routed_repairs.py --rev master` must print `routed repairs verified 6 of 6` and exit 0; `--self-test` prints `0 failure(s)` and exits 0. (A run before the receipt commit scores 5 of 6, exit 1.)

### 2.2 Check list (each is an exact command, run in the lane repo with `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin` or `git -C`)

**V1 — both revs resolve to commits.** `git rev-parse --verify <C_ctl>^{commit}` and
`git rev-parse --verify <C_data>^{commit}` each exit 0 and print a full 40-hex hash
(`git cat-file -t <hash>` → `commit`).

**V2 — strict precedence (not the same commit).** `git rev-parse <C_ctl> <C_data>` prints two
different hashes; equivalently `test "$(git rev-parse <C_ctl>)" != "$(git rev-parse <C_data>)"` exits 0.
(Needed because `--is-ancestor X X` exits 0, §1.5.)

**V3 — controls are ancestors of the data commit.** `git merge-base --is-ancestor <C_ctl> <C_data>`
exits 0. This is the named R-f check; the receipt must paste this exact invocation (C_ctl first).

**V4 — both are ancestors of the branch tip.** `git merge-base --is-ancestor <C_ctl> <TIP>` and
`git merge-base --is-ancestor <C_data> <TIP>` both exit 0, where `<TIP>` = `git rev-parse master`
(`refs/heads/master`) at check time. Record `<TIP>` in the receipt.

**V5 — both are lane-identity commits.** For each of C_ctl, C_data:
`git log -1 --format='%an|%ae|%cn|%ce' <C>` must print exactly
`kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local` (author AND committer).

**V6 — C_ctl carries the controls receipt.** `git show <C_ctl>:.ufo/waves/round-61/receipts/C1-worlds.txt`
exits 0 and the blob names all seven frozen worlds (W1 CtlReopenForged d, W2 CtlReopenHeldKey b,
W3 CtlReopenHeldKey a, W4 CtlReopenHeldKey c, W5 wrong scope-key/ExecKeyForms, W6 invented action,
W7 v1-hollow rescore) with `exit 1` each; and
`git show <C_ctl>:verifiers/check_scoped_rules.py | sha256sum` equals the sha256 line recorded inside
C1-worlds.txt (frozen v3 counter bytes).

**V7 — C_data carries the C1 measurement.** `git show <C_data>:.ufo/waves/round-61/C1-measure.txt`
exits 0; the blob contains the `--fetch` invocation, the same counter sha256 as V6, the frozen
predicate sentence (`worlds reject 7 of 7; eligible rows pass 4 of 4`), and `exit 0` on the fetch run
(plus the base run `exit 1`).

**V8 — receipt re-plays everything.** From `.ufo/waves/round-61/receipts/controls-ancestry.txt`
alone, an independent reader can re-run V1–V7 at the recorded hashes and reproduce every pasted
output. The file contains the literal substrings `merge-base --is-ancestor` and `exit 0` (frozen
grep contract, §1.1) in a real command/output pair — not merely as prose.

**V9 — final counter run (after receipt commit).** `python3 -B verifiers/check_routed_repairs.py --rev master` → `routed repairs verified 6 of 6`, exit 0; `python3 -B verifiers/check_routed_repairs.py --self-test` → `0 failure(s)`, exit 0.

---

## 3. Receipt template — exact target path `.ufo/waves/round-61/receipts/controls-ancestry.txt`

```text
# Round-61 controls-ancestry receipt (R-f)
lane repo: /home/vgpnk/Projects/shokunin/kotoba-shokunin
date -u: <YYYY-MM-DDTHH:MM:SSZ>
branch tip at writing (git rev-parse master): <TIP>
C_ctl (control-receipts commit, landed): <C_CTL>
C_data (C1 data commit, landed): <C_DATA>

Sequence performed by the L1 (M90 controls-before-data):
  phase 1: C_ctl = `landed <hash>` of the helper commit carrying
           .ufo/waves/round-61/receipts/C1-worlds.txt (+ counter v3 + fixtures)
  phase 2: C1 --fetch measurement run AFTER that landed line; output written to
           .ufo/waves/round-61/C1-measure.txt
  phase 3: C_data = `landed <hash>` of the helper commit carrying
           .ufo/waves/round-61/C1-measure.txt
  phase 4: this receipt, committed after the checks below

Checks (all run in the lane repo):

$ git rev-parse --verify <C_CTL>^{commit}
<C_CTL>
exit 0

$ git rev-parse --verify <C_DATA>^{commit}
<C_DATA>
exit 0

$ test "$(git rev-parse <C_CTL>)" != "$(git rev-parse <C_DATA>)"
exit 0

$ git merge-base --is-ancestor <C_CTL> <C_DATA>
exit 0

$ git merge-base --is-ancestor <C_CTL> <TIP>
exit 0

$ git merge-base --is-ancestor <C_DATA> <TIP>
exit 0

$ git log -1 --format='%an|%ae|%cn|%ce' <C_CTL>
kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local
exit 0

$ git log -1 --format='%an|%ae|%cn|%ce' <C_DATA>
kotoba-shokunin|kotoba@shokunin.local|kotoba-shokunin|kotoba@shokunin.local
exit 0

$ git show <C_CTL>:.ufo/waves/round-61/receipts/C1-worlds.txt | grep -cE '^W[0-9]+ .* exit 1$'
7
exit 0

$ git show <C_CTL>:verifiers/check_scoped_rules.py | sha256sum
<COUNTER_SHA256>  -
exit 0

$ git show <C_DATA>:.ufo/waves/round-61/C1-measure.txt | grep -F '<COUNTER_SHA256>'
<COUNTER_SHA256>  verifiers/check_scoped_rules.py
exit 0

$ git merge-base --is-ancestor <C_CTL> <C_DATA>
exit 0
```

Placeholders (all must be replaced by real values): `<TIP>`, `<C_CTL>`, `<C_DATA>`,
`<COUNTER_SHA256>`, `<YYYY-MM-DDTHH:MM:SSZ>`. The final `git merge-base --is-ancestor`/`exit 0`
pair is the line the frozen checker greps; keep it literal.

---

## 4. Failure modes (each named, with detection)

| # | Failure mode | How it manifests | Detection / prevention |
|---|---|---|---|
| FM-1 | **Measuring before committing controls (M90 class)** — `--fetch` runs before C_ctl exists/lands | C_ctl missing, or both files land in one commit; topology check fails or degenerates | Phase ordering (§2.1); V2/V3 catch the degenerate case |
| FM-2 | **Same commit for both** — `--is-ancestor X X` exits 0 trivially (§1.5) | Receipt looks green while controls and data share one commit (the M90 shape) | V2 strict inequality |
| FM-3 | **Reversed arguments** — `--is-ancestor C_data C_ctl` | Exits 0 only if data precedes controls; wrong direction passes | V3 + pasting the exact `C_ctl C_data` order in the receipt |
| FM-4 | **Non-commit / ambiguous / jj change-id hashes** — `merge-base` takes git revs; jj change-ids don't resolve; abbreviated hashes are ambiguous | `rev-parse --verify` fails or resolves wrong | V1 with `^{commit}` + `cat-file -t`; cite full 40-hex hashes from `landed <hash>` lines |
| FM-5 | **Unlanded / rewritten hashes** — citing a local-only commit that a recovery rebase later rewrites | Dangling hash; V1/V4 fail later | Cite only `landed <hash>` lines (helper prints them after remote verification; pushes are fast-forward only); re-run V3/V4 at final tip |
| FM-6 | **Identity violation** — author or committer not lane identity (e.g. `--as protocol`, seat's own git config) | Commit exists, is an ancestor, yet is not lane-identity (base `f3246d1` is the live counterexample, §1.3) | V5 checks `%an|%ae|%cn|%ce` exactly; jj-lane also blocks at commit and push |
| FM-7 | **Misroot (M79)** — checks run from the fleet root or without `git -C` | Lane SHAs don't resolve in the fleet repo; wrong go's refs may answer | Every command pinned to the lane repo; receipt records the lane path |
| FM-8 | **Grep-only fabrication** — receipt contains the two literal substrings but no real runs (Q31: checker does not judge honesty) | Counter shows 6 of 6 while claims are false | V8: every number in the receipt must be re-derivable by re-running the pasted commands at the recorded hashes; residual reviews re-run |
| FM-9 | **Format trap** — `exit=0`, `exit 0` split across lines, case-mismatched `Merge-Base`, or missing space | The frozen grep `"exit 0"` / `"merge-base --is-ancestor"` does not match → R-f scores 5 of 6, exit 1 | Use the template verbatim lines |
| FM-10 | **Checker run before receipt commit** — `--rev master` measured before the receipt lands | R-f reads missing at the measured rev → 5 of 6 | Phase 5 after the receipt commit; re-run at the final tip |
| FM-11 | **Branch-ref ambiguity** — lane `HEAD` is detached; `@{u}` is meaningless | Wrong "tip" used (e.g. HEAD, or a stale origin ref) | Always `git rev-parse master` (`refs/heads/master`), recorded in the receipt; checker default is `master` |
| FM-12 | **Wrong carried files** — C1-worlds.txt not in C_ctl or C1-measure.txt not in C_data | The binding checks fail even when all hashes/identity look right | V6/V7 `git show <commit>:<path>` |

---

## 5. Residual risk and verification gaps

- **Wall-clock probe order is not provable from git.** The DAG proves C_ctl precedes C_data in
  commit topology; it cannot prove the `--fetch` probe process ran after C_ctl was pushed. That
  ordering is enforced operationally (phase sequence, §2.1) and recorded in the receipt; the same
  declared limit as C1 arm A4 (cannot authenticate wall-clock fetch time against forged dates).
- **The frozen counter is a substring grep.** R-f's counter arm only requires the two literals;
  the honesty of the receipt rests on re-derivability (V8) and residual review. This is a known
  design limit of `check_routed_repairs.py` (Q31), not a defect of the receipt.
- **Not verified (does not yet exist):** the C1 counter v3 source, fixtures, and C1-worlds.txt are
  wave outputs not yet landed; V6/V7 content-binding checks are specified against the plan-pinned
  names and can only be executed after integration. The C1 measurement path `.ufo/waves/round-61/C1-measure.txt`
  follows the r60 precedent and the committed ExecReceiptsDesign item.
- **Tip moved during this review:** `master` was `7827628` (plan freeze) at first read and
  `c630c4c` (E1 erratum) at final read; both are lane-identity and landed. The spec's `<TIP>` is
  resolved at check time; no impact on C1/C2.
- All other claims in this report were exercised here: base control, self-test, identity demos,
  ancestry edge demos, tip/ref resolution, receipt existence at master (absent, exit 128).

## 6. Deliverable

The full R-f spec (§2), receipt template (§3), failure-mode table (§4), and grounding (§1) are
contained in this report — the L1 can lift §3 verbatim into
`.ufo/waves/round-61/receipts/controls-ancestry.txt` (with placeholders replaced) and must run
V1–V9 in order before committing it.

Installs: no installs.
Blockers: none.
Attacked/produced: defined the exact R-f controls-ancestry verification (checks V1–V9, phase order,
receipt template, 12 named failure modes) grounded in the committed checker, the C2 base control
(live re-run 0 of 6, exit 1), the lane-identity tooling, and live `merge-base` edge demos.
