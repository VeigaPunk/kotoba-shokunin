# A13SkillLine151 — falsify SKILL.md:151 (C1 freshness, 887b6af)

Seat: KotobaR48.A13SkillLine151. Date 2026-10-22 (UTC). Leaf: no delegation, no tool installs
(system Python 3 + curl only; pacman untouched).

## Verdict

**CONFIRMED.** Every clause of the rewritten line 151 matches the live sources and the named
build evidence; all four cited SOURCES rows exist; the gate is fully green in-situ at the landed
commit (exit 0, 11 PASS / 0 FAIL). No defect found in scope. Residuals below are declared or
cosmetic, none rises to DEFECT.

## Identity and bounds

- Lane working tree SKILL.md sha256 `1923484600b5879c16d390aff43698f0974616946150c0b20787ed5e65d3ee22`
  == clone @ `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1` (same for verify_skill_checklist.py
  `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a`).
- `git diff 75f671b 887b6af -- SKILL.md` shows exactly this rewrite: citations S001/S002/S003/S008 →
  S018/S002/S019/S008; "gates the XML-tag rule" → "approximates … on the unparsed text"; "is
  stricter and refuses" → "refuses any `<`/`>` in the parsed value, so the two disagree in both
  directions"; entry pointer appended. Commit subject confirms "SKILL.md portability floor corrected".
- No lane mutation; gates run in `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A13SkillLine151/kotoba-shokunin`
  (private clone) plus one in-situ read-only run (verifier's only writes are inside its `--self-test`
  fixture arm, verify_skill_checklist.py:2154+; plain `--json` writes nothing — grep-verified).

## Clause-by-clause vs live sources (all re-opened by this seat)

1. Cited rows exist: corpus/SOURCES.md S002 (:15), S008 (:21), S018 (:31), S019 (:32) — plus S012
   (:25), S017 (:30), S020 (:33), S021 (:34) used by the entry. Entry tracked at 887b6af
   (blob `ddf07e59…`).
2. `name` ≤64 — spec line 63 "Must be 1-64 characters". URL https://agentskills.io/specification.md,
   accessed 2026-10-22T08:52:35Z, 7,608 B, sha256 `9a67de89…a8dfde16` — byte-identical to S018's
   recorded fetch; recheck grep 'Must match the parent directory name' → 1.
3. lowercase letters/digits + single hyphens — spec:64 "May only contain unicode lowercase
   alphanumeric characters (`a-z`, `0-9`) and hyphens"; :65 no leading/trailing hyphen; :66 "Must
   not contain consecutive hyphens". "Single hyphens" is a fair compression. Equal-to-directory:
   spec:67 (quote above).
4. Spec charset ambiguity on Unicode — CONFIRMED as a genuine self-contradiction: :64 says
   "unicode …" but lists ASCII-only `a-z`/`0-9`, while the frontmatter table (:30) says "Lowercase
   letters, numbers, and hyphens only". Validators split accordingly (skills-ref NFKC+isalnum valid;
   packager `^[a-z0-9-]+$` invalid — C2LaneCheckerRun f04).
5. `description` ≤1024 — spec:101 "Must be 1-1024 characters"; bp.md:161 "Maximum 1,024 characters".
6. "no XML tags (Anthropic rule)" — bp.md:155/:162 "Cannot contain XML tags"
   (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md, accessed
   2026-10-22T08:52:35Z, 42,169 B, sha256 `f0a5d61b…3423960` = S019's superseding fetch). The live
   spec has 0 hits for angle-bracket/XML (grep -c → 0, exit 1), so the Anthropic attribution is exact.
7. YAML clause — https://yaml.org/spec/1.2.2/ (383,078 B, accessed 2026-10-22T08:54Z), §7.3.3
   verbatim: "Plain scalars must never contain the ': ' and ' #' character combinations." Lenient/
   strict: S002 page (accessed 2026-10-22T08:57Z) "technically invalid YAML that their parsers happen
   to accept. The most common issue is unquoted values containing colons" + "Lenient validation" §.
8. "lexical approximation on the unparsed name/description text" — verifier XML_TAG_RE (:404-406) +
   YAML_ANGLE_ESCAPE_RE (:409), check body :1294+; C2LaneCheckerRun F2 states the same mechanism.
9. Packager "refuses any `<`/`>` in the parsed value" — quick_validate.py at pin `dbd4588`
   (https://raw.githubusercontent.com/anthropics/skills/dbd4588…/skills/skill-creator/scripts/quick_validate.py,
   accessed 2026-10-22T08:52:35Z, sha256 `67cf5703…fde365` = S012 receipt): :35
   `yaml.safe_load(frontmatter_text)`, :79-81 bracket refusal message.
10. "disagree in both directions" — CONFIRMED against C2LaneCheckerRun.md (the named evidence):
    6/10 fixtures diverge from S012; lane LAXER in five (f02/f02b alias-hidden tag, f05 `->`,
    f06 `a < b`, f07 folded split: lane PASS, packager FAIL) and lane STRICTER in one (f08
    single-quoted `'\u003cb\u003e'`: lane FAIL, packager PASS). Both directions present; the
    round-47 "stricter" claim was rightly dropped (old line visible in the diff).

## Gate run (assignment command)

- In-situ canonical (lane checkout, cwd = lane root):
  `python3 -B verifiers/verify_skill_checklist.py --json` → **exit 0; 11 PASS / 0 FAIL / 0 N/A.**
  The declared worst case ("governance.citation_resolves possibly red on SCORECARD.md's
  not-yet-landed fleet report path") did not materialize: SCORECARD.md:28/:32 cite lane-internal
  receipts (`.ufo/round-48/verification/…`), and its older report refs are tracked lane paths;
  LOG.md's `../` citations resolve against the fleet parent, where round-7/9/11 reports,
  PROTOCOL.md and .ufo/l0-questions.md all exist (sampled, all EXIST).
- Bare private clone (dir correctly named kotoba-shokunin) at 887b6af: exit 1, exactly 2 FAILs —
  trigger.citation_resolves (SKILL.md:518 → `../.ufo/reports/round-7/kotoba.md`) and
  governance.citation_resolves (LOG.md:177/255/311/779 +20 more, all `../` fleet paths). Pure
  location artifacts of cloning away from the fleet parent; zero failures touch line-151 content.
  First clone attempt in a dir named `clone` also tripped trigger.name_directory — artifact of the
  directory name, cleared by renaming.

## Residual risk and verification gaps

- The check's FAIL-detail string still claims the packager "is stricter"
  (verify_skill_checklist.py:1306-1307) — contradicts line 151's correction but is DECLARED left
  unchanged this round (entry §4; C2LaneCheckerRun F5). Known text defect, unchanged; not charged.
- Line 151 compresses spec "1-64"/"1-1024" to ≤; the non-empty floors are enforced by
  trigger.frontmatter_parses in the same gate. Cosmetic.
- S017/S021/Codex-CLI cells of the knowledge entry were not independently re-executed here (no
  skills-ref/PyPI or Codex CLI run by this seat); their rows exist and the entry marks the Codex-CLI
  figures as untabled. Out of my clause set (line 151 cites S018/S002/S019/S008/S012 only).
- No runtime trigger/load behavior was measured — entry's own Limits say the same.

Report: .ufo/waves/round-48/falsify/A13SkillLine151.md
