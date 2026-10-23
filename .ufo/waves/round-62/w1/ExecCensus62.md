# ExecCensus62 — S118 source-census probe

## Scope and result

Read the fleet `CORPUS.md` SOURCES.md contract v1 and its census instructions. Copied `corpus/SOURCES.md` to `/fast/scratch/hyaku/kotoba-r62/ExecCensus62/kotoba/corpus/SOURCES.md`, appended the S118 probe row below directly inside `## Registry` after S117, and ran the maintained validator plus every manual census command on that scratch copy. The only repository write is this report; the ledger copy, fetched page, and symlinks used to let the validator resolve existing `used-by` paths are under `/fast/scratch`.

S118 probe row (exact tested text):

```markdown
| S118 | Claude Code Docs — How Claude remembers your project (`paths` rule-frontmatter reference) — https://code.claude.com/docs/en/memory.md | docs | A | Claude Code rule-frontmatter `paths` semantics for matching-file scope (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`); fetched 2026-10-23T20:54:04Z, HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801` | re-opens S103 — Claude Code defines `paths` as “Glob patterns that scope the rule to matching files”; it accepts a YAML list or a comma-separated string | queued | 2026-10-23 | 90d | — |
```

This is a census probe, not a lane write or a claim that the eventual S118 status/`used-by` is final. `queued` / `—` is appropriate for this probe because contract v1 calls a row `mined` when at least one knowledge entry or lesson is cited in `used-by`; that final use path must be set by integration if one exists. The row's 11 cells contain no embedded `|`.

## Contract facts applied

- Contract v1's registry table has 11 columns; with its leading and trailing Markdown delimiters the row has `NF=13`. It requires append-only rows, a source opened in the row-author's round, an exact section/heading/page/line and revision in `anchor`, one grounded learner benefit in `teaches`, and the round lesson's `## Gate` to record each new row's URL, access date, and a quote of at most 25 words with location. The page/census work here is only a shape probe and does not replace the S118 author's access record or the planned second-seat re-open.
- The source page quote used in the probe is from `§ Rule frontmatter reference`, `memory.md:244-250`; the exact table line is: `| \`paths\` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |`. The quoted phrase in `teaches` is the exact link text; the following list/string statement is also from that line.
- Fetch measurement at `2026-10-23T20:54:04Z` (exit 0); exact scratch-only command:
  ```sh
  curl -fsSL --max-time 30 -o /fast/scratch/hyaku/kotoba-r62/ExecCensus62/S118.page -w 'http=%{http_code}\\n' 'https://code.claude.com/docs/en/memory.md' && wc -c /fast/scratch/hyaku/kotoba-r62/ExecCensus62/S118.page && sha256sum /fast/scratch/hyaku/kotoba-r62/ExecCensus62/S118.page && date -u +%Y-%m-%dT%H:%M:%SZ
  ```
  Output: `http=200`; `55354 /fast/scratch/hyaku/kotoba-r62/ExecCensus62/S118.page`; `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /fast/scratch/hyaku/kotoba-r62/ExecCensus62/S118.page`; `2026-10-23T20:54:04Z`. No fetched-page content was treated as instructions.

## Maintained validator

Command, 2026-10-23T20:54:32Z (UTC), exit 0:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-23 --root /home/vgpnk/Projects/shokunin /fast/scratch/hyaku/kotoba-r62/ExecCensus62/kotoba
```

Exact stdout and exit receipt:

```text
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/fast/scratch/hyaku/kotoba-r62/ExecCensus62/kotoba/corpus/SOURCES.md
exit=0
```

W04 is explicitly a warning (“same URL across scopes”) and does not fail validation. S103 already holds the URL, so the new distinct-scope S118 row correctly produces W04; the output also retains S103's existing W04. This is the expected declared re-open result. The validator's E04 is different: it flags the same URL within the same scope unless `teaches` contains `supersedes S###`. `re-opens S103 —` is not an E04 exemption; the probe's scope is distinct from S103's scope, so the observed condition is W04, not E04.

## Manual census block

The following are the exact commands from `CORPUS.md`, run from `/fast/scratch/hyaku/kotoba-r62/ExecCensus62/kotoba` on the final scratch copy. UTC date and each exit code are retained. Rows/tier/status checks were captured at `2026-10-23T20:54:32Z`; duplicate-ID, enum, and used-by checks at `2026-10-23T20:54:40Z`.

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
```

```text
2026-10-23T20:54:32Z
116
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
```

```text
2026-10-23T20:54:32Z
0
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
```

```text
2026-10-23T20:54:32Z
A=113 B=2 C=1 
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
```

```text
2026-10-23T20:54:40Z
mined=107 queued=8 rejected=1 
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
```

```text
2026-10-23T20:54:40Z
(no output)
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
```

```text
2026-10-23T20:54:40Z
(no output)
exit=0
```

```sh
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

```text
2026-10-23T20:54:40Z
(no output)
exit=0
```

The shape command's zero means no source row had a field count other than 13; it verifies the requested 11-column shape. The count is 116 table rows in this scratch ledger after adding S118.

## `census-after.txt` receipt template

No lane after-receipt was written or run: the lane is read-only to this seat, and the row above exists only in scratch. After integration, run the recorded lane-root command and paste its fresh stdout and actual UTC time/exit code. Based on the current scratch validation and `census-before.txt`, the expected template is:

```text
# census-after — round 62 (lane kotoba)
date_utc=<actual output of date -u +%Y-%m-%dT%H:%M:%SZ>
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
kotoba	W04	S018 duplicate url agentskills.io/specification across scopes
kotoba	W04	S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes
kotoba	W04	S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S054 duplicate url learn.chatgpt.com/docs/build-skills across scopes
kotoba	W04	S055 duplicate url code.visualstudio.com/docs/agent-customization/agent-skills across scopes
kotoba	W04	S056 duplicate url docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference across scopes
kotoba	W04	S065 duplicate url code.claude.com/docs/en/skills.md across scopes
kotoba	W04	S086 duplicate url developers.openai.com/plugins/build/plugins.md across scopes
kotoba	W04	S103 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	W04	S104 duplicate url learn.chatgpt.com/docs/agent-configuration/agents-md.md across scopes
kotoba	W04	S106 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S110 duplicate url code.claude.com/docs/en/hooks.md across scopes
kotoba	W04	S111 duplicate url learn.chatgpt.com/docs/hooks.md across scopes
kotoba	W04	S114 duplicate url docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md across scopes
kotoba	W04	S115 duplicate url cursor.com/docs/rules across scopes
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
```

This is a template, not an observed lane receipt. W04 is expected and non-failing; refresh all stdout at the actual after run in case integrated rows change the warning set.

## Files, risks, and blockers

- Repository file written: `.ufo/waves/round-62/w1/ExecCensus62.md` only. No lane/fleet/source ledger write or git/jj mutation.
- Risk/hand-off: the probe's `queued | —` is census-safe but must be reconciled with the actual S118 source/lesson citations during integration. Preserve the exact `re-opens S103 —` prefix and expected W04; do not misreport W04 as an E04 failure.
- Blockers: none.
- Installs: no installs.
- Produced: an exact scratch-only S118 census probe, measured validator/manual census evidence, and the `.ufo/waves/round-62/census-after.txt` command/receipt template.
