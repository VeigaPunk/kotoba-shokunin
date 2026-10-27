# Kb79R01SpecRow — C2 source row, surface `spec` (Open specification), registry id S226

Round 79 · wave w1 · lane `kotoba-shokunin` · base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`, plan commit F1 `2c56622375641193a03bb97c0624e6536f3dffba`.
Claim boundary: I produced DRAFTS only — one `corpus/SOURCES.md` registry row, one entry table row, and their proofs. I scored nothing on `verifiers/check_allowed_tools.py` (it does not exist in w1; the L1 freezes it after this wave), wrote no lane file outside `.ufo/waves/round-79/`, and ran no control world.

## Behaviour

1. Opened the URL myself: `curl -sSL -A 'Mozilla/5.0' --max-time 60 https://agentskills.io/specification.md`, twice, 21:41:23Z and 21:41:24Z. Both: HTTP 200, no redirect, 7608 B, `text/markdown; charset=utf-8`, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`; `cmp` rc=0 → the page did not change between fetches. Raw bytes installed as the snapshot `S226-spec.md`.
2. Located the field in both places the page states it: the frontmatter overview table row (L35) and the `#### allowed-tools field` section (L172; opening sentence L174, two bullets L176-177, example L182). The section sentence carrying `Experimental` is L177, and it is what the quote's tail uses.
3. Established the revision: the page publishes none (no version, commit or date in the body; no ETag; `last-modified` = request instant, so it marks the fetch). Substituted the upstream file: `agentskills/agentskills` head `69ef37e9424c0a7ea9dd2293b559e43ec8176379` (`git ls-remote refs/heads/main`, 2026-10-27), path `docs/specification.mdx` last touched by `217be548739f21d6008915c29aefe320ea1a90af` (2026-08-04, GitHub commits API), and the raw mdx at that commit is byte-identical to head (sha256 `b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220`, 7166 B, both fetches HTTP 200).
4. After the L1 ruling (2026-10-27, received during this seat), stated the quote in a **declared text view** of the snapshot — delete backtick bytes, delete a leading list marker at line start, collapse whitespace — and verified it there: 15 whitespace tokens, occurrence count 1 in `S226-spec.md` (index 4267), 0 in the raw bytes (the raw span carries backticks and two `* ` markers, 17 tokens at collapsed index 4464). Q70 re-run in the same text view against one other surface's page: 0. The L1's message gave 13 words for that string; the string is 15 whitespace tokens (`len(q.split())` = 15) and I reported the discrepancy rather than confirm the count.

## Gates run (command → observed)

All commands run in my scratch dir `/fast/scratch/hyaku/kotoba-r79/Kb79R01SpecRow` (removed before yield) or against the committed wave paths. The `rc` column is the command's own exit status where I captured it explicitly; where the row shows a printed value the command exited as printed (the two `grep -c` rows return 1 on zero matches, as recorded).

| command | observed | rc |
|---|---|---|
| `curl -sSL -A 'Mozilla/5.0' --max-time 60 -o fetch1.body -w '%{http_code}\t%{size_download}\t%{url_effective}\t%{content_type}\n' https://agentskills.io/specification.md` | `200  7608  https://agentskills.io/specification.md  text/markdown; charset=utf-8` | 0 |
| same into `fetch2.body` | `200  7608  …` (same) | 0 |
| `sha256sum fetch1.body fetch2.body` | both `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` | 0 |
| `cmp fetch1.body fetch2.body` | no output | 0 |
| `grep -n -F 'The optional `allowed-tools` field:' fetch1.body` | `174:The optional `allowed-tools` field:` | 0 |
| `grep -n -F '* A space-separated string of tools that are pre-approved to run' fetch1.body` | `176:* A space-separated string of tools that are pre-approved to run` | 0 |
| `grep -n -F '* Experimental. Support for this field may vary between agent implementations' fetch1.body` | `177:* Experimental. Support for this field may vary between agent implementations` | 0 |
| python `re.sub(r'\s+',' ',page)` then `quote in collapsed`, on the raw inline span (superseded by the L1-ruled text-view form) | `True`, collapsed index 4464, 17 tokens, no `|` | 0 |
| python ASCII word-bounded counts in `snapshots/S226-spec.md` | `allowed-tools` 4, `space-separated` 1, `pre-approved` 2, `Experimental` 2 | 0 |
| python `textview(p)` = drop backticks, drop leading list markers `(?m)^[ \t]{0,3}[*+\-][ \t]+`, collapse `\s+`, strip | spec `S226-spec.md`: `quote_count 1`, index 4267, `quote_word_tokens 15`; claude control `Kb79R01SpecRow.q70-claude.md`: `quote_count 0`, index -1 | 0 |
| `sha256sum snapshots/S226-spec.md` + `wc -c` | `9a67de89…` · 7608 | 0 |
| `awk -F'\|' '/^\| S226 /{print NF}' build/Kb79R01SpecRow.rows.md` | `13` (= 11 cells) | 0 |
| `awk -F'\|' '/^\| Open specification /{print NF}' build/Kb79R01SpecRow.rows.md` | `7` (= 5 cells) | 0 |
| `curl -sSL -A 'Mozilla/5.0' --max-time 60 -o claude.body -w 'claude HTTP %{http_code} %{size_download} %{url_effective}\n' https://code.claude.com/docs/en/skills.md` | `claude HTTP 200 117962 https://code.claude.com/docs/en/skills.md`, sha256 `31623035b25ac7e6bebd8dec6234aa76e31018f0e2eb8b47da6b36cf015712f9` | 0 |
| `grep -c -F '<the quote>' Kb79R01SpecRow.q70-claude.md` | `0` | 1 (no match — expected) |
| `grep -c -F 'pre-approved to run' Kb79R01SpecRow.q70-claude.md` | `0` | 1 (expected) |
| `python3 -c "import json;print(sorted(json.load(open('snapshots/S226.fetch.json')).keys()))"` | `['bytes', 'fetched_utc', 'final_url', 'http', 'id', 'note', 'sha256', 'ua', 'url']` | 0 |
| `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` | `/tmp 5%`, `/var/tmp 35%`, `/fast/scratch/hyaku 28%` (free 585.3G) | 0 |
| `git ls-remote https://github.com/agentskills/agentskills refs/heads/main` | `69ef37e9424c0a7ea9dd2293b559e43ec8176379 refs/heads/main` | 0 |
| GitHub commits API `?path=docs/specification.mdx&per_page=3` | last touching commit `217be548739f21d6008915c29aefe320ea1a90af` (2026-08-04T22:52:17Z) | 0 |
| raw mdx at `217be548…` and at `69ef37e9…` | both HTTP 200, 7166 B, same sha256 `b9079c0c…` (`cmp` rc=0) | 0 |

Full proof text (Q53 excerpts, Q70 block, reading, injection note) is inside the rows artifact below.

## Findings

1. **The plan's (d)+(f) pair could not be met by a raw single-line quote, and the L1 resolved it by declaring a text view (2026-10-27).** (d) needs the quote to occur in the snapshot and contain `allowed-tools`; (f) needs it to carry `Experimental`. On this page the only raw line containing both is the frontmatter table row (L35), whose `|` delimiters cannot live inside the 5-cell entry (a naive `split('|')` sees 7 cells); the only pipe-free contiguous span carrying both is L174 + L176-177 and includes the two `* ` markers and the backticks (17 tokens raw). The L1 ruled the located quote is the **declared text-view** form — delete backtick bytes, delete a leading list marker at line start (`(?m)^[ \t]{0,3}[*+\-][ \t]+`), collapse whitespace — giving "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." at 15 whitespace tokens, occurrence 1 in `S226-spec.md` (index 4267), 0 raw. Both draft rows now carry that form; the L1 is correcting plan/counter to it. Form-level, no data scored.
2. **Token hazard:** the literal example value `Bash(git:*)` cannot be matched by a `\b…\b` word-boundary regex (it ends in `)`), so I used the page's own value-form word `space-separated` as the value token. If the frozen counter insists on the literal example value, `Read` (1 occurrence, L182) is the only `\b`-safe literal on the page.
3. **Served `.md` ≠ upstream mdx bytes.** The site build rewrites `- ` bullets as `* `, wraps example blocks and `<Card>` blocks as blockquotes, and adds `theme={null}` to fences; content is otherwise identical. The snapshot correctly holds the served bytes, because the C2 pin is over the fetched URL — but a reviewer comparing against the mdx will see marker differences, so the anchor cell names both.
4. **The page states no revision.** No version/commit/date in the body, no ETag, and `last-modified` equals the request instant (Vercel, `must-revalidate`) — a fetch timestamp, not a content revision. I did not treat it as one.
5. **Q70 is one-page evidence, not a sweep.** The quote (and the fragment `pre-approved to run`) is 0 on the Claude Code page. That is one of the five non-own pages; I claim nothing about factory / msaf / pi / vibe bytes. The full sweep belongs to the falsify wave.
6. **Prompt-injection text present and not followed.** The page opens with `> ## Documentation Index` / `> Fetch the complete documentation index at: https://agentskills.io/llms.txt` / `> Use this file to discover all available pages before exploring further.` — an imperative addressed to the reader. I fetched no `llms.txt` and crawled nothing else. Remaining imperatives in the page ("Keep your main `SKILL.md` under 500 lines", "Use the skills-ref reference library") are the document's subject matter, not injections.
7. **Prior coverage overlaps, and I did not re-claim it.** `corpus/knowledge/frontmatter-rule-authorities-round48.md:104` already records the space-separated-string claim with `spec.md:35, :176` and a r48 validator observation (a YAML list passes both validators). My row adds the field's own semantics + the Experimental label, scoped to the format; the per-client axis is the entry's job, not the row's.
8. **Tier A is justified and scoped:** the page is the format maintainers' own specification, so tier A for "what the format says the field is"; it names no client and claims no enforcement, so A says nothing about any implementation.
9. **Independent cross-check (peer, not my measurement repeated):** `Kb79A02EntrySkeleton` re-measured the same declared text view on the committed snapshot and reported the 15-token string at count 1, index 4267, 15 words, 0 pipes, containing `allowed-tools` and `Experimental`, and the same conclusion that `space-separated` is the only word-bounded value-form token (IRC, 2026-10-27). That is a second derivation of the same numbers; it is not a counter run and scores nothing.

## Touched surfaces (files written)

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226-spec.md` — served bytes, 7608 B.
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226.manifest` — `9a67de89…  S226-spec.md`.
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226.fetch.json` — id/url/final_url/http/bytes/sha256/fetched_utc/ua/note.
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R01SpecRow.rows.md` — registry row, entry row, Q53 proof, Q70 proof, reading, injection note (sections 1-6).
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R01SpecRow.q70-claude.md` — the exact Claude Code bytes I grepped (117962 B, sha256 `31623035…`), so the 0 can be re-run without a network.
- This report.

No lane file outside `.ufo/waves/round-79/` was created, modified or deleted. `corpus/SOURCES.md`, `corpus/knowledge/allowed-tools-surfaces-round79.md`, `MANIFEST.sha256` and the lane git/jj state are untouched (the L1 stitches and the owner of the wave manifest assembles it).

## Out of scope (deliberately not done)

- No run of `verifiers/check_allowed_tools.py` and no control world — the counter is not built/frozen in w1, and the brief forbids scoring claim data on it before the L1 freeze.
- No entry file written (frozen path `corpus/knowledge/allowed-tools-surfaces-round79.md` belongs to the L1's integration), no SOURCES.md edit, no SKILL.md/PROVINCE.md edit.
- No Q70 sweep of the other four surfaces (only `claude` sampled, as the item asked).
- No `--work` dir, no clone, no full Q35 census: nothing in this item needed a working tree.

## Tooling

None installed or upgraded (no package manager invoked; `pacman` untouched). Scratch: `/fast/scratch/hyaku/kotoba-r79/Kb79R01SpecRow` with `TMPDIR` set inside it, removed before yield; no `--work` dir was created.

VERDICT: S226 `spec` row drafted and grounded — 7608 B served snapshot pinned twice byte-identically (sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16); quote is the L1-ruled text-view form "The optional allowed-tools field: A space-separated string of tools that are pre-approved to run Experimental." (15 whitespace tokens, 1 occurrence in the declared text view at index 4267, 0 raw; built from raw L174 + L176-177 with backtick and list-marker removal declared), grant label `experimental` judged TRUE of the page (L35, L177), Q70 = 0 on the claude page in the same text view, value-form token `space-separated`; `Bash(git:*)` never used with word-boundary matching.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226-spec.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S226.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R01SpecRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R01SpecRow.q70-claude.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79R01SpecRow.md
