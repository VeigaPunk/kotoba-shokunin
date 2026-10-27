# Kb79R02ClaudeRow — S227 `claude` (Claude Code) — round 79 w1

Seat: leaf, no subagents, no background jobs, no tool installs (nothing was needed; no pacman, no package manager ran).
Scope: open https://code.claude.com/docs/en/skills.md myself, snapshot it, locate the `allowed-tools` frontmatter row and the `Pre-approve tools for a skill` section, record the `allowManagedPermissionRulesOnly` caveat as a Limit, and draft the S227 registry row plus the entry-table row for `corpus/knowledge/allowed-tools-surfaces-round79.md`. L1 stitches; I did not touch `corpus/SOURCES.md` or the entry, and I did not run or score the C2 counter (it does not exist in the lane yet).

**Pre-data amendment taken (L1, IRC, before any data was scored):** frozen grant-grounding token for claude is `without prompting you for approval` (not `without asking permission`), and the entry quote must be a pipe-free prose quote. Both rows now use it; the entry row is 5 cells. The superseded draft (a table-row quote at L404 under the old token) remains visible in `build/Kb79R02ClaudeRow.facts.txt` and is described under Findings 1.

## What I did (commands, own exit status)

```
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
S=/fast/scratch/hyaku/kotoba-r79/Kb79R02ClaudeRow   # TMPDIR=$S/tmp

curl -sSL -A 'Mozilla/5.0' --max-time 60 -o f1.bin -w 'http=%{http_code} bytes=%{size_download} final=%{url_effective}\n' \
  https://code.claude.com/docs/en/skills.md            # rc=0  http=200 bytes=117962 final=same  2026-10-27T21:41:02Z
curl ... (same) -o f2.bin                              # rc=0  http=200 bytes=117962 final=same  2026-10-27T21:41:04Z
sha256sum f1.bin f2.bin
# 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9  f1.bin
# 31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9  f2.bin
```

Both fetches identical (the page did not change between them). The URL serves the **plain markdown llms.txt-style export**, not an HTML shell: line 1 is `> ## Documentation Index`, line 5 `# Extend Claude with skills`; 0 NUL bytes; no tags to strip and no entities to decode on the quoted line. Snapshot is therefore `.md`.

```
curl -sSL -A 'Mozilla/5.0' --max-time 60 -o spec.bin -w ... https://agentskills.io/specification.md
  # rc=0 http=200 bytes=7608 sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16   (Q70 cross-page)
# re-check of the amended quote runs against the lane snapshots (both untracked drafts, same bytes):
$ grep -c -F '<amended quote>' .ufo/waves/round-79/snapshots/S226-spec.md   # 0, rc=1 (zero matches — the count is the datum)
$ grep -c -F '<amended quote>' .ufo/waves/round-79/snapshots/S227-claude.md # 1, rc=0
```

Located material, with line numbers in the snapshot (`sed -n '<L>p'`; receipts `build/Kb79R02ClaudeRow.facts.txt`, `build/Kb79R02ClaudeRow.quote-amended.txt`):

- **L404** — frontmatter-reference row for `allowed-tools`: "Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message. Accepts a space- or comma-separated string, or a YAML list."
- **L615** `### Pre-approve tools for a skill`; **L617** "The `allowed-tools` field grants permission for the listed tools during the turn that invokes the skill, so Claude can use them without prompting you for approval … It does not restrict which tools are available: every tool remains callable".
- **L619** workspace trust does not gate the field; a checked-in skill can grant itself broad tool access.
- **L636** `#### When managed settings lock hooks to plugins` — a skill declaring `hooks` under `strictPluginOnlyCustomization` loses its `allowed-tools` pre-approval.
- **L643** `#### When only managed permission rules apply` — `allowManagedPermissionRulesOnly` makes Claude Code "ignore `allowed-tools` in project and personal skills"; "requires Claude Code v2.1.282 or later". **This is the Limits note, not the quote.**
- **L789** an unmatched injected command can be pre-approved with `allowed-tools`; **L861** the grant restated in "Restrict Claude's skill access".

Revision: **the page states none for itself** (no last-modified, no commit in 117 962 B). The only version marker near the field is v2.1.282 at L643. Identity rests on the fetch sha256; the registry anchor cell says exactly that.

## Gates / evidence produced

| item | result |
|---|---|
| HTTP status / size / sha256, twice | 200 / 117 962 B / `31623035…712f9`, identical across 2 s |
| snapshot saved as raw fetched bytes | `.ufo/waves/round-79/snapshots/S227-claude.md` (117 962 B, sha matches) |
| `S227.manifest` | one line `31623035…712f9␠␠S227-claude.md` (sha256sum format) |
| `S227.fetch.json` | keys `id,url,final_url,http,bytes,sha256,fetched_utc,ua,note`; parsed back OK |
| registry row shape | `awk -F'\|'` → **NF=13** (11 cells), no `\|` inside any cell; enums `kind=docs tier=B status=mined`; id matches `^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|` |
| entry row shape | `awk -F'\|'` → **NF=7** (5 cells), frozen header cells `surface source page tokens grant located quote`; grant cell plain `pre-approves` |
| amended entry quote | 25 words, `raw_count 1`, collapsed 1, offset 68 988, paged `sed -n '617p'` pasted; contains `allowed-tools` and the ground token |
| registry quote | 16 words, offset 68 984, raw 1 / collapsed 1, substring of the same line |
| page tokens word-bounded in the snapshot | `allowed-tools` 21 · `space- or comma-separated string` 2 · `YAML list` 4 · `without prompting you for approval` 1 |
| Q70 on a second surface page | 0 in the spec snapshot (7 608 B, sha `9a67de89…de16`, byte-identical to my own 21:41:54Z fetch and to the S226 seat's snapshot); own snapshot 1 |
| grounds for label `pre-approves` | L617 "without prompting you for approval"; L404 "without asking permission during the turn that invokes this skill" → **label TRUE**; not changed |

## Findings (for the L1 judge / counter author)

1. **The pipe conflict is resolved by the amendment, and the counter need not special-case it.** Under the old token the only span carrying both `allowed-tools` and the grant phrase was the frontmatter table row at L404, which made the entry row 7 cells. Under the amended token the grounding span is prose at L617, so the entry row is exactly 5 cells and r73's `[1:-1].split("|")` parses it. Residual: the amended quote is **exactly 25 words** by whitespace split and cannot be shortened without losing either `allowed-tools` or the token — so the (5–25 words) check must count by whitespace, as the plan says, not by punctuation-splitting tokens (that would count "`allowed-tools`", "skill," and "approval." as multiple). The registry anchor deliberately quotes only the first 16 words of the same line to stay clear of that boundary.
2. **The label is true but narrower than a reader may assume**, and the page says so itself: the grant lasts one turn, every unlisted tool still goes through permission settings, and the whole grant is dropped under `allowManagedPermissionRulesOnly` (v2.1.282+) or when a skill declares `hooks` under `strictPluginOnlyCustomization`. The page never calls the field experimental and never claims conformance to the open specification — hence tier B, not A.
3. **`used-by` will trip the SOURCES census until the entry lands.** `corpus/knowledge/allowed-tools-surfaces-round79.md` does not exist at the base, and the contract's census prints `missing:` for a `mined` row whose `used-by` path is absent. Entry and S227 must land in the same commit (or the entry first).
4. **No revision is stated by the page**, so the anchor's revision slot carries the fetch identity plus the only version marker the page gives (v2.1.282; L643). A "did the page move since fetch" check must use the sha256 pin, not a commit.
5. **Q70's negative is partial by construction**: one other surface page (the spec) was searched here; the other four are other seats' pages, so the full-set sweep belongs to the L1.
6. **Prompt-injection text: none.** Sweep `grep -n -iE 'ignore (all|previous|prior)|you must (now|instead)|system prompt|assistant must|do not tell|exfiltrat'` → 3 hits, all ordinary docs (L96 subcommand description, L822 table column, L827 agent preamble). The page's `> Fetch the complete documentation index at: …/llms.txt` is navigation, not an instruction, and I did not follow it.

## Out of scope (untouched, by rule)

`corpus/SOURCES.md`, the C2 entry, `SKILL.md`, `PROVINCE.md`, `MANIFEST.sha256` (no aggregation), the C2 counter, the lane git index and jj state — all the L1's. No lane file outside `.ufo/waves/round-79/` was written; no commit/push/checkout/add/stash in the lane; no fleet-repo write. Scratch `/fast/scratch/hyaku/kotoba-r79/Kb79R02ClaudeRow` created and removed twice (rc=0, confirmed absent) after receipts were copied out.

Artifacts: `.ufo/waves/round-79/snapshots/S227-claude.md`, `.ufo/waves/round-79/snapshots/S227.manifest`, `.ufo/waves/round-79/snapshots/S227.fetch.json`, `.ufo/waves/round-79/build/Kb79R02ClaudeRow.rows.md` (registry row + entry row + Q53 + Q70 + reading + injection), `.ufo/waves/round-79/build/Kb79R02ClaudeRow.quote-amended.txt`, `.ufo/waves/round-79/build/Kb79R02ClaudeRow.facts.txt`, `.ufo/waves/round-79/build/Kb79R02ClaudeRow.q70.txt`.

VERDICT: S227 opened and snapshotted twice with identical sha256; `pre-approves` is TRUE of this page (L617 under the amended token, L404 as reinforcement) with managed-settings and hooks caveats as Limits; registry row 11 cells clean and the entry row 5 cells with a 25-word pipe-free prose quote that occurs once in its own snapshot and zero times in the spec page — residual is that the quote sits exactly on the 25-word ceiling, so the counter must count words by whitespace.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R02ClaudeRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R02ClaudeRow.quote-amended.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R02ClaudeRow.facts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R02ClaudeRow.q70.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S227-claude.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S227.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S227.fetch.json
