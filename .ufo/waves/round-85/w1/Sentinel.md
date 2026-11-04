# Sentinel scoped findings — round 85

Detailed findings table, exploit path/evidence/impact/minimum fixes:
`.ufo/waves/round-85/w1/Sentinel/audit.md`.

**No new fail-open in inspected four omp path edits and C2 pins/surfaces paths.** No new execution of pinned ELF or normal-path writes. Existing readers follow symlinks (not a confinement guard).

Inherited medium defect: `verifiers/verify_harness_claims.py:651–670` returns 0 in JSON mode if baseline is missing; text mode returns 3. Outside C2 predicate; static evidence only, no live-session probing. Smallest fix: consistent missing-baseline failure except explicit observation mode. Inherited low hygiene: `verify_surfaces.py:2370–2374` leaves eight ledger fixture directories under TMPDIR per self-test.

Independent content proof: requested normalized SOURCES diff exit0, empty output; 203260→202824 bytes, 436→0 CRLF, identical SHA-256 `71bf6915a29498c23a87c86e417501b69d25ba0c422a166571a311e4d56a99e3`. Of 11543 compared existing base regular files, only SOURCES changed CRLF count. Receipts: `Sentinel/content-diff.txt`, `Sentinel/content-diff.json`, `Sentinel/line-endings.json` (all relative to this report directory).

Leak scan: authored eval TSV no matches; exact patterns/output retained in `Sentinel/leak-grep.txt`. Entry/lesson absent at observations; L1 retains final-file inspection. Counter subsequently landed and was statically inspected (details below). No blanket clean certification for absent bytes or later commits. C1 killed per L1's R6 forgery report; no predicate repair attempted.

Scout recorded read-only public HTTPS GET, HTTP200, 13403 bytes; independent committed-snapshot hash matches `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`. shokuknow recent-file read-only census: zero files since16:45 (corroboration, not full forensic proof).

Exercised: explicit scratch TMPDIR, pins self-test exit0 `0 failure(s) over 62 assertions`; surfaces self-test exit0 `0 failure(s) over 218 assertions`. No production writes, git mutations, runtime invocation, or tool installations. Scratch cleaned before yield; receipts retained under Sentinel/.

## Counter security addendum

**High for untrusted revisions:** `check_description_render.py:264–275,359–379` executes census Python extracted from the measured revision with inherited environment/permissions; code can mutate outside TMPDIR, read credentials or forge success. Use trusted pinned executable code rather than candidate code. **Medium provenance:** R8 at330–352 accepts an invented short quotation without location/source-byte corroboration. Missing inputs otherwise fail statically; no new execution of pinned omp. Detailed table S85-08–10 in audit.md.

**Recommendation: quarantine the failed C1 instrument byte-exact under wave/frozen and remove active verifier/registry routing; preserve historical evidence, do not rewrite it into a new claimed predicate.** L1 accepted this disposition (reported historical commit759cf354); actual quarantine integration was not exercised by this seat. No exploit or counter invocation executed.
