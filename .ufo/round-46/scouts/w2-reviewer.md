# R46 W2 reviewer — comparator correctness review (committed 36ab0d3, HEAD 78ee57e)

Scope: `git diff 055d3b9 36ab0d3 -- verifiers/ ':!verifiers/fixtures'` (5 files; comparator +475/-117) and fixture stat (31 files, +414/-5). Line numbers cite `git show HEAD:verifiers/compare_harness_independent.py` (sha256 `ccf41c23…bc04d`). Scratch: `/tmp/kotoba-r46-reviewer/` (repros in `rp/`).

## Self-test and floors

- `python3 -B verifiers/compare_harness_independent.py --self-test` at HEAD: `self-test: 0 failure(s) over 328 assertions`, exit 0.
- Floor values consistent: `check_assertion_floors.py` 255→328 (EXPECTED_INSTRUMENTS line ~124, INSTRUMENTS line ~148), `floors-registry.json` 328. Not run: the full `check_assertion_floors.py --repo` guard (reruns every instrument; not required by this assignment).
- Live producer at HEAD: `verify_harness_claims.py --json` exit 0, 28 rows, top-level keys `modes, observed, results, summary_paths, verdicts`.
- Full join at HEAD (command from the assignment) exits **2** — see H-2. Reproduced twice; frozen 055d3b9 comparator also exits 2 on identical inputs.

## Findings (ranked)

### HIGH-1 — C2a live-shadow checks are gated by a caller-controlled discriminator; the claim "cannot change only a row's mode/verdict and stay green" is false for non-producer shapes
- Code: `validate_live_metadata` L591–592: `summary = payload.get("observed")`; `producer_payload = isinstance(summary, dict) and bool({"omp","opencode"} & set(summary))`. The mirror-presence requirement at L602 runs only if `producer_payload`. Mirror checks at L595 run only if the key is present. A payload without `observed` (or with `observed` lacking omp/opencode) gets no mirror requirement, and `parse_live` (L659–678) then trusts row `mode`/`verdict` as-is. The module docstring (lines ~9–18 of HEAD) states the bound as "a caller cannot change only a row's mode, verdict or source-summary value and retain a green join"; that is not true for these shapes, and the docstring does not disclose the exemption.
- Repro (`/tmp/kotoba-r46-reviewer/rp/`; honest baseline A and control F):
  - A honest (observed 6, mode equal, FAIL, full mirrors) → exit 1 "disagreements".
  - B same values, row mode flipped to `positive`, `verdict` PASS, **no `observed`/mirrors** → **exit 0 "all checks agree, both instruments green"**.
  - C same flip but producer `observed` + mirror kept → exit 2 "live mode shadow" (shadow works when gated on).
  - H observed 7 (agrees), verdict FAIL→PASS, no `observed` → **exit 0** (control F with FAIL → exit 3).
  - G producer `observed` present, verdict flipped, mirror kept → exit 2 "live verdict shadow" (works).
  - Bare-list live payload `[{check,mode,observed,verdict:"PASS"}]` → exit 0 with no shadow checks at all.
- Repro commands: `python3 -B verifiers/compare_harness_independent.py --live-json rp/B.json --independent-json rp/ind7.json --cwd $PWD --scope-file verifiers/harness-independent-scope.json --expect-n 1 --no-stamp --json` (B = `{"results":[{"check":"omp.x","mode":"positive","observed":6,"verdict":"PASS"}]}`, ind7 = `{"results":[{"check":"omp.x","expected":7}]}`) → exit 0.
- Harm: a changed mode/verdict or dropped `observed` passes green. This is the exact claim C2a says is closed. The producer's emitted payload is not the attack surface; the gate is.
- Fix: require the three mirror maps unconditionally for any live payload that carries row channels (drop the `producer_payload` discriminator); update fixtures that lack mirrors. Do not key enforcement on a field the payload controls.

### MED-1 — omitted row verdict is treated as PASS
- `parse_live` L674–675 records `verdicts[cid]` only when `verdict` is a string; `decide_exit` (HEAD ~L1216) counts only non-PASS entries, so a missing verdict is green. Repro I: `{"results":[{"check":"omp.x","mode":"equal","observed":7}]}` → exit 0. Pre-existing (the `parse_live` body is unchanged in the diff), but it is the same hole as HIGH-1 once the mirror gate is removed. Fix together with HIGH-1: require `verdict` string per row.

### HIGH-2 (claim-blocking, pre-existing) — committed scope-out rows are payload-controllable; a live value for those rows is never compared
- The scope-out lock (committed set, reason, evidence, probe target) is satisfied when the payload declares a committed row out and supplies the recomputed census observable. The census is a property of the carrier (`~/.omp/agent/sessions`), not of the payload's derivation. Repro: live `omp.catalogue.found` observed 5; independent scopes it out with reason, evidence, `scoped_out_probes`, and the real recomputed observable → **exit 0 "all checks agree, both instruments green"**, `joined_scope 1, live_checks 2`. Control (same live, independent derives 6) → exit 2 "scope-out value laundering". So the four committed rows can leave the join and turn any disagreement green, as long as the carrier census is non-degenerate. `scoped_out_absent_from_live` only checks presence.
- Answer to the C3 question: yes, an attacker who controls the payload but not the scope file passes for the four committed rows. Non-committed rows are protected (laundering check L1092–1097 and `check_independent_scope_values`).
- r46 pins (reason L1100, evidence L1102–1113, target L1125–1136) do not close this; they validate the scope-out's text, not whether the rows should be out. The residual is pre-existing (r39 design). The `decide_exit` reason "all checks agree" overstates what was checked.
- Also: the census carrier is the lane's own writable session tree, so the payload-producing environment can influence `distinct_totals` (`[INFERENCE]`, not tested).

### HIGH-3 (claim-blocking, pre-existing) — the scope-out probe is not re-derivable on the live carrier; the committed join does not reproduce
- Live join at HEAD exits 2: `false blocker: scoped row omp.catalogue.{found,matched,missing_names,total} declares observable {candidate_blocks:1127, …} but recomputation gives {candidate_blocks:1131, …}`. Reproduced twice; the frozen 055d3b9 comparator with its frozen scope file fails identically (`cmp_frozen_run.py`, exit 2). 78 `*.jsonl` under `~/.omp/agent/sessions` were modified after the independent payload was produced (`find -newer`). The observable is a time-of-check value against a carrier that live agents write.
- Consequence: C3's "re-measurement at the committed bytes" cannot succeed while sessions change. The r46 fixtures use synthetic carriers and cannot catch this.
- Fix options (not implemented): snapshot-pin the carrier (hash the transcript set the observable was computed over and recompute over that snapshot), or drop the exact census-equality requirement to a stable invariant (e.g., `distinct_totals` set spread) before exact comparison.

### MED-2 — live/independent receipt sides are not closed against TOCTOU (scope side is closed)
- Scope side is fixed: single `read_bytes` (L896–897), hash of the same bytes (L928), receipt uses `meta["scope_sha256"]` (L1677, L2498). Parsed bytes == hashed bytes; `..`, absolute, and `--cwd` relative paths are resolved once (`build_meta` L2441–2444; repro from `/tmp` with `--cwd` resolves correctly).
- Not fixed on the other sides: `build_meta` reads `Path(args.live_json).read_text()` (L2397, L2410, locale encoding, universal newlines) and `side_receipt` hashes `text.encode("utf-8")` (≈L1640) and re-reads the file with `path.read_bytes()` for `file_sha256` (L1651). Two reads → the receipt can attest bytes different from those parsed if the file changes between reads. For CRLF files the `sha256` field is not the file digest `[INFERENCE: Python universal-newline semantics; not tested]`.

### MED-3 — extract_json: one duplicate-member fragment in prose aborts the whole load (availability regression)
- `extract_json` L237 and L265 call `json.loads(..., object_pairs_hook=_unique_json_object)` inside `except ValueError`. `DuplicateJSONMemberError` subclasses `CompareError`, not `ValueError`, so it escapes the brace scan. Repro: prose line `warn: saw {"a":1,"a":2} in log` followed by a valid payload → exit 2 `live: duplicate JSON member 'a'`; same payload without the prose line → exit 0. Fail-closed (no green), not a crash. Fix: catch the duplicate inside the scan and continue, or scope detection to the selected candidate.

### LOW-1 — scope evidence check is "any record"
- L1104–1110: evidence is required in at least one channel and every present copy must match. A scoped row missing `evidence` in one channel passes if another channel carries it. Current producer carries it in `rows` only (checked), `results` omits it. Tighten to "every channel record for a scoped row carries matching evidence".

### LOW-2 — receipt scope path is now machine-absolute
- `build_meta` L2441–2444 resolves the path; `render_receipt` L1676 records it. Receipts no longer compare across checkouts (previously repo-relative). Symlinked scope files record the resolved target, not the link path.

### LOW-3 — mirror maps reject empty and non-dotted id maps (fail-closed)
- `_dotted_map` (L287–290) returns None for `{}` and non-dotted keys; `validate_live_metadata` raises. Repro: `results:[]` with `modes:{}` → exit 2 "modes is not a check-id map"; `verdicts:{"x":"PASS"}` → exit 2. Only matters for zero-row or non-dotted live ids.

### LOW-4 — doc drift
- `harness-independent-scope.json` `round` still says "r39"; `probe_contract.target` is the literal `$HOME/.omp/agent/sessions` while `census_rule` says "absolute path". Code special-cases the literal (L1124–1128).

## Crash-class check (C2)
- 12 malformed live payloads (observed list/null, modes list, summary_path string/empty part, verdict null, non-string mode/check id, non-dict record, duplicate keys nested in observed). No Traceback in any; all CompareError → exit 2. `_channel_maps` L349–351 and `parse_live` L668–669 guard non-dict records before `validate_live_metadata` runs.

## Regression check
- Self-test 328/0 at HEAD. Fixtures: 13 new suites present; scope-file-cwd arm exercises honest vs planted cwd.
- No prior door reopened by the comparator diff that I could demonstrate; HIGH-1/MED-1 are gaps in the new C2a gate, and HIGH-2/HIGH-3 are pre-existing r39 behavior that r46's C3 pins do not close.

## Housekeeping disclosure (required)
- My first repro batch used a failed `cd`; heredocs wrote 28 stray files directly into the FLEET ROOT `/home/vgpnk/Projects/shokunin/`: `ind_mode.json`, `live_honest.json`, `live_bypass_noobserved.json`, `live_bypass_otherobserved.json`, `live_mode_honest.json`, `live_mode_flip.json`, `live_mode_flip_shadowed.json`, `live_nondict.json`, `live_nondict_noobs.json`, `live_prose_dup.json`, `err.{honest,bypass_noobserved,bypass_otherobserved,mode_honest,mode_flip_noobserved,mode_flip_shadowed,nondict,nondict_noobs,prose_dup}.txt`, `out.{honest,bypass_noobserved,bypass_otherobserved,mode_honest,mode_flip_noobserved,mode_flip_shadowed,nondict,nondict_noobs,prose_dup}.json`. Not deleted by me (per SOURCES/fleet instruction, integrator removes). Reported to W2RoundSouji-8. All other writes: `/tmp/kotoba-r46-reviewer/`, and this file.

## Per-claim verdict
- C1 (scope resolution / receipt): `no-harm found` on the scope path (single read, bytes hashed == parsed, `--cwd` resolution). Residual MED-2 (live/independent receipt sides) and LOW-2 are not C1-scope harms.
- C2 (live shadow / duplicate members): `harm: producer-gate bypass (HIGH-1) — dropping/altering observed or sending a bare list lets row mode/verdict change without mirror checks and stay green; omitted verdict = PASS (MED-1). Duplicate-member detection itself: no-harm found; its prose-fragment false-fail is MED-3.`
- C3 (scope-out reason/evidence/probe-target): `harm: committed scope-out rows can be dropped by a payload whose census-matching probe is supplied, turning live disagreements green (HIGH-2); and the probe observable is non-reproducible on the live carrier, so the join exits 2 at HEAD (HIGH-3).`
