# A21NoHarmBattery: round-48 falsify, no-harm battery (attempt 2)

Seat KotobaR48.A21NoHarmBattery (leaf). Lane /home/vgpnk/Projects/shokunin/kotoba-shokunin. Scratch work lives under /fast/scratch/hyaku/kotoba-r48-a2/seats2/A21NoHarmBattery/.

## Verdict

- DEFECT, medium, resolved at lane HEAD. Records commit 84b9c9b turned `verifiers/verify_skill_checklist.py --json` from exit 0 to exit 1. Cause: its new SCORECARD.md:110 pointer `.ufo/reports/round-48/kotoba.md` names a report that exists nowhere yet. At eb5a80f (current lane HEAD) the path token is gone and the gate is exit 0 again (11 PASS, 0 FAIL).
- DEFECT, low, latent, still open at eb5a80f. C2's configured-root count keys skills by directory name, while the agents-root count keys them by frontmatter name. A configured skill whose directory differs from its name is counted twice (probe: 4 to 5). No effect on this host.
- No other gate regressed. Every other change is an intended round-48 floor, arm or corpus-baseline change, or live host state. The gates that fail (pins, surfaces, harness claims) fail identically at 75f671b.

## Revisions and method

- Four revisions: 75f671b (base); 84b9c9b (assigned tip); eb5a80f (lane HEAD, which moved during the run through d28b16b, 2788704, 48819b9 and eb5a80f); and eb5a80f plus the lane's uncommitted edits (four corpus files, see Lane state).
- Each revision runs in a mirror: a `kotoba-shokunin` clone whose parent holds read-only symlinks to every fleet-root entry. This is required. The checklist resolves `../.ufo/...` and `../PROTOCOL.md` against the checkout's parent, so in a bare scratch clone base also exits 1 (checked: logs/ base run, name_directory and citation FAIL). The mirror reproduces the lane's layout.
- Deadline: 900 s per gate, enforced by subprocess timeout. Longest gate 28.5 s. None timed out.
- Lane access was read-only: `git clone` from the lane, `git --git-dir ... rev-parse / log / ls-files --others`, `cmp`, `test -e`. No lane writes, no index refresh.
- Installed or upgraded: nothing. Used system python3 3.14.8, bash and git.
- Logs: logs-mirror (75f671b, 84b9c9b), logs-eb5 (eb5a80f), logs-wt (working tree), logs-extra (concurrent and back-to-back runs, compare driver), each with summary.json.

## Battery table (exit code; key result; cause)

| Gate | 75f671b base | 84b9c9b tip | eb5a80f HEAD | Cause and verdict |
|---|---|---|---|---|
| verify_harness_independent.py --self-test | rc0, 104 assertions | rc0, 115 | rc0, 116 | d1ae458 (+11 arms); 48819b9 (+1). Intended. |
| verify_harness_independent.py --json | rc0 | rc0 | rc0 | d1ae458 changed the evidence wording only; oc.roots.names_plus_builtin = 10 at all three. candidate_blocks and session_files move with the live session census (6069 for all three in one concurrent run). No harm. |
| check_assertion_floors.py | rc0, harness_independent 104/104 | rc0, 115/115 | rc0, 116/116 | d1ae458 (registry and script); 48819b9. Intended. |
| verify_skill_checklist.py --json | rc0, 11 PASS / 0 FAIL, governance 872 | rc1, 10/1, governance FAIL at SCORECARD.md:110 | rc0, 11/0, governance 901 PASS | 84b9c9b caused the FAIL. eb5a80f removed the token. 887b6af added one citation (SKILL.md 44 to 45). DEFECT, finding 1. |
| verify_skill_checklist.py --self-test | rc0 | rc0 | rc0 | No change. |
| verify_corpus_integrity.py --json | rc0, tracked 61, report_total 40 | rc0, tracked 63, report_total 40 | rc0, tracked 63, report_total 41 | 887b6af (61 to 63; corpus-baseline.json moved with it). eb5a80f added one host-absolute pointer (40 to 41). Intended. |
| verify_corpus_independent.py | rc0, 61 files / 79 tokens | rc0, 63 / 81 | rc0, 63 / 81, report 41 | Same commits as above. Intended. |
| check_substrate_pins.py | rc1, DRIFT 2/3 (omp sha 85d9daf3 vs pinned fdbc8136; mtime) | rc1, identical | rc1, identical | Host omp binary. verifiers/baseline.json has blob 7fe48e9734c9 at all three. Pre-existing, not round-48. |
| verify_surfaces.py --json | rc1, 5/7 PASS (literal_present, no_uncovered_class FAIL) | rc1, identical | rc1, identical | Host omp. Surfaces baseline and census untouched. Pre-existing. |
| verify_harness_claims.py | rc1, 21/28, 7 DRIFT | rc1, same 7 DRIFT | rc1, same 7 DRIFT | Host state (catalogue timestamp, session count). Script and baseline untouched. Pre-existing. |
| compare_harness_independent.py --self-test | rc0, 331 lines | rc0, identical | rc0, identical | No change. |
| fault_injection_corpus.sh | rc0, ALL PASS | rc0, ALL PASS | rc0, ALL PASS; fault-f and fault-h control counts 40 to 41 | eb5a80f's new pointer. No harm. |

Extras, run at all three revisions (rc0 each): fault_injection_corpus.sh --self-test ("self-test: OK"), and --self-test of verify_corpus_integrity, verify_corpus_independent, verify_surfaces, check_substrate_pins, verify_harness_claims and check_assertion_floors. Output identical except the fault harness's temp-directory name (a PID on its first line).

Not in the list, run anyway: compare_harness_independent.py --json exits 1 at 75f671b and at 84b9c9b, with the same disagreement set (18 of 24 protocol agreements, 6 disagreements, 4 scoped out). LOG.md's "exit 2" claim for base is not reproduced. The compare driver's output moves with live state.

Working-tree mirror (eb5a80f plus lane edits): every rc matches the committed eb5a80f run. verify_corpus_integrity JSON and the checklist are identical to eb5a80f. Only path headers, harness timestamps and the live census differ.

## Attribution of count changes (verifier's own citation_subjects and citation_resolve)

- SKILL.md citations 44 to 45: adds `corpus/knowledge/frontmatter-rule-authorities-round48.md` (resolves). Commit 887b6af.
- Governance 872 to 901 = LOG.md +20 plus SCORECARD.md +9, all from 84b9c9b. The one LOG.md subject that does not resolve (line 2111, `.ufo/round-45/drafts/v10/post-r44-hunt.py`) is excused by a pinned errata row at all revisions. Pre-existing.
- The only non-resolving subject at 84b9c9b: SCORECARD.md:110 `.ufo/reports/round-48/kotoba.md`. It is absent from the lane tree (git ls-tree at 84b9c9b shows 25 tracked reports, rounds 20 to 45 only; lane path test -e absent) and from the fleet (`.ufo/reports/round-48/` holds only kotodama.md).
- C1 claim, knowledge Markdown entries 34 to 35: confirmed with git ls-tree at 75f671b (34), 84b9c9b (35) and eb5a80f (35).

## Finding 1: checklist gate regression at 84b9c9b (DEFECT, medium, resolved at eb5a80f)

- Rule (verify_skill_checklist.py docstring at 84b9c9b, lines 187 to 199): every governance subject "must resolve at HEAD", except quoted meta-findings, literal round-N schematics, and LOG.md lines pinned by GOVERNANCE_ERRATA. SCORECARD.md has no errata route.
- Lane convention at base: every SCORECARD report pointer (rounds 37 to 45) resolves to a tracked report. 84b9c9b is the first pointer to a report that did not exist.
- Evidence at 84b9c9b: rc1; governance line "SCORECARD.md:110: '.ufo/reports/round-48/kotoba.md' does not resolve from .../mirror-tip/kotoba-shokunin".
- At eb5a80f line 110 reads "Report: the round-48 kotoba report in the fleet repository's reports tree." No token, so the gate is rc0 (11 PASS, governance 901 PASS). The report itself still exists in neither tree. Closure must write it, or the reference must stay prose.
- S020 in corpus/SOURCES.md says `--json` exit 0 at 75f671b with 11 PASS and 0 FAIL. That holds in the fleet-shaped mirror. It is false at 84b9c9b (exit 1) and true again at eb5a80f (exit 0).

## Finding 2: C2 keys skills two ways (DEFECT, low, latent, open at eb5a80f)

- Code at eb5a80f, verifiers/verify_harness_independent.py: line 606 keys agents-root skills by frontmatter name (`skill["frontmatter"].get("name") or skill["dir"]`). Lines 608 to 624 key the configured and log-named roots by directory name (`names.add(entry.name)`). The C2 comment at lines 595 to 597 says "the same operator for every root", which is not true across these two keyings.
- Probe, scratch file probe/dir_vs_name_probe.py, run against the eb5a80f module: the fixture (twin=False) counts 4. After adding skill/renamed-dir/SKILL.md with `name: alpha` (the agents root already offers alpha), the count is 5. The new configured skill is counted under its directory name while the agents root already holds the same frontmatter name.
- Effect on this host: none. The default --oc-config is /home/vgpnk/.config/opencode (line 127). Its skill/ and skills/ are absent, so the evidence line reads "present: none".
- Test gap: build_configured_root_fixture (lines 895 to 944) gives every configured skill a directory equal to its name. No arm exercises the alias case.
- Whether opencode keys skills by frontmatter name is [INFERENCE]; I did not check opencode's behaviour.

## Pre-existing, not caused by round-48

- verify_skill_checklist's citations and governance rule depend on the checkout's parent (see Method). Outside a fleet-shaped parent, base also exits 1.
- candidate_blocks moves with the live census: 5913, 5934, 5937, 6006, 6009, then 6069 for base, 84b9c9b and eb5a80f in one concurrent run. Not code.
- LOG.md claims checked: pins exit 1 with omp 85d9daf3 (confirmed); surfaces exit 1 at 5/7 (confirmed); compare exit 2 at base (not reproduced, exit 1).

## Lane state

- Lane HEAD is eb5a80f. Four files differ from it in the lane working tree (uncommitted): corpus/README.md (lane f87e23a3 vs eb5a80f c5b5d89a), corpus/QUALITY.md (b5cd9e3e vs 0dde35c7), corpus/lessons/round-48.md (8a5732e7 vs 49927e5f), corpus/knowledge/frontmatter-rule-authorities-round48.md (92f0796f vs 3a043c99). The lane also holds 4087 untracked non-ignored files, none under corpus/ or verifiers/ and none of SKILL.md, LOG.md, SCORECARD.md or PROVINCE.md.
- Blob hashes (12 hex): verify_skill_checklist.py ef7d95245a97 at 75f671b and 84b9c9b, 100644df7c7a at eb5a80f; verify_harness_independent.py 06322fc5b023, 134f756eb482, 2a9d32e7f844; check_assertion_floors.py 945f473fd88b, 4583fdea09c5, c635b91f61ff.

## Verification gaps

- The lane path itself was not executed (read-only rule). Results come from mirrors holding the same committed bytes and the same fleet parent. Untracked lane files are not mirrored, but none sits under corpus/, verifiers/ or the governance files, so the mirrors see the same citation targets.
- Gates that fail at every revision (pins, surfaces, harness claims) were compared for equality with base, not for correctness.
- Not run: fault_injection_corpus.sh --keep-worlds; the adjacency replay (not in the list). LOG.md's "instrument_drift" claim for the adjacency replay is unchecked.
- The compare driver's "exit 2" claim is not reproduced. Its exit code depends on live state.
