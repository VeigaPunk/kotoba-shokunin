# ScoutR65Registries — round-65 swarm-registry.json blobs at tip (r66 C2/D1 evidence)

Base for the round: `11385e04e368c1e94ab1a5a89d7439033eb1f855`.
Measured tip (jj working copy `@`): `98c994b017ca50393e0316c8409028f8cdeb4031`, parent `2a8eba56b3f9` ("round-66 verifier spot-check (integrator, hyaku): non-author admit/reject"). Working copy carries one unrelated modification: `M .ufo/waves/round-66/w1/swarm-registry.json`; both round-65 paths are clean.

## Observed

| Item | w1 | w2 |
|---|---|---|
| Path | `.ufo/waves/round-65/w1/swarm-registry.json` | `.ufo/waves/round-65/w2/swarm-registry.json` |
| Size | 12,844 B | 11,755 B |
| sha256 (worktree) | `a40abb1ac94e0d19fdf03cb383772985cb945d399a76c98da1fe629b5c5bcd30` | `d71ffed342bdb4e657886ca28c20bee1666f8ab10eacdd9ab96931671d7e551b` |
| sha256 (`git show` @ `98c994b0`) | identical | identical |
| Git blob id | `362c9969e78fb2478ddb4f940747bb63b946dfb1` | `d2866536da7d671a3095b86e80c43ea9894ea896` |
| JSON | parses, nonempty dict (6 keys: schema, wave, createdAt, updatedAt, reportDir, members) | same shape |
| schema / wave | `ufo-swarm-registry-v1` / `kotoba-r65-w1` | `ufo-swarm-registry-v1` / `kotoba-r65-w2` |
| members | 32 | 32 |
| createdAt | `2026-10-24T06:15:11.921Z` | `2026-10-24T06:15:11.947Z` |

- **Nonempty valid JSON:** both parse to nonempty dicts with real member sets — satisfies the counter's D1 byte predicate shape (`tracked_nonempty_json`, `verifiers/check_r66_routed_repairs.py:63-75`, paths at lines 30-33).
- **Tracked:** `git ls-files --error-unmatch` accepts both; index mode `100644` stage 0; index blob IDs equal the tip tree blob IDs (`git rev-parse 98c994b0:<path>`), and committed bytes equal worktree bytes by sha256.
- **Absent at pinned base:** `git cat-file -e 11385e04:…` → rc 128, "exists on disk, but not in '11385e04…'" for both paths. So they were indeed uncommitted working-tree artifacts at the pinned base — the D1 defect class as routed.
- **Landed by:** `806b53b4491d6a52856ee856cd9c7c20a5472e27` "round-66: land G9 coupling and integrity fixes" — `git diff-tree` shows both files added (`A`) with exactly the blob IDs `362c9969`/`d2866536` that survive unchanged at tip. No commit before it in `11385e04::@` touches these paths.

## Match to the routed D1 artifacts

- **Provenance corroboration:** `w1-dispatch.json` and `w2-dispatch.json` are already tracked at the pinned base and each embed `registry.path` = the exact committed path plus a `members` map equal to the live file's (32/32 members identical). The committed blobs are the rendered registries those dispatches name.
- **Timestamp corroboration:** file mtime `Oct 24 03:15` local (−0300) == `createdAt`/`updatedAt` `06:15Z` inside the JSON — the on-disk files are the artifacts the wave tooling generated, unmodified since.
- **Counter status:** `C2-routed-after.txt` records `check_r66_routed_repairs.py --rev fc1b71e5` → `D1-r65-registries-committed: PASS`, `2 of 2`, exit 0; pinned base stays `0 of 2` (`controls/C2-before.txt`). I did not re-run the counter; receipt observed only.

## Limits

- No pre-commit sha256 of the uncommitted blobs was recorded in repo text (grep for `a40abb`/`d71ffe` across `.ufo/`, `corpus/`, `LOG.md`, `SCORECARD.md` → 0 hits). Byte-identity with the pre-landing artifacts rests on git object custody (add-time blob IDs == tip tree == index == worktree bytes) plus the timestamp/dispatch corroboration above — strong, but not a pinned pre-commit hash pair.
- The counter's D1 predicate is structural (parses to nonempty dict), not byte-pinned; a regenerated registry of equal shape would also satisfy it.
- Only unrelated dirty file at tip: `.ufo/waves/round-66/w1/swarm-registry.json` (the prepared w1 wave render), outside this item's scope.

**Confidence:** high on tracked/nonempty/valid/absent-at-base/byte-stable-through-tip; high on artifact identity modulo the unrecorded pre-commit hash caveat.
