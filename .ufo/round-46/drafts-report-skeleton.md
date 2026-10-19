# Round 46 report — [PENDING landing]

> This scaffold records the measured C3 result only. C1/C2, the full gate battery, SHONEN, landing, and round-close outcomes remain pending; do not infer them from this partial C3 record.

## Registration and measurement boundary

- Registration fields (`round=46`, `loop=A`, `position=10 of 12`, `seats=40`, and the preregistered depth/operability/calibration scores) are copied from `.ufo/round-46/claims.json`, not results. Recheck with `sha256sum .ufo/round-46/claims.json` and `python3 -m json.tool .ufo/round-46/claims.json`; observed SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53` at `2026-10-19T19:29:02Z`.
- Pre-write repository snapshot: `date -u +%Y-%m-%dT%H:%M:%SZ && git rev-parse HEAD && git rev-parse 'HEAD^{tree}' && git status --porcelain=v1` returned `2026-10-19T19:29:02Z`, HEAD `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae`, tree `e8dced184612a9738c5b8d244a0837fbd955a7da`, and only the pre-existing untracked `.ufo/round-46/` directory. Repeat that command at each measurement boundary; this is not the landing pin.
- Frozen before comparator: `git show 055d3b9:verifiers/compare_harness_independent.py | sha256sum` returned SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`. Freeze and run the same counting inputs against these bytes before claiming any red-to-green/green-to-red change; record the exact argv, cwd, input digests, stdout/stderr, exit, and before/after tree pins. Landing comparator/result: `[PENDING: landing commit, blob SHA-256, command, result artifact SHA-256]`.
- R45 recipe sources were pinned by `sha256sum .ufo/round-45/scouts/H05.md .ufo/round-45/scouts/R2.md .ufo/round-45/scouts/C2.md .ufo/round-45/scouts/S1.md corpus/knowledge/harness-independent-round41-census.md` at `2026-10-19T19:29:02Z`: H05 `29ea88455b3f43ea00b690c0c18743d32d829c945adc0dda01d003d5780f0d83`; R2 `ba2aa3b99ad45ab1b67b17916bcc3c67b13109cd95d07df977757cb7d5687f05`; C2 `b368715ca422cf15dc38bfb51fef99fc89f2dff55d2f774b32c71b7e9c38fe0d`; S1 `4c22966d719879d5370eaef6f91ae3a64cae4740db8f4cb4392b6daaddc3b083`; Round 41 census `286937b7a5d7d2e0c370282a13ef7cd326dc1e77e2263f57a8e11b1ba8ee6cc7`. Each report contains its reproduction recipe and limits; these are source pins, not fresh reproductions by B1.
- The current SCORECARD snapshot is SHA-256 `ee49aa071cfe670ec51aae9edc4e2db2468e0292406b20f995f42cba0ba9af9d`, from `sha256sum SCORECARD.md` at `2026-10-19T19:29:27Z`. C3 must reconcile it with the landing evidence; this scaffold does not edit it.

## Claims and landing cells

The exact claim text and the registered before/after conditions below are pinned by `.ufo/round-46/claims.json` SHA-256 `ff60fce90a203dbd793fa4fc21bd8e7139df196601e1b76d935aa62903af0e53` (re-run `sha256sum .ufo/round-46/claims.json`). Registered values are requirements, not measured outcomes.

### C1 — depth: scope-file cwd seam

- Required move: resolve `--scope-file` once against `--cwd`; receipt records the resolved path and digest of the file actually enforced.
- Registered planted-CWD before: exit `0`, `23/23`, planted superset enforced while honest-file digest is attested. Registered after: planted-CWD input exits `2` with a class-named error; receipt path/digest agree with the enforced file; honest join remains `24/24`. These values are claim-file expectations, not B1 measurements.
- Frozen-byte red-before replay command, exact arm/input hashes, and result SHA-256: `[PENDING]`.
- Landing-byte after replay using the identical inputs and the same runner: `[PENDING]`.
- Superset-scope control, honest-CWD control, receipt path/digest comparison, live join and floors evidence: `[PENDING]`.
- Disposition and depth verdict: `[PENDING: improved / harmed / unproven; evidence and scorecard command @ landing tree]`.

### C2 — operability: caller-supplied live JSON and raw duplicate members

- Required move: exercise caller-supplied mode/verdict/summary shadow fields and duplicate top-level `results` / per-record `re_derived` JSON members; either reject/class-name them or state the trust boundary with reason. The producer-vs-payload trust decision must be explicit.
- Registered before/after outcomes: `[PENDING: per-arm exit/class, explanation, input SHA-256, frozen comparator SHA-256, landing comparator SHA-256]`. Do not treat a last-wins decode as detected unless the raw-member arm actually proves it.
- Fresh producer and honest-join control, on the same source snapshot: `[PENDING]`.
- Disposition and operability verdict: `[PENDING: improved / harmed / unproven; no forced verdict]`.

### C3 — calibration: scoped-out probe/reason/evidence drift

- Required move: validate the scoped-out metadata against the committed file or declare it inside the trust boundary with a reason; reconcile the census and SCORECARD to the post-landing state.
- Frozen-byte replay: `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/drafts/v3/replay_scope_out_drift.py` exited 0; comparator copied from HEAD `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae`, SHA-256 `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; result `.ufo/round-46/evidence/v3/scope-out-drift-results.json` SHA-256 `076772f53d975c660570a18c5038283e2527a7ff08d646a8b0e550659e11f711`. The three targeted arms (`fabricated-reason`, `fabricated-evidence`, `unconstrained-probe-target`) each exit 0 at protocol 24/24, strict 20/24, four adjudicated/four scoped out; all remain accepted residuals, not class-named. No comparator change or trust-boundary declaration landed, so no landing-byte after result is claimed; per-arm inputs/outputs/receipts and hashes are in the result artifact and `.ufo/round-46/scouts/C3.md`.
- Census reconciliation: append-only Round 46 annotation in `corpus/knowledge/harness-independent-round41-census.md` leaves the historical R41/R45 46-arm counts unchanged, records these three accepted observations, and preserves R45's archived-target false-blocker disclosure. `sha256sum corpus/knowledge/harness-independent-round41-census.md` → `ef78ffe9d1c24674d04d5f1f9a68a44bb2c339989f93871f2d9b37b396158471`; no full 46-arm census replay is claimed here. SCORECARD records the same bounded finding; `sha256sum SCORECARD.md` → `2f217ddc5a091687c021eda51a74022de7aad2a7980686b3316201f8ccbfe517`. Claim-to-evidence: the registered C3 after-condition is unmet; this focused replay does not bound the full residual set or establish C1/C2/full-round status.
- Disposition and calibration verdict: **unproven / not improved**; calibration remains 8.5. No score increase or closure is claimed.

## Required verification record

C3-scoped documentation checks are recorded below; every other listed check remains pending. These results do not resolve the accepted C3 residuals or establish C1/C2/whole-round status. Preserve counting inputs/results under `.ufo/round-46/evidence/` and cite their exact SHA-256; do not rely on ephemeral output paths. If a `.ufo/round-46/drafts/` path is cited, explicitly tell the integrator to preserve it. At every run, record UTC instant, HEAD/tree, source hashes, command, exit, and output hash.

| Check | Re-run command | Result / output SHA-256 |
|---|---|---|
| Live producer | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_claims.py --json` | `[PENDING]` |
| Independent producer | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_independent.py --json` | `[PENDING]` |
| Live join | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --live-json <live.json> --independent-json <independent.json> --cwd "$PWD" --scope-file verifiers/harness-independent-scope.json --expect-n 28 --no-stamp --json --receipt <receipt.json>` | `[PENDING: protocol/strict counts, adjudicated/scoped-out counts, exit, receipt hash]` |
| Comparator self-test | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/compare_harness_independent.py --self-test` | `[PENDING]` |
| IND self-test | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_harness_independent.py --self-test` | `[PENDING]` |
| Assertion floors | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py --repo "$PWD"` | `[PENDING: all rows, exact vector, exit, stdout SHA-256]` |
| Corpus integrity | `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_corpus_integrity.py --json` | 2026-10-19T19:50:51Z; HEAD/tree `055d3b9a3f7eb28d13452a0d26853ef4feabf2ae` / `e8dced184612a9738c5b8d244a0837fbd955a7da`; source SHA-256 `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`; exit 0, 9/9 PASS; `.ufo/round-46/evidence/v3/final-doc-gates/corpus-integrity.stdout.json` SHA-256 `63b07476d14a168071670ec659e3725a66ad29f5589bcbd1cdfcea60d918f9d4`, stderr empty SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. |
| Independent corpus | `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_corpus_independent.py --json` | 2026-10-19T19:50:51Z; same HEAD/tree; source SHA-256 `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`; exit 0, zero unindexed/stale/missing/dead/unresolvable/nonhash findings; `.ufo/round-46/evidence/v3/final-doc-gates/corpus-independent.stdout.json` SHA-256 `97145f793a25f8a1e902ed33eb03f4df5c02aac20b36fa235bca52baf641f03c`, stderr empty SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. |
| Skill checklist | `PYTHONDONTWRITEBYTECODE=1 python3 -B verifiers/verify_skill_checklist.py` | 2026-10-19T19:50:51Z; same HEAD/tree; source SHA-256 `214ae44dcba45ba19656a0b2aa6c49900c618f6716a64fef0776f06437cfc8d0`; exit 1, 9 checks PASS and `governance.citation_resolves` FAIL for the pre-existing missing R45 draft runner documented in U1.md; not a C3 outcome. `.ufo/round-46/evidence/v3/final-doc-gates/skill-checklist.stdout.txt` SHA-256 `1fda35910cb99a09d8f5bcc3785119a7fa31a916e9891af8df8049a2f9ccdf29`, stderr empty SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. |
| Surfaces | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_surfaces.py --self-test` | `[PENDING]` |
| Substrate pins | `PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_substrate_pins.py --self-test` | `[PENDING]` |

The dispatch-provided expected floors, not verified here, are `10/150/91/87/1597/62/104/255/150`; rerun the assertion-floor command above. The relevant source pins were captured by `sha256sum` at `2026-10-19T19:28:23Z` / `19:29:02Z`: live verifier `6b8eb4b6e85b1640cbdbfedd10a6ee9055923caaad226736e7f672e8dff934f3`; IND verifier `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`; comparator `1101213a7bed5410151564aeb5a4b49030a4821c86e7469286f046253fbc51e4`; floors guard `b9e0ce16cdb5de8592ffd877de684560495118b499ef41209cd904027f5fc6ef`; floor registry `36536063ef803122c16a13cc9db6cad5cc47b58e173caeafa1fd6f2677619622`; surfaces `9fa10d44848a9ff7e9d516125beafe501d62d3df7dbcb777dd13fef074d69657`; substrate pins `bcfd5230eabb8b16343e11b21ec354d9860c65e4712187fc6650fc3f329495ce`; corpus integrity `28224c76510dcafc4d7a52da41ffd2d366337414f65320cbb21e6d9de12aba9d`; independent corpus `254b5a2f57aabbf0b8376fce34c42250b56499d9fd7a92b5e6374ac505315d69`; scope file `fbcdc8d247475a5f1c2c613d78b6188dab77a766b02497a729a884687a70f77a`. Recompute source hashes with `sha256sum` at the actual check instant; these are not output-pass claims. The dispatch-provided live-join baseline is protocol `24/24`, strict `20/24`, four adjudicated and four scoped out; not rerun by B1. Reproduce with the producer/join commands above and pin the emitted output and receipt hashes.

## Round close

- Per-axis verdicts (depth, operability, calibration): `[PENDING]`.
- SHONEN check and mark (if applicable): `[PENDING]`.
- Landing commit and final tree: `[PENDING]`.
- Changed paths and post-write status: `[PENDING]`.
- Integrator preservation note for evidence artifacts: `[PENDING]`.
