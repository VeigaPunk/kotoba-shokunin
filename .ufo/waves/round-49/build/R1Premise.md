# R1 premise check — findings

Seat `KotobaR49.R1Premise`, kotoba round 49 BUILD wave (attempt 1), hyaku session
2026-10-22. Scope: verify routed defect R1 (round-48 spot-check, line 154) on the base
consumer before the fix lands. Leaf member — no subagent dispatch. Lane untouched except
this report file.

## Verdict

**R1 is REAL and LATENT, exactly as routed.** The double count reproduces on base
`a5adc146a2995dcc5a95a6d8db6e5674f75191ac` with the smallest fixture (agents root
offering name `x`, configured `skills/dir-y/SKILL.md` with `name: x`): the instrument
reports `oc.roots.names_plus_builtin = 2` where S016 semantics say 1. The base
self-test is green, so no arm catches it. No live effect on this host.

## Findings

1. **Mechanism confirmed in the base consumer** (`verifiers/verify_harness_independent.py`
   at a5adc146; working-copy sha256 `f576c23f3e2ddb586b81c5f3bceb0618f47e5696e7a675c028325992195730b6`):
   - agents root keys by frontmatter name —
     `names = {skill["frontmatter"].get("name") or skill["dir"] for skill in offered}` (line ~608);
   - log-named and configured roots key by directory name —
     `names.add(entry.name)` inside the `sources | configured` loop (line ~627).
   A configured skill whose directory name differs from a frontmatter name already
   contributed by the agents root therefore adds a second, distinct string for one
   opencode identity. The row's own comment (lines ~594-600) states the contract and
   already concedes it is "narrower than opencode's recursive loader (S016)".

2. **Minimal repro (probe_r1.py, exit 0).** Fixture: `skills/x/SKILL.md` (name `x`) in the
   agents root; `config/skills/dir-y/SKILL.md` (frontmatter `name: x`) under `--oc-config`;
   empty log, empty cache, fake omp binary carrying only the template markers.
   - observed `oc.roots.names_plus_builtin` = **2**
     (evidence: "…configured --oc-config roots (present: skills) plus the shared agents
     root (1 names); built-in names: 0 by declaration");
   - expected under S016 = **1** — opencode identity is the frontmatter name, so
     `x` (agents root) and `dir-y` (configured, frontmatter `x`) are one skill;
   - delta exactly 1, matching the routed A21 probe shape (4 → 5) at fixture scale 1 → 2.

3. **S016's claim verified against its named source.** Fetched
   `https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts`
   (v1.19.3 = the tag named in the S016 row) — 11843 bytes, sha256
   `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6`,
   fetched 2026-10-22T09:42:59Z. Keying line:
   `packages/opencode/src/skill/index.ts:134` — `state.skills[md.data.name] = {`
   (7 words; the registry is keyed by frontmatter name). Line 125
   (`if (state.skills[md.data.name]) {`) emits a `"duplicate skill name"` warning, and
   the assignment at :134 proceeds regardless — same-name skills collapse to ONE registry
   entry, last writer wins. So the S016-true expectation for the alias case is 1, not
   "2 with a warning". The row's `#L24` anchor also checks out: line 24 is
   `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`.

4. **Latent, not live: the base self-test has no alias arm.** In a fresh clone of the lane
   at a5adc146: `python3 -B verifiers/verify_harness_independent.py --self-test` →
   exit 0, "0 failure(s) over 116 assertions". All 116 arms pass while the alias case
   miscounts, which is why R1 was routed as latent and why the fix needs a must-fail arm
   (as the routing text demands). Fixture-matrix note: the round-48 matrix generates
   `name == dir name` skills (falsify finding: mutant J "name identity switched to
   frontmatter name … cannot be distinguished"), so this blind spot is structural, not a
   one-off.

5. **No live effect on this host, re-confirmed 2026-10-22.** All four opencode configured
   roots are absent: `~/.config/opencode/skill`, `~/.config/opencode/skills`,
   `~/.opencode/skill`, `~/.opencode/skills` (test -d, each absent). With no configured
   root, the directory-keyed contributor is empty and the double count cannot fire here.
   Consistent with R1's routing statement.

6. **Sizing note for the fixer.** The defect needs the configured/log-named contributor to
   key by the SKILL.md's parsed frontmatter name (`name` field, falling back to the
   directory only when the name field is absent — mirroring the agents-root operator and
   upstream's `md.data.name`). A same-identity fix must also survive the "name == dir"
   majority (no count regression on the existing 116-arm battery) and add a must-fail arm
   with the alias fixture above (expected 1, observed 2 at base).

## Residual risk and verification gaps

- I verified the keying lines and duplicate-name branch of upstream `index.ts` by reading
  the fetched file; I did not execute opencode (no fetched code run — bounds). The 1-not-2
  expectation rests on the read of :125-140, which is unambiguous.
- The bare-copy self-test run (`verify_harness_independent_base.py` outside the lane tree)
   fails 1/79 on a missing fixture directory — an artifact of copying the file without
  `verifiers/fixtures/harness-independent`, superseded by the in-clone run in finding 4.
- I did not re-run A21's original 4→5 fixture; my probe is the smaller canonical case with
  the same delta. The routed defect cites A21's numbers, which I take as recorded evidence.

## Evidence (commands with exit codes)

Scratch: `/fast/scratch/hyaku/kotoba-r49/seats/R1Premise/`. No tools installed (none
needed); no pacman transaction; no jj or git write command against the lane or fleet.

| command | exit | result |
|---|---|---|
| `git -C <lane> show a5adc146…:verifiers/verify_harness_independent.py > verify_harness_independent_base.py` | 0 | 1627 lines, sha256 `f576c23f…` |
| `git -C <lane> rev-parse HEAD` | 0 | `a5adc146a2995dcc5a95a6d8db6e5674f75191ac` |
| `python3 -B probe_r1.py` | 0 | observed 2, expected 1, `double count: True (observed 2, expected 1, delta 1)` |
| `git clone -q <lane> clone && git -C clone rev-parse HEAD` | 0 | `a5adc146…` |
| `python3 -B verifiers/verify_harness_independent.py --self-test` (in clone) | 0 | `0 failure(s) over 116 assertions` |
| `python3 -B verify_harness_independent_base.py --self-test` (bare copy) | 1 | `1 failure(s) over 79 assertions` — missing fixture dir, see gaps |
| `curl -fsSL -o skill-index-v1.19.3.ts https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts` | 0 | 11843 B, sha256 `91dce57f…`, 2026-10-22T09:42:59Z |
| `test -d` loop over the four configured roots | 0 | all four `absent` |
| `grep -n 'skills\[' skill-index-v1.19.3.ts` | 0 | hits at :125, :128, :134 (plus internals :278, :291, :296) |

Probe fixture set kept in scratch: `probe_r1.py`, `fixture/skills/x/SKILL.md`,
`fixture/config/skills/dir-y/SKILL.md`, `fixture/omp`, `fixture/oc.log`,
`fixture/skill-descriptions.db`, fetched `skill-index-v1.19.3.ts`.

Report: .ufo/waves/round-49/build/R1Premise.md
