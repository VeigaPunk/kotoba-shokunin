# A17 Gate-lines falsify — round 48 Gate table (S016–S021) + status-changes sentence

Verdict first: **CONFIRMED — all six rows and the 'Status changes logged' sentence. No defect found.**

Method: every URL re-opened 2026-10-22 via curl (S016/S017/S018/S021 at 08:52:49Z, S019 at
08:54:59Z UTC); line locations taken with `grep -n` (authoritative; my first sed ranges
mis-arithmetic'd, grep corrected them — see residual risk 3). Quotes recorded below are from the
fresh fetches, each ≤25 words. S020 reproduced from a `git archive` of 75f671b in scratch
(no lane mutation). SOURCES diffed between 75f671b109d8eddd0d64c1429bd6379fe577175a and
887b6af54d3f4446f1fe51dc16f26b2e83bc82e1. No tools installed (system curl/git/python3/sha256sum
sufficed).

## Row verdicts

- **S016 — CONFIRMED.** URL https://raw.githubusercontent.com/anomalyco/opencode/v1.19.3/packages/opencode/src/skill/index.ts, fetched 08:52:49Z (sha256 91dce57f…). `git ls-remote … refs/tags/v1.19.3` → `e3c4eb242585dcd77be1a867391b7c25fd47ce52` — single ref line, so the tag id equals the commit id (lightweight tag), matching "tag v1.19.3 = `e3c4eb24`". Quote exists verbatim:
  - `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` (index.ts:24) — 4 words, ≤25 ✓. Location `:24` exact ✓.

- **S017 — CONFIRMED.** URL https://raw.githubusercontent.com/agentskills/agentskills/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref/src/skills_ref/validator.py, fetched 08:52:49Z (sha256 b5ee3d85…). Quote exists verbatim:
  - `if not all(c.isalnum() or c == "-" for c in name):` (validator.py:54) — 11 words, ≤25 ✓. Location `:54` exact ✓.

- **S018 — CONFIRMED.** URL https://agentskills.io/specification.md (200, 7608 B), fetched 08:52:49Z, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` — byte-identical to the row's recorded revision (`9a67de89…`, 7608 B). Quote exists verbatim:
  - "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)" (specification.md:64) — 12 words, ≤25 ✓. Location `:64` exact, under `#### \`name\` field` heading ✓ (matches "§ `name` field").

- **S019 — CONFIRMED.** URL https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md (200, 42169 B), fetched 08:54:59Z, sha256 `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` — byte-identical to the row's recorded revision (`f0a5d61b…`, 42169 B). Quote exists verbatim twice:
  - "Cannot contain XML tags" (best-practices.md:155 and :162) — 4 words, ≤25 ✓. Both locations exact, both bullets under `## Skill structure` (heading at :146) ✓ (matches "§ Skill structure"). :155 is the `name` bullet, :162 the `description` bullet — consistent with S019's "no-XML-tags rule on both name and description".

- **S020 — CONFIRMED.** Reproduced: `git archive 75f671b` extracted to /fast/scratch/hyaku/kotoba-r48-a2/seats2/A17GateLines/selftest-75f671b (instrument sha256 4ea2100d…); `python3 -B verifiers/verify_skill_checklist.py --self-test` at 08:54:59Z → final line "0 failure(s) over 1845 assertions", exit 0. Quote "0 failure(s) over 1845 assertions" — 5 words, ≤25 ✓; "final line, exit 0" true ✓.

- **S021 — CONFIRMED.** URL https://learn.chatgpt.com/docs/build-skills.md (200, 11035 B, 232 lines), fetched 08:52:49Z, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` — byte-identical to the row's recorded revision (`ed6e324f…`, 11035 B, 232 lines). Quote exists verbatim:
  - "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." (build-skills.md:37–39) — 22 words, ≤25 ✓. Sentence starts after "file path." on :37 and ends on :39; location "md:37-39" exact ✓.

## 'Status changes logged' sentence — CONFIRMED

Claim under test: "S016–S021 created as `mined` … No other row moved."

`git diff 75f671b 887b6af -- corpus/SOURCES.md`: **0** removed/modified lines
(`grep -cE '^-[^-]'` → 0), **6** added lines (`grep -cE '^\+[^+]'` → 6), each the full registry
row `| S016 |` … `| S021 |` with status cell `mined`, opened 2026-10-22 (S016–S021 in the
hunk context show S013–S015 unchanged). No existing row's any cell — status, recheck, used-by, or
otherwise — differs between the two commits. The sentence is true, and the stronger form also
holds: the diff touches nothing but the six additions. The lesson's companion claim "S001, S003,
S010 and S013 stay as written … superseded by new rows" is consistent: supersession lives in the
new rows' teaches cells (S018 "supersedes S001", S019 → S003, S020 → S010, S021 → S013), not in
edits to the old rows.

## Findings by severity

- Critical/High/Medium/Low: none.

## Residual risk and verification gaps

1. My S016/S017/S018/S021/S019 fetches matched the recorded sha256s exactly (S018, S019, S021) or
   the recorded tag commit (S016), so row identity is proven, not just today's content.
2. S016/S017 verified against raw.githubusercontent.com renders (same blobs as the cited
   github.com URLs); S018/S019/S021 against the .md render endpoints the rows themselves cite.
   The S018/S019/S021 HTML pages were not re-fetched this session; the sha256 equality with the
   seats' recorded fetches closes that gap for revision identity.
3. False alarm worth logging: my first line-location reads used `sed -n '20,28p'`/`'58,70p'` and
   mis-counted the print window, suggesting off-by-one defects at index.ts and specification.md;
   `grep -n` proved both Gate locations (`:24`, `:64`) exact. Reviewers counting sed windows by
   hand will manufacture this defect; grep -n is the check.
4. Operational note: the first S019 curl failed (scratch dir race between parallel shells, exit 2);
   retried once and succeeded. Not a source-side issue; both attempts logged above.
5. S020 reproduction used `git archive` of the commit tree rather than a checkout of the lane
   working tree — identical content by construction (same commit object), bounds-compliant.
6. The Gate sentence "each opened on 2026-10-22 by a wave-1 seat; the seat report holds the full
   fetch record" was not audited seat-report-by-seat-report — out of my scope (rows and status
   sentence only); the sha256 matches above independently corroborate the seat fetches.

Artifacts kept under /fast/scratch/hyaku/kotoba-r48-a2/seats2/A17GateLines/ (spec.md,
validator.py, index.ts, claude-bp.md, build-skills.md, selftest-75f671b/). No lane file touched
except this report.
