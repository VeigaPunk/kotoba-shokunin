Result: MIXED — All 35 v1.2 controls are NOT MET with G=0, but the not-a-base-source rule still accepts live re-citations through URL aliases and redirects.

# CtlC1HeldVariant — v1.2 re-attack

Axes: depth, source provenance, identity consistency, calibration. This is a bounded critic result, not a round judgment. The counter was copied verbatim into the existing sandbox under L1's explicit instruction; no counter fix was made.

Sandbox: `/fast/scratch/hyaku/kotoba-r56/CtlC1HeldVariant`.
Start: `Fri 23 Oct 2026 02:41:16 AM UTC`.
Counter SHA-256: `b5d58ec2f39063099742f642b217de559e1ffaa3888d813a19872c293f6f71ff` (observed `sha256sum`, exit 0).
Full per-world checksum, commit, command, stdout, stderr, exit and predicate receipt: `.ufo/waves/round-56/controls/CtlC1HeldVariant-v12.txt`.
All 35 fixture commits include the v1.2 counter bytes. The first 25 replay the original held-world content, followed by 10 new URL-alias worlds. No build, lint, self-test or unrelated verification ran.

## Answers

- **Any tested held form counted as new ground? No.** Every run reports G=0. Found case/home/glob variants still have `.claude/agents` base_count=3, `.opencode/agents` base_count=10, and `.config/opencode/agents` base_count=24. Codex variants have diagnostic base_count=5, but their source rows are rejected before live fetching; that is not claimed as a live experiment on Codex documentation. Non-dot `opencode/agents/*.md` remains malformed.
- **Can a base page still be re-cited? Yes.** A GitHub/raw redirect reaches the exact held S062 source URL and is FOUND. Legacy-host redirects reach exact held S026 and are FOUND. Internal duplicate slashes also remain accepted and FOUND. All yield F=1/G=0 and exit 1, not a full-predicate shortcut.
- The prior S026 path-case/www/uppercase-suffix controls are now rejected as already-base URLs. The singular-prefix control is now BACKED but found=no: the right-boundary repair changes the observed F from 1 to 0.

## Strongest counterexample: redirect reaches an exact held base URL

World `s062-github-raw-redirect`, commit `9af7ea813b4a4da761b56027366e80ceac5bbc7b`:

Input: `https://github.com/anthropics/claude-code/raw/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md`.
Observed final URL: `https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/CHANGELOG.md`, the exact base S062 source (`corpus/SOURCES.md:75`).

Fresh ordinary curl evidence:

```
Fri Oct 23 02:43:09 AM UTC 2026
HTTP 200; 1070244 bytes
sha256 121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49
curl exit 0
```

The digest equals the previously fetched held pinned S062 bytes. A fresh source id and input URL do not make it a new source. Its agent path is held, so G correctly stays zero.

Command, cwd sandbox:

```
timeout 70 python3 -B verifiers/check_agent_definitions.py --rev 9af7ea813b4a4da761b56027366e80ceac5bbc7b --fetch
```

Full stdout:

```
agent-definition locations found on the live page 1 of 1; new ground 0
Claude Code  BACKED token=.claude/agents/*.md norm=.claude/agents found=yes base_count=3
Codex        no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
VS Code      no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

`exit 1`

C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET

Evidence: `verifiers/check_agent_definitions.py:597-600` checks only the input URL against base-source keys; `:759-763` obtains the final URL but checks only its host. It never excludes a final URL already held at base.

Smallest safe correction, only by explicit pre-data erratum if chosen: reject a fetched page if its final URL key is in the frozen base-source set. This closes the exact-final-URL redirect counterexample without merging distinct GitHub revisions or globally equating unrelated content.

## Independent same-page aliases

- `s026-legacy-claude-code-route`, commit `cac05f1e13b708ca820349f3a6a2845ffd1ed8c6`: `https://docs.claude.com/en/docs/claude-code/sub-agents` redirects to exact held `https://code.claude.com/docs/en/sub-agents`; F=1/G=0, exit 1.
- `s026-anthropic-legacy-route` likewise redirects from `docs.anthropic.com/en/docs/claude-code/sub-agents` to the exact held URL; F=1/G=0, exit 1.
- `s026-internal-double-slash`, commit `fa6643997116b6fb72f35527062fa61cc4d0903e`: `https://code.claude.com/docs//en/sub-agents` remains on that input URL but returns the same 1,336,521-byte page digest as the legacy routes: `3a7ce2e991513a9df8f866b707e58d587d69e3629f25c680565d4b63f9e62d7d`; F=1/G=0, exit 1. Leading and before-page double slashes also succeed locally.

For duplicate slashes, the smallest bounded correction is rejecting redundant-slash spellings or normalizing them on this proven served-docs host before comparing source identity. A final-URL check alone cannot close these no-redirect aliases. Do not silently redefine all URL path semantics.

Not-found aliases are not passed: the double-percent and `.html` forms return HTTP 404, and the alternate legacy docs-host route serves a different page that does not back the quote. Single percent encoding is already caught as a base URL. Old GitHub blob mirrors are still BACKED but not FOUND. The mutable `main` changelog retains the old quote and is FOUND, but is not described as byte-identical to a pinned source.

## Tradeoff versus demonstrated defect

The G exclusion held for every tested case, including genuinely documented held paths quoted correctly on the opencode page. That genuine documentation work is NOT a shortcut; no new-client research was performed merely to fill F. URL identity is a separate partial defect: the newly FOUND rows can be old sources even though their held tokens buy no G. These local defects do not establish that any complete C1 control MET its frozen predicate.

The previously noted project/home quote equivalence is still explicitly allowed by the frozen contract; it remains a scope-fidelity tradeoff, not a newly demonstrated G escape. No claim about unseen variants or overall C1 soundness is made.

## Complete executed-world matrix

| World | Sandbox commit containing v1.2 | Counter first-line values | Frozen predicate |
|---|---|---|---|
| do-nothing-freeze | `caadb675cc1fdd5de6253bb5b43819511e1f80dd` | 0 of 0; new ground 0 | exit 1; NOT MET |
| s026 | `60f803319d8f0921937477e7e247450b93e2560f` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-md | `5e06b0fb10d799d8e616e67781c9f84c1c886094` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-slash | `c94ea5f02bdafad4e6cbf4a575d2efc62e712a67` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-query | `b9f06d3464940c73c96adfc80817a545d1d07c52` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-www | `76e5f4a80be8bf62e7683d8b71992438a414836a` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-case | `40d041ffb67b1eda64ac1a882fff014aff1a8334` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-upper-md | `1955d2d672dac742ab5fbe53265eb74620f96dd0` | 0 of 1; new ground 0 | exit 1; NOT MET |
| opencode-held-new-page | `49ba2ca0a57923ff2348a5fd8db7b427492b7803` | 1 of 1; new ground 0 | exit 1; NOT MET |
| opencode-case-flip | `cf1cc6f892d6601952f1081749fafaf23312873f` | 1 of 1; new ground 0 | exit 1; NOT MET |
| opencode-home-prefix | `1200625648ad14cd4828bb72e2850752a91cc390` | 1 of 1; new ground 0 | exit 1; NOT MET |
| opencode-config-home | `38b5372da4bc5d6c3b15b4b7ce5400f86aeedb44` | 1 of 1; new ground 0 | exit 1; NOT MET |
| opencode-config-bare | `19c87d2c84ec5a80a8973ff79aadeb1314e06b4a` | 0 of 1; new ground 0 | exit 1; NOT MET |
| opencode-singular-prefix | `c29787cfb4978144c5e969aff0eb9d09c4a4e16d` | 0 of 1; new ground 0 | exit 1; NOT MET |
| opencode-singular-with-slash | `a35489fe638ea1d6ca360ca94b218067538ae3a6` | 0 of 1; new ground 0 | exit 1; NOT MET |
| claude-held-glob-main-alias | `e95e77a7fd84d857178a244e2124a5d42bacac15` | 1 of 1; new ground 0 | exit 1; NOT MET |
| claude-held-case-home-glob | `dee76f23d99cfa81cabeebde200183f9ed4391bb` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s062-original-raw | `0a85e9c1fc47535415d6d2fa4d1ffb6d2bfa3b03` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s062-github-mirror | `dc48e17e441421f8afa30acad6630816835a4ae6` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s016-original-github | `aa0ecb816d52d799f21a45750c24c36cf5866d18` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s016-raw-mirror | `5f21ed7b295a04becf3ab9079f596df2bfec8313` | 0 of 1; new ground 0 | exit 1; NOT MET |
| codex-case-flip | `3d1bf670cd033d3b9025f03e64885077aff864be` | 0 of 1; new ground 0 | exit 1; NOT MET |
| codex-home-prefix | `05c5025d1eb49135739a76b42df09390085fabe3` | 0 of 1; new ground 0 | exit 1; NOT MET |
| codex-home-glob | `4ed0052b206891e27a2630939afa60651454e312` | 0 of 1; new ground 0 | exit 1; NOT MET |
| non-dot-held-opencode-path | `3651d60fc9cfbe4f1606e64d62b6d3c29264edc1` | 0 of 0; new ground 0 | exit 1; NOT MET |
| s026-internal-double-slash | `fa6643997116b6fb72f35527062fa61cc4d0903e` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s026-leading-double-slash | `7d6608d30abad170c0e533ae23921cf561e22844` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s026-before-page-double-slash | `5c62c4478682be94578791fb845af8acfda4387b` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s026-legacy-docs-host | `9d05d465ab6371b27cebd08d426ef0a6fa0d539c` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-legacy-claude-code-route | `cac05f1e13b708ca820349f3a6a2845ffd1ed8c6` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s026-anthropic-legacy-route | `0cda16ef2ba0c84a13bdbe40d965235f99dfaa80` | 1 of 1; new ground 0 | exit 1; NOT MET |
| s026-html-suffix | `c34b802f3e284450e9ce31e52b597dadf55ac4d0` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-double-percent | `d5b32b70fec79de43576ade470e18071f4d1778d` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s026-single-percent | `0809aae13f4c1a4f925af8d189e0b26dc4794614` | 0 of 1; new ground 0 | exit 1; NOT MET |
| s062-github-raw-redirect | `9af7ea813b4a4da761b56027366e80ceac5bbc7b` | 1 of 1; new ground 0 | exit 1; NOT MET |

## Evidence and bounds

New access metadata, full curl commands, final URLs, UTC date lines, HTTP statuses, byte counts and sha256 values are preserved in the plain-text receipt and scratch `held-variant-v12/fetches.json`. Prior acquisition evidence for unchanged quote excerpts is explicitly identified as prior, not relabeled fresh.

Byte-exact short source excerpt (no markdown stripping in recording), scratch `held-variant-v12/s062-github-raw-redirect.body:7609`: "Fixed custom agent `model` field in `.claude/agents/*.md` being ignored when spawning team teammates".

Claude excerpt, prior fetched markdown `held-variant-evidence/s026-md.body:103`: "Create a personal code-improver subagent in ~/.claude/agents/ that scans". Both excerpts are below 25 words. Fabricated or path-truncated fixture quotes are control data only, never admitted documentation facts.

No challenge workaround, browser, paid model call, alternate judging runtime, task spawn, install, lane Git write, counter repair or push. Only the named v1.2 report/receipt were written in the lane. All launched commands completed; no persistent process or service was started.
