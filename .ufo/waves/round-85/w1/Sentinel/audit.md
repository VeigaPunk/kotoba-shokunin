# Sentinel — round-85 scoped security audit

Axes: command safety, filesystem confinement, missing-input failure, provenance, secret exposure.
Read-only production review; receipts only. No production remediation or tool installation.

## Findings table

| id | file:line | severity | verdict |
|---|---|---|---|
| S85-01 | verifiers/check_substrate_pins.py:69,139,245–267 | informational | New default selects the actual non-symlink ELF; hashing and stat do not execute it. Missing binary is UNREADABLE, absent pin PIN_ABSENT; neither passes. |
| S85-02 | verifiers/verify_surfaces.py:170,295–312 | informational | Runs argv `strings -n 4 <binary>`, not the pinned binary; no shell interpolation. Missing binary/tool yields environment failure. PATH lookup of strings is inherited, not introduced. |
| S85-03 | verifiers/verify_harness_claims.py:53,94,280–286; verifiers/verify_harness_independent.py:125,175 | informational | Remaining two default-path changes feed byte readers. Claims uses SQLite mode=ro. No new binary execution or normal-path write introduced by defaults. |
| S85-04 | verifiers/verify_harness_claims.py:651–670 | medium, inherited | Missing baseline with --json returns 0 after observations, whereas text mode returns 3 at 692–694. This is a pre-existing fail-open outside the frozen C2 predicate, not a new defect from the path edits. |
| S85-05 | verifiers/verify_surfaces.py:2370–2374 | low, inherited | Self-test ledger fixtures use mkdtemp without cleanup: observed eight vs-ledger directories under explicit TMPDIR. No repo status change; no escape from TMPDIR observed. |
| S85-06 | corpus/SOURCES.md:1–436 | informational | Independent normalized content diff exit 0; 436 CRLF pairs removed, zero cell changes at observation. Only SOURCES changed CRLF count across 11,543 compared base regular files. |
| S85-07 | .ufo/waves/round-85/w1/ScoutSource/fetch-record.txt:13–31,42–51 | informational | Recorded curl commands are public HTTPS GETs, output only to scout scratch. S213 bytes are preserved by the existing snapshot; independent hash/size agree. |
| S85-08 | verifiers/check_description_render.py:264–275,359–379 | high for untrusted revisions | Executes target-revision census Python with inherited environment and permissions. TMPDIR placement does not sandbox the child; arbitrary external mutation, credential reads and forged R5 success are possible. Static finding; no exploit executed. |
| S85-09 | verifiers/check_description_render.py:330–352 | medium, provenance | R8 checks source/date/recheck markers and 3–25-word quote length, but no quote location or source-byte identity; an invented short quote can pass this rule. |
| S85-10 | verifiers/check_description_render.py:125–141,258–263,291–293,330–332,421–435 | informational | Missing committed inputs fail content rules; missing override/environment exits2. Disk --eval follows symlinks; committed symlink blobs become ordinary staged bytes. Fixed staging destinations and TemporaryDirectory honor TMPDIR. |

## Exploit paths, impact, smallest remediation

- **S85-04:** remove/unprovide the baseline and consume only `--json` process status; the observation-only branch can appear green without a comparison. Static evidence is the unconditional `baseline is None` success at line 670. Smallest remediation: require a readable baseline for comparison mode, with identical nonzero behavior in JSON/text; keep explicitly requested observation mode distinguishable. No live session/db reads were executed by this audit to demonstrate it. The round's two-command C2 predicate does not invoke this instrument.
- **S85-05:** repeated self-tests accumulate eight ledger fixture directories per execution. Use a shared TemporaryDirectory for those fixtures. The audit's outer scratch cleanup removes its own leftovers before completion.
- **Symlink boundary (inherited):** open/read_bytes/stat and inventory reads follow symlinks; there is no repo-root confinement guarantee for caller-supplied inputs. The default ELF is itself not a symlink. Normal scoring only reads these paths, but this is not a sandbox for untrusted worktrees. Missing inputs do not thereby become passes. If confinement is required, resolve and enforce approved roots before reading; do not describe the current behavior as symlink rejection.

## Independent content-diff proof

See `content-diff.txt`, `content-diff.json`, `line-endings.json` in this directory.

Executed the requested `git show BASE:corpus/SOURCES.md | tr -d '\r'` versus `tr -d '\r' < corpus/SOURCES.md` comparison independently: exit **0**, stdout **0 bytes**, stderr **0 bytes**. Base 203260 bytes/436 CRLF; worktree 202824 bytes/0 CRLF. Both normalized SHA-256 values:

`71bf6915a29498c23a87c86e417501b69d25ba0c422a166571a311e4d56a99e3`.

Batch-read committed regular-file blobs (symlinks excluded, never followed for this census) and compared 11,543 existing regular files. Only `corpus/SOURCES.md` changed CRLF count: 436 → 0, normalized content identical. This is a timestamped worktree observation, not a guarantee about later edits. The planned later S213 used-by addition would be a separate intentional cell edit, not part of pure normalization.

## Fetch provenance and read-only boundary

Scout record: HTTPS agentskills.io optimizing-descriptions.md, HTTP 200, **13403 bytes**, SHA-256 `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`. Independent hash and byte count of `.ufo/waves/round-76/snapshots/optimizing-descriptions.md` match. Command has no POST/data/upload option. Supporting best-practices fetch is also a public GET to scout scratch (15060 bytes, recorded SHA-256 ab9f3b60…). This audit did not refetch or execute fetched content.

Read-only mtime census of `/home/vgpnk/Projects/shokuknow` for files newer than 2026-11-04 16:45 returned **0 files**; scout also explicitly records zero writes. This corroborates but cannot forensically prove absence of an earlier write subsequently reverted or timestamp-restored. No fabricated filesystem monitoring claim is made.

## Exercised checks

- `TMPDIR=/fast/scratch/hyaku/kotoba-r85/Sentinel python3 -B verifiers/check_substrate_pins.py --self-test`: exit 0, **0 failure(s) over 62 assertions**.
- Same explicit TMPDIR, `python3 -B verifiers/verify_surfaces.py --self-test`: exit 0, **0 failure(s) over 218 assertions**. Expected missing-input arms printed errors; repo porcelain output unchanged across this run. Full output preserved in `surfaces-selftest.txt`.
- `file /home/vgpnk/.local/bin/omp`: ELF x86-64; SHA-256 `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`. No invocation of that binary by this audit.

## Final bounded verdict and exclusions

**No new fail-open in the inspected four default-path edits or the C2 pins/surfaces paths.** The inherited JSON missing-baseline defect S85-04 remains; it is not a C2 predicate success. No new execution of the pinned binary, normal-path write, or symlink-escape write was introduced by these changes. Existing readers follow symlinks; they must not be advertised as confinement guards.

`leak-grep.txt` preserves the literal-pattern/credential-shape scan. Available eval TSV: **no matches** for HOME=, TOKEN, KEY=, /home/, credential shapes or private-key headers. Knowledge entry and lesson were absent; no clean verdict for them. Integrated eval fixture was not present; authored wave TSV reviewed instead. Counter subsequently landed and received the static addendum below.

L1 explicitly instructed this seat to finalize current coverage rather than wait for those writers; L1 retains final-file inspection. L1 also reported C1 killed under the literal frozen R6 after duplicate/irrelevant forgeries scored 8/8; that is an attributed coordination fact, not an independently exercised counter result here. No predicate repair or production edit performed.

`resume_continuity_v1` is not part of this assigned instrument surface and was not exercised. Tools installed/updated: none.

Self-evaluation: accuracy4 (static findings, no exploit execution); completeness3 (entry/lesson transferred to L1); clarity4 (exclusions separated); actionability4 (smallest fixes named); conciseness4 (receipts separate). Overall3.8. L1 retains final-file inspection; this is not blanket approval.

## Counter addendum — newly available bytes

Inspected snapshot EEDC (686 lines), read-only, after L1 reported counter availability. No counter/self-test invocation or fixture git writes.

**S85-08 exploit path/impact:** an untrusted candidate commit replaces `verifiers/check_sibling_census.py`. `evaluate()` retrieves its bytes at359–366, and R5 stages/executes them at264–275 with inherited cwd, environment and user permissions. The child can mutate outside scratch, read secrets or fabricate the exact accepted stdout/exit; no timeout/process-group cleanup is supplied. Another missing content rule does not prevent R5 execution. Temp placement is not a sandbox. Smallest remediation: execute a trusted independently pinned census implementation, stage only measured data. This does not execute the omp ELF or use shell interpolation; the defect is executing revision-controlled Python.

**S85-09 exploit path/impact:** an invented short quotation plus source/date/recheck markers passes R8 without any location. This can fabricate sourced readiness. Smallest remediation: enforce the frozen located-quote requirement, corroborating source-byte provenance before describing the quotation as verified. No frozen predicate repair performed; C1 remains killed per L1.

Final overall finding is therefore **not** blanket “no new fail-open”: C2 inspected edits introduce none; the new counter introduces the S85-08 executable-input trust boundary and S85-09 provenance false acceptance.

Disposition recommendation: **quarantine failed counter bytes unchanged under wave/frozen; remove active verifier/registry routing, preserve historical evidence, and do not repair the frozen predicate into a claimed success.** L1 accepted that disposition and identified historical commit759cf354. This is attributed disposition, not a claim that this seat verified integration. No exploit executed.
