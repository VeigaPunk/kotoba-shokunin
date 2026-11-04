# Round 86 — kotoba (attempt 1, Linux host, omp/18.15.0)

Base: `e5d966b51494f4177868ad5f46806a204783ef6c` (`master`, the round-85 non-author
spot-check landing). Freeze: `ecfad51fe3f24540a6d67d2b54920929c7b83041` (plan, counter,
fixture and controls K0–K2, committed before any candidate data). One claim, on
freshness (tied-lowest non-retired axis with adjacency, both 8).

**C1 — freshness: the lane's omp catalogue model re-derived against omp 18.15.0**,
verbatim from `plans/round-86.md` § C1:

> **Surface changed:** the lane's executable model of how omp builds the `<skills>`
> catalogue a model sees — `verifiers/verify_harness_claims.py` (`WALKUP_REL`,
> `USER_ROOTS`, `discover_skills`, `parse_frontmatter`, `omp_key`, `preview`) plus a new
> roots ledger `verifiers/omp-skill-roots.tsv` whose every row cites a quote located in
> the omp 18.15.0 ELF.
>
> **Frozen predicate** (the same sentence here, in the counter's docstring and in every
> receipt):
>
>     python3 -B verifiers/check_omp_catalogue_repro.py --rev <rev>
>         -> prints "omp catalogue lines reproduced N of 215", exit 0 iff N >= 205
>            and guards G1-G4 all PASS; exit 1 otherwise; exit 2 = could-not-evaluate.
>
> **Target:** N ≥ 205 of 215 with G1–G4 PASS. **Base:** 83 of 215, G4 FAIL, exit 1.

Counter `verifiers/check_omp_catalogue_repro.py` sha256
`2390eec230743e3bc464b4253f563a6c45095360c6d3e2d14d6c054421ad6514`; fixture
`verifiers/fixtures/omp-catalogue-r86/catalogue.json` sha256
`0b3443e1058fffa75a287faca7d839d4bbfa3b7cd6f672783e1b0e70d714b488` (both printed at the
head of every receipt below). After value: `<L1 fills>` (measured by the L1 at the landing commit).

## Gate

- **S255 — opened this round (kind `code`, tier A, status `mined`, access date
  2026-11-04, recheck `on-release`).** The omp 18.15.0 TypeScript source embedded in the
  installed bun ELF `/home/vgpnk/.local/bin/omp`: `sha256sum` →
  `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`, `stat -c '%s %y'`
  → `276785328 2026-11-01 17:11:07.281808804 -0300`, `omp --version` → `omp/18.15.0`.
  Read with python `mmap` (ACCESS_READ) + `re`; nothing copied out. Module header
  `// packages/coding-agent/src/extensibility/skill-descriptions.ts` at byte offsets
  178767936 and 178768227; **located quote** (11 whitespace tokens, ≤ 25 words) at
  offset **178770368**, in that module: `const c = o >= E ? r.slice(0, o).trimEnd() : r;`
  (the `…` word cut, with `E = 40` the minimum cut). Upstream corroboration: tag
  `v18.15.0` of `https://github.com/can1357/oh-my-pi` (HTTP 200; raw
  `packages/coding-agent/src/extensibility/skill-descriptions.ts` 16 687 B, sha256
  `7321adfccb057f20da02d44793778f91eb449bd8101572e39ba8ed5c1b1cf6ee`, constants
  `MAX_PREVIEW_CHARS = 100`, `MIN_PREVIEW_CUT = 40`, `MAX_COMPRESSED_CHARS = 160`,
  `MAX_COMPRESSED_WORDS = 12` matching the ELF's `k/E/T/_`); byte identity is not
  claimed (the ELF holds a minified transpile). Record:
  `.ufo/waves/round-86/w1/ScribeSources/fetch-record.txt`; row text:
  `.ufo/waves/round-86/w1/ScribeSources/row.md`.
- **Rows added: 1 (S255)**, appended at `corpus/SOURCES.md:196` after S254 (next free id:
  `grep -oE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md | sort | tail -1` → `| S254` at base);
  `git diff --numstat -- corpus/SOURCES.md` → `1 0`. **Rows touched: 0** other rows.
  S255's `used-by` names `corpus/knowledge/omp-catalogue-model-round86.md` and
  `verifiers/omp-skill-roots.tsv`, so the census reads E11 until both paths exist (see
  census lines below).

- **Census before** — `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
  validate --root /home/vgpnk/Projects/shokunin kotoba` at the freeze → `census-exit=0`,
  **33** `W04` duplicate-URL warnings (plan § Frontier step), last line `kotoba ok
  /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`
  (`.ufo/waves/round-86/receipts/census-round-start.txt`). That receipt is a 4-line
  digest: `grep -c 'W04' .ufo/waves/round-86/receipts/census-round-start.txt` → **2**
  (S249, S254), so the 33 is not re-derivable from it. Re-derived on the base bytes by
  this seat: `git show e5d966b:corpus/SOURCES.md > $S/base-SOURCES.md && bash
  …/sources-census.sh validate --file $S/base-SOURCES.md | grep -c W04` → **33** (that
  form exits 1 with 249 `E11 … missing used-by` rows — every non-W04 row, e.g. `S002
  missing used-by SKILL.md` — because a scratch copy resolves `used-by` paths against
  the scratch dir; a form artefact, not a registry red; receipt
  `.ufo/waves/round-86/w1/ScribeLesson/census-base-file.txt`).
- **Census mid-round** (this seat, 2026-11-04, S255 present in the worktree): the `--root`
  form → exit **1**, 33 `W04` + 1 `E11 S255 missing used-by
  verifiers/omp-skill-roots.tsv`; read again after the ledger appeared → exit **1**, 33
  `W04` + 1 `E11 S255 missing used-by corpus/knowledge/omp-catalogue-model-round86.md`
  (both in `.ufo/waves/round-86/w1/ScribeLesson/census-mid-round.txt`). S255 reads clean
  only once ScribeEntry's knowledge entry exists. Not the after value.
- census after: <L1>

**Controls and self-test** (receipts in `.ufo/waves/round-86/receipts/`, each opening
with the counter and fixture sha256 above; executed before the freeze):

| id | world | observed | receipt sha256 |
|---|---|---|---|
| K0 | do-nothing: the round base's model | `omp catalogue lines reproduced 83 of 215`, G1–G3 PASS, `guard G4 roots FAIL (1): verifiers/omp-skill-roots.tsv absent at the revision`, `exit=1`; 132 `MISS` rows, all `not-discovered`, 0 `render-differs` | `c1-K0-base.txt` `ec418646052a40bd852e7f4be27450299670bc96400f668b93f7995fe0eea2da` |
| K1 | echo forgery (reads fixture/transcript, writes backdated fake SKILL.md) | sandbox denies the reads and the write: `83 of 215`, G4 FAIL, `exit=1` | `c1-K1-forgery.txt` `0397427af946c053cd8c59fe918180586514744ffa5e2bcbcd1903dce0c8bc53` |
| K2 | answer key: all 215 renders as module literals | `guard G1 no-echo FAIL (215): hardcoded render literal …`, `exit=1` | `c1-K2-hardcode.txt` `cfdfa95100012994bfd4533d41eced1bfa839dfcae804fca6a046960f18b2079` |
| S | counter self-test worlds | `0 failure(s) over 34 assertions`, `exit=0` | `c1-counter-selftest.txt` `ea77630f4168508411efb436c487f8b8b65aa064508fddea26b621f52fb7e9b4` |

Counting commands for K0: `grep -c '^MISS' .ufo/waves/round-86/receipts/c1-K0-base.txt`
→ 132; `grep -c 'not-discovered' …` → 132; `grep -c 'render-differs' …` → 0. Receipt
digests: `sha256sum .ufo/waves/round-86/receipts/c1-*.txt`.

**Addendum 1 — the counter amended before any candidate data**
(`plans/round-86-addendum-1.md`, commit `b9ee5484a139c4428a2d53e572868abe86844821`,
2026-11-04 19:27:12 -0300; counter sha256 now
`39a014f2f3142096b43031faedb0ea9819995fb2926138c3ebf2b194002e4520`; predicate sentence,
215 total, 205 target and fixture sha256 unchanged). Three attack-seat falsifications of
the frozen instrument (F1 Critic: one irrelevant root + a `*` ledger row read `215 of 215`,
exit 0; F2 Sentinel: `~/.omp/logs/http-400-requests/*.json` carried all 215 renders inside
the sandbox; F3 ReviewerCounter: an encoded answer key served through `preview` read `215 of
215`, exit 0) → three amendments: G4 dot-directory rule, sandbox allowlist + namespaces,
parent-side reference render. Controls re-run on the amended counter:

| id | world | observed | receipt sha256 |
|---|---|---|---|
| S | self-test | `0 failure(s) over 46 assertions`, `exit=0` | `c1-counter-selftest-a1.txt` `45bfe56b562a72756b2e04c6c2c6378cc7fb1ac658a818fd7032f6e2a2cbf5fb` |
| K0 | round base | `83 of 215`, G4 FAIL (no ledger), `exit=1`; 132 `not-discovered` | `c1-K0-base-a1.txt` `cd66a106fb83c58fbf5ef3e98f0e20f21014f3f12a13727c97e9a7c79d002c7b` |
| K1 | echo forgery | `83 of 215`, `exit=1` | `c1-K1-forgery-a1.txt` `642970799777753196a7d18952daaeac523620262a615958e502deeac5417904` |
| K2 | literal answer key | `guard G1 no-echo FAIL (215)`, `exit=1` | `c1-K2-hardcode-a1.txt` `39db34225de6f863823a183b2efe20217b70086db1b577d4286786aea00da5e6` |
| K3 / K3b | F1 world / per-root `.zcode` row | `215 of 215` but `guard G4 roots FAIL (216)` (first-segment wildcard / quote does not name `.zcode`), `exit=1` | `c1-K3-critic-wild-a1.txt` `2076b9a02324ca7f3b3a1baf90ce0476edda217e268f1070a273134900ffa366` |
| K4 | sandbox visibility probe | sandboxed: logs/sessions/cache/agent DB `absent`, network `blocked`, home write `denied`, 4 env vars; unsandboxed: 16 506 logs, network `open`, home `WRITABLE`, 274 env vars | `c1-K4-sandbox-a1.txt` `5cef9c3d9d66662050f42a41b1ce0cd10a931716b6e67a15584d3d600946eafc` |

Conflict reported verbatim, not judged here: the plan's kill rule lists "the counter,
its fixture or its pins changed after this freeze"; addendum 1 changes the counter after
`ecfad51` and before any candidate was scored, citing the round-74 addendum precedent.
Whether that is admissible is the judge's call.

**Candidate reading (ExecModel, not this seat's measurement):**
`.ufo/waves/round-86/w1/ExecModel/score.txt` — scratch commit
`903bd78e18c0dbb6d4013d9726d89dbe7c190bcd` (clone of `b9ee548` + candidate
`verify_harness_claims.py` sha256 `bd793b6c…0ab7`, `omp-skill-roots.tsv` sha256
`36021309…7800`), amended counter `39a014f2…4520` → G1–G4 PASS, `omp catalogue lines
reproduced 215 of 215`, `exit=0`. The lane worktree's two files carry the same sha256
(`sha256sum verifiers/verify_harness_claims.py verifiers/omp-skill-roots.tsv`, run by
this seat). Not the landing after value.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| **M86-1 — a model of an observed artefact was checked against a cache, not against the artefact, so its unmodelled lines read as a DRIFT count instead of as model failure.** The lane's catalogue check `omp_newest_catalogue` assumes "every line of the newest block must byte-equal a cached description" (its docstring). On omp 18.15.0 that premise is false: of the newest catalogue's 215 lines, 132 come from skill roots the lane model does not discover, and the check reports them only inside a DRIFT count against round-13 expected values — today `16/28 checks pass`, `omp.catalogue.total: observed=215 expected=7`, `omp.catalogue.matched: observed=15 expected=7`, `newest catalogue … (15/215 lines from cache …)`, exit 1 — never as "the model reproduces 83 of 215". The model itself was never asked to reproduce what omp showed. | `verifiers/verify_harness_claims.py:370` (`def omp_newest_catalogue`), docstring `:371-382`, premise sentence `:374-376` (same at the base: `git show e5d966b:verifiers/verify_harness_claims.py \| grep -n 'byte-equal a cached'` → `376:`); the docstring landed at `abef8aa` (round 10, 2026-09-28: `git log --format='%h %ad %s' --date=short -S 'must byte-equal a cached description' -- verifiers/verify_harness_claims.py`); base model measurement `.ufo/waves/round-86/receipts/c1-K0-base.txt` (`83 of 215`, 132 `not-discovered`); today's check output `.ufo/waves/round-86/w1/ScribeLesson/harness-base-catalogue.txt` | **none** — no criterion required a model to reproduce the observed artefact it describes; the DRIFT count was read as staleness of expected values, not as a model miss | a QUALITY criterion (proposal below; the L1 appends it to `corpus/QUALITY.md`), with the C1 counter as its first instrument |

**Criterion proposal (M86-1):** "A model of an observed artefact is scored by reproducing
that artefact line for line, and an unmodelled line counts against it." Scope: lane
models of observed client behaviour (render, discovery, listing). The reproduction
measure names its frozen artefact (path, line, sha256) and runs the model where it cannot
read that artefact (here: fixture sha256 `0b3443e1…b488`, scored inside bwrap with the
transcripts and cache hidden).

**The criterion can fail:** the round's base model fails it — `python3 -B
verifiers/check_omp_catalogue_repro.py --rev e5d966b51494f4177868ad5f46806a204783ef6c` →
`omp catalogue lines reproduced 83 of 215`, `exit=1` (K0 above; also `c1-K0-base-a1.txt`
under the amended counter). The same base model, under the pre-existing cache-match
check, never reported a failure of the model: the 132 lines were absorbed into a DRIFT
count. The old check also cannot tell a right model from a wrong one: with ExecModel's
candidate (215 of 215 under the counter) it still reads `16/28 checks pass`,
`omp.catalogue.matched: observed=35 expected=7`
(`.ufo/waves/round-86/w1/ExecModel/cli-after.txt`) — the same verdict as the base.

How long it stood: the premise sentence has been in the check since round 10 (`abef8aa`,
2026-09-28) — 76 rounds by number, 37 days by date. When the premise first became false
(the first newest catalogue carrying a line from a root the model does not know) is not
measured here; this round's brief says "~30 rounds" and no command in the record
re-derives that figure, so it is not adopted.

Integration note: `corpus/QUALITY.md` in the lane worktree already carries an
uncommitted `Q77` row (2 lines added; `git diff --stat -- corpus/QUALITY.md` →
`1 file changed, 2 insertions(+)`) that cites M86-1 and states the same rule in longer
form ("… scored by reproducing that artefact entry for entry from the client's own
inputs, and every observed entry the model does not produce counts against it …"). It is
the L1's row, not this seat's; the proposal above is the sentence it must carry.

## Routed defects (r85 spot-check)

From `corpus/lessons/round-85-verifier-spotcheck.md` § 6; dispositions as
`plans/round-86.md` § Routed defects names them (status-neutral; addressed, not claimed).

- **D1** count without its selection rule → corrected count in `corpus/lessons/round-85.md`
  § Correction, round 86: `git diff 1c8f37e cfcb9a4 -- corpus/README.md | grep -c '^+| '` → 9.
- **D2** tip after-value without receipt → stated: the round-85 C2 after-value's receipt
  is `.ufo/waves/round-85/receipts/c2-after.json` at `bf9ab28e011e4243356078951e33d919ad63a0c5`;
  no receipt exists at the tip `cfcb9a4` (`grep -rl 'cfcb9a4' .ufo/waves/round-85/` prints
  nothing, per the spot-check), so the tip was not re-run on the record.
- **D3** baseline note subject → additive note in `verifiers/corpus-baseline.json`
  (L1-integrated; the round-79 row is not rewritten).
- **D4** LOG range → corrected citation `LOG.md:3088`–`:3235` in `corpus/lessons/round-85.md`
  § Correction, round 86: `git show cfcb9a4:LOG.md | wc -l` → 3235.
- **D5** size pair → corrected wording in the same block: final size 202 884 B,
  `git cat-file -s cfcb9a4:corpus/SOURCES.md` → 202884 (202 824 B is normalization-only).
- **D6** truncated capture line → re-captured K4 line:
  `.ufo/waves/round-86/receipts/r85-D6-K4-recapture.txt` (sha256
  `cd3d5917ed57de80671a93263bb3df04510f0f81a72fa2c39f353535aa90f357`), first stdout line
  `FAIL omp_binary_sha256: sha256 drift: expect=6737ee24… got=ca9b3ee2…`, `exit=1`.
- **D7** WAVE-DONE unartifacted → this round commits `<wave>-wavedone.txt` with the
  orchestrator message (L1-integrated at settlement).
