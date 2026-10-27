# Kb79R04MsafRow — w1 seat report (C2 source row S229, surface `msaf`)

Round 79, wave 1, attempt 1. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`, plan commit F1 `2c56622375641193a03bb97c0624e6536f3dffba`. Leaf seat: no subagents, no background jobs, no lane commit.

## Behaviour

Opened S229 (Microsoft Agent Framework skills page) myself, twice, saved the raw bytes, pinned them, located the `allowed-tools` frontmatter-table row, and drafted the registry row and the entry table row for the L1 to stitch.

Commands and their own exit statuses (all run from my scratch dir under `/fast/scratch/hyaku/kotoba-r79/Kb79R04MsafRow`, `TMPDIR` set inside it):

| # | command | result |
|---|---|---|
| 1 | `curl -sSL -A 'Mozilla/5.0' --max-time 60 -o msaf-1.html -w '%{http_code} %{size_download} %{url_effective}' https://learn.microsoft.com/en-us/agent-framework/agents/skills` | rc=0, `200 157339 https://learn.microsoft.com/en-us/agent-framework/agents/skills`, `2026-10-27T21:41:02Z`, sha256 `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2` |
| 2 | same fetch again (`msaf-2.html`) | rc=0, same status, same 157 339 B, same sha256; `cmp msaf-1.html msaf-2.html` rc=0 → **page did not move between fetches** |
| 3 | `grep -n -F allowed-tools S229-msaf.html` | rc=0, exactly one hit: `818:<td><code>allowed-tools</code></td>` |
| 4 | `grep -n -F "Space-delimited list of pre-approved tools" S229-msaf.html` | rc=0, `820:<td>Space-delimited list of pre-approved tools the skill may use. Experimental - support may vary between agent implementations.</td>` |
| 5 | `sed -n 816,820p S229-msaf.html` | rc=0, the three cells `allowed-tools` / `No` / description (Q53 receipt) |
| 6 | `sed -n 817,819p S229-msaf.html \| grep -c '&'` | rc=0, `0` → no entity decoding inside the quote span |
| 7 | Q70 greps (`grep -c -F '<quote>'`) on spec / claude / factory / pi / vibe, raw and TEXT_VIEW | raw 0,0,0,0,0 (grep rc=1 each); TEXT_VIEW 0,0,0,0,0 (rc=1 each); own msaf TEXT_VIEW control = 1 (rc=0) |
| 8 | Q70 greps on the sibling seats' committed snapshots S226/S227/S228/S231 | 0 each (rc=1) |
| 9 | `sha256sum snapshots/S229-msaf.html` | `34016233a42a2191e319bb6ed49362956c6a6e86bbe64f2fa2e370326de548d2  …/snapshots/S229-msaf.html`, 157 339 B |

No `verifiers/check_allowed_tools.py` exists in the lane yet (`ls verifiers/ | grep -i allowed` → no output, rc=1), so nothing was scored against the frozen C2 counter and no control world was run by me. The freeze discipline is honoured: this seat produced drafts only.

## Gates satisfied by this seat's bytes

- (a)-input: 4 backticked page tokens (`allowed-tools`, `Space-delimited`, `pre-approved`, `Experimental`), each ASCII-word-bounded in the snapshot's TEXT_VIEW; one value-form token (`Space-delimited` — the page prints no example value anywhere, its only `allowed-tools` occurrence is the table row); one grant-semantics token (`Experimental`).
- (b)-input: registry row `S229` is 11 cells, `status` `mined`, `tier` `B`, `used-by` = `corpus/knowledge/allowed-tools-surfaces-round79.md`, URL host+path `learn.microsoft.com/en-us/agent-framework/agents/skills` (= the frozen `msaf` host).
- (c)-input: snapshot `S229-msaf.html` sha256 `34016233…48d2` = the pin written to `snapshots/S229.manifest` = the sha256 in the anchor cell's fetch record. **The round-level `snapshots/MANIFEST.sha256` did not exist when I wrote (checked: `ls` → no such file), so the L1 must concatenate the per-seat `S*.manifest` lines into it and commit the pin.**
- (d)-input: located quote is 19 whitespace-separated words, a whitespace-collapsed substring of the snapshot's TEXT_VIEW, contains `allowed-tools`, comes from the SKILL.md-format frontmatter table (not a banner/subtitle/first-heading block), and occurs in no other surface page (Q70).
- (e)-input: `opened` 2026-10-27.
- (f)-input: grant plain text `experimental`, grounded by the page's own "Experimental - support may vary between agent implementations".

## Touched surfaces (writes)

- `.ufo/waves/round-79/snapshots/S229-msaf.html` (157 339 B, raw HTML)
- `.ufo/waves/round-79/snapshots/S229.manifest`
- `.ufo/waves/round-79/snapshots/S229.fetch.json`
- `.ufo/waves/round-79/build/Kb79R04MsafRow.rows.md`
- `.ufo/waves/round-79/build/Kb79R04MsafRow.q53.txt`
- `.ufo/waves/round-79/build/Kb79R04MsafRow.q70.txt`
- `.ufo/waves/round-79/w1/Kb79R04MsafRow.md` (this report)
- scratch `/fast/scratch/hyaku/kotoba-r79/Kb79R04MsafRow/` — created, used, **removed** (`rm -rf`, then `test ! -e` rc=0).

No lane file outside `.ufo/waves/round-79/**` was read-modified or written; no git/jj mutation anywhere; no corpus/SOURCES.md or entry edit (L1 stitches). No tool installs or upgrades (nothing was needed). `disk-guard.sh` was not consulted because the pass was three ~160 KB fetches, not a heavy pass.

## Out of scope (deliberately not done)

- Writing `corpus/knowledge/allowed-tools-surfaces-round79.md`, `corpus/SOURCES.md`, SKILL.md rule line, PROVINCE bullet, README/LOG/SCORECARD, lesson — L1 integration.
- Editing the C2 counter or its fixtures (it does not exist yet), running any control world, or scoring claim data on it.
- Deciding the `experimental` label for the other surfaces (S226, S227, S228, S230, S231 — sibling seats).
- Snapshotting the five comparison pages I fetched for Q70; they live only in scratch and are identically sized/hashed to the sibling seats' committed snapshots for spec/claude/vibe (see the Q70 receipt for the hashes, useful for dedupe).

## Findings

1. **The label `experimental` is TRUE of this page.** The row itself reads "Experimental - support may vary between agent implementations"; it is the page's only statement about support. I quote the contradicting line would be needed only if I judged it false — there is none.
2. **A contiguous-span artefact the counter's evaluator should know about.** The TEXT_VIEW rule (tags → one space) + "the quote must contain `allowed-tools`" forces the table's *Required* column value into the quote, so the S229 quote begins "allowed-tools No Space-delimited …". `No` is the Required column (`<td>No</td>`), **not** a modifier of "space-delimited"; read without that knowledge, the span can be misread as "not space-delimited". There is no alternative contiguous span on this page: `allowed-tools` occurs exactly once, and every ≥5-word window around it crosses the `No` cell. Reported, not repaired — the predicate was not narrowed and the quote was not massaged.
3. **msaf is not a copy of the open spec.** The spec (`agentskills.io/specification.md` L35) says "Space-**separated** string … (Experimental)" and puts the limit in a separate bullet; the msaf table says "Space-**delimited** list … Experimental - support may vary between agent implementations". So the vendor page restates the field rather than mirroring the spec, which also made a Q70-clean quote possible (0 hits on the spec page for both the full quote and the 6-word fragment "Space-delimited list of pre-approved tools").
4. **No example value on the page.** The YAML frontmatter sample at L773-782 lists `name`/`description`/`license`/`compatibility`/`metadata` and omits `allowed-tools`, so the page prints no scoped-tool syntax (no `Bash(git:*)`) and no list form. The value form must be taken from prose ("Space-delimited list"), which is what the token `Space-delimited` records.
5. **No stated enforcement.** The page never says the framework gates or filters tool calls by `allowed-tools`; its "Security best practices" section assigns sandboxing and access limiting to the integrator ("Sandboxing - Run skills that include executable scripts in isolated environments. Limit filesystem, network, and system-level access to only what the skill requires."). [INFERENCE] marked as such in the deliverable: the page's general load-failure rule ("a collection where a scalar field is expected prevent the skill from loading") implies a YAML *list* value for this scalar field would fail to load on this client — the page does not name `allowed-tools` in that sentence, so this is derived, not stated.
6. **Prompt injection: none.** Sweep over the fetched bytes for `disregard` (0), `ignore previous` (0), `<|im_start|>` (0), `assistant:` (0); the 4 `system prompt` and 11 `You are a ` hits are documentation prose and `Instructions = "You are a helpful assistant."` code samples. The page's own caution to readers ("Check for adversarial instructions that attempt to bypass safety guidelines, exfiltrate data, or modify agent configuration files.") is content, reported, not followed. Neither my quote nor my reading contains anything instructed by the page.
7. **`MANIFEST.sha256` gap** (see (c)-input above): the per-seat `.manifest` fragments exist (S226/S227/S228/S229/S231 at 21:44Z) but no round-level `snapshots/MANIFEST.sha256`; without it, conjunct (c) is unevaluable and the r73-counter precedent raises it as an environment error. L1 action.
8. **Two seats' factory snapshots differ in bytes** — my raw fetch of `docs.factory.ai/cli/configuration/skills` is 341 235 B (sha256 `81457fbf…`), the committed `snapshots/S228-factory.md` is 17 567 B (sha256 `81409d89…`), i.e. a different representation of the same page. Not my row; flagged only because conjunct (a) checks tokens against the *committed* snapshot. Q70 still greps 0 on the committed bytes.

VERDICT: S229 (`msaf`) drafted and self-checked — snapshot pinned (157 339 B, sha256 34016233…48d2, two identical fetches), quote 19 words, Q70-clean against all five other surfaces and the four committed sibling snapshots, label `experimental` TRUE of the page; no scoring against the unfrozen C2 counter and no lane writes outside `.ufo/waves/round-79/`.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R04MsafRow.rows.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S229-msaf.html, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S229.manifest, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/snapshots/S229.fetch.json, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R04MsafRow.q53.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79R04MsafRow.q70.txt
