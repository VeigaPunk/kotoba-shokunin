# Kb79SN01Sentinel — round 79 w1, process and safety review

Seat: leaf sentinel. Scope: the round-79 plan as process, the helpers it lands through, the
counter it freezes, and the bytes this wave fetches. No edits outside this file and my receipts.
Tooling: nothing installed or upgraded this wave (no pacman, no network installs); only `git`,
`curl`, `grep`, `diff`, `sha256sum`, `python3 -B`.

Evidence file: `.ufo/waves/round-79/build/Kb79SN01Sentinel-receipts.txt` (R1–R10; every command
with its own exit status). Plan frozen at F1 `2c56622375641193a03bb97c0624e6536f3dffba`
(`git -C <lane> rev-parse HEAD` = that hash in my scratch clone). Lane base `b10bcbc6…`.
Counter sha verified: `sha256sum verifiers/check_tip_battery.py` =
`e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`, equal to
`receipts/freeze-shas.txt:2` and plan line 15.

---

## (1) Landing steps cannot commit outside the lane or delete a tracked path

Expected invocations (plan §Landing order, steps 1–4) and the guard that must stop a bad one:

| Invocation the L1 will run | Guard that stops the bad version |
|---|---|
| `scripts/hyaku/jj-lane.sh commit /home/vgpnk/Projects/shokunin/kotoba-shokunin --as KotobaR79 -m "r79 F1 …" -- plans/round-79.md .ufo/waves/round-79/receipts/` | `lane_realdir` (`scripts/hyaku/jj-lane.sh:77-88`) refuses the fleet root by literal *and* derived path, and refuses anything without a `.git` **directory** (worktree/submodule) → `commit /home/vgpnk/Projects/shokunin …` exits 1. |
| `jj-lane.sh commit <lane> … -- .`, `-- ../shokuknow`, `-- /abs/path`, `-- .git`, `-- .ufo`, `-- .ufo/state/x` | `repo_path_allowed` (`:506-518`) rejects `''|.|..|../*|/*`, `.git*`, `.jj*`, `.ufo`, `.ufo/state*`, `.ufo/watchdog.log` → exit 1 before any jj call. `take_lock` keys on the physical path (`:131-143`), so `commit .` and `commit /abs/lane` contend on one lock. |
| `jj-lane.sh commit <lane> … -- verifiers/ corpus/` (a directory request) | `validate_change_scope` (`:522-570`): every changed path must lie under a requested prefix (`:556` "commit changed a path outside the request"), statuses outside `A|M|D|T` fail, and a `D` whose path still exists on disk is refused (`:561`, nested-repo guard). |
| any commit with a stray `git commit` under the operator identity in the range | `candidate_has_identity` (`:589-596`) + `push_preflight` (`:200-232`, `:224-227`) refuse any author/committer not `<id>-shokunin` or `protocol-shokunin` → exit 3 at push. |
| `jj-lane.sh push <lane>` | `push_preflight`: conflicted bookmark/tip refused, non-descendant refused (`:215` "refusing a backwards/sideways push"). |
| a working copy parked on a non-tip parent | `cmd_commit` refuses a **non-empty** `@` on a non-tip base (`:689`), so a seat's `jj commit wip` is never swept in. |
| F1 receipt directory request `.ufo/waves/round-79/receipts/` + step 3 path list | `.ufo/waves/…` is deliberately committable (4,925 tracked `.ufo/waves` files at base), so receipts land as lane bytes as the plan says. |

Defects found:

### F1 — the fleet-shaped sandbox is writable, so a C1 measurement can mutate the fleet repo (MEDIUM)
`verifiers/check_tip_battery.py:175-203` builds the sandbox by `git clone --shared` into
`<tmp>/kotoba-shokunin` (`:189`) and then **symlinks every fleet entry** into the same parent
(`:197`, `(parent / entry.name).symlink_to(entry)`). The six gates then run with `cwd` = the
sandbox clone, so any gate that writes `../LOG.md`, `../.ufo/…`, `../AGENTS.md` or
`../<sibling-lane>/…` writes through the symlink into `/home/vgpnk/Projects/shokunin` or a
sibling lane. The counter's own contract says only "Read-only on the *lane*" (`:68`) — true — and
that is what the receipt would be read as.
- Exploit path: a repair or a future gate edit that "regenerates" a fleet-root file during the
  battery (e.g. writing `../.ufo/reports/...`), or a gate that appends to `../LOG.md`; the
  measurement prints `guards 5 of 5; tip battery exit 0: 6 of 6` while the fleet repo has changed.
  Nothing in the counter sees it: the sandbox is thrown away and no post-run status is taken.
- Impact: a green C1 receipt is compatible with an unauthorised fleet write. This is exactly the
  trust-boundary the round's own "write scope" section forbids.
- Smallest remediation (cannot land this round: the counter is frozen): add to `measure()`
  (`:361-400`) a pre/post pair `git -C <fleet> status --porcelain` and
  `git -C <repo> status --porcelain` and fail closed on any difference. Until then the L1's C1
  receipt must take a **pre-run** `git -C /home/vgpnk/Projects/shokunin status --porcelain` and
  compare the post-run one against it (baseline diff, not a clean-tree requirement: at
  2026-10-27T18:49Z the fleet tree already carried 4 pre-existing entries —
  ` M .ufo/reports/round-58/chousa.md`, `?? .scratch/closure-mado-r50.json`,
  `?? .scratch/source-routing-queue.md`, `?? o.bin` — none of them mine). My lane writes are the
  only files this seat created: `.ufo/waves/round-79/w1/Kb79SN01Sentinel.md` and
  `.ufo/waves/round-79/build/Kb79SN01Sentinel-receipts.txt`. Cheaper variant for the same counter
  version: symlink only the entries the gates read and copy the rest read-only.

### F2 — a named *directory* admits a deletion of any path under it (MEDIUM)
`validate_change_scope` refuses a `D` only when the path is still on disk (`:561`). A file that is
genuinely removed and then covered by a directory request is a legitimate `D` and lands. The
C1 battery's `no-deletions` guard covers only `corpus/`, `verifiers/` and `SKILL.md`
(`check_tip_battery.py:104-106`, `GUARDED_PREFIXES`), so a silent deletion of `plans/…`,
`PROVINCE.md`, `README.md` or a previous round's `.ufo/waves/…` receipt would pass both helpers.
- Exploit path: `rm corpus/lessons/<old>.md` then `jj-lane.sh commit <lane> -- corpus/lessons/`
  → lands; or any directory request in this round's step-3 list.
- Impact: unrequested loss of tracked bytes with no guard anywhere in the chain; for C2 the
  "snapshots, entry, SOURCES rows, SKILL.md rule …" step names a mix of files and directories.
- Smallest remediation: name explicit files in this round's commits (allowed — the plan's list is
  file-level already, except receipts), and treat the wave directory as the only directory
  request allowed; in the helper, refuse a `D` unless the deleted path is itself named.

### F3 — `.ufo/waves/round-79/build/` must not be committed wholesale (LOW)
The directory now holds other seats' raw fetched vendor pages (`Amp.html` 105 KB,
`Kb79S02SilentB-cursor/gemini/opencode.html`). Swept: no credential shapes (receipt R10), but
committing `build/` as a directory would land third-party page bytes into the lane as corpus-like
content under this round's message. Commit the seat reports/patches by name, or move research
pages out of the wave directory first.

---

## (2) Snapshot credential sweep

Method: each page fetched by me with `curl -sSL --max-time 45` — no `-b` cookie jar, no
`-H Authorization`, no `--netrc`, no credential on the command line (receipts R1, R2). Plain
pattern sweep and a token-shape sweep over the fetched bytes and over the six committed
snapshots (R3–R6).

Result: **no API keys, no secrets, no `op://` strings, no bearer values, no `Set-Cookie`, no
CSRF/verification tokens, no JWTs, no GitHub/Slack/AWS key shapes, no PEM blocks** in any of the
six surfaces. Every positive is documentation or site chrome:

- `spec` (S226): 0 hits on all six patterns.
- `claude` (S227): 1× `api_key` — line 253: "*…authenticates with an API key, or one where
  `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`, or an `apiKeyHelper` script supplies the
  credential*" — documentation prose, no value.
- `factory` (S228): `api_key`×8, `secret`×14, `cookie`×1 — docs-site nav links
  (`/docs/api-keys-keyid-rotate`, `/docs/api-keys-keyid-revoke`, `secret-scan`) and the
  `CookieBanner` class; no value.
- `msaf` (S229): `cookie`×3 — `id="cookie-consent-holder"`, `class="manage-cookies-holder"`,
  page chrome.
- `pi` (S230): 0 hits.
- `vibe` (S231): `api_key`×17, `bearer`×1 — documentation only:
  `export MISTRAL_API_KEY="your_mistral_api_key"`, `api_key_format = "Bearer {token}"`,
  `api_key_env` — placeholders, no value. Its fetch note explicitly records "no credentials,
  cookies or session data are involved".
- Token-shape sweep: the only `sk-…`-looking hits are `sk-learn-assistant-entry`
  (msaf, CSS class names at lines 453/469/471/485) — not keys.

### F4 — S229-msaf.html carries Akamai bot-manager *session* material and is not byte-reproducible (LOW)
An independent fetch of the same URL minutes after the seat's (`2026-10-27`, receipts R7) returns
156,963 B / sha256 `8fc249df…` where the committed snapshot is 157,339 B /
`34016233…`; `diff -u` rc=1 with exactly three differing lines, all Akamai Bot Manager:
`<script>bazadebezolkohpepadr="69065007"</script>`,
`<script src="https://learn.microsoft.com/akam/13/41ddb17" defer>` and the noscript pixel
`https://learn.microsoft.com/akam/13/pixel_41ddb17?a=dD1hMTA2…`.
- Characterisation: *not* a credential — a server-issued per-client bot-detection seed and beacon
  URL, no account linkage, no cookie jar, no authentication value. It is session-scoped state and
  it is the only such material in the round's snapshots.
- Impact (freshness/consistency, not secrecy): (i) the page is served non-deterministically, so a
  `recheck:` written as "fetch and compare sha256" can never pass for S229; (ii) the row's fetch
  record says "page did not move between the two fetches", which is true only for the seat's own
  two fetches and must not be generalised.
- Smallest remediation: keep the raw snapshot (the plan requires raw bytes), add to the S229 row's
  anchor cell "origin not byte-stable: Akamai Bot Manager instrumentation varies per response
  (sha 34016233… vs 8fc249df…, 2026-10-27)" and define `recheck:` as *the committed snapshot
  matches the MANIFEST pin*, never as a fresh-fetch equality. If the L1 prefers not to publish
  the seed at all, fetch S229 twice and keep a response without the `bazadebezolkohpepadr` line —
  but that must be recorded, not silent.

---

## (3) Prompt injection

Swept the six pages for reader-directed instruction patterns (`ignore previous|disregard|system
prompt|you are an AI|do not tell|exfiltrat|send the contents|curl … | sh|eval(`), then read every
hit. **No injection aimed at an agent.** Two findings:

- **F5 — an imperative-to-reader banner is present in two snapshots (INFO, benign).**
  `S226-spec.md:1-3` and `S227-claude.md:1-3` open with the Mintlify banner:
  `> ## Documentation Index` / `> Fetch the complete documentation index at:
  https://agentskills.io/llms.txt` / `> Use this file to discover all available pages before
  exploring further.` (claude variant: `https://code.claude.com/docs/llms.txt`). It is vendor
  chrome that tells the *reader* to go fetch another URL. It must be treated as data and never
  followed; it also confirms why the plan's Q70 rule matters — the first block of both snapshots
  is exactly the "banner / subtitle / first-heading block" a quote may not come from. No fix
  needed beyond a one-line note in the entry that the first block of S226/S227 is a docs-index
  banner.
- All other `system prompt` / `instructs the agent` hits are documentation subject matter about
  skills themselves, not instructions to the reader: msaf `:834`, `:847`, `:2283`, `:2544`
  (the last is a security recommendation — "Review before use … Check for adversarial
  instructions"), pi `:43`, vibe `:480`, `:870-885`. `factory` and `msaf` have no
  reader-directed imperative ("you must/should") in the fetched bytes.

---

## (4) Fixtures that could touch lane/fleet git

Checked every fixture-creating site that C1/C2 will run:

- `check_tip_battery.py`: worlds under `tempfile.TemporaryDirectory` (`:363`, `:476`); every git
  call carries `-C <lane>` (`:408-412`); and `_commit_all` asserts
  `git -C <lane> rev-parse --show-toplevel` **equals the fixture lane** before `add`/`commit`
  (`:415-417`) → a `TMPDIR` that points inside a real repo fails closed before any commit.
  This is the correct pattern (Git-fixture incident rule).
- `check_assertion_floors.py`: all `write_tree`/`swap` worlds under
  `TemporaryDirectory(prefix="floors-selftest-")` (`:785`); the refusing-`git` shim and its
  `PATH` override are written inside the same tmp dir (`:1398-1400`). No call outside tmp.
- `verify_corpus_integrity.py`: `_one_commit_repo` runs `git init -q <path>` (`:1037`) under
  `TemporaryDirectory` (`:1010`, `:1062`), with `-C` on every later call.
- `verify_corpus_independent.py`: `tempfile.mkdtemp(prefix="corpus-independent-selftest-")`
  (`:771`), `_git_init` → `_git(root, …)` (`:645-655`).
- The new C2 counter does not exist yet (`ls verifiers/check_allowed_tools.py` → ENOENT, and the
  plan freezes it only at F2). If it needs any git fixture it must copy `_commit_all`'s toplevel
  assertion; better, it should need none — the claim reads committed bytes only.

No fixture in the round can reach lane or fleet git. Residual noted: only the tip battery asserts
toplevel; the other three rely on `mkdtemp` + `-C` alone, which is sufficient but not asserted.

---

## (5) Scratch discipline in the counters C1/C2 will run

`grep -n 'mkdtemp\|/tmp'` over the three named files:

- `verifiers/check_tip_battery.py`: **no `/tmp` literal and no `mkdtemp`** — it uses
  `tempfile.TemporaryDirectory(prefix="k72-tip-")` (`:363`) and `…-selftest-` (`:476`), so it
  honours `TMPDIR` exactly as the seat spec requires.
- `verifiers/check_cn_vendor_surfaces.py`: `tempfile.TemporaryDirectory(prefix="k73-c1census-")`
  (`:558`) and `tempfile.mkdtemp(prefix="k73-c1-")` (`:1015`) — no `/tmp` literal.
- `verifiers/verify_corpus_integrity.py`: `/tmp` hits are `:231`, `:1189`, `:1197`, `:1212` —
  all string literals inside a path-class self-test (`token_path_class("/tmp/x/")`), not scratch
  directories.

Conclusion: no hardcoded `/tmp` in the counters C1 runs. Requirement for C2's new counter: use
`tempfile.mkdtemp(prefix="k79-…")`, never a `/tmp` literal, and never write into the sandbox
clone or the lane.

---

## (6) Defects in the frozen predicates and control worlds (calibration)

### F6 — C2 conjunct (c) names an artifact that does not exist at that path (MEDIUM)
Plan line 39: the snapshot's sha256 must equal "the pin in the committed `MANIFEST.sha256`". The
lane has no `MANIFEST.sha256` at its root (`find . -maxdepth 3 -name MANIFEST.sha256` → empty);
the round-73/74/76 convention is `.ufo/waves/<round>/snapshots/MANIFEST.sha256`
(e.g. `.ufo/waves/round-73/snapshots/MANIFEST.sha256` exists, and r73's entry cites
`snapshots/MANIFEST.sha256`). The r79 snapshots dir at 2026-10-27 18:5x has only per-file
`S###.manifest` — no combined manifest yet — and the plan's C2 data-commit list (step 3) does not
name generating one.
- Impact: if the counter resolves "MANIFEST.sha256" at the lane root every row fails (c) and C2
  cannot exit 0; if it resolves inside the entry's snapshots dir, the wave must still produce the
  file before the data commit. Today neither is stated.
- Fix (before F2): freeze the path as `.ufo/waves/round-79/snapshots/MANIFEST.sha256` in
  `sha256sum` format `<hex>  <basename>` (the r73 convention), add it to the step-3 commit list.

### F7 — C2 conjunct (b) can be satisfied by a snapshot fetched from a *different* host (HIGH)
The frozen host table (plan line 35) pins `factory` to `docs.factory.ai`, but
`https://docs.factory.ai/cli/configuration/skills` issues 2 redirects and the bytes the seat
committed come from `https://docs.factory.com/harness/skills.md` (receipt R2;
`snapshots/S228.fetch.json` records `"final_url": "https://docs.factory.com/harness/skills.md"`).
The plan's escape clause allows another URL form only "on the SAME host and path prefix" — not
the case. So one of two unstated rules is in force:
- counter matches the **cited URL only** → the row passes while its provenance host and path
  prefix are different, i.e. any redirect to any host would launder provenance, which is exactly
  what Q32 exists to stop;
- counter matches the **fetch record's final_url** → factory is unbacked and is the margin row
  (N=5, still exit 0).
- Impact: the pass/fail of C2 turns on an unstated rule; and the second reading means the claim's
  "N ≥ 5" is reached with the one row the predicate silently discards.
- Fix (before any data is scored; the counter is not frozen yet): freeze (b) as *both* the cited
  URL and the fetch record's `final_url` must match the surface host+prefix, and choose one:
  (i) re-pin the surface to `docs.factory.com` with `/harness` as the prefix and record the
  `.ai → .com` redirect chain in the anchor cell, or (ii) keep `.ai`, mark S228 as the expected
  unbacked row, and say so in the entry. Also note `docs.factory.com/harness/skills.md` is the
  markdown route, so the snapshot is text — good for quoting, but the row must say which route it
  cites.

### F8 — msaf's located quote must be a raw-HTML substring (INFO, satisfiable)
`S229-msaf.html` is the raw HTML snapshot; the field and its semantics are in one table row:
`<td><code>allowed-tools</code></td> <td>No</td> <td>Space-delimited list of pre-approved tools
the skill may use. Experimental - support may vary between agent implementations.</td>`. The
whitespace-token distance from `allowed-tools` to `Experimental` is ~12, inside the 5–25-word
cap, but the quote necessarily carries `<td>`/`<code>` tags. Freeze the word count on the
whitespace-collapsed raw substring (as the plan says) so the seat does not "helpfully" strip tags
and break (d)'s "occurs in its own snapshot".

### F9 — C1 control W1 attacks the wrong baseline file (MEDIUM)
Plan line 21's W1 is "`verifiers/baseline.json` rewritten to observed values with no index rows".
The corpus gate does not read that file: `verify_corpus_integrity.py:125` sets
`BASELINE_NAME = "corpus-baseline.json"` (repo-relative, docstring `:103-105`), and
`verifiers/corpus-baseline.json:13-15` carries `corpus.index.tracked_files expect 144` — the 150
vs 144 in the base receipt. `verifiers/baseline.json` is a different 9 KB file last touched in
round 72.
- Impact: the control world mutates a file the counter never opens, so it "fails as predicted"
  vacuously and proves nothing; a counter-defect that made the real baseline editable would go
  undetected — the exact failure mode the control set exists to exclude.
- Same confusion in `receipts/freeze-shas.txt`, which pins `verifiers/baseline.json` while the
  actual C1 repair must touch `verifiers/corpus-baseline.json` (and `LOG.md`, and the corpus
  index). Fix: W1 rewrites `verifiers/corpus-baseline.json` (expects 150 / 106) and must still
  read exit 1 through the `zero`-mode rows (`corpus.index.unindexed` 6); add
  `verifiers/corpus-baseline.json` to `freeze-shas.txt` as the pre-state.

### F10 — C1 control W5's premise is false (LOW)
Plan line 21: "W5 placeholder registry rows for the two verifiers with no real script". Both
scripts exist (`ls verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` → rc=0);
the base failure is that neither has a `SKILL.md` registry row (`grep -c
'check_desc_craft\|check_r75_routed_repairs' SKILL.md` → 0). As written the control does not
distinguish a truthful row from a placeholder one. Fix: restate W5 as "a registry row that parses
but is not backed by a real gate (nonexistent path, or `kind` mismatch)" — the meaningful
shortcut — and keep "two truthful rows" as the intended repair, not a control.

### F11 — C1 is reachable inside the `instrument-pin` guard (INFO, positive)
The plan's repair set is not blocked by the pin. In a sandbox built exactly like the counter's
(`clone --shared` + fleet symlinks + checkout `b10bcbc6`, receipts R8):
- `python3 -B verifiers/verify_skill_checklist.py --self-test` → `rc=1`,
  `1 failure(s) over 1863 assertions`, the one failure being
  `governance: live round-65 corrections land … LOG.md:2818: '.ufo/reports/round-76/kotoba.md'
  does not resolve`;
- `python3 -B verifiers/verify_skill_checklist.py` → `rc=1`, same `governance.citation_resolves`
  failure;
- `python3 -B verifiers/check_assertion_floors.py` → `rc=1`,
  `FAIL checklist observed=1863 floor=1863 self_test_failures=1` (the floors gate reruns each
  instrument's `--self-test`, `check_assertion_floors.py:640-656`, so the same dead citation
  surfaces there).
So two of the six gates close with one non-instrument edit (the LOG.md hop to
`../.ufo/reports/round-76/kotoba.md`), which `instrument-pin` does not touch. My first run from a
bare scratch clone showed 2 such failures instead of 1 — the extra one is the missing fleet
`.ufo` beside the clone, i.e. fleet-shape matters; a seat that measures from a bare clone will
report a false second failure. Record that in the C1 note.

---

## Severity summary

| # | Severity | Where | One-line |
|---|---|---|---|
| F7 | HIGH | plan:35,39 (C2 (b)) | factory snapshot's provenance host differs from the frozen host; predicate passes or fails on an unstated rule |
| F6 | MEDIUM | plan:39 (C2 (c)) | `MANIFEST.sha256` path unspecified and not produced; (c) unsatisfiable today |
| F1 | MEDIUM | `check_tip_battery.py:197` | fleet-shaped sandbox is writable; a gate can mutate the fleet repo during a C1 run, unseen |
| F2 | MEDIUM | `jj-lane.sh:559-562` | a named directory admits a deletion of any tracked path under it; C1's no-deletions guard covers only corpus/verifiers/SKILL.md |
| F9 | MEDIUM | plan:21 (C1 W1) | control rewrites `verifiers/baseline.json`; the gate reads `verifiers/corpus-baseline.json` |
| F4 | LOW | `snapshots/S229-msaf.html` | Akamai bot-manager seed in the snapshot; page not byte-reproducible, so `recheck:` must pin, not refetch |
| F10 | LOW | plan:21 (C1 W5) | control's "verifiers with no real script" premise false; tests nothing |
| F3 | LOW | `.ufo/waves/round-79/build/` | other lanes' fetched vendor HTML must not be committed by directory |
| F5 | INFO | S226/S227:1-3 | docs-index banner is imperative reader text; data, never instruction; also the Q70 banner block |
| F8 | INFO | S229 row | msaf's quote is a tag-bearing raw-HTML substring (~12 words) — satisfiable |
| F11 | INFO | C1 feasibility | both checklist-side reds close with one non-instrument LOG.md edit; pin does not block C1 |

No claim data was scored by this seat; no counter was edited; nothing outside this report and
`build/Kb79SN01Sentinel-receipts.txt` was written. Scratch `/fast/scratch/hyaku/kotoba-r79/Kb79SN01Sentinel`
removed after copying receipts.

VERDICT: round-79 is safe to land through `jj-lane.sh` (guards stop a fleet-root or out-of-scope commit), but C2 must fix the factory-host rule (F7) and the `MANIFEST.sha256` path (F6) before the F2 freeze, C1's W1 must target `verifiers/corpus-baseline.json` (F9), and the C1 receipt must record the pre/post fleet status because the frozen counter's sandbox is writable (F1).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79SN01Sentinel.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79SN01Sentinel-receipts.txt
