# ReopenS038 — SOURCES row S038 (supersedes S031), judged rev `c8407a453788df964df5a7b835dd0ce1360de882`

Result: HOLDS — S038 conforms to SOURCES contract rule 2 and its Gate quote, sweep counts and bytes re-open byte-identical; three minor calibration defects (D1–D3) are recorded for the L1 and none falsifies a claim as written.

## Target and artifact

- Row: `corpus/SOURCES.md:51` (11 cells, `NF=13`).
- Gate record: `corpus/lessons/round-52.md:35-40`.
- Page re-opened cold in my own scratch (`/fast/scratch/hyaku/kotoba-r52a2/ReopenS038/`), ordinary `curl` only.

### Re-open evidence (URL, time, bytes, sha256)

| fetch | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| command reference `.md` | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md` | 2026-10-22T17:50:11Z | 200, `content-type: text/markdown; charset=utf-8` | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| same page, HTML route | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference` | 2026-10-22T17:50:55Z | 200 | 1,971,126 | `fbc28449733cb1f4e0df2dbe1d4f872f52418d055a9202291349c8b39f8bf379` |
| config-dir reference `.md` (linked from :1300) | `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md` | 2026-10-22T17:50:55Z | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |

The `.md` artifact is byte-identical to both recorded reads: S038's `2026-10-22T17:07:03Z` (461,944 B, `c61997ef…`) and S031's `2026-10-22T14:19:21Z` (461,944 B, `c61997ef…`). Three independent opens 3 h 31 m apart, same hash: no rot behind the row.

## HOLDS — checks that survived

1. **Sweep counts reproduce exactly** (cwd = scratch; artifact = the 17:50:11Z `.md`):
   ```
   $ grep -c -F disabledSkills cli-command-reference.md
   0
   exit=1                      # zero matches; the printed 0 is what the Gate records
   $ grep -c -F ignoredSkillsLocations cli-command-reference.md
   1
   exit=0
   $ grep -c -F disable-model-invocation cli-command-reference.md
   2
   exit=0
   $ grep -c -F 'copilot skill disable' cli-command-reference.md
   1
   exit=0
   ```
   Occurrence counts (`grep -o … | wc -l`) are identical to the line counts here, so the Gate's bare numbers are unambiguous on this page. The two `disable-model-invocation` hits are `:1278` (frontmatter table) and `:1334` (commands section), which agrees with the teaches cell naming it as a frontmatter field.

2. **Gate quote is verbatim, located, and inside the word limit.** Line 1300 begins with the quoted string; it is a contiguous substring, 13 words (limit 25):
   ```
   line1300 starts with quote: True
   quote words: 13
   substring: True
   ```
   Quote as recorded in `corpus/lessons/round-52.md:38-39`: "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their descendants) from discovery".

3. **Rule 2 shape is exact.** The `teaches` cell begins `supersedes S031 — ` with U+2014, matched by `^supersedes S\d{3} — ` (python `re`, True). The correction is a new row, not a rewrite, and the old row is untouched:
   ```
   $ git diff c8579a4c… c8407a45… -- corpus/SOURCES.md | grep -cE '^\+[^+]'
   7
   $ git diff c8579a4c… c8407a45… -- corpus/SOURCES.md | grep -cE '^-[^-]'
   0
   ```
   This independently confirms the lesson's "Rows touched (old → new): None of S001–S031 changed in place" (`corpus/lessons/round-52.md:62`): seven added rows, zero removed or modified bytes.

4. **All three anchor lines land in their claimed sections** (headings in the artifact): `:1278` inside `### Skill frontmatter fields` (heading `:1269`); `:1300` inside `### Skill locations` (heading `:1280`), and `ignoredSkillsLocations` occurs only there; `:1324` inside `### Managing skills non-interactively` (heading `:1304`), the `copilot skill disable my-skill` example line.

5. **The teaches claims are true as written.** `disable-model-invocation` is a frontmatter field at `:1278` ("Prevent the agent from automatically invoking this skill. Default: `false`."); `copilot skill disable my-skill` is a documented form at `:1324` and `copilot skill` is listed with `…, enable, and disable skills` at `:21`; the negative holds on both routes of the page (`disabledSkills` 0 in `.md`, 0 in the 1.97 MB HTML).

6. **Row shape and registry hygiene.** `rows=38`, `malformed=0`, duplicate-id check prints nothing; `S038` appears once; `opened 2026-10-22` matches the re-open, `recheck 90d`, `tier A` on `kind docs` is legitimate under the tier definition (vendor documentation, scoped to the command reference). Rule 1's Gate record carries URL, access date, bytes, sha256 and a located quote, so rule 1 is satisfied in letter for S038.

## Defects found (calibration; none falsifies a claim as written)

**D1 — the negative is true of one page, but reads as a denial of the field. Severity: minor.**
`disabledSkills` is documented by Copilot CLI on the page the quoted paragraph itself links to (`:1300` → `cli-config-dir-reference#configuration-file-settings`), fetched 17:50:55Z:
- `cli-config-dir-reference.md:461`: "`disabledSkills` | `string[]` | `[]` | Skill names to disable. Listed skills are discovered but not loaded."
- `cli-config-dir-reference.md:566`: "`disabledSkills` | `string[]` | Union—repository can add entries, never remove | Skills discovered but not loaded."
- the sibling `ignoredSkillsLocations` row is at `:473`, and it points back to the command reference's `#skill-locations`.

So S031's key was not invented; it was attributed to the wrong page. S038's sentence "it does not contain `disabledSkills` (0 occurrences), which S031 named" is literally true of the command reference and its `scope` cell is bounded to "in its command reference", so this is not a break — but a reader can leave with "Copilot CLI has no `disabledSkills`", which is false. Suggested repair (one clause, no new claim): say the field is documented in the configuration-file reference, not in this page.

**D2 — the headline quote grounds the lever this round removed from the per-skill list. Severity: minor.**
The row's `scope` cell says "per-skill removal levers", yet its anchor lead, its `teaches` and its Gate quote all centre on `ignoredSkillsLocations` (`:1300`), which is directory-scoped, not per-skill. The lane's own frozen counter expects Copilot CLI's per-skill lever to be `disable-model-invocation` (`verifiers/check_overlap_levers.py:165`), and the same round's repair block lists exactly that (`corpus/README.md:163`). Suggested repair: add the `:1278` quote (or swap it in as the Gate quote) and keep `ignoredSkillsLocations` as the neighbouring mention.

**D3 — `scope` retains a claim the row no longer grounds. Severity: minor.**
`scope` still says "and the name-keyed arbitration rules it repeats", but the anchor lists only the three skills sections and neither `teaches`, the anchor nor the Gate quote touches arbitration. The arbitration text is on the page (`:1298` "follow the same name-based priority"; `:1302` plugin-qualified names with "the bare name routes to the higher-priority plugin"), so the claim is true but unquoted: A-tier scope for text the row does not cite. Repair: narrow `scope`, or add the `:1298-1302` quote.

**D4 — `mined` rests on the row's own Gate record. Severity: informational.**
`used-by` is `corpus/lessons/round-52.md` and that path names S038 only as its birth record (`:35`), not as provenance for a claim. The strict contract split is `queued` (opened, worth mining) vs `mined` (cited by ≥1 path in `used-by`). Precedent in this registry treats a lesson as sufficient (S001, S003, S016 are `mined` with a lesson-only `used-by`), so this is the established convention; flagging only because the ticket asks about rule conformance.

**D5 — superseded row is still the citation behind two live claims. Severity: informational.**
`SKILL.md:412` and `corpus/knowledge/skill-overlap-levers-round51.md:1,21` cite S031 for the true `disable-model-invocation` claim (`:1278`). The quoted content is correct at that line, so no false claim is carried; but a clean cutover would repoint those two citations to S038, since S031's `teaches` is now known wrong in its other clause. No contract rule requires it (rule 2 keeps the old row's true content usable).

## What I did not check (out of my question)

- `S024`'s superseding row, the C2 client rows (S032–S037), `check_mcp_instructions.py`, the C1 counter, the repair diffs and M36's sweep — other seats.
- Freshness beyond this one page: the row's `recheck 90d` is a stated cadence, not a measurement.
- Whether the page's HTML and `.md` routes agree on the other six quoted lines; I compared only the four sweep terms plus `:1300`.

## Method / tooling

- No installs, no upgrades. Tools used: `curl`, `grep`, `awk`, `sed`, `python3 -B` (inline), read-only `git diff` in the lane.
- Writes: this file, plus scratch artifacts under `/fast/scratch/hyaku/kotoba-r52a2/ReopenS038/` (`cli-command-reference.md`, `html.html`, `config.md`, `headers.txt`). Nothing else touched in the lane; no lane git or jj writes.
- Inference is marked by phrasing; every count, byte total and hash above is pasted from a command I ran in this session.
