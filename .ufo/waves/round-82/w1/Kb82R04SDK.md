# Kb82R04SDK — S249 synced-frontmatter reconnaissance

Axes: freshness (live source identity and located clause); operability (reproducible bounded receipts, no production scoring).

Base: `47dbe8781657de563ff867caca6244d28e3db504`. Read round-82 plan and operator RULES before research. This seat adds no S-row, code patch, corpus change, score, or SDK claim. SDK work remains deferred behind C1/C2.

## Observed: live S249 and link target

Accessed 2026-10-30T14:39:16Z. `curl -fSL -A Mozilla/5.0 --max-time 45 --silent --show-error <URL> -o <seat-artifact> -w 'http=%{http_code} final=%{url_effective} redirects=%{num_redirects}\n'` captured its own exit; both requests returned exit 0, HTTP 200, zero redirects, empty stderr. Full argv/output/timestamps are in `build/Kb82R04SDK.fetch.json`. Initial urllib request returned HTTP 403; reader-tool fallback and curl succeeded. No failed fetch is claimed successful.

- SDK source: https://code.claude.com/docs/en/agent-sdk/skills.md — 28,395 bytes; sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`, identical to S249's recorded digest.
- Located clause at raw line **348**, under **Pre-approve tools for skills**: “Skills [synced from claude.ai](https://code.claude.com/docs/en/skills.md#how-claude-code-handles-the-frontmatter-of-a-synced-skill) follow their own frontmatter rules.” The preceding sentences distinguish frontmatter/query grants and the managed-settings override; the exception does not itself enumerate its rules.
- Linked target: https://code.claude.com/docs/en/skills.md#how-claude-code-handles-the-frontmatter-of-a-synced-skill — fetched document 118,872 bytes; sha256 `907a9929f54ad8b730a55088108311acb9bb5677c33b1861fb2664a53ab15688`. Heading raw **301**, introductory sentence **303**, rules **305–306**.
- Target 305: frontmatter applies in every kind of session; `allowed-tools` uses the normal permission flow; `allowManagedPermissionRulesOnly` makes the grant not apply.
- Target 306: display text is sanitized; control characters removed; angle brackets escaped in text reaching Claude, including descriptions; sanitization requires Claude Code **v2.1.228+**. Short exact quote: “It removes control characters” (4 words).

These are vendor documentary statements, not measured SDK/client behavior.

## Whole-base coverage, not filename inference

Read-only `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only <base> corpus` returned exit 0 and **158 files**. Each file was extracted with `git -C <lane> show <base>:<path>` (each exit asserted 0) into seat scratch. Every tracked corpus file was searched, including all knowledge, lessons, README and SOURCES; complete file sha256s and untruncated matched lines are preserved in the manifest/sweep artifacts. No working-tree content was substituted for the frozen base.

Literal sweep 1: `synced|claude\.ai|own frontmatter|how-synced-skills` — 158 files, **11 matching lines**. Sweep 2: `saniti|control characters|escap.{0,40}angle|2\.1\.228|permission flow|every kind of session|allowManagedPermissionRulesOnly|six specification fields` — 158 files, **9 matching lines**. These are textual coverage evidence, not semantic proof of universal absence. LSP is unavailable: `read xd://lsp` answered `No such tool`; prose definitions/citations were traced by text fallback, not presented as semantic references.

Already held, with confidence high:

1. **The exact SDK exception is already taught**, not merely present in a snapshot: `corpus/knowledge/allowed-tools-sdk-round81.md:32` has a dedicated matrix row (“skills synced from claude.ai … follow their own frontmatter rules”); **:42** explicitly describes that exception. Therefore “synced-frontmatter clause newly uncovered” would be false.
2. **The boundary is explicitly recorded:** `corpus/README.md:162` says the SDK defers these rules without stating them; **:249** identifies the precise linked section and says it has not been read at row level. The new reachable area is the linked section's contents, not discovering the SDK's link.
3. **Grant mechanisms already held:** the round-81 knowledge entry **:25–31,38–45** teaches frontmatter versus `allowedTools`/`allowed_tools`, managed override, Skill auto-allow, explicit tools-list interaction, and pre-approval rather than restriction. `corpus/SOURCES.md:190` S249 scopes query grants and managed override, is mined, and cites the knowledge entry plus `corpus/lessons/round-81.md`. Lesson **:30,51,55** records that documentary admission. S248 **:189** covers the same page under a frontmatter scope and remains queued at base; its repair belongs to the designated owner.
4. **Adjacent claude.ai coverage is not the synced rule:** `corpus/knowledge/allowed-tools-surfaces-round80.md:74–76,119` already teaches six-field upload/API packaging acceptance and the loss of Claude-Code-only restriction fields. Upload validation is not synced display-text sanitization. Likewise `corpus/knowledge/harness-system-prompt.md:28–30` mentions this host's sanitized user input, not Claude Code synced-skill metadata.

## Future candidate only

**Candidate:** deepen the existing allowed-tools entry with the linked synced-skill frontmatter contract: ordinary permission flow across session kinds, managed-rule override, and runtime display-text sanitization (control removal and angle escaping, documented v2.1.228 floor). Distinguish author-time angle-bracket validation from runtime escaping, and upload acceptance from sync handling. Reuse existing source/page context and evaluate exact scope before deciding any future registry append; no new S-row is proposed or allocated here.

**Inference, confidence medium-high:** the linked section's synced-specific sanitizer contract is not taught in the frozen corpus. This conclusion combines a full-content sweep, explicit README gap, and review of the matching contexts; it is stronger than a filename search but is not a proof against every possible paraphrase. The managed override itself is already held, so it must not be counted as an entirely new mechanism.

**Remaining unknowns:** installed client/SDK implementation and observed permission/sanitizer behavior; equivalence of HTML and Markdown renderings; historical introduction of rules beyond the page's stated version floor; future admission predicate/counter. None is required to resolve this source reconnaissance. No SDK package installed/imported/session run.

## Receipts, bounds, and hygiene

- Disk guard status exit 0 before corpus extraction: scratch use 47%, 428.9G free. No heavy gates, selftests, production after-values, tip battery, or 6/6 claim.
- No installs/updates, pacman calls, services, subprocess background jobs, delegates, git mutations/commits, or index/jj changes. Research used read-only git extraction, not a code-work clone.
- `build/Kb82R04SDK.base-manifest.json`: sha256 `522fca738a13a3c56f7c412e8bd02e606ea9553c4b1a1cb76511cdd5601e34e4`.
- `build/Kb82R04SDK.sweep.json`: sha256 `8735ff0d5056569894584c4ee5ca1f8db0ee058b65c370f6f26acd0d728714fc`.
- `build/Kb82R04SDK.fetch.json`: sha256 `a823bde440671d5eabffae2a03cf51cda8489998b80669ca3ffbed5280cad4b6`.
- Live pages preserved as `build/Kb82R04SDK.sdk.md` and `build/Kb82R04SDK.synced-target.md` with hashes above. Scratch extraction removed after receipt creation.

VERDICT: S249 live clause is already held; only linked synced-specific rules are a future documentary candidate. SDK claim deferred; no new S-row.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82R04SDK.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R04SDK.base-manifest.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R04SDK.sweep.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R04SDK.fetch.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R04SDK.sdk.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82R04SDK.synced-target.md
