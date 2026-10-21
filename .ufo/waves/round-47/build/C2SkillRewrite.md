verdict: Replace the literal `<skills>` token in the SKILL.md:14 description sentence with the plain phrase `omp skill catalogue`; the description drops to zero XML-tag-like tokens, stays at 824 chars (≤1024), and every trigger/anti-trigger phrase is byte-identical. Draft only; production SKILL.md untouched.

# C2 — description `<skills>` rewrite (lane C2SkillRewrite, BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd)

## Scope
Target: `SKILL.md:3-15` frontmatter `description` (YAML folded scalar `>`). The only edit is the final sentence's `<skills>` token at `SKILL.md:14`. Production files were read only. The draft lives in the scratch clone `/fast/scratch/kotoba-r47/C2SkillRewrite/lane` (detached at BASE) and the diff is saved as `.ufo/waves/round-47/build/C2SkillRewrite.patch`.

## Before / after YAML block (exact)

Before (`SKILL.md:12-15`, unchanged lines 12–13 shown for context):
```yaml
  this skill audits and reports; fixes route to the owning lane. Note: the
  shokunin files are not in an omp skill discovery root, so their descriptions
  never reach the `<skills>` router — craft here is audit-side, not
  router-visible.
```

After:
```yaml
  this skill audits and reports; fixes route to the owning lane. Note: the
  shokunin files are not in an omp skill discovery root, so their descriptions
  never reach the omp skill catalogue router — craft here is audit-side, not
  router-visible.
```

Patch hunk (`C2SkillRewrite.patch`, `@@ -11,7 +11,7 @@`): one line removed, one added; `git diff --stat` = `1 file changed, 1 insertion(+), 1 deletion(-)`.

Meaning preserved: `<skills>` named the omp catalogue tag (see `SKILL.md:22`, which explains the omp `<skills>` catalogue in the body). The replacement names the same router without a tag-shaped token. The em dash `—` is kept.

## Measurements
Measured on the YAML-parsed `description` value (PyYAML `safe_load`), which is what S001's 1–1024 bound applies to:

| Version | chars | UTF-8 bytes | XML-tag-like tokens (`</?[A-Za-z][^>\s]*>`) |
|---|---|---|---|
| BASE (`SKILL.md:3-15`) | 815 | 821 | `<skills>` (1) |
| Draft | 824 | 830 | none |

Char delta = +9 (remove 10-char `` `<skills>` `` incl. backticks, add 19-char `omp skill catalogue`). Headroom to 1024: 200 chars.

Checks run (all in scratch clone or read-only on production):
- `git clone -q --no-hardlinks … && git checkout -q --detach c61a973…` → exit 0, HEAD `c61a973`.
- `sha256sum SKILL.md` (production) = `c8b245b7…eaa0fb`; `git show c61a973…:SKILL.md | sha256sum` = same → exit 0. Production matches BASE.
- Python/PyYAML parse of before and after → both parse, exit 0.
- XML scan `</?[A-Za-z][^>\s]*>` on after: no match; `<` and `>` characters in after value: none. `<skills>` in after: False.
- Trigger/anti-trigger byte-identity (count of phrase in parsed value, before == after == 1): `"skill file"`, `"SKILL.md"`, `"frontmatter description"`, `"trigger words"`, `"prompt craft"`, `"write a skill"`, `"audit this skill"`, `"skill quality"`, and the full Anti-triggers clause `Anti-triggers: general prompt engineering for model outputs (not skill files), runtime code changes, and domain content inside a skill's reference/ tree.` All True.
- Prefix of the value up to `Note: the` identical before/after: True. Tail after edit: `Note: the shokunin files are not in an omp skill discovery root, so their descriptions never reach the omp skill catalogue router — craft here is audit-side, not router-visible.`
- Third person: regex `\b(you|your|I|we)\b` over after → no matches (exit-status-free check, empty result).
- `git -C lane diff > …C2SkillRewrite.patch` → exit 0.

## Counterexamples / caveats
- Counting by raw file lines (including 2-space indent and the `>` folded markers) gives different numbers; the 1024 bound is applied to the parsed value here. Both are far under 1024 either way.
- Removing the literal tag means a grep for `<skills>` in the frontmatter will no longer hit; that is intended, but any checker that keyed on the literal `<skills>` (rather than the XML-tag regex) would need its pattern rederived. Not checked against `verifiers/verify_skill_checklist.py` (not read; owned by the C2 verifier item).
- The body still contains `<skills>` in prose (e.g. `SKILL.md:22`, and other body lines). The S003 rule and this item cover only the description; body occurrences are out of scope and were not edited.
- `(omp) skill catalogue` vs `<skills>` naming: the phrase `omp skill catalogue` is a paraphrase, so the router name is preserved in meaning, not in literal token form. Judge whether that satisfies "keeps its meaning".

## What I did NOT check
- Did not run `verifiers/verify_skill_checklist.py`, `verifiers/verify_surfaces.py`, or any lane gate; did not confirm S001/S003 live text beyond the summary rows in `corpus/SOURCES.md:14,16`.
- Did not re-verify the claim that shokunin files are outside omp skill discovery roots (taken as given by the assignment).
- Did not edit `SKILL.md` in production or any sibling lane; no git add/commit/stash/checkout in production.
- No tools installed or upgraded.

Report: `.ufo/waves/round-47/build/C2SkillRewrite.md`; artifact: `.ufo/waves/round-47/build/C2SkillRewrite.patch`.
