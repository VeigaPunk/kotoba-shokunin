# A25ArmReview: round-48 falsify, C2 self-test arm (d1ae458)

Seat: KotobaR48.A25ArmReview (leaf, read-only lane). Target: the self-test arm added by d1ae458 in verifiers/verify_harness_independent.py (blob 134f756; sha256 d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937; unchanged through clone HEAD d28b16b). Probes ran in the private clone /fast/scratch/hyaku/kotoba-r48-a2/seats2/A25ArmReview/lane. Line numbers are the verifier's.

## Verdict

- Self-test arm (L1347-1445): DEFECT, MEDIUM. Pristine run is green (115 of 115). Seven of ten mutants fail at least one arm assertion; M4, M5 and M6 survive. Four assertions are vacuous or mis-targeted (T1-T4).
- C2 derive block (L603-623): DEFECT, MEDIUM, two error paths that neither the arm nor the frozen oracle covers (P1, P2).
- Q1, fixture log free of configured roots: CONFIRMED.
- Q2, expected 5 names: CONFIRMED for the declared contract. The name set is never checked, and the declared contract is narrower than upstream (T4, T7).
- Q3, vacuous assertions: DEFECT (T1 to T4; T5 minor).
- Q4, evidence assertion wording: DEFECT (T1). It tests English substrings, passes the pre-C2 mislabel, and cannot see a singular-root omission.

## Q1. Is the fixture log free of configured roots?

Yes. The log has three lines: two rescan lines with skills="[...]" naming alpha and beta, and run=bbb "cli starting". It has no sources= token and no directory: token (repr probed). The derive regex (L603-605) cannot match it, and the premise at L1360-1361 passes. Limit: the premise checks two tokens only (T6).

## Q2. Are the expected values right?

Right for the declared contract. The oracle's contract.new_behavior unions direct-child names of both configured roots with the legacy names. Independent walk: alpha, beta, solo-p, solo-s, twin. Excluded: group/ (nested), not-a-skill (no SKILL.md), README.md (plain file). The other fixture expectations also hold: flat 5, no-pair 4, log-named 6, log plus config on one root 5. As loader behavior the number is narrower: upstream globs {skill,skills}/**/SKILL.md and keys names by frontmatter (E8), so upstream would also list zeta and eta [INFERENCE, T7].

## Mutant matrix (clone, --self-test; one edit each)

| id | edit (verifier line) | exit | failing arm assertions (line) |
|---|---|---|---|
| pristine | none | 0 | none; 0 of 115 |
| M1 | configured union removed (L609) | 1 | 1369, 1381, 1401, 1415, 1418, 1434, 1443 (7) |
| M2 | recursive rglob (L613-615) | 1 | 1369, 1381, 1399, 1418, 1434, 1443 (6) |
| M3 | SKILL.md filter removed (L614) | 1 | 1369, 1381, 1399, 1401, 1418, 1434, 1443 (7) |
| M4 | evidence names plural root only (L623) | 0 | none; survives 1388 (T1) |
| M5 | configured roots enumerated twice (L609) | 0 | none; survives 1443 (T3) |
| M6 | configured names keyed by frontmatter (L615) | 0 | none; survives all 11 expects (T4) |
| M10 | configured = plural root only (L608) | 1 | 1369, 1381, 1401, 1418, 1434, 1443 (6) |
| M11 | log-named roots ignored (L609) | 1 | 1434 (1) |
| M12 | configured = singular root only (L608) | 1 | 1369, 1381, 1401, 1418, 1434 (5) |
| M13 | evidence without root names (L623) | 1 | 1388, got (True, False) (1) |

Pre-C2 (parent 75f671b) on the same fixture: value 2, and the evidence still holds both tokens (T1).

## Arm defects (verifier lines at d1ae458)

T1 [MEDIUM] L1387-1389, evidence assertion. Wording-dependent and partly always true. "skill" in evidence cannot fail, because the constant text at L617 ("distinct skill names ...") supplies it. It passes the pre-C2 mislabel: at 75f671b the same fixture reads "(0 configured dirs present: skill, skills)" and (True, True) holds, though the comment at L1384-1386 says the base mislabelled the two families. M4 survives; only total removal fails (M13). The comment at L1386 ("survives a re-worded detail string") is false: the check survives only rewording that keeps both tokens. Fix: parse the "(present: ...)" list and compare it to ["skill", "skills"]; check configured-versus-log wording through a helper.

T2 [MEDIUM] L1401-1404, "on disk but not counted", checks the wrong fixture. The second tuple element is flat_rows (the flat fixture has no nested skill), not cfg_value. M2 passes it because flat stays 5, so nothing here tests "not counted"; L1399-1400 does. Fix: use cfg_value in that tuple.

T3 [LOW-MEDIUM] L1443-1445, "a root named by the log and by the configuration is one root", is vacuous for dedupe. names is a set (L606-607, L615), so a double enumeration cannot move the count, and M5 gives 0 failures. The expect can only catch extra names. Fix: drop the mechanism claim, or expose root multiplicity and assert on it.

T4 [MEDIUM] L1371-1384, "independent enumeration", never compares derive's names. The mirror (L1376-1380) copies the product rule (directory name plus SKILL.md is_file), is compared to a literal (L1383-1384), and the count is re-checked (L1382). derive() yields only a count (L616-623). M6 gives 0 failures, because every fixture folder equals its frontmatter name. Collision probe: folder skill/solo-s with name: alpha gives derive 5, while the frontmatter-keyed set {alpha, beta, solo-p, twin} has 4. No arm case covers it. Fix: expose a names helper, compare sets, and add the collision case with the operator pinned.

T5 [LOW] L1399-1400, "a nested skill is not a name", passes under M1 (no configured enumeration: 2 - 2 = 0). Other expects catch M1; this expect does catch recursion (M2).

T6 [LOW] L1360-1361 premise, with overclaiming comments at L1350 and docstring L903-904 ("names no root at all"). A log line path="<config>/skill" keeps the premise at (False, False) and the count at 5. The oracle's log_format says "one sources=... per named source; no other log content", which the arm does not enforce. Fix: assert the log holds no other content.

T7 [LOW, labelling and scope] Docstring L911-913 and arm L1352-1354 call direct-children-only "the frozen contract". The located source is the oracle's contract.scope (E10), which calls it a bounded input-class repair and says "Upstream source supports broader recursive discovery". Upstream globs {skill,skills}/**/SKILL.md (index.ts:24, :207) and keys names by frontmatter (index.ts:134). So L1399-1400 and the nested clause of L1401-1404 pin a declared divergence that any parity fix would invert. Expected 5 is right for the declared bound, not for loader behavior. Fix: cite the oracle file and key, and label the nested assertions as pinned bounds.

T8 [LOW] L596-597 comment ("names come from enumerating direct children with the same operator for every root") is wrong. The agents root keys by frontmatter (L606-607); configured and log roots key by directory (L615). The oracle declares the legacy directory operator and "no name-identity rule", so the split is declared but unpinned (see T4). Fix: reword.

## Product defects (C2 derive block)

P1 [MEDIUM] L613-615 accepts an unreadable SKILL.md under the configured roots (is_file() only). Oracle new_behavior says "Enumerate readable direct child SKILL.md files" (E10). offered() skips unreadable files (L206-209, try/except OSError; its docstring at L197 says readable). Reproduced as uid 1000: chmod 000 on skill/unread/SKILL.md gives a configured count of 6 (fixture 5); the same file under the agents root leaves offered at 2 and names at 2. Neither the arm nor the 13-case oracle covers it.

P2 [MEDIUM] L613, path.iterdir() on a configured root that exists but is search-only, raises PermissionError out of derive(). Pre-C2 (75f671b) returns 2 on the same fixture. C2 enumerates --oc-config/skill and skills unconditionally, so the crash no longer needs the log to name the root. The base already crashes on an unreadable log-named root (same loop), so the class predates C2, but the reach is new. Neither the arm nor the oracle covers it. Fix for P1 and P2: wrap the read and the iterdir in try/except OSError, as offered() does, and add arm cases for an unreadable SKILL.md and a search-only root (each expects an unchanged count and no exception).

Live effect: none today. ~/.config/opencode/* holds only opencode.json, cli.json and service.json (E11), so no configured skill root exists on this host.

## Residual risk and verification gaps

- I did not execute opencode (read-only bound). "Upstream would list zeta and eta" is an inference from the globstar pattern. C1UpstreamLoaderSource.md item 2 reports a depth-3 probe, which I did not re-run.
- I did not run the ruler or the floor guard; other seats own those. The 115 floor counts expect() calls (floors-registry.json:30), not discriminating power. Eleven expects were added (L1360, 1363, 1369, 1381, 1388, 1399, 1401, 1415, 1418, 1434, 1443).
- The chmod probes ran as uid 1000; root would bypass them.
- Overlap: A32NoHarmCritic (calibration note) and A23C2Framing (F4) reached T1 and T7 separately. This report adds the mutant evidence and P1 and P2.

## Evidence (exit codes, hashes, URLs)

- E1 git show d1ae458 -- verifiers/verify_harness_independent.py: rc 0 (175 insertions, 8 deletions).
- E2 git clone -q <lane> .../seats2/A25ArmReview/lane: rc 0; clone HEAD d28b16b.
- E3 git diff --stat d1ae458..HEAD -- verifier: empty. git hash-object: 134f756eb482cae2467218357349f9c1ba256cd6. sha256 d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937.
- E4 python3 verifiers/verify_harness_independent.py --self-test (clone): rc 0, "0 failure(s) over 115 assertions", 24.5 s.
- E5 M1-M13 as verifiers/_mut_*.py in the clone, each run with --self-test; exit codes in the table; files removed afterwards.
- E6 Probes through importlib on the clone module: log repr; dir-name walk; collision 5 vs 4; path-line premise (False, False) with count 5; pre-C2 via git show 75f671b:verifiers/verify_harness_independent.py (rc 0, 69,865 bytes): value 2, evidence naming skill, skills.
- E7 Unreadable probes (euid 1000): open() raises PermissionError; configured count 6 vs 5; agents offered 2 vs 2; search-only skill/ raises PermissionError at HEAD and returns 2 at 75f671b; log-named unreadable root raises at 75f671b.
- E8 Upstream, fetch only: curl -fsSL https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts, rc 0, accessed 2026-10-22T09:08:17Z, sha256 91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6. Located: line 24 `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`; lines 205-207 config.directories() loop with scan(state, dir, OPENCODE_SKILL_PATTERN); line 134 `state.skills[md.data.name] = {`.
- E9 Shipped binary ~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode (186,013,824 bytes; sha256 prefix 179ca421d61eefea): byte count of {skill,skills}/**/SKILL.md is 1. Read only, not executed.
- E10 Oracle .ufo/round-48/oracle/config-root-cases.json. contract.scope: "Direct-child disk-root enumeration only, matching the legacy instrument existing log-root operator." Also: "Upstream source supports broader recursive discovery; this bounded input-class repair does not claim whole loader parity." contract.new_behavior: "Enumerate readable direct child SKILL.md files in both explicit --oc-config/skill and --oc-config/skills".
- E11 glob /home/vgpnk/.config/opencode/* (hidden on): opencode.json, cli.json, service.json.
- Tooling: none installed or upgraded (git, python3, curl already present). No lane, fleet or sibling write; the only lane write is this report.
