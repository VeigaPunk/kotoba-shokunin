# A25Sentinel — security review of round-76 wave bytes (kotoba, w1)

Seat: A25Sentinel (leaf, report only). Role: sentinel. Axes touched: depth (credential/URL surface
enumerated from bytes, not assumed), consistency (every claim below names the command that produced
it), calibration (two gate artifacts tested with exploit fixtures, not described), freshness (live
re-fetch, live drift compare), coverage (58 files, digest-pinned), operability (repro commands),
adjacency (render-length convention, committed-history anchor).

VERDICT: PASS on CORPUS.md rule 6 — no credential material, no session tokens, no private URLs, no
`op://` references, no key/PEM/JWT material, no invisible-character smuggling, snapshot domains benign,
fetch records carry no headers at all. Two gate-integrity defects in the wave's own
`build/check_receipt_revs.sh` — F1 fail-open (MEDIUM, undisclosed), F2 wrong-revision acceptance (LOW,
disclosed by its author but still reported green) — both fixable in five lines, neither a rule-6
violation. No write outside this report was made by this seat.

## 1. What was reviewed, and when

- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (verified: `git rev-parse --show-toplevel`
  prints exactly that path).
- Surface: every file under `.ufo/waves/round-76/`. **58 files at final sweep, 2026-10-27T17:03:46Z**
  (the directory grew 15 → 58 files while this seat ran; the wave is live, see F4).
- Lane HEAD moved during the review (`4de12b61` → `7eed80e9` → `eab64394`). The whole round-76 wave
  directory stayed untracked throughout:
  `git status --porcelain` → `?? .ufo/waves/round-76/{build,receipts,snapshots,w1,w1.ready.dispatched}`.
  That is expected pre-freeze, and it is why every verdict below is pinned to a file digest rather than
  to a revision.
- Pinned digests of the security-load-bearing files at review time (sha256):

```
7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837  snapshots/optimizing-descriptions.md
a799805f3a285390c1b6e906b691f56684fa1031b499d177f664f464d99fb684  snapshots/evaluating-skills.md
ab9f3b6091a0f24816b52cd7b90a3fdf53e621f47dba13b36694be272b87fb41  snapshots/best-practices.md
37088074548703866fabcdab37305933e930d1a29b0775a3f1639ace77f0bdaa  snapshots/MANIFEST.sha256
96d7978d367dafce051abd59f584e2fba72ba9c02e23674b794676a519f79ad0  snapshots/fetch-record.json
caf84c403c589e71510b742db82a5db064023a2b0ff4a5352a444b11b8627a1e  build/check_receipt_revs.sh
186daadbe0e332b01a84771433b0e3dca9adc9059d56dd718abd945a608bdf7a  receipts/tip-battery.sh
6ff08be67d8e20312e541b7467c83f927c6c7f9e20882e015ffe188e77d1e4f9  build/entry-draft.md
253a382e170b3766bc7346dd5311cefb559e3156864f10ae8ea32def09d6f8aa  build/skill-patch.md
e7dc6330b1bbcdc678feb303856c22a19a6c53a43bddd477c244ec58809839ad  build/quotes-s213.md
fb7f9f7184ad0ce059e7654109a15a605938532182bba81858cb6877b2881c3d  build/scorecard-draft.md
a3c1e399acc928056aaa8edf7cee88ee09255fc993497159b873a3e25e370f9c  build/w2-registry-note.md
f8db05137cae12f24e292b8bebf811fab15892801cafc27ecf58962781f4226a  w1-spec.json
01daa750600dc9cdf1da6de578894160c7bf39cd8156f1f1db930ecce61478a7  w1-dispatch.json
```

Reproduce the full 58-file manifest with, from `.ufo/waves/round-76/`:
`find . -type f -print0 | sort -z | xargs -0 sha256sum`

**Scope boundary stated honestly:** bytes written after 17:03:46Z are not covered by the §1 digest
set. The wave kept producing (65 files by 17:06Z); every file written in that delta was re-scanned
with the same commands as §2 and §3 — the new `build/B08-*`/`lesson-draft.md`/`log-draft.md`,
`receipts/description-audit-4de12b61…txt`, `w1/A26SentinelAppend.md`, `w1/A27SimplifierAudit.md`,
`w1/B14SourcesUpdate.md`, `w1/B15Simplifier.md`, `w1/B18ScorecardScribe.md`,
`w1/B23GateRegistryCalc.md`, `w1/B27ReceiptVerifier.md` — **zero hits on every rule-6 pattern and zero
invisible characters**, so the verdict covers the 65-file state as well as the pinned digest set. A
later writer should still re-run §2/§3 over the landed wave before citing this PASS as covering the
frozen set.

**Seat adjacency:** `w1/A26SentinelAppend.md` is the wave's second sentinel and covers a different
surface (append-only integrity of `LOG.md`/`SCORECARD.md`/`corpus/lessons/round-75.md`/
`corpus/SOURCES.md` against `eab6439`). No overlap with this report's byte-surface review; the two
PASSes are independent and should not be read as one doubled check.

## 2. Rule 6 — credential material, session tokens, private URLs, `op://`

Scope text (fleet `CORPUS.md:129`): "**No credential material**, session or private URLs, or `op://`
references — ever."

Commands run at the final sweep (cwd `.ufo/waves/round-76/`), all patterns over **all 58 files, binary
inclusive** (`grep -rniE`, so binary hits would print):

1. Credential shapes: `op://|ghp_|gho_|ghs_|github_pat_|glpat-|xox[baprs]-|AKIA[0-9A-Z]{16}|
   AIza[0-9A-Za-z_-]{35}|sk-[A-Za-z0-9]{20,}|-----BEGIN|ssh-(rsa|ed25519)|eyJ[A-Za-z0-9_-]{12,}|
   Bearer [A-Za-z0-9._-]{12,}|(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*\S`
   → **zero hits** (the first sweep's only matches were the words "op:// refs" and "credential
   material" inside this seat's own dispatch prompt in `w1-spec.json`/`w1-dispatch.json`, i.e. the rule
   text, not a reference; excluded explicitly on re-run). Re-scanners should likewise exclude **this
   report** and `w1-spec.json`/`w1-dispatch.json`: the rule's own tokens (`op://`, the key prefixes)
   live in the pattern literals quoted here and in the seat prompt, so a raw grep will always hit them
   and nothing else.
2. Private/internal targets: `localhost|127\.0\.0\.1|0\.0\.0\.0|192\.168\.|10\.[0-9]+\.[0-9]+\.[0-9]+|
   \.internal\b|file://|ssh://|ftp://|s3://|gs://` → **zero hits**.
3. Sensitive local paths: `~/\.ssh|\.ssh/|id_rsa|id_ed25519|\.aws|\.config/gh|\.netrc|\.pgpass|
   \.gnupg|\.kube|credentials\.json|\.npmrc|\.pypirc|\.docker/config|/etc/shadow|/proc/[0-9]+/environ`
   → **zero hits**.
4. Signature-shaped or protocol-shaped secrets: PEM blocks, OpenSSH public keys, 12+ char JWT
   (`eyJ…`), `Bearer <token>` → **zero hits**.
5. High-entropy blob scan (my own heuristic: any `[A-Za-z0-9+/_=-]{24,}` run with Shannon entropy
   > 4.2 bits/char, ≥32 chars, excluding the three known snapshot digests and 40/64-hex tokens):
   every hit was a **path string** (`/home/vgpnk/Projects/shokunin/…`, `ufo/waves/round-76/…`). No
   secret-like blob.
6. Only URL schemes present: `https://` (12 distinct hosts, §3), plus `agent://B13SkillPatch` and
   `agent://B19LogScribe` — internal harness IRC addresses quoted in seat reports (B19LogScribe,
   B13SkillPatch coordination). These are not private URLs in the rule-6 sense (no credential, no
   network location, no secret path) and are the wave's normal peer-coordination text.
7. Invisible-character smuggling (zero-width, bidi overrides, soft hyphen, BOM): decoded all 58 files
   as UTF-8 and counted `\u200b-\u200d \u2060 \ufeff \u202a-\u202e \u2066-\u2069 \u00ad`, plus control
   chars other than tab/LF/CR → **0 files with any**.
8. Prompt-injection phrasing aimed at later readers (`ignore (all )?previous|disregard (all )?prior|
   you are now|do not tell|exfiltrat|send .* to https?://`) → **zero hits**. The nine hits for
   "system prompt" are the lane's own subject matter (kotoba audits system prompts) inside B21's
   measurement transcript and the entry's audit rows.
9. Filesystem hygiene: `find . -type l` → **no symlinks**; `find . -perm -o+w` → **no
   world-writable path**; no file above 50 MB (largest: `w1-dispatch.json`, 99,664 B).

Not a rule-6 finding, recorded for consistency: `w1/swarm-registry.json` is mode **600** while every
other wave artifact is 644. Content checked — 64 harness members (`kind`,`agentId`,`role`,`item`,
`axes`,`milestone`), **no secret**. Harmless; if the wave artifacts are meant to be readable by another
user, the mode is the odd one out (F5).

## 3. Snapshot domains, fetch records, provenance

**Domains are benign and public.** Host inventory over the snapshot set: `agentskills.io` (16 links),
`github.com` (2, `github.com/anthropics/skills/tree/main/skills/skill-creator`), and
`platform.claude.com` (1, deep link into Anthropic's Agent-SDK docs). All HTTPS, all public
documentation, no tracking query parameters anywhere (`grep -rhoE "https?://[^ )\"'<>`]*\?[^ )\"'<>`]*"`
→ zero hits: no `utm_*`, no `?token=`, no signed URL). The report-only hosts outside the snapshots
(`web.archive.org`, `vercel.com`, `junie.jetbrains.com`, `docs.roocode.com`,
`roocodeinc.github.io`, `ai.google.dev`) appear only in `w1/A22ScoutAssimilation.md` as citations of
lane registry rows; all public documentation hosts.

**Independently corroborated on the wire (not self-consistency).** At 2026-10-27T16:59:49Z this seat
fetched the three URLs from scratch with `curl -sS --max-time 25` (no `-L`, so a redirect would have
shown as non-200) and got `http=200 size=13403/16973/15060`; `sha256sum` of the three fresh bodies
equals the three snapshot digests byte for byte (`7cc54fbb…`, `a799805f…`, `ab9f3b60…`). So the snapshot
set is the live page, not a hand-authored copy, at a time independent of the two seats that fetched it.

**Committed-history anchor exists at the base rev (recommendation, see F6).** `git show
b7f13f4:.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md | sha256sum` → `7cc54fbb…`;
`…/S209-evaluating-skills.md` → `a799805f…`; `git show b7f13f4:.ufo/waves/round-74/snapshots/
best-practices.md | sha256sum` → `ab9f3b60…`. The same three digests are already committed at the base
revision, so a working-tree forgery cannot satisfy a history-anchored check.

**Fetch records carry no headers — structurally, not by filtering.** `snapshots/fetch-record.json` is a
JSON array of exactly three objects, each with exactly six keys: `url, fetched_at, http_status, bytes,
sha256, filename`. There is no `headers`, `request`, `response`, `cookie`, `authorization` or `set-cookie`
key anywhere in the wave (`grep -rniE '"(headers|authorization|cookie|set-cookie|x-api-key|auth|session|
credential)"' --include='*.json'` → zero hits). The record cannot leak a header it does not carry.
Byte counts and digests verified against disk (`bytes == len(file)`, `sha256 == hash(file)` → True for
all three); `sha256sum -c MANIFEST.sha256` → three `OK`, exit 0.

**Two external page claims with exact numbers were spot-checked** (fabricated live access is a
correctness defect in this seat's remit): A22's `https://vercel.com/blog/agents-md-outperforms-skills-in-
our-agent-evals` → HTTP 200, **899,785 bytes** (report says 899,785); `https://junie.jetbrains.com/docs/
agent-skills.html` → HTTP 200, **38,509 bytes** (report says 38,509; my run shows 38,509). Both exact.
`https://docs.roocode.com/features/skills` → **301**, and A22 discloses exactly that redirect chain
("served as Roo Code's current canonical documentation (`roocodeinc.github.io/Roo-Code/features/skills/`)").
No claim of live access without the access.

## 4. Findings

### F1 — MEDIUM (gate integrity, fail-open): the wave's Q36/Q50 checker passes on nothing

`build/check_receipt_revs.sh` (digest `caf84c40…`) exits **0** with a green line when it measured
**zero** receipts, and exits **0** when `--repo` does not exist.

Exploit path: a report can cite "receipt revision check: PASS n of n" while the checker saw no files
(a mistyped root, a receipts dir that has not been created yet, a wave whose receipts never landed).
The verdict line `PASS 0 of 0` reads as green.

Evidence (fixtures under `/fast/scratch/hyaku/kotoba-r76/A25Sentinel`, never in the lane):

```
$ bash build/check_receipt_revs.sh --repo <dir with four EMPTY round-7{3,4,5,6}/receipts dirs>
   receipts scanned: 0
   PASS 0 of 0 ; FAIL 0 of 0
EXIT=0
$ bash build/check_receipt_revs.sh --repo /fast/scratch/hyaku/kotoba-r76/A25Sentinel/nope
   ## .ufo/waves/round-73 : NO receipts directory …
   ## .ufo/waves/round-75/w1 : absent
EXIT=0
```

Impact: this is the gate-survivor family the lane has already paid for (`mistakes.md` §5 L1: a
comparison that accepts an empty prior, M030). It makes any "PASS n of n" citation from this script
unfalsifiable when n is small.

The author seat's report (`w1/B27ReceiptVerifier.md:115`) claims "The check is not vacuous:
`SELFTEST=1` drives the same verdict function over synthetic fixtures". That is true of *shape* and
false of *population*: every one of the ten arms injects at least one file, so the arms never observe
`total = 0`. Empirical check of the claim's edge (this report's fixtures): ten arms PASS, and the same
binary still exits 0 on an empty tree. The honest form of the claim is "not vacuous on shape; vacuous
on population until an empty-tree arm exists".

Smallest remediation (5 lines, no redesign): after the summary, `if [ "$total" -eq 0 ]; then printf
'0 receipts measured — cannot pass\n'; exit 2; fi`, treat a `--repo` that is not a git work tree
(`git -C "$REPO" rev-parse --show-toplevel` non-zero) as exit 2 rather than as "all rounds absent", and
add the matching `SELFTEST=1` arm (empty fixture must exit 2).

### F2 — LOW (disclosed gate limitation): "names a revision" is checked as "contains any 40-hex token"

The script grades a receipt `MEASURED` when a 40-hex token sits on a line containing a revision-ish
word, and `TOKEN` (still exit 0) when the token appears anywhere. It cannot tell the tip from the base,
a blob id, or a sibling lane's head; its own header says so ("TOKEN … may be a sha256, a blob id or a
sibling-lane head"), and the author seat states the same limit in `w1/B27ReceiptVerifier.md`: "A receipt
naming a wrong-but-full 40-hex rev passes." So this is a **disclosed** limitation, not a hidden bug —
graded LOW for that reason, and kept because the exit status still reports it as green (a disclosed
limitation that returns PASS is still a pass).

Exploit path (run and observed): a receipt whose whole content is `measured rev
b7f13f4b39cbd43076a85568adca763a6f674e7a` — **the base revision**, no measurement, no exit code —
scores `MEASURED`, `PASS 1 of 1`, exit 0:

```
   MEASURED        71  [receipt]  [UNCOMMITTED]  .ufo/waves/round-76/receipts/noharm-at-tip.txt
   MEASURED 1 / TOKEN 0 / PLACEHOLDER 0 / ABBREV 0 / FAIL 0
EXIT=0
```

And a receipt with no measurement at all plus one random 40-hex reaches `PASS 1 of 1`, exit 0.

Impact: Q36's rule is "names the revision **it measured**"; the check is satisfied by a token of the
right shape next to a keyword. A receipt that measures the base and claims the tip — exactly the
M75-1 failure mode — passes the checker and would be cited as clean.

Smallest remediation: add `--expect-rev <rev>`; when given (the tip battery always can), a `MEASURED`
token must equal it, else `FAIL` and exit 1; keep `TOKEN` as a **non-passing** advisory tier (or delete
the tier). Five lines plus one comparison. If the team prefers to keep the tier as-is, the report's
citation rule should read "n MEASURED of n" rather than "PASS n of n", so a TOKEN receipt cannot ride
into a green count.

The script's own `SELFTEST=1` arms (10 arms, run: 10 PASS / 0 FAIL, exit 1 only because my fixture held
an unrelated binary receipt) do not cover either F1 or F2 — the arms are all about token *shape*.

### F3 — LOW (hygiene, reviewed-benign): an executable lives inside `receipts/`

`receipts/tip-battery.sh` is mode 755 inside the directory the lane treats as **evidence**. A later
reader (or Q36 checker, which scans `receipts/**` and classed it `[other]`) meets an executable where it
expects a transcript. Reviewed byte by byte: `set -u`, no `eval`, no network (only the census script
and the verifiers), read-only git (`rev-parse`), writes only inside `mktemp -d "${TMPDIR:-/tmp}"` and
deletes only that dir via `trap … EXIT`, `"$@"`-passed commands (no string re-splitting), `--repo` and
`--rev` validated before use. **No defect in behaviour**; the finding is placement. Smallest
remediation: move it to `build/` (where the other wave script already lives) and leave a receipt that
says what it ran.

### F4 — LOW (process): wave artifacts mutate under read; one intermediate version was broken

`build/check_receipt_revs.sh` had three digests inside this session (`81898f5b…` → `ca4e3844…` →
`caf84c40…`). Against the second byte-state, my token-dump fixture aborted with
`line 193: uncommitted_list: unbound variable` under `set -u` (exit 1, truncated report). That byte-state
is **not** what is on disk now: the current file declares `fail_list=(); weak_list=(); uncommitted_list=()`
at line 110 and runs its arms clean. Recording it as a race, not a defect: **any verdict on a wave file
must name its digest**, which is why §1 pins 14 of them. Same hazard for the L1's integration pass —
re-hash before citing.

### F5 — INFO: `w1/swarm-registry.json` mode 600

Harness artifact, content checked, no secret (see §2). Only note: it is the one non-644 file under the
wave, so a landing step that copies wave artifacts should be explicit about mode.

### F6 — MEDIUM (provenance residual, with a cheap fix): three of C1's four digest homes are wave-authored

C1 conjunct (a) pins the snapshot digests in `MANIFEST.sha256`, `fetch-record.json`, the counter's
in-file table, and the lesson `## Gate` record. All four are written inside this same untracked wave
tree, so a coordinated forgery (fabricate page bytes, then write all four homes to match) satisfies the
conjunct without any touching of reality. Today's control is out-of-band: two seats fetched the pages
independently (B26 `urllib`, A24 `curl`) and so did this seat (16:59:49Z, §3) — all four body-hash sets
agree, and the r70/r74 committed copies are identical.

Smallest remediation, one line of counter logic: conjunct (a) should additionally require the
optimizing-descriptions digest to equal the blob digest of a **committed** historical snapshot at the
measured rev's ancestry — `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md` exists at the
base rev `b7f13f4` with exactly `7cc54fbb…` (verified above), ditto S209 and the r74 best-practices
copy. A working-tree forgery cannot satisfy that without rewriting committed history, which `--rev`
evidence would expose.

## 5. Adjacency checks run (kept because they are cheap and load-bearing)

- **Render-length convention (the C1(d)/R1 number).** Reproduced both sides on committed bytes:
  `yaml.safe_load('\n'.join(frontmatter_lines[1:end])+'\n')['description']` → **1022**;
  without the trailing newline → **1021**; first sentence → **151**; the manual fold (strip indent,
  join with one space) equals the YAML value exactly at both lengths. `plans/round-76-addendum-1.md`
  § "Render-length convention" names clip = 1022 and requires every receipt to print both variants,
  which matches B21's recipe. The residual risk is not the number but the implementation: a counter that
  slices naively gets 1021 and fails the frozen label while having measured correctly; a counter that
  hardcodes 1022 has turned measurement into a literal. Both are fail-closed at the tip, and the plan's
  required must-fail arm ("audit values that disagree with the recomputed ones") is what forces the
  counter to recompute. **Not yet testable**: `verifiers/check_desc_craft.py` and
  `verifiers/check_r75_routed_repairs.py` did not exist at 17:03Z, so conjunct (a)'s in-file digest
  table and (d)'s recompute have no bytes for me to attack this pass.
- **Write-scope escape.** Independent of A35: parsed all 64 tasks in `w1-dispatch.json` `taskCall.tasks`
  and extracted every `Report: write your scoped findings to <path>` route → **64 routes, 64 unique, all
  under `.ufo/waves/round-76/w1/`, none absolute, none containing `..`, no duplicate target**. Every
  non-lane absolute path in the wave is `…/scripts/sources-census.sh` (read/execute input, 2 mentions).
- **`resume_continuity_v1`**: not applicable to this surface, and stated rather than skipped — the wave's
  dispatch carries `counts = {spawn: 64, resume: 0, total: 64}` and `resumeSends: []`, so no
  resume-rejection path exists to verify against a canonical run loop. Same conclusion the round-64
  sentinel recorded for its wave.
- **Third-party bytes are treated as data.** The three snapshots are upstream markdown that the lane now
  reads as guidance; scanned for network/exec/script patterns (`<script|iframe|onload=|eval\(|exec\(|
  base64|curl |wget |pip install|npm install|sudo |rm -rf|chmod \+x`) → **zero hits**; the only HTML
  comments are the upstream page's own editorial asides (`<!-- Too verbose … -->`). The nine rules the
  entry drafts (B12/B13) are therefore drawn from prose the page itself writes, not from smuggled text.
- **Quotes re-verified independently** (adjacent to a security read, since a quote is a byte claim):
  parsed the JSON block in `build/quotes-s213.md` and recomputed every row — 13 rows, 13 verbatim in the
  optimizing-descriptions body, each **absent** from both other snapshots, each ≤25 words, each after
  the first heading (line 5), line numbers and word counts all matching → **0 mismatches**.

## 6. Install / cleanup / honesty

- Tools installed: **none** (system `curl`, `python3`, `sha256sum`, `git` sufficed). Nothing written to
  `~/.local/bin` or any PATH directory. No pacman (host-wide pause respected).
- Scratch: `/fast/scratch/hyaku/kotoba-r76/A25Sentinel/` (fixtures, fresh bodies, captured outputs) —
  **removed before this report is final**.
- Lane writes: this report only. No git/jj mutation of any kind; only `git status/log/show/cat-file/
  rev-parse/merge-base` were used. `.jj` exists in the lane and was not touched.
- Limits: I did not execute the two frozen counters (absent at review); I did not attack the entry,
  the SKILL.md patch or the lesson diffs for claim quality — other seats own those; my read of
  `build/entry-draft.md` was for credential/URL/injection surface and for the numeric claims named
  in §5.

## 7. Repro appendix (from `kotoba-shokunin/.ufo/waves/round-76/`)

```sh
# 1. full surface + digests
find . -type f -print0 | sort -z | xargs -0 sha256sum

# 2. rule 6 credential / private-URL / op:// sweep
grep -rniE "op://|ghp_|gho_|ghs_|github_pat_|glpat-|xox[baprs]-|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|-----BEGIN|ssh-(rsa|ed25519)|eyJ[A-Za-z0-9_-]{12,}|Bearer [A-Za-z0-9._-]{12,}" .
grep -rniE "localhost|127\.0\.0\.1|192\.168\.|10\.[0-9]+\.[0-9]+\.[0-9]+|\.internal\b|file://|ssh://|s3://|gs://" .

# 3. snapshot chain + live corroboration
( cd snapshots && sha256sum -c MANIFEST.sha256 )
for u in optimizing-descriptions evaluating-skills best-practices; do
  curl -sS -o "/tmp/live-$u.md" -w "$u http=%{http_code} size=%{size_download}\n" \
    "https://agentskills.io/skill-creation/$u.md"; done

# 4. committed-history anchor at the base rev
git show b7f13f4b39cbd43076a85568adca763a6f674e7a:.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md | sha256sum

# 5. F1/F2 repro (fixtures, never in the lane)
#    empty tree:                     bash build/check_receipt_revs.sh --repo <empty-fixture>   -> exit 0, PASS 0 of 0
#    nonexistent root:               bash build/check_receipt_revs.sh --repo /nonexistent     -> exit 0
#    receipt naming the BASE rev:    printf 'measured rev b7f13f4b39cbd43076a85568adca763a6f674e7a\n' \
#                                      > <fixture>/.ufo/waves/round-76/receipts/noharm-at-tip.txt
#                                    bash build/check_receipt_revs.sh --repo <fixture>        -> MEASURED, exit 0
```

A25SENTINEL-VERDICT: PASS-on-rule-6 (0 credentials, 0 private URLs, 0 op://, 0 secret headers, benign
domains, live-corroborated snapshots) with F1 fail-open on empty input (MEDIUM, fix before citing the
checker's PASS counts) and F2 wrong-revision acceptance (LOW, disclosed, exit status still green); plus
F6 provenance hardening: anchor C1 conjunct (a) to a committed historical snapshot digest, which exists
at the base rev.
