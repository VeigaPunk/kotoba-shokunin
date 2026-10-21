verdict: C2 alternative implementation lands — `trigger.description_no_xml_tags` in verify_skill_checklist.py checks the strict-YAML-loaded description (yaml.safe_load) with four named, non-silent fallbacks, is discriminating (fixtures green at BASE, red under the patch), and ships as a BASE-applying patch with self-test 0 failures / 1835 assertions.

# C2 competing draft — strict-YAML description XML-tag check

Seat: MoriR22R.ExecDescriptionCheckAlt-9 (leaf executor). BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd. Production tree untouched; all work in scratch clone `/fast/scratch/kotoba-r47/MoriR22R.ExecDescriptionCheckAlt-9/lane` (detached at BASE).

## Deliverables

- `.ufo/waves/round-47/build/ExecDescriptionCheckAlt.patch` — 20,547 bytes, applies clean to BASE (`git apply --check` OK; applied + self-tested on a fresh clone, below). 9 files, +348/−8:
  - `verifiers/verify_skill_checklist.py` — check implementation, CHECK_IDS registration, main dispatch, CASES updates (7 existing cases), 4 new CASES, targeted self-test arms.
  - `verifiers/fixtures/checklist/{description-tag-skills,description-tag-ok,description-tag-escape,description-tag-fallback-colon}/{SKILL.md,map.json}` — bodies byte-identical to `clean/` so the copied map.json sha256 pins stay valid.
- This report (includes the comparison note vs regex-on-raw-lines).

**Not in the patch (L1 owns it — production file not mine to write): the SKILL.md companion edit.** BASE `SKILL.md:13-15` carries ``the `<skills>` router`` inside the folded `description`; the check therefore FAILs on the live file until that token is removed. Demonstration edit (scratch only, reverted before diffing): line 14 rewritten to `never reach the skills router catalogue — craft here is audit-side, not`. After it, live `--json` shows my check PASS and no other verdict changes.

## Design

New check id `trigger.description_no_xml_tags` (registered in CHECK_IDS, BASE :282-293; dispatched in `main`, BASE :2215 block — wired after the anti-trigger branch). Value selection per assignment:

1. **Strict path**: re-derives the `---`-bounded block bounds exactly as `parse_frontmatter` (BASE :472-558) does, then `yaml.safe_load` on the block. When it returns a mapping with a string `description`, that decoded string is what the check inspects — i.e. what a strict client loads (folded scalars folded, quotes stripped, `\u003c`-style escapes resolved).
2. **Named fallbacks** (never silent; each names its reason inside the check detail, and the detail names which path produced the verdict — `description (strict YAML) …` vs `description (structural fallback) …`):
   - PyYAML not importable → structural value, note `pyyaml unavailable: …`
   - `yaml.YAMLError` → structural value, note `strict YAML parse failed (<first line>): …`
   - load is not a mapping / no `description` key / description not a string → structural value, note naming the type.
   The structural value comes from the existing parser (unchanged for all other checks — that is the axis this draft differs on from a raw-lines approach, see comparison).
3. Tag test: `XML_TAG_RE = r"</?[A-Za-z][A-Za-z0-9._:-]*(?:\s[^<>]*?)?/?>"` (module constant, added at BASE :306 vicinity). Scope-outs, pinned by probes: comparisons (`a < b and c > d`), arrows (`->`, `<=>`), and angle autolinks (`<https://example.com>`) are not tags; `<skills>`, `</skills>`, `<br/>`, `<foo bar="1">`, `<kotoba:tool>` are.
4. Empty/absent description → `FAIL 0 cannot evaluate: …`, mirroring sibling checks `check_frontmatter` (BASE :1176-1192) and `check_anti_trigger` (BASE :1230-1249); unparseable frontmatter → `FAIL 0 cannot evaluate: <problem>`. No N/A class (consistent with the trigger siblings); evaluated = 1 whenever a description was inspected (non-vacuous).

PyYAML is a guarded optional import (`try: import yaml as _yaml / except ImportError: _yaml = None`); module docstring's "stdlib only" claim (BASE :251) updated to declare the optional dependency.

## Self-test arms (fixtures + unit)

CASES additions at the fm-stray-indent entry (BASE :1700): `description-tag-skills` (FAIL, needle `<skills>`), `description-tag-ok` (exit 0), `description-tag-escape` (FAIL), `description-tag-fallback-colon` (exit 0). Seven existing frontmatter cases updated for the new id (`no-frontmatter`, `fm-null`, `fm-malformed`, `fm-dup-key`, `fm-body-yaml`, `fm-stray-indent`, `empty-file`). Targeted extras after the negation-respected arm (BASE :1926): text-mode needles for all four fixtures, a `--json` arm asserting the FAIL row in the payload, and unit arms that run the escape class through both paths — `globals()["_yaml"] = None` monkeypatch proves the pyyaml-missing fallback hermetically — plus the non-string (`date`) strict description fallback.

## Evidence (commands run in the scratch lane; exit codes verbatim)

1. `python3 -B verifiers/verify_skill_checklist.py --self-test` at BASE → exit 0, `0 failure(s) over 1597 assertions`.
2. PyYAML probes (host python3, PyYAML 6.0.3): `description: Triggers: "run"` → `ScannerError: mapping values are not allowed here`; `"a \u003cskills\u003e b"` → `'a <skills> b'`; folded `>` joins lines; `123/true/2026-01-01` load as `int/bool/date`. Tag-regex probes as in Design §3.
3. **Red at BASE**: BASE script extracted via `git show c61a973…:verifiers/verify_skill_checklist.py`, run on each new fixture: all four **exit 0, zero FAIL lines** — the planted `<skills>` is invisible to BASE. (First attempt exited 2 ×4: the /tmp-placed BASE script resolves its default vocabulary from its own `__file__`; rerun with explicit `--vocabulary verifiers/checklist-command-vocabulary.json` → exit 0.)
4. Patched self-test → **exit 0, `0 failure(s) over 1835 assertions`** (+238 assertions over BASE).
5. Patched per-fixture runs (exit / detail line):
   - description-tag-skills → exit 1, `FAIL … description (strict YAML) carries XML tag(s): <skills>`
   - description-tag-ok → exit 0, `PASS … description (strict YAML) carries no XML tag`
   - description-tag-escape → exit 1, `FAIL … description (strict YAML) carries XML tag(s): <skills>` (structural view has no literal `<` — see comparison)
   - description-tag-fallback-colon → exit 0, `PASS … description (structural fallback) carries no XML tag (strict YAML parse failed (mapping values are not allowed here): checked the structural parse value)`
6. Live `--json` on the lane's own BASE SKILL.md → exit 1, `"detail": "description (strict YAML) carries XML tag(s): <skills>"` (my check is the only new FAIL; the other FAILs are scratch-clone artifacts: `name_directory` because the clone dir is named `lane`, `../`-rooted citation and governance misses because the clone's parent lacks the fleet tree — at BASE in production the live run is 9 PASS / 1 FAIL per before/SUMMARY.md).
7. Companion-edit demo (scratch) → live `--json` `PASS description (strict YAML) carries no XML tag`, pass 8 / fail 3 (the three scratch artifacts above). SKILL.md then reverted; `git status --short` confirms only my 9 files changed.
8. Shipped-artifact check: fresh clone at BASE + `git apply --check` → OK; `git apply` + `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 0, 1835 assertions.

## Comparison note — strict YAML vs regex-on-raw-lines

Both drafts share the tag regex; the axis is **which string the regex runs over**.

1. **Escape decoding gap (proven discriminator).** `description: "Flags a \u003cskills\u003e token …"` loads, in every YAML client, as a string containing `<skills>`. On raw source lines the bytes are `\u003c` — a regex-on-raw-lines sees no `<` and PASSES. Fixture `description-tag-escape` is exit 0 at BASE (and would stay 0 under a raw-lines rule) and exit 1 here. The strict path closes this by construction: the checked value is the decoded string.
2. **Value attribution.** A raw-line scanner must decide which key each folded/indented continuation line belongs to. `parse_frontmatter` (BASE :472-558) already attributes indented continuations to the open key; the strict path gets attribution from the YAML parser itself. A naive all-frontmatter-lines regex would flag a tag inside a different key's nested block (e.g. a `metadata:` sub-mapping) as a description defect — false positive; a description-span-bounding regex re-derives, line-heuristically, what both parsers already do structurally.
3. **What the raw-lines draft gains.** No optional dependency, and it inspects the literal source bytes (immune to nothing — gap 1 — but also never surprised by parser divergence). It also matches the *file* rather than the *loaded value*; S003's rule is about the value the router receives, which favors the decoded view.
4. **Costs/risks of this draft, named.** (a) PyYAML becomes an optional dependency; absence degrades to the structural view **with a named note**, so a pyyaml-less host silently catching no tags is impossible — the PASS detail says `structural fallback (pyyaml unavailable…)`. (b) Blocks strict YAML rejects but the structural parser accepts (the unquoted-colon class S002 records as common in the wild) fall back, so on those files this draft's coverage equals the structural view — `description-tag-fallback-colon` pins that the fallback is visible. (c) PyYAML is stricter than the lenient clients S002 describes (warn-and-load); "strict client" here is the assignment's chosen model, not a claim about any vendor's validator.
5. **Shared declared scope-out:** `<https://example.com>`-style autolinks are not flagged by the tag regex in either approach; S003's prose ("cannot contain XML tags") does not settle autolinks, and the validator internals are unobserved.

## Not checked

- A real interpreter without PyYAML (the fallback is proven via the self-test monkeypatch arm only; no yaml-less environment was available).
- The non-mapping strict-load fallback: unreachable when the structural parse succeeded (any column-0 `key: value` block that satisfies the structural parser parses as a YAML mapping); code path present defensively, exercised by no fixture — reasoning, not a run.
- Production-tree live run (production files read-only; all live evidence is from the scratch clone with the three environment-artifact FAILs named above).
- C1 substrate and C3 erratum work (other seats); governance FAIL at BASE untouched.
- No tools were installed or updated (none needed; PyYAML 6.0.3 already present host-wide).
