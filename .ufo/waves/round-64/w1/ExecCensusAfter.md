# Round-64 sources census runbook — round-start record

Scope: read-only census of `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md`; this report is the only file written. No tools were installed or updated.

## Round-end command sequence

Run the following from the lane root. The first command is the maintained round-end gate; then run the frozen commands from `CORPUS.md` § “SOURCES.md — where a shokunin learns” verbatim:

```sh
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin

bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba

grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

Note: the frozen block contains **seven separate shell invocations** (rows, malformed, tier, status, duplicates, enum/tier inflation, mined used-by paths), although the request calls them six. I retained and ran every invocation in the contract so all seven requested result categories are covered.

## Round-start manual census — run now

Commands were run from the lane root against the current tree. Each command exited 0.

| Frozen command/result | stdout | exit |
|---|---:|---:|
| rows (`grep -cE ...`) | `117` | 0 |
| malformed rows (`awk ... NF!=13`) | `0` | 0 |
| tier histogram | `A=114 B=2 C=1 ` | 0 |
| status histogram | `mined=109 queued=7 rejected=1 ` | 0 |
| duplicate IDs | *(empty)* | 0 |
| enum violations and tier inflation | *(empty)* | 0 |
| mined used-by paths missing on disk | *(empty)* | 0 |

Maintained gate also run:

```text
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
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

The W04 warnings are present at round start; the script's header states warnings do not affect the clean-lane exit status. The current registry has no S120 row yet (exact search `^\|[[:space:]]*S120[[:space:]]*\|` returned no matches), as expected before opening this round's new source.

## Round-end exit-0 checklist for S120

- [ ] S120 is a registry table row with 11 data columns (`NF=13` when split on `|`); do not put `|` inside a cell.
- [ ] `kind` is one of `spec`, `docs`, `paper`, `code`, `tool`, `dataset`, `talk`, `book`, `community`, `own-work`.
- [ ] `tier` is `A`, `B`, or `C`; `community` must not be tier `A`.
- [ ] `status` is `queued`, `mined`, or `rejected`.
- [ ] If `status=mined`, `used-by` names at least one comma-separated repo-relative citing path, is not blank/`—`, and every named path exists. (For a row not mined, `—` is allowed.)
- [ ] Run the maintained `validate` gate and retain its actual exit code. Exit 0 may still include warnings such as the current W04s; inspect the manual census outputs as well.

## Evidence and bounds

- Read the frozen plan `plans/round-64.md` (claim framing and S120 intent), `CORPUS.md` § “SOURCES.md — where a shokunin learns” (contract, frozen command block, CLI note), and `.ufo/waves/round-64/census-before.txt` (prior W04 listing).
- Current results support only the round-start SOURCES registry census/runbook; they do not test or support C1's 223-assertion predicate or C2's routed-repairs counter. No build, test, lint, or formatter was run.
- No implementation blocker. Round-end S120 status remains dependent on the source/row being opened and written later in the round.
