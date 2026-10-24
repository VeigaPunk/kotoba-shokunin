# Round-64 wave-2 — fresh round-end SOURCES census

Seat: `kotoba-r64.ScoutW2CensusAfter-2`  
Scope: working-tree census only; primary axis **freshness**, with complete command evidence and no production mutation.

## Findings

**Observed: all eight requested commands exited 0.** The maintained validator emitted **zero E-class errors**, **16 W04 warnings**, and the lane `ok` line. The seven frozen manual commands returned 118 rows, zero malformed rows, `A=115 B=2 C=1`, `mined=110 queued=7 rejected=1`, and no duplicate IDs, enum/tier-inflation violations, or missing mined used-by paths. **No CRITICAL census finding observed.** This is the census gate result, not admission of either round claim.

Run interval: **2026-10-24T04:20:12.178387+00:00–2026-10-24T04:20:12.464156+00:00**. Every command ran from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; stdout and stderr were captured separately; all eight stderr streams were empty. Independent commands were launched concurrently against the live working tree, not a copied table.

## Runbook result table

| Requested command / expectation | Actual stdout result | Exit | Observation |
|---|---|---:|---|
| Maintained `sources-census.sh validate` / no E errors | 16 existing W04 lines, then `kotoba` / `ok` / registry path | 0 | Zero E-class lines |
| Rows / 118 | `118` | 0 | Matches |
| Malformed / 0 | `0` | 0 | Matches |
| Tier histogram / new A-tier paper included | `A=115 B=2 C=1 ` | 0 | Matches |
| Status histogram / mined 110+ | `mined=110 queued=7 rejected=1 ` | 0 | Matches |
| Duplicate IDs / empty | Empty | 0 | Matches |
| Enum violations and tier inflation / empty | Empty | 0 | Matches |
| Missing mined used-by paths / empty | Empty | 0 | Matches |

Commands are the seven invocations frozen in `/home/vgpnk/Projects/shokunin/CORPUS.md:131-147`, also carried by canonical `skills/shokunin/protocol/CORPUS.md`. The maintained CLI's documented E01–E12 and warning semantics are at `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh:16-33`.

### S120 and before→after

`corpus/SOURCES.md:132` contains **S120**, *Practical Mutation Testing at Scale: A view from Google*, URL `https://arxiv.org/html/2102.11378`, **kind `paper`, tier `A`, status `mined`, opened `2026-10-24`, recheck `180d`**. Its two used-by paths are `corpus/knowledge/g7-span-pinning-round64.md` and `corpus/lessons/round-64.md`. The frozen missing-path command emitted nothing across all mined rows.

Wave-1 baseline `.ufo/waves/round-64/w1/ExecCensusAfter.md:29-37` recorded 117 rows, `A=114 B=2 C=1`, and `mined=109 queued=7 rejected=1`. This fresh run records **117→118 rows, A 114→115, mined 109→110**, with B/C/queued/rejected unchanged. The validator's 16 W04 source IDs match that report's baseline listing (`:42-60`); they are cross-scope URL reuse warnings, not duplicate source IDs or E04 URL+scope errors.

## Freshness and working-tree state

Observed HEAD was **`b99fb79c27042e0f8a598cbbb4d81479a806b518`**, not the earlier measured-data commit `c019919c97ab5fe98e87a7754b4449ea4e699c99`. The actual working-tree registry and `c019919c` registry have the same SHA-256. Thus this census uses fresh working-tree reads while also binding its registry bytes to the measured tip.

At the recorded status snapshot, **SCORECARD.md and SHONEN.md were not uncommitted changes**; HEAD's subject names their round-64 updates. The observed tracked modification was `.ufo/waves/round-64/receipts/noharm-tip.txt`, and `.ufo/waves/round-64/w2/` was untracked. These changes were not altered by this seat.

Pre-run input hashes at `2026-10-24T04:19:58+00:00` and post-run hashes at `2026-10-24T04:20:27.502113+00:00` were identical:

| Input | SHA-256 before = after |
|---|---|
| `corpus/SOURCES.md` | `975cbce9d2f23291b34389db1419c7b2698825c5dddc8921063e6202824fc847` |
| Fleet `CORPUS.md` | `88556402940e7a0f1dbbed3abef9e00c87a90db6f80eaed03269e371f50050b8` |
| Fleet `scripts/sources-census.sh` | `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30` |

### Freshness command evidence

#### Measured input hash

Started `2026-10-24T04:20:27.500280+00:00`; finished `2026-10-24T04:20:27.502566+00:00`.

```text
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/SOURCES.md | sha256sum
975cbce9d2f23291b34389db1419c7b2698825c5dddc8921063e6202824fc847  -
exit=0
```

#### Post-run census input hashes

Started `2026-10-24T04:20:27.500476+00:00`; finished `2026-10-24T04:20:27.502113+00:00`.

```text
$ sha256sum corpus/SOURCES.md /home/vgpnk/Projects/shokunin/CORPUS.md /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
975cbce9d2f23291b34389db1419c7b2698825c5dddc8921063e6202824fc847  corpus/SOURCES.md
88556402940e7a0f1dbbed3abef9e00c87a90db6f80eaed03269e371f50050b8  /home/vgpnk/Projects/shokunin/CORPUS.md
3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30  /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
exit=0
```

#### Working tree measured at census

Started `2026-10-24T04:20:27.500619+00:00`; finished `2026-10-24T04:20:27.523380+00:00`.

```text
$ git log -1 --format='%H%n%s%n%cI' && git status --short
b99fb79c27042e0f8a598cbbb4d81479a806b518
round-64: measurements — C1/C2 receipts at c019919c, SCORECARD round-64 annotations + Next-65, SHONEN refresh, README corpus-index rows, w2 spec/dispatch
2026-10-24T01:18:01-03:00
 M .ufo/waves/round-64/receipts/noharm-tip.txt
?? .ufo/waves/round-64/w2/
exit=0
```

## Requested command transcripts — exact commands and actual output

### 1. Maintained validate

Started `2026-10-24T04:20:12.178387+00:00`; finished `2026-10-24T04:20:12.464156+00:00`.

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

### 2. Rows

Started `2026-10-24T04:20:12.178692+00:00`; finished `2026-10-24T04:20:12.180533+00:00`.

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
118
exit=0
```

### 3. Malformed rows

Started `2026-10-24T04:20:12.178894+00:00`; finished `2026-10-24T04:20:12.182121+00:00`.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0
exit=0
```

### 4. Tier histogram

Started `2026-10-24T04:20:12.179022+00:00`; finished `2026-10-24T04:20:12.181493+00:00`.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
A=115 B=2 C=1 
exit=0
```

### 5. Status histogram

Started `2026-10-24T04:20:12.179150+00:00`; finished `2026-10-24T04:20:12.182476+00:00`.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
mined=110 queued=7 rejected=1 
exit=0
```

### 6. Duplicate IDs

Started `2026-10-24T04:20:12.179268+00:00`; finished `2026-10-24T04:20:12.181857+00:00`.

Stdout was empty.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
exit=0
```

### 7. Enum violations and tier inflation

Started `2026-10-24T04:20:12.179361+00:00`; finished `2026-10-24T04:20:12.183293+00:00`.

Stdout was empty.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md
exit=0
```

### 8. Missing mined used-by paths

Started `2026-10-24T04:20:12.179750+00:00`; finished `2026-10-24T04:20:12.184908+00:00`.

Stdout was empty.

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; gsub(/[[:space:]]/,"",s); if (s=="mined") {n=split($12, a, /[,;]/); for (j=1;j<=n;j++) {p=a[j]; gsub(/^[[:space:]]+|[[:space:]]+$/,"",p); if (p!="" && p!="—") print p}}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
exit=0
```

## Confidence, bounds, and remaining unknowns

- **High confidence in this observed census:** actual commands and exits are retained; registry/contract/script hashes were stable across the run; the registry hash equals `c019919c`.
- No inference is needed for the reported row counts or exit statuses. The S120 projection is a literal registry read, not independent verification of the paper's truth or tier appropriateness.
- This seat did not test C1/C2 predicates, receipt semantics, no-harm verifiers, source quotes, or whether used-by files substantively cite every row. Census checks establish structure/enums and existing named paths, not those semantic properties. No exported-code contract is inferred from text searches; no definition/reference tracing was needed for this command-execution assignment.
- No needed census artifact was absent and no requested command was blocked. The frozen manual path check skips blank/`—` cells; the maintained validator emitted no W03 warning in this run. Subsequent registry or used-by-path edits would require a new census; this report does not certify future tree states.
- Tooling prerequisite note: `read /home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` returned “not found”; a targeted `/home/vgpnk/Projects/shokunin/.omp/**/RULES.md` glob found no match. No tool installation or update was needed or attempted, so this missing installation-rules file did not block the census. **Installs/updates: none.** No pacman transaction, service action, Git/JJ write, production-file edit, or subagent dispatch was performed. This report is the seat's only written file.
