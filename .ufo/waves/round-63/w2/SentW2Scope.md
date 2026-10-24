# SentW2Scope — scope and hygiene sweep

- **Role:** UFO-FSD sentinel / attack seat `SentW2Scope`
- **Item:** Wave-1 report placement, committed round-63 artifact secret/private-URL scan, and push scope
- **Axes:** path hygiene; credential/URL exposure; remote provenance
- **Severity:** **INFO / no committed-byte violation found.** Current checkout has unrelated untracked W2/runtime receipts (listed below); no W1-named report is among them.

- **Exploit path:** none found in the scoped committed artifacts or wave-report roots.
- **Impact:** no credential/session-token exposure or W1 evidence misroot found; the live untracked paths are W2/integration artifacts, not W1 seat reports.

## Attack and evidence

### 1. Wave-1 report placement / misroot

Plan and registry set `.ufo/waves/round-63/w1` as the W1 report directory. The registry has 32 members. At `cbbee56e9a3589b0b46736ad36f1b77701def80e`, the W1 tree contains 32 seat `.md` reports plus `swarm-registry.json`; the 32 report basenames match the roster. A basename sweep over the lane's `.ufo/waves/**` found the current W1 reports only under `round-63/w1`; the other matching basenames reported by the sweep are historical W1/build reports from rounds 58–62, not round-63 duplicates. The same 32-basename sweep under the fleet-root `.ufo/waves/**` found none. The exact fleet-root misroot path `.ufo/waves/round-63` is absent.

Relevant command output (verbatim):

```text
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --short --untracked-files=all
?? .ufo/waves/round-63/w2-dispatch.err
?? .ufo/waves/round-63/w2-dispatch.json
?? .ufo/waves/round-63/w2-spec.json
?? .ufo/waves/round-63/w2/swarm-registry.json
?? receipts.new-C1.txt
?? receipts.new-C2-interim.txt
```

These are current W2/integration artifacts, not W1 seat reports. Therefore the live worktree is not clean at the time of this sweep; this does not establish a W1 misroot. No wave-1 seat report appears in the untracked list.

Committed W1 paths were enumerated with:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only cbbee56e9a3589b0b46736ad36f1b77701def80e -- .ufo/waves/round-63/w1
```

The following is its verbatim output:

```text
.ufo/waves/round-63/w1/ConnSibling.md
.ufo/waves/round-63/w1/CriticC1Bound.md
.ufo/waves/round-63/w1/CriticCalib.md
.ufo/waves/round-63/w1/ExecCalibBefore.md
.ufo/waves/round-63/w1/ExecCalibInstrument.md
.ufo/waves/round-63/w1/ExecG9Attacks.md
.ufo/waves/round-63/w1/ExecG9Guard.md
.ufo/waves/round-63/w1/ExecLateWriteFold.md
.ufo/waves/round-63/w1/ExecLessonMistake.md
.ufo/waves/round-63/w1/ExecNoHarmBaseline.md
.ufo/waves/round-63/w1/ExecScorecardRow.md
.ufo/waves/round-63/w1/ExecSensorS049.md
.ufo/waves/round-63/w1/ExecSourceProbe.md
.ufo/waves/round-63/w1/ExecSourceS119.md
.ufo/waves/round-63/w1/ExecSourcesRow.md
.ufo/waves/round-63/w1/ExecV32SelfTest.md
.ufo/waves/round-63/w1/MutCalibInstrument.md
.ufo/waves/round-63/w1/MutG9Guard.md
.ufo/waves/round-63/w1/RevCalibChecks.md
.ufo/waves/round-63/w1/RevClaimC1.md
.ufo/waves/round-63/w1/RevG9Guard.md
.ufo/waves/round-63/w1/RevSourceQuote.md
.ufo/waves/round-63/w1/ScoutEligibleRisk.md
.ufo/waves/round-63/w1/ScoutG9Arms.md
.ufo/waves/round-63/w1/ScoutR62Defects.md
.ufo/waves/round-63/w1/ScoutRegistry.md
.ufo/waves/round-63/w1/ScoutS049.md
.ufo/waves/round-63/w1/ScoutSeatCounts.md
.ufo/waves/round-63/w1/ScribeCorrections.md
.ufo/waves/round-63/w1/ScribeEntry.md
.ufo/waves/round-63/w1/ScribeLesson.md
.ufo/waves/round-63/w1/ScribeReportSkeleton.md
.ufo/waves/round-63/w1/swarm-registry.json
```

The fleet-root exact-directory query returned `Path not found: .ufo/waves/round-63`; the targeted fleet `.ufo/waves/**/<32 W1 basenames>` query returned `No files found matching pattern`. A broader fleet-root `**/ExecG9Guard.md` query timed out; exact tool output:

```text
Glob timed out after 5s before finding any matches — the scan is incomplete, NOT proof of absence. The walk is bounded by directory size, not pattern width; scope the search to a deeper directory (e.g. `sub/dir/*.ext` instead of `*.ext` at a huge root).
```

An attempted Git `:(glob)` pathspec duplicate check was unsupported by `git ls-tree` and was not counted as evidence; the basename glob checks above are the replacement.

### 2. Credential, session-token, and private-URL scan

Scanned the committed S119 row and snapshot, `corpus/knowledge/compound-clause-citation-round63.md`, `corpus/lessons/round-63.md`, the appended `LOG.md` round-62 correction block (lines 2568–2575), `.ufo/waves/round-63/receipts/`, and `.ufo/waves/round-63/controls/`.

Scan query patterns and exact outputs:

- Credential assignment, credential-bearing URL, and private-IP URL pattern:
  `(?i)(?:api[_ -]?key|secret|password|passwd|authorization|bearer|session[_ -]?(?:id|token)|access[_ -]?token|refresh[_ -]?token|cookie)\s*[:=]\s*["']?[A-Za-z0-9_./+=:-]{8,}|https?://[^/\s:@]+:[^/\s@]+@|https?://(?:localhost|127\.\d+\.\d+\.\d+|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)[^\s"'<>]*`
  against the paths in line 70:

  ```text
  No matches found.
  ```

- Common credential-token/JWT/Bearer shapes:
  `(?i)(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{20,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}|(?:Bearer|Basic)\s+[A-Za-z0-9._~+/=-]{12,})`
  against the same paths:

  ```text
  No matches found.
  ```

The new row and lesson URLs are ICMJE, Cursor, publicationethics.org, and niso.org; the snapshot's visible third-party links/scripts are public CDN/Google/Annals/ACP endpoints. No private host, credential-bearing URL, authorization value, password, cookie, or session token was found. The snapshot's inline Cloudflare `r`/`t` page parameters are public page metadata; decoding the `t` value yielded `1792796702`, not an authentication value.

### 3. Push scope

Command `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin remote -v`; output (verbatim):

```text
origin	https://github.com/VeigaPunk/kotoba-shokunin.git (fetch)
origin	https://github.com/VeigaPunk/kotoba-shokunin.git (push)
```

Live remote check (verbatim):

```text
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-remote origin refs/heads/master
cbbee56e9a3589b0b46736ad36f1b77701def80e	refs/heads/master
```

Only `origin` is configured, and its live `master` tip is exactly the pinned commit.

## Verdict on committed bytes

At the pinned commit, all 32 W1 report files are in their assigned lane path; the wave-root basename sweep found no round-63 W1 duplicate elsewhere in the lane, and the fleet wave-root sweep found none. The requested landed security artifacts show no credential/session-token/private-URL finding. Push scope is the lane's single `origin`; live `origin/master` equals the pinned tip. No violation found.

## Smallest correction / explicit bound

No production correction is warranted. Exact proposed text: **“No correction proposed; the committed-byte sweep found no W1 misroot or credential/private-URL exposure. This finding covers the pinned commit and the current W1 basename placements under lane/fleet `.ufo/waves`; it cannot establish transient writes deleted before this snapshot or same-named files in arbitrary non-wave fleet directories.”** A broad whole-fleet-root glob timed out, so the fleet absence finding is deliberately bounded to the wave-report tree (the expected misroot surface).

- **Tooling:** no tools installed or updated.

Report: .ufo/waves/round-63/w2/SentW2Scope.md
