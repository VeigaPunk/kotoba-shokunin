# ReopenS031 — attacking C2's GitHub Copilot CLI row (kotoba round 51, falsify)

Verdict: HOLDS — re-opening the live page (hash-identical to the landed record) confirms the quote
verbatim at the cited line, every cell of the entry row and SKILL.md row, all S031 row attributes
and its Gate record, and no page rule that decides between two differently named skills that both
remain candidates.

## Fetch (my own re-open, not a replay of the seat's)

URL https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md,
2026-10-22T15:15:35Z, HTTP 200, 461,944 B, sha256
`c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` — prefix `c61997ef` as expected,
same size and hash as the S031 record's 2026-10-22T14:19:21Z fetch and the entry recheck's target:
the page is byte-identical to the bytes the row was mined from.

## Point 1 — quote verbatim at cited line, ≤25 words, exact backtick span — HOLDS

Entry quote (§ Levers by client, Copilot CLI row): "Use the `ignoredSkillsLocations` setting to
exclude specific directories (and their descendants) from discovery, regardless of which location
above would otherwise surface them." (cli-command-reference.md:1300).
- Fixed-string count of the full quote in the fetched bytes: 1 (the quote occurs, character-exact,
  as the first sentence of line 1300; the line continues "See [GitHub Copilot CLI configuration
  directory](…)").
- Word count 22 (≤ 25). `ignoredSkillsLocations` appears exactly once in all 1945 lines — inside
  this quote — so the key term is an exact backtick span in the quote and unique to this lever.
- Cited line 1300 is exact (grep with line numbers).

## Point 2 — the page says what the cells say — HOLDS

Read § Skills reference end-to-end (page lines 1267-1335), not just line 1300.
- Entry lever cell "the user's settings exclude whole skill directories from discovery": line 1300
  says the setting excludes "specific directories (and their descendants) from discovery,
  regardless of which location above would otherwise surface them"; the line links to the CLI
  configuration-directory reference (a user config file). Whole directories, by settings. Match.
- SKILL.md lever "exclude the skill's directory from discovery": same line; directory granularity
  honestly bounded again in the entry's Limits ("works per directory, not per skill name"). Match.
- SKILL.md "held by: user or operator": `ignoredSkillsLocations` is a CLI setting, not frontmatter —
  the § Skill frontmatter fields table (1269-1279) has six fields (name, description,
  argument-hint, allowed-tools, user-invocable, disable-model-invocation) and no location-exclusion
  field; the § Skill locations exclusion belongs to the config file (`copilot config` scopes
  global/repo/local at 131-136). The skill author cannot set it. Match.
- SKILL.md "effect: removed everywhere": § Skills reference intro (1267-1268) says invocation is
  "via `/SKILL-NAME` or automatically by the agent" of discovered skills; exclusion from discovery,
  "regardless of which location", leaves no retained invocation path on the page (contrast VS Code
  `user-invocable`, which the Gate rejected for the opposite effect). Supported reading.
- SOURCES S031 details also check out on this page: `disable-model-invocation`, default `false`,
  stops automatic invocation only (1278); `copilot skill enable/disable <name>` by name (1304-1330);
  "first found wins for duplicate names" (1282); plugin same-name coexistence with the bare name
  routing to the higher-priority plugin (1302); commands lose to skills of the same name (1334).

## Point 3 — S031 row and Gate record — HOLDS

corpus/SOURCES.md line 44: kind `docs`, tier `A`, status `mined`; URL under the vendor docs prefix
(docs.github.com/en/copilot/reference/copilot-cli-reference/); fetch cell records (200, 461,944 B,
sha256 `c61997ef…`) at 2026-10-22T14:19:21Z — matching my fetch byte-for-byte; `used-by` names
corpus/knowledge/skill-overlap-levers-round51.md. corpus/lessons/round-51.md § Gate → Admitted
records S031 with this quote, line 1300, the 22-word count, Tier A, `docs`, `mined`, `used-by` the
entry, and the note that S028 (plugin reference) was not used because it lacks this lever.

## Point 4 — no rule deciding between two skills that both remain candidates — HOLDS

Sweep `grep -niE 'overlap|conflict|precedence|tie|both|choose|select|priorit'` on the fetched bytes:
449 matched lines, overwhelmingly UI/keyboard and flag rows; every skill-relevant hit read:
- 1282 "first found wins for duplicate names" — name-keyed; the loser is not loaded.
- 1295 bundled skills "Lowest priority—overridable by any other source" — name-keyed.
- 1298 remote vs local "follow the same name-based priority when a local skill has the same name".
- 1302 two plugins, same name: both coexist under plugin-qualified names, bare name routes to the
  higher-priority plugin — the closest hit to "both remain candidates", but it requires identical
  names and is priority-keyed, not description-based. SOURCES S031's teaches cell already records
  exactly this, and SKILL.md's negative is scoped to "two differently named, author-written skills
  whose descriptions both match". No contradiction.
- 1334 commands vs skills of the same name — component-type rule, name-keyed.
- 1176 remote catalog: relevance-ranked candidates "presents candidates for you to choose from" —
  the discover-resources skill suggesting MCP servers/skills to install; not a routing rule.
`description` (1271) carries no precedence language. The page documents no tie-break between two
differently named skills whose descriptions both match — consistent with the entry's finding 2 and
SKILL.md's "none decides between two skills that both remain candidates" as scoped by the
error-pattern sentence.

## Findings by severity

- Blocking: none.
- Major: none.
- Minor/informational:
  1. "removed everywhere" is an inference from exclusion-from-discovery; the page never states in
     so many words that an excluded skill cannot be manually invoked. The § Skills reference intro
     (invocation only via `/SKILL-NAME` or automatically, of discovered skills) supports it, and the
     entry's Limits already discloses that the effect taxonomy is a reviewer's judgment frozen in
     the checker. No repair required.
  2. The quote is a sentence-prefix of line 1300 (drops the trailing "See […]"); the citation is to
     the sentence, and the checker bounds quotes to ≤25 words. Cosmetic, no repair required.

## Residual risk and verification gaps

- Scope is the Copilot CLI row only (my assignment); the other six client rows were not re-opened
  here. The L1's `--fetch` (7 of 7 at 15:10:48Z per the round context) is the instrument that covers
  all seven; I did not rerun it.
- A decision rule phrased with none of the swept terms could evade the grep; mitigated by reading
  the entire § Skills reference (1267-1335), the only section where a skill-routing rule could live.
- Pages move: this fetch is a point-in-time confirmation (15:15:35Z); the entry's recheck line is
  the standing instrument.

## Evidence (commands and exit codes)

- `date -u +%Y-%m-%dT%H:%M:%SZ` → 2026-10-22T15:15:35Z; `curl -sS -w 'HTTP_STATUS=%{http_code}' -o
  page.md <URL>` → HTTP_STATUS=200, curl_exit=0; `wc -c < page.md` → 461944; `sha256sum page.md` →
  c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9.
- `grep -n ignoredSkillsLocations page.md` → single hit, line 1300 (grep tool, line-numbered).
- `grep -Fc '<full quote>' page.md` → 1 (exit 0); `printf '%s' '<full quote>' | wc -w` → 22;
  `grep -c ignoredSkillsLocations page.md` → 1.
- Skill-scoped sweep: `(?i)skill.*(conflict|preceden|priorit|tie|duplicate|same.name|first.found|
  dedup|choose|both)|…` → hits 1176, 1282, 1295, 1298, 1300, 1302, 1334, all read with context.
- Reads: SKILL.md:380-405; corpus/knowledge/skill-overlap-levers-round51.md:1-100;
  corpus/SOURCES.md:44; corpus/lessons/round-51.md § Gate; page.md:1249-1335.
- Tool installs/updates: none (curl, sha256sum, grep already present; pacman untouched per pause).
