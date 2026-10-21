verdict: C2 is sound only if the check is scoped as the S003 Anthropic rule, runs on parsed `name`+`description` values, does NOT exempt backticked spans (the obvious reuse of `ALL_QUOTED_SPANS_RE` lets BASE pass, so the "before" is no longer red), and is pinned by four parse-path fixtures plus a string battery. A reference patch with seven killed mutants is at `C2CriticRule.patch`.

Lane: MoriR22R.C2CriticRule-9 (critic, leaf). BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. This is advice written inside the lane. It is not closure by a non-author.
Artifacts: `.ufo/waves/round-47/build/C2CriticRule.patch` (17,785 B; `git apply --check --reverse` exit 0 in the scratch clone) and `.ufo/waves/round-47/build/C2CriticRule.battery.json` (55,927 B: detector × case matrix plus a 101-file fleet scan).
Axes judged: operability (does the check pass or fail the right descriptions), calibration (the label matches the source, and the docs match the state), freshness (the S003 wording was re-read live today).

## 1. What S003 actually says, and whose rule it is

- `corpus/SOURCES.md:16` (S003) records that "The description cannot contain XML tags … an Anthropic-only rule the open spec lacks". I re-fetched it live on 2026-10-21. Both the best-practices page (§ Skill structure, and again in § Technical notes) and the overview (§ Skill structure) say **both** `name` and `description` "Cannot contain XML tags". The lane already knew this: `corpus/lessons/round-46.md:65` notes "name field repeats it line 162".
  - **Counterexample (calibration):** a check that covers only `description` implements half of the cited bullet. The S003 row text also under-states the rule. Smallest fix: scan `name` as well. It costs nothing, since a valid name never contains `<`. The alternative is to state the `name` gap as a named limit.
- The open spec has no such rule:
  - `agentskills.io/specification`, fetched live, gives the description constraints as only "1-1024 chars, non-empty". The S001 row is at `SOURCES.md:14`.
  - The reference validator `skills-ref/src/skills_ref/validator.py` (`_validate_description`) checks only empty and length.
  - The S002 client guide (`SOURCES.md:15`) adds nothing on this.
  - `SOURCES.md:24` (the rejected S011 row) already records "credits an angle-bracket ban to the agentskills.io spec which has none".
  - **Consequence:** the check must carry the label "S003 / Anthropic-compat". Neither the check id nor the detail line may imply that the open spec requires it. Reviewers in round 46 agreed it is vendor-specific (`corpus/lessons/round-46-verifier-spotcheck.md:12`).
- Anthropic's own tooling is **stricter than S003's words**:
  - `anthropics/skills` `skills/skill-creator/scripts/quick_validate.py`, fetched live, contains `if '<' in description or '>' in description: return False, "Description cannot contain angle brackets (< or >)"`.
  - `package_skill.py` calls `validate_skill` before it zips.
  - The Claude Code skills docs say claude.ai uploads, the Skills API and `package_skill.py` validate frontmatter. Claude Code also refuses a skill `name` that contains `<` or `>`, and escapes angle brackets in synced descriptions.
  - **This is a tradeoff the planner must decide, not a defect.** A tag-grammar check (faithful to S003) passes `a -> b`, which Anthropic's packager rejects. An any-bracket check (faithful to `quick_validate.py`) needs its own SOURCES row, because S003 does not say it. Fleet evidence shows **no observed divergence**: across 95 parsed fleet and fixture descriptions, both detectors hit exactly the same 2 files (section 4). Recommendation: keep the tag grammar under the S003 label, and record the stricter packager rule as a named limit in the docstring and in the detail line.
- There is a substrate rationale too, but it is our own observation and not S003. Both local hosts insert descriptions **raw** into XML-framed prompt blocks:
  - omp compiles its templates with `h.compile(e, { noEscape: true, strict: false })` (`/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings:648585`). It renders `<available_skills>…<description>{{description}}</description>` (`:2413744-2413751`) and `<skills>\n- {{name}}: {{description}}\n</skills>` (`:2423496-2423500`).
  - opencode 1.19.3 builds `` `    <description>${z.description}</description>` `` (`opencode-1.19.3.strings:445661`, also `:445402`).
  - So a description holding `</description>` or `</skills>` closes the frame on both hosts. [INFERENCE] I located no pre-escape call for skill descriptions in omp (`escapeXml(` call sites: 0 matches). Cite these strings as lane evidence if the motivation is written down; S003 gives no rationale.

## 2. False positives: real descriptions the check must not fail

The detector cases below are from `C2CriticRule.battery.json`. Results are shown as structural parse / YAML parse.

| control | any-bracket (`quick_validate`) | tag grammar (recommended) |
|---|---|---|
| `a -> b, x => y, <- back` | FAIL/FAIL | pass |
| `<= 600 lines, >= 2` | FAIL | pass |
| `a < b and c > d` | FAIL | pass (a first draft that allowed `<\s*name` FAILED this one: no whitespace is allowed after `<`) |
| `Under <500 lines`, `cat <<EOF`, `1<2>0`, `<> op` | FAIL | pass |
| `≤ 600 → split`, `‹skills›`, `&lt;skills&gt;` | pass | pass |
| raw-line scan of `description: >` | — | **FAIL on 10 fleet files**: the block-scalar indicator is a `>`. The check must read the parsed value, never raw frontmatter lines |
| whole-file scan | — | **FAIL on the live SKILL.md body**: `<skills>` appears at `SKILL.md:22,91,99,111` and `<available_skills>` at `:430`. Only the frontmatter values are in scope |
| `metadata:` nested `note: <internal>` | — | must stay green. `parse_frontmatter` folds nested lines into the `metadata` value (`verify_skill_checklist.py:513`), so an "every field" scan would fail it. Scan `name` and `description` only |

These are FPs that remain in the recommended design, kept as named limits:
- `description: foo # <skills>`: YAML drops the plain-scalar comment, but the structural parse keeps it, so the check FAILs. There are no fleet instances. This direction fails closed.
- `a <b and c> d`: this is genuinely ambiguous. `<b and c>` is a well-formed HTML start tag with attributes. Accept the FAIL.

## 3. False negatives: tags a client sees that the check would miss

- **Backtick or quote exemption (the most likely build defect).** The live description puts the token inside a code span (`SKILL.md:14` `` `<skills>` ``). The verifier already has a span-stripper, `ALL_QUOTED_SPANS_RE` (`verify_skill_checklist.py:364`), used by `check_anti_trigger` (`:1237`). A builder who copies that idiom gets a check that **PASSes BASE**. The before value then stops discriminating, and the shokunin host skill's `"train <id>"` passes as well. Frontmatter is plain text to every client: omp and opencode insert it raw, and `quick_validate.py` counts every `<`. No exemption is warranted.
- **Folded or literal split.** In `</Skills` / `  > inside it.`, the structural parse joins lines with a space (`:513`) and yields `</Skills >`. Literal `|` keeps a newline in YAML; both are valid end tags. A regex that requires `>` straight after the name, or one that only accepts lowercase `<[a-z]+>`, misses it.
- **YAML double-quoted escapes.** `description: "… \u003cskills\u003e …"` (also `\x3c`) is decoded to `<skills>` by every YAML client: `yaml.safe_load` in the battery, and `quick_validate.py` itself. `parse_frontmatter` only strips the quotes (`:547`) and decodes nothing. All five detectors miss it on the structural value. Smallest fix: also fail on `\\(x3[cCeE]|u003[cCeE]|U0000003[cCeE])` in the value. This fails closed, with a theoretical FP only for a plain scalar that spells the escape literally.
- **Other fields clients show.**
  - Claude Code's `when_to_use` is "Appended to `description` in the skill listing" (code.claude.com/docs/en/skills, frontmatter table). It is outside S003 and outside the API/upload field set (the six spec fields). Record it as a named limit; don't scan it.
  - `name` is covered by S003 (section 1).
  - omp and opencode render only `name` and `description` (strings above).
- **Look-alikes.**
  - Fullwidth `＜skills＞` is not an XML tag, but NFKC maps it to `<skills>`. Any client that NFKC-normalises would expose it; `skills-ref` NFKC-normalises `name` only.
  - Guillemets `‹›` and `〈〉` survive NFKC and are never tags.
  - Entities `&lt;…&gt;` are literal text in a prompt.
  - None of these occur in the fleet (`nfkc_changes_desc` is false for all 95). Record them as limits rather than adding rules (no scope creep).
- **YAML alias.** `description: *d` resolves in YAML to the anchored value, but the structural parse reads `*d`. This is a named limit and has no fleet instance.
- **Entities, comments, CDATA, PI, declarations.** `<!-- -->`, `<![CDATA[`, `<?x`, `<!X` all need explicit alternations. A start/end-tag regex alone misses `<!-- hidden -->`.

## 4. Fleet measurement

I scanned 101 SKILL.md files: fleet lanes, `~/.agents|.claude|.codex|.config/opencode/skills`, and the 71 checklist fixtures. `~/.omp/agent/skills` does not exist. 6 files are fixtures that intentionally fail to parse.
- Only 2 descriptions hit, and every detector agrees on them:
  - `~/Projects/shokunin/kotoba-shokunin/SKILL.md`: the backticked `<skills>`.
  - `~/.agents/skills/shokunin/SKILL.md:7`: `"train <id>", "teach <id>"`.
- The second is a true S003 violation in a host skill outside this lane. The span-stripping variant passes **both**.
- No fleet description contains `->`, `<=` or `<500`. That is why the any-bracket and tag-grammar detectors cannot be told apart on fleet data. Their difference shows up only in the controls, and that is the reason a control fixture is required.
- Every one of the 65 parseable existing fixtures is tag-free, so adding the check flips none of them.

## 5. Minimal discriminating fixture set (reference patch)

Four on-disk fixtures, plus a nine-row in-process battery in `self_test`. Each one kills a specific wrong implementation:

| fixture | expect | kills |
|---|---|---|
| `xml-tag-codespan`: folded, `` `<skills>` `` (the BASE shape) | exit 1, FAIL `trigger.no_xml_tag`, names `'<skills>'` | span-stripping (M1) |
| `xml-tag-split`: folded `</Skills` / `> inside it.` | FAIL, names `'</Skills >'` | lowercase-naive (M2), no-whitespace-before-`>` (M6), raw-line scanners |
| `xml-tag-dq-escape`: `"… \u003cskills\u003e …"` | FAIL, names `\u003c` | escape-blind (M4) |
| `xml-tag-control`: `->`, `=>`, `a < b`, `<= 600`, `<500`, `cat <<EOF`, `≤`, `&lt;skills&gt;`, plus `metadata.note: <internal>` | **exit 0**, all checks PASS | any-bracket (M3), all-fields scan, space-after-`<` (M7) |
| string battery: `</skills>`, attr tag, `<br/>`, `<!-- -->`, `"train <id>"`, `name: <x>` → FAIL; arrows, comparisons, `<=`/`<500`/heredoc/`1<2>0`/`<>`, `≤`, guillemets, entity → PASS | per row | description-only (M5) and the comparison FP |

**Arms that must stay green:**
- `clean`, `fm-nested-metadata` and every other existing fixture. The harness rule at `verify_skill_checklist.py:1839` makes every unlisted check an implicit PASS assertion, so this is enforced automatically.
- The 7 frontmatter-broken cases (`no-frontmatter`, `fm-null`, `fm-malformed`, `fm-dup-key`, `fm-body-yaml`, `fm-stray-indent`, `empty-file`) must list the new id under FAIL with `evaluated 0`. This matches the "subject must exist → FAIL" contract, and the patch does it.
- The live `SKILL.md`: FAIL at BASE, PASS after the token is removed. The rest of the frontmatter checks (`name_directory`, `literal_trigger_string`, `anti_trigger_clause`) must stay PASS after the rewrite. The rewrite keeps the description at 814 chars.

**Mutation result.** `bash /fast/scratch/kotoba-r47/C2CriticRule/mutate.sh` replaces only the detector line. All 7 mutants turn the self-test red, with exit 1 each:
- M1: 4 failures
- M2: 7
- M3: 7
- M4: 3
- M5: 1
- M6: 5
- M7: 2

## 6. Stale-record hazards if C2 lands (calibration)

- `SKILL.md:151` says "This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47)." That becomes false the moment the token goes. The patch rewrites it to point at `trigger.no_xml_tag`.
- `verifiers/floors-registry.json:6` sets `"floor": 1597`. The patch's self-test reports **1837** assertions. `check_assertion_floors.py` still prints `PASS checklist observed=1837 floor=1597`, but the lane reports floors as "EXACT", so the integrator should ratchet the floor to the landed count. The C3 erratum work will move it again, so ratchet once after both land.
- `corpus/SOURCES.md:23` (S010, own-work) cites "9 PASS / 1 FAIL" and "1597 assertions". This is historical, dated 2026-10-19. If S010 is re-cited for round 47, it needs a fresh run, not an edit.
- The plan's after-count `grep -c '<skills>' <(sed …)` prints `0` **with exit 1** (observed). Print it as `… || true`, or state "count 0, exit 1". Otherwise it repeats the round-46 "printed counting command exits non-zero" residual.
- The plan says "11/11 with C2". The patch adds exactly one id, `trigger.no_xml_tag`, after `trigger.anti_trigger_clause`. A sibling (C2SimplifyFrontmatter) proposes `trigger.description_no_xml_tag`. If `name` is scanned, the shorter id is the honest name. Pick one before integration.

## Commands run (exit codes)

- `git show c61a973…:verifiers/verify_skill_checklist.py > /tmp/c2critic-vsc.py`: exit 0. This is the BASE copy that every `verify_skill_checklist.py:N` above cites.
- `python3 -B verifiers/verify_skill_checklist.py --self-test` in the scratch clone at BASE: **exit 0**, "0 failure(s) over 1597 assertions".
- The same command with the patch: **exit 0**, "0 failure(s) over 1837 assertions".
- `--check trigger.no_xml_tag` on the BASE SKILL.md: **exit 1**, "FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '<skills>'".
- Patched, via a symlink dir named `kotoba-shokunin`, `--json`: `trigger.no_xml_tag` PASS (evaluated 2). The only FAILs were `trigger.citation_resolves` and `governance.citation_resolves`, and both come from the scratch location: `../.ufo/reports/...` resolves only beside the fleet root. In a clone named `lane`, `name_directory` also FAILs ("!= directory 'lane'"); executors should use a symlink.
- `python3 -B battery.py battery.json`: exit 0. The matrices are quoted above.
- `bash mutate.sh`: exit 0, and all 7 mutants were killed.
- `python3 -B verifiers/check_assertion_floors.py | tail -12` (patched): checklist `observed=1837 floor=1597 PASS`. The same run printed `FAIL harness_independent self-test timed out after 120s`, which is unrelated to C2 and probably host load. The `$?` I captured belongs to `tail`, so I did not capture the floors exit code.
- `git -C lane apply --check --reverse C2CriticRule.patch`: exit 0.
- WebFetch, all read-only and live on 2026-10-21: the platform.claude.com best-practices and overview pages, agentskills.io/specification, `anthropics/skills` `quick_validate.py` and `package_skill.py`, `agentskills/agentskills` `skills-ref` `validator.py`, and code.claude.com/docs/en/skills.
- Greps over the frozen `/fast/scratch/kotoba-r47/shared/*.strings` snapshot. Nothing was copied into the lane.

## What I did NOT check

- What the live Skills API or claude.ai upload server enforces. No upload was attempted. "Any bracket" versus "tag grammar" on the server is unobserved; only Anthropic's published packager (`quick_validate.py`) is observed.
- Whether omp escapes descriptions somewhere upstream of the `noEscape` template. [INFERENCE: no escape call site found.] The omp `<skills>` line is also a cached LLM summary or a truncator (`SKILL.md:91`), so what reaches the router may differ from the raw description.
- I did not run the lane-wide gates in the production repo, or any C1/C3 verifier.
- Whether the live checklist needs a new box with an `executed:trigger.no_xml_tag` disposition. The patch adds none, so the box map is unchanged at 41.
- PyYAML corner cases beyond those listed: tags `!!str`, multi-document frontmatter, CRLF.
- Tooling: nothing was installed or upgraded. PyYAML 6.0.3 was already present and is used only in my scratch battery; the verifier stays stdlib-only.
