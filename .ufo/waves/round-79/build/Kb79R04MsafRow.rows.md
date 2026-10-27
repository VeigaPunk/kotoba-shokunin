# Kb79R04MsafRow — C2 source row S229, surface `msaf` (Microsoft Agent Framework)

Surface key: `msaf`. Registry id: `S229`. Entry: `corpus/knowledge/allowed-tools-surfaces-round79.md` (not written by this seat; the L1 stitches).
Snapshot: `.ufo/waves/round-79/snapshots/S229-msaf.html` (raw HTML, 157 339 B, sha256 `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2`).
Fetch: `curl -sSL -A 'Mozilla/5.0' --max-time 60 https://learn.microsoft.com/en-us/agent-framework/agents/skills`, HTTP 200, final URL == requested URL, 157 339 B, `2026-10-27T21:41:02Z`; fetched twice, `cmp` rc=0 (identical sha256 both times — the page did not move between fetches).
Page-stated revision: `ms.date` `2026-10-23T00:00:00Z` (rendered "Last updated on 2026-10-23", `datetime="2026-10-23T08:00:00.000Z"`), `git_commit_id` `d34f426053dba6703197776e7aad4d30fd4d06f5`, `original_content_git_url` `https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/agent-framework/agents/skills.md`.

---

## (1) Registry row for `corpus/SOURCES.md` — 11 cells, no `|` inside any cell

| S229 | Microsoft Learn — Agent Framework: Agent Skills — https://learn.microsoft.com/en-us/agent-framework/agents/skills | docs | B | Microsoft Agent Framework's own statement of the `allowed-tools` frontmatter field: the Required column, the one-sentence description, and the grant wording a skill author on this client reads (tier B: one vendor's framework documentation, not the open specification — the table restates the spec's field in the vendor's own words, so it is this client's reading and not the spec's text; scoped to this page alone, with no claim about runtime enforcement) | § SKILL.md format (h3 id=skillmd-format), frontmatter field table, `allowed-tools` row (snapshot L818-820); page revision `ms.date` 2026-10-23 (rendered 2026-10-23) and `git_commit_id` d34f426053dba6703197776e7aad4d30fd4d06f5 (azure-ai-docs-pr, live, agent-framework/agents/skills.md); located quote "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." (19 words); fetched 2026-10-27T21:41:02Z, HTTP 200, 157339 B, sha256 34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2 | On this client `allowed-tools` is an optional frontmatter field described as a space-delimited list of pre-approved tools and flagged Experimental with support varying between agent implementations, so a skill author who relies on it for portability gets a grant hint, not a guaranteed restriction | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-surfaces-round79.md |

Cell-by-cell: `id` S229 · `source` title — canonical URL · `kind` docs · `tier` B (state why: vendor docs, one client's page, not the spec) · `scope` above · `anchor` above (section, revision, located quote, fetch record) · `teaches` one learner benefit · `status` mined · `opened` 2026-10-27 · `recheck` 90d · `used-by` the entry. No cell contains a `|`.

Note for the stitch: the anchor cell says "located quote" rather than the bare `quote` used by S217–S225. Both are readable by a `quote\s+"…"` matcher; keep "located quote" if the frozen counter's regex is the one used by `check_cn_vendor_surfaces.py` (`located quote\s+["“]([^"”]+)["”]`), otherwise drop the word "located".

## (2) Entry table row (frozen header `| surface | source | page tokens | grant | located quote |`)

| Microsoft Agent Framework | S229 | `allowed-tools` `Space-delimited` `pre-approved` `Experimental` | experimental | located quote "allowed-tools No Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." |

- Page tokens (4, all ASCII-word-bounded in the snapshot's TEXT_VIEW, each `grep`-verified below): `allowed-tools` (the field key) · `Space-delimited` (the value form the page prints — it prints no example value anywhere on the page; the only `allowed-tools` occurrence is the table row) · `pre-approved` (the grant word inside the description) · `Experimental` (the grant-semantics token that grounds the `experimental` label).
- Grant cell: plain text `experimental`, not backticked, exactly the frozen label for `msaf` in the round-79 plan (f).
- The quote cell repeats the same string the registry anchor carries, so `quote_for`-style "exactly one distinct located quote for this id" holds; no other quoted string sits on the row.

## (3) Q53 proof — the source lines and exactly what shaping produced the quote

Full command output is in `build/Kb79R04MsafRow.q53.txt`. Verbatim:

```
$ grep -n -F allowed-tools .../snapshots/S229-msaf.html
818:<td><code>allowed-tools</code></td>
rc=0

$ grep -n -F "Space-delimited list of pre-approved tools" .../snapshots/S229-msaf.html
820:<td>Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations.</td>
rc=0

$ sed -n 816,820p .../snapshots/S229-msaf.html
</tr>
<tr>
<td><code>allowed-tools</code></td>
<td>No</td>
<td>Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations.</td>

$ sed -n 817,819p .../snapshots/S229-msaf.html | grep -c "&"
0
```

Byte accounting for the quote (TEXT_VIEW: `<script>`/`<style>` blocks removed, each tag replaced by one space, entities decoded, whitespace collapsed — no other shaping):

- L818 `</td>` `\n` … dropped: the four tags `<td>`, `<code>`, `</code>`, `</td>` each became one space. Nothing inside them was dropped — `allowed-tools` is cell text.
- L819 `<td>No</td>` → ` No `: the tags became spaces, the cell text `No` is retained. **This is why the quote reads "allowed-tools No Space-delimited …": `No` is the table's Required column value for this row, and a contiguous span that starts at the field name necessarily crosses that column.** It is not part of the description.
- L820 `<td>…</td>` → the description text verbatim, tags to spaces. The `-` between "Experimental" and "support" is ASCII hyphen-minus U+002D (`od -c` confirms `E x p e r i m e n t a l   -   s u p`), not an en/em dash — no normalisation happened.
- Line breaks and the table markup between the three cells collapsed to single spaces.
- Entities decoded inside the quote span: none — `grep -c '&'` over L817–819 is 0, so nothing was unescaped here.
- Result string, 19 whitespace-separated words (5–25 OK), one occurrence in the snapshot's TEXT_VIEW (`grep -c -F` positive control = 1).

## (4) Q70 check — the quote occurs in no other page of the set

Full output in `build/Kb79R04MsafRow.q70.txt`. Five other surfaces fetched this seat (raw bytes, sha256 in the receipt) and each grepped both as raw bytes and as TEXT_VIEW:

| page | raw `grep -c -F` | TEXT_VIEW `grep -c -F` |
|---|---|---|
| spec — `https://agentskills.io/specification.md` (7 608 B sha256 9a67de89…) | 0 | 0 |
| claude — `https://code.claude.com/docs/en/skills.md` (117 962 B sha256 31623035…) | 0 | 0 |
| factory — `https://docs.factory.ai/cli/configuration/skills` (341 235 B sha256 81457fbf…) | 0 | 0 |
| pi — `raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md` (4 793 B sha256 5b980552…) | 0 | 0 |
| vibe — `raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md` (77 634 B sha256 fc48a5db…) | 0 | 0 |
| own msaf TEXT_VIEW (positive control) | — | **1** |

The same quote greps **0** in the sibling seats' already-committed snapshots present at 2026-10-27T21:44Z — `snapshots/S226-spec.md` (sha256 9a67de89132948b2…), `S227-claude.md` (31623035b25ac7e6…), `S228-factory.md` (81409d890cb1b07f…), `S231-vibe.md` (fc48a5dbafe572fe…); `S230-pi` was not yet written. `grep` exits 1 on the five (no match) and 0 on the control. The nearest sibling text — the open spec's own row, `| \`allowed-tools\` | No | Space-separated string of pre-approved tools the skill may use. (Experimental) |` (specification.md L35) — shares no 6-word run with the msaf quote: **"Space-separated" vs "Space-delimited"**, and the spec's limit clause is a separate bullet ("Experimental. Support for this field may vary between agent implementations", L174-177). The msaf page is not a verbatim copy of the spec table.

## (5) Reading — what the page says, what it does not

The page's only statement about the field is one table row under **§ SKILL.md format**: `allowed-tools`, Required **No**, "Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations." So on this client the field is (i) optional, (ii) a single scalar string whose items are separated by spaces — not a YAML sequence (the page's own frontmatter sample at L773-782 does not include the field at all, so it prints no example value and no scoped-tool syntax such as `Bash(git:*)`), and (iii) a *statement of pre-approval* attributed to the skill, carrying an explicit limit: Experimental, support may vary between agent implementations. The page does **not** say who enforces the list, at what granularity (per turn, per invocation, per skill), whether entries naming unknown tools are ignored or fatal, what happens when the list is absent, or whether any tool call is filtered by it. The nearest thing to an enforcement statement is its "Security best practices" section, which pushes the work onto the integrator — "Sandboxing - Run skills that include executable scripts in isolated environments. Limit filesystem, network, and system-level access to only what the skill requires." (rendered L~2546) — i.e. the page never claims the framework gates tool calls on this field. A derived point the page states generally but not about this field: "Invalid YAML, duplicate recognized fields, incorrect field casing, or a collection where a scalar field is expected prevent the skill from loading." — [INFERENCE] applied to `allowed-tools`, a YAML *list* value would therefore be the "collection where a scalar field is expected" and the skill would fail to load on this client; the page does not name `allowed-tools` in that sentence. **The frozen label `experimental` is TRUE of this page**: the row itself says "Experimental - support may vary between agent implementations", which is verbatim the wording the plan's (f) rule requires for `msaf`. I see no line on the page contradicting it.

## (6) Prompt-injection text seen in the page

None found. Sweep of the fetched bytes: `disregard` 0, `ignore previous` 0, `<|im_start|>` 0, `assistant:` 0. The 4 `system prompt` hits and 11 `You are a ` hits are ordinary documentation prose and code samples, not instructions to the reader: the first is "Skill names and descriptions are injected into the system prompt at the start of each run"; the second is repeated `Instructions = "You are a helpful assistant."` inside C#/Python sample agents. The page carries one relevant caution *aimed at skill authors* — "Check for adversarial instructions that attempt to bypass safety guidelines, exfiltrate data, or modify agent configuration files." — reported, not acted on. Nothing in the page was followed as an instruction.
