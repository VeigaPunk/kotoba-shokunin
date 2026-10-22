# ReviewOverlapRows — pre-landing cross-check of the C2 source set (round 51, 2026-10-22)

CROSS-CHECK COMPLETE: three pages re-opened independently by plain curl, all HTTP 200; one lever
sentence pinned per page with line anchors; round-50 "What this changes for craft" paragraph has no
false statement on these bytes, but three imprecisions, one of which constrains which key term the
C2 Claude Code row may use.

## Fetch record (curl -sS, plain fetch, no browser; UTC)

| URL | time (UTC) | status | bytes | sha256 |
|---|---|---|---|---|
| https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills.md | 2026-10-22T14:19:37Z | 200 | 35,455 | `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` |
| https://opencode.ai/docs/skills.md | 2026-10-22T14:19:38Z | 200 | 5,365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| https://code.claude.com/docs/en/skills.md | 2026-10-22T14:19:37Z | 200 | 111,557 | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |

Drift: opencode `f10ced73…` and Claude `cdfcb0df…` match the round-50 entry's recheck prefixes
(byte-identical since the L1's 13:36Z verification). The SDK page's `64856ff4…`, 35,455 B matches
`corpus/lessons/round-50-verifier-spotcheck.md:188` (the round-50 sample's bytes) — stable since
then. No page moved between the round-50 reads and this re-read.

## Per-page lever (best sentence, other than description wording, for keeping a skill from being chosen)

### GitHub Copilot SDK (`skills.md`, fetched bytes in scratch as `github-copilot-sdk-skills.md`)

Quote (6 words, line 809, under `### Skill conflicts` at :805, which opens "If multiple skills
provide conflicting instructions:" :807):

> Use `disabledSkills` to exclude conflicting skills

What the lever does per the page: `disabledSkills` is a session-configuration field of the embedding
application, set at session creation, keyed on the skill's `name` — "Disable specific skills while
keeping others active" (:179), example `disabledSkills: ["experimental-feature", "deprecated-tool"]`
(:187), config-table description "Skills to disable" (:697), and the frontmatter `name` is "used
with `disabledSkills` to selectively disable it" (:288). Precision limit: the page does NOT state
whether exclusion means the skill is dropped from the model's catalog listing or rejected at
invocation — listing-vs-use is undocumented on this page; "disable/exclude" is all it claims. It is
an application-side config lever, not user-only and not a permission rule. Same-page companions:
provider `enableSkills: false` keeps a provider "bound but never called" (:683); `mode: "empty"`
"excludes every runtime-bundled built-in skill" (:714-715); provider catalog metadata optionally
carries `userInvocable` and `disableModelInvocation` (:302), and serving existing SKILL.md files
maps `user-invocable` / `disable-model-invocation` frontmatter (:648); a provider skill with the
same name as a file-based skill replaces it (:685, name-keyed).

### opencode (`skills.md`, fetched bytes in scratch as `opencode-skills.md`)

Quote (11 words, line 128, under § Recognize tool description):

> Skills with `metadata["opencode/autoinvoke"]` set to `"false"` are not included in `<available_skills>`.

What the lever does per the page: hides the skill from the model-facing auto-selection guidance —
the bullet form says "set to `\"false\"` to keep the skill out of model-facing auto-selection
guidance" (:45; restated in troubleshooting at :231). It is a hide-from-model-listing lever, NOT a
deny: "They can still be selected manually and loaded by exact name." (:129). Contrast with the
stronger access lever on the same page: permission `deny` in `opencode.json` = "Skill hidden from
agent, access rejected" (:153, § Configure permissions :133), i.e. hide AND reject at use; and
`tools: skill: false` per agent omits the `<available_skills>` section entirely (:194, :219).

### Claude Code (`skills.md`, fetched bytes in scratch as `claude-skills.md`)

Quote (18 words, line 886, under § Restrict Claude's skill access, in the "Three ways to control
which skills Claude can invoke" passage):

> Hide individual skills by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely.

What the lever does per the page: a frontmatter flag that removes the skill from the model's side
entirely — description not in context ("Description not in context", :577), Claude cannot invoke it
on its own (:549; :844 "By default, Claude can invoke any skill that doesn't have
`disable-model-invocation: true` set"), and it also prevents preloading into subagents and
scheduled-task runs (:393). User invocation by `/name` still works (:393 "trigger manually with
`/name`"; :577 "Not on its own"). So: disable/hide for the model, user-only invocation remains; not
a permission deny (separate `Skill(deploy *)` deny rules exist, :846-870). Same-page companions:
`paths` globs condition auto-activation on file matches (:403); `user-invocable: false` hides from
the `/` menu while Claude keeps it (:394, NOTE :890); `skillOverrides` `"off"` / `"user-invocable-only"`
/ `"name-only"` from settings without editing the file (:892-907).

## Comparison: round-50 entry, § What this changes for craft (`corpus/knowledge/skill-selection-rules-round50.md`)

Verified accurate on these bytes: the S022 line refs 390 (`when_to_use` "Appended to `description`
in the skill listing"), 393 (`disable-model-invocation` "prevent Claude from automatically loading
this skill"), 403 (`paths` "Glob patterns that limit when this skill is activated") all match the
byte-identical fetch. The negative claim — no client documents a rule comparing two descriptions —
still holds on all three pages: the SDK's conflicts section routes to `disabledSkills` or directory
reorganization (name/config-keyed), opencode routes to unique names, permissions and `autoinvoke`,
and Claude Code's § Skill triggers too often pairs description specificity (:1194) with
`disable-model-invocation: true` (:1195) rather than any inter-description rule.

Findings (imprecision, in increasing severity):

1. **"limit activation" understates `disable-model-invocation`** — per :886/:577 it is a categorical
   model-side removal (user-only invocation remains), not a soft activation limit. Conservative
   direction; the lever is stronger than the entry states.
2. **"The description is the lever every client listed here reads"** holds only for skills that
   remain model-invocable: with `disable-model-invocation: true` the description is not in context
   at all (:577), and under opencode `deny` the skill is hidden and rejected (:153).
3. **`when_to_use` is classified as a lever "other than" the description, and per these bytes it is
   description wording.** S022:390 says it is "Appended to `description` in the skill listing" —
   additional choice-guidance text in the same input. The page itself treats the two as different
   remedy classes (:1194-1195). C2 consequence: if the Claude Code row's key term is `when_to_use`,
   it is exposed to the checker's "key term about the description" mutant class; the defensible
   Claude Code key terms are `disable-model-invocation` (or `paths`).

Confirmed gap (the gap C2 exists to fill, not an error): the round-50 paragraph's lever inventory is
Claude-Code-only. The other two pages document non-description levers it does not list — SDK
`disabledSkills` (:809) and opencode `opencode/autoinvoke` (:128, :45) plus permission `deny`
(:153). Nothing on the three pages contradicts finding 1's negative or the name-keyed
characterization of documented collision rules (SDK :685 is name-keyed, as the round-50 falsify
correction already recorded).

Corpus state observed (context only, not graded): no `copilot-sdk/features/skills` row in
`corpus/SOURCES.md` yet and `corpus/knowledge/skill-overlap-levers-round51.md` not yet present —
expected mid-build; the C2 counter requires those rows to be `mined` with `used-by` naming the entry.

## Evidence

- `curl -sS -w 'HTTP_STATUS %{http_code}' -o <scratch file> <url>` ×3 → `HTTP_STATUS 200`, `EXIT 0`
  each; bytes and sha256 as in the fetch record (`wc -c`, `sha256sum`).
- Round-50 recheck prefixes compared by eye against `sha256sum` output: opencode `f10ced73` ✓,
  Claude `cdfcb0df` ✓; SDK `64856ff4` ✓ against `round-50-verifier-spotcheck.md:188`.
- Line anchors from `grep -n`-equivalent over the fetched bytes and raw range reads
  (SDK :175-190, :285-291, :683, :713-719, :804-812; opencode :38-50, :120-135, :145-160, :190-235;
  Claude :840-891, :1186-1196, plus table rows :389-403 from the anchored grep).
- Bounds honored: lane untouched except this report file; fetches and scratch only under
  `/fast/scratch/hyaku/kotoba-r51/build/ReviewOverlapRows/`; no subagents; no headless browser; no
  tool installs (none needed); no Src* seat reports read.
