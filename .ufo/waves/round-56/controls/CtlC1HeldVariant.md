Result: MIXED — All 25 executed worlds miss C1 and no tested held form contributes G, but a case-only alias of held S026 is accepted as a new source and FOUND.

# CtlC1HeldVariant — frozen C1 control review

Axes: depth, source provenance, source-identity consistency, and calibration. This is a bounded control result, not an admission, round judgment, or integration recommendation. No counter was edited.

Sandbox: `/fast/scratch/hyaku/kotoba-r56/CtlC1HeldVariant`.
Freeze: `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257`.
Base held tree: `b0b7140b5a7cf8a50f13989ee6285fc8ee245c41`.
Counter: `verifiers/check_agent_definitions.py`.
Observed `timeout 30 sha256sum verifiers/check_agent_definitions.py`, exit 0:

```
1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
```

Full per-world commit, command, checksum, stdout, stderr, exit and predicate label: `.ufo/waves/round-56/controls/CtlC1HeldVariant.txt`. Machine-readable scratch evidence: `held-variant-evidence/scores.json`; construction harness: `run_worlds.py`. All paths in this paragraph other than the receipt are under the sandbox.

## Strongest counterexample: re-cited base page passes the new-source guard

World `s026-case`, sandbox commit `770daebd9c53fe5f1b225297a2bbaef3594658d7`, changes the URL path spelling from held S026's `/docs/en/sub-agents` to `/docs/en/Sub-Agents`, using a fresh S900 id and otherwise the same held Claude path. Both URLs returned HTTP 200, 1,336,521 bytes, sha256 `c6278eab615bafe7be2db72596b26c536b5e6760545e6e9b6a5b66355d82b9eb`. The fetched bytes are identical; this is not new source knowledge.

Command, cwd sandbox:

```
timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 770daebd9c53fe5f1b225297a2bbaef3594658d7 --fetch
```

Full stdout:

```
agent-definition locations found on the live page 1 of 1; new ground 0
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
Codex        no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
VS Code      no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
```

`exit 1`

C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET

Evidence: held S026 is `corpus/SOURCES.md:39` at base; `url_key()` retains path case (`verifiers/check_agent_definitions.py:368-381`), and the base-source check uses that key (`:553-554`). This is a demonstrated source-identity subguard weakness, NOT a demonstrated false-positive C1 predicate: F=1 and G=0 still fail the frozen thresholds.

Smallest safe correction, only as an explicitly declared pre-data erratum if chosen: resolve this proven alias to the same source identity as S026. Do not lowercase every URL path globally; GitHub/raw paths can be case-sensitive. Preserve the held-path G exclusion.

## Held-path result: G counts none of these forms

- `.OpEnCoDe/AgEnTs/`, `~/.opencode/agents/`, and the unmodified project path are all FOUND; all normalize to `.opencode/agents`, with counter `base_count=10`, G=0.
- `~/.config/opencode/agents/` is FOUND with `base_count=24`, G=0. Base already records it at `SKILL.md:520`. The bare `.config/opencode/agents/` variant is BACKED but not FOUND: the live page uses `~/`, and the frozen left boundary does not allow the bare token to start after that slash. This is a miss, not proof of G behavior from that world's live run.
- `.claude/agents/*.md` and `~/.CLAUDE/AGENTS/*.MD` are FOUND against the raw changelog alias, normalize to `.claude/agents`, `base_count=3`, G=0. Case, home-prefix and trailing-glob variants do not buy new ground.
- `.CODEX/AGENTS`, `~/.codex/agents`, and `~/.codex/agents/*.md` normalize to `.codex/agents`; separate calls to the frozen `git_grep_count` return 5. Their scored worlds are rejected for re-citing a base URL, before live fetching. Their quotes are deliberately fabricated controls, not evidence of documented Codex agent-definition locations; no live success is claimed.
- The non-dot held `opencode/agents/*.md` is malformed under the pinned token grammar, K=0; it cannot count as new ground.

The `opencode-held-new-page` world correctly quotes actual agent paths from `https://opencode.ai/docs/agents.md`, records a new source row, and obtains F=1/G=0. This is genuine documentation work on a held location, NOT a shortcut that meets the predicate. No attempt was made to fill the missing clients with genuine new-path research to force a passing control.

The base-count exclusion is observed directly in the FOUND worlds, not inferred only from a normalization formula. The auxiliary counts for unfound worlds are explicitly marked diagnostic in the receipt.

## Identity changes accepted locally, but no full-predicate break

1. `opencode-singular-prefix` truncates a plural path inside the source quote to `.opencode/agent`. It is FOUND with F=1/G=0 even though the quoted source's full token is `.opencode/agents/`. The frozen matcher checks only a left boundary (`verifiers/check_agent_definitions.py:651-670`); it accepts the singular as a prefix of the plural. Adding a trailing slash to the fabricated singular yields F=0. Smallest safe correction in a new declared rule: require an end-of-segment boundary as well. This is a quote/location-identity defect, not a G escape.
2. `opencode-home-prefix` claims `~/.opencode/agents/` while quoting only the documented project `.opencode/agents/`. The frozen spec explicitly permits dropping `~/` for quote matching (`verifiers/check_agent_definitions.py:55-58,470-483`). Thus the observed acceptance is a stated equivalence tradeoff, not an implementation deviation; it can erase project-versus-home scope. [INFERENCE] If exact scope is part of the decision table's learning claim, quote validation must preserve it even if the G normalization continues to merge held forms.

These partial weaknesses must not be reported as controls that MET C1. None did.

## URL variant outcomes

- Exact S026, `.md`, one trailing slash, and query/fragment re-citations are rejected as base URLs.
- S026 `www.` is accepted by source/host validation but is not FOUND; ordinary curl exits 6, HTTP status 000, DNS resolution failure. It is not a live-source success.
- S026 path-case alias is both BACKED and FOUND, with identical bytes to the held base page, as shown above.
- S026 uppercase `.MD` bypasses base-URL validation but its ordinary request returns HTTP 404; the counter reports found=no. No live credit.
- The GitHub blob mirror of held S062's exact raw URL is BACKED, but not FOUND. The raw mirror of held S016's GitHub URL is likewise BACKED, not FOUND. Thus both mirrors pass the not-a-base-URL subguard, but neither yields live-path credit in its scored world. S016's fixture quote is intentionally unrelated agent text.
- S062's mutable `main/CHANGELOG.md` URL accepts a held historical quote and is FOUND. It is already mentioned in base S062's anchor cell, but the frozen base-URL set reads only source cells (`verifiers/check_agent_definitions.py:384-392`). The main snapshot differs from the pinned snapshot; no byte-identity claim is made for them. Its held path still gives G=0.

Smallest safe correction for mirror/alias provenance, if required before data: a pinned source-identity map for proven GitHub/raw counterparts and served-page aliases, rather than a second independently authoritative source id. Do not silently change the frozen rule or count a syntactic guard bypass as a full predicate success.

## World matrix

Every row was actually run with the frozen counter; every exit is 1. “URL guard” says only whether the lexical base-URL check rejects this fixture, not whether its quote is true or its fetch succeeds.

| World | Sandbox commit | Counter first-line values | URL guard | Frozen predicate |
|---|---|---|---|---|
| do-nothing-freeze | `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257` | 0 of 0; new ground 0 | — | exit 1; NOT MET |
| s026 | `1383721bfc709bc0a5a2338afb660b66a5cfe14b` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s026-md | `b65ef499615e799c9d40ad4dce57b90710024cf8` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s026-slash | `9e31972d09bbd5c14fdf4353626e6b204d37a23d` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s026-query | `fcd8d0022a6502f2b44a6d50614ca9cd83d36f8b` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s026-www | `8ffb60957621cf939101347f3cb69a74cf3479e6` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| s026-case | `770daebd9c53fe5f1b225297a2bbaef3594658d7` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| s026-upper-md | `0afd36c011701e4cf0d6a848c3c5e474fe82a602` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-held-new-page | `d6fc73ef997ec7abab4650f9d9cf3054df0f5cbd` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-case-flip | `85420cfd980f3835964443b998f480b95150f53e` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-home-prefix | `6702ad4de4c3ebe04799cfd6d03e58004d34d657` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-config-home | `f3167dbf15973ef04a2ee66e5810bc01d0e7fbcb` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-config-bare | `a27732fc99bc06def2374acc371af3a26783126b` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-singular-prefix | `75f2aa9ac1d7e2fd569a896653766e01fd6d6cfb` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| opencode-singular-with-slash | `921069ac0ae2ff4d7a403e2d27dbdc8c56b2f1d0` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| claude-held-glob-main-alias | `94dc89104d8394f1c81df7f977a8ff403f68ac82` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| claude-held-case-home-glob | `38fc0222d11dc1b4878c5d7d5498cb897407298d` | 1 of 1; new ground 0 | accepted | exit 1; NOT MET |
| s062-original-raw | `65533a2589b8f8fcaf20938428042f2b995bc092` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s062-github-mirror | `87af17f7b4471f9278e2895e152a5c45f97c7e6d` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| s016-original-github | `bc8ad9e7d2f268acc9e4b827a010d0dec94ba36e` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| s016-raw-mirror | `bbf7a64e3bf64cda96c1d59e5b07f03db1bf6586` | 0 of 1; new ground 0 | accepted | exit 1; NOT MET |
| codex-case-flip | `6939475cfbcc5e9a3ff96655bc7190aebd1e7358` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| codex-home-prefix | `106eb9d8302f651e0aa72db1a69bcd01b2b301c1` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| codex-home-glob | `84905090a5d7756e1058a4a2f620fdc8b85dcca6` | 0 of 1; new ground 0 | rejected | exit 1; NOT MET |
| non-dot-held-opencode-path | `4706b21546a9d02258ec5b056152413756f42b18` | 0 of 0; new ground 0 | accepted | exit 1; NOT MET |

## Source-access evidence and byte-exact quotes

All acquisition was ordinary curl with finite timeouts; no browser, captcha workaround or access-control bypass was used. Full URL, `date -u` output, HTTP status, byte count, digest, saved body and curl exit are in the plain-text receipt for each fetched URL. The following short excerpts preserve fetched markdown exactly; no markdown was stripped in recording them. The counter itself strips markdown during its documented normalization.

- `held-variant-evidence/s026-md.body:103`: "Create a personal code-improver subagent in ~/.claude/agents/ that scans"
- `held-variant-evidence/opencode-agents.body:718`: "Create a new agent by adding a markdown file to `.opencode/agents/` for the project or `~/.config/opencode/agents/` globally."
- `held-variant-evidence/s062-raw.body:7609` and `held-variant-evidence/s062-main.body:7691`: "Fixed custom agent `model` field in `.claude/agents/*.md` being ignored when spawning team teammates"

All three quotes are at most 25 words each. The singular-prefix fixture is deliberately truncated inside the path; it is NOT represented here as documentation of a singular directory. Fabricated Codex/control quotes are never represented as source facts.

Observed access-time lines:

```
Fri Oct 23 02:26:27 AM UTC 2026
Fri Oct 23 02:26:28 AM UTC 2026
Fri 23 Oct 2026 02:27:28 AM UTC
```

No client-silence claim was made, so this report does not pretend to be a Q30 changelog/docs-tree/corpus sweep. No tool was installed or updated. All run commands finished; no service or persistent process was started. Only this seat's report and receipt were written in the lane; world commits and fetched bytes remain solely in its sandbox. No counter fix, integration, push, delegated task, client model call, alternate judging runtime, build, lint or unrelated test was performed.
