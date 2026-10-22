# kotoba round 48 plan (attempt 2; hyaku session 2026-10-22)

Lane base: branch `master` at `75f671b109d8eddd0d64c1429bd6379fe577175a` (attempt 1 pushed
`c0185da` instrument and `75f671b` before receipt; this attempt re-verified both inside the lane
repo before reuse). Attempt 1's private trees, approval windows and hash chains are not continued.

## Claims (two, causally separable, distinct axes)

**Re-ordering after build-wave critics (08:30Z, before any landing):** `C1ClaimCritic` showed the
configured-root change does not repair routed defect 1 (the join drop is the built-in marker, which
the change leaves alone). The repair-first claim is therefore the knowledge entry, which repairs
routed defect 3 (parsed vendor rule versus the lane's lexical mirror, counterexamples retained).
Numbering below: **C1 = the entry (freshness)**, **C2 = configured-root (depth, improved-bounded,
does not resolve defect 1)**. Targets are unchanged; only the order and the framing moved.

### C2 — depth (owned-axis lowest, score 9): configured-root input gap in the row routed by defect 1 (does not resolve defect 1)

The independent instrument `verifiers/verify_harness_independent.py` counts
`oc.roots.names_plus_builtin` only from roots the opencode log names. A skill placed in
`--oc-config/skill/` or `--oc-config/skills/` that the log does not name is invisible.
The candidate unions direct-child `SKILL.md` directory names from both configured roots with the
legacy log-root names (same operator, set semantics). Built-ins stay 0 by declaration — the
production-marker disagreement is NOT resolved by this claim and stays routed.

- Before (committed receipt `.ufo/round-48/verification/before-configured-root.json`,
  sha256 `8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`, base
  `197b5a4`): ruler verdict `failed`, 5 target failures, 0 behavioral mismatches, 8 clean controls.
- After (declared): ruler verdict `clean`, **0 target failures**, 0 behavioral mismatches, ruler exit 0,
  run over the landed lane commit.
- Command (one): `python3 -B .ufo/round-48/tools/config-root-ruler.py --repo <lane> --revision <landed>
  --consumer-sha256 <sha of landed consumer> --oracle .ufo/round-48/oracle/config-root-cases.json
  --oracle-sha256 1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883 --scratch
  /fast/scratch/<new dir> --baseline-receipt .ufo/round-48/verification/before-configured-root.json
  --baseline-sha256 8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`
- Scratch candidate: `/fast/scratch/hyaku/kotoba-r48-a2/cand` branch `r48-cand` commit
  `26035dcec54d8e42f3a8b47ae8ca551c18aec295` (consumer sha256 `2d824c0b…`); patch
  `/fast/scratch/hyaku/kotoba-r48-a2/c1-candidate.patch`. L1 pre-run: exit 0, verdict clean.
- Q05: the fix must ship its own regression arm in the consumer's `--self-test`.

### C1 — freshness (all-axes lowest, score 8): admitted knowledge on uncovered ground; repairs routed defect 3

New knowledge entry `corpus/knowledge/frontmatter-rule-authorities-round48.md`: which authority
imposes which SKILL.md frontmatter rule — the open spec (agentskills.io, S001), the reference
validator `skills-ref` (new row), Anthropic docs (S003), Anthropic's packager `quick_validate.py`
(S012), Codex (S013), and what the lane's own lexical checker (`trigger.no_xml_tag`) actually
executes — with the counterexamples the round-47 spot-check routed (YAML alias, Unicode name,
escaped value) observed by running the lane checker. Sweep: no existing entry under
`corpus/knowledge/` covers per-authority frontmatter validity (grep for `agentskills|skills-ref`
returned only SOURCES/lessons rows).

- Before: 34 Markdown knowledge entries.
- After (declared): **35**, the new entry citing at least one SOURCES row added this round.
- Command: `git ls-tree -r --name-only <landed> corpus/knowledge | grep -c '\.md$'`

## Frontier step and routed-defect repairs (inside the cap; not claims)

- SOURCES: new rows for sources opened this round; superseding rows for the routed S001/S003/S010
  defects and S013's versioned semantics (old cells preserved).
- Lesson `corpus/lessons/round-48.md`: `## Gate` (URL, access date, ≤25-word quote per new row),
  `## Mistakes` (one mined mistake with a fix shown able to fail).
- QUALITY.md: lesson-backed criteria for routed defects 3-5, or the report says why not.
- README: qualify the stale live 24/24 recipe and the erratum horizon (routed defect 2).
