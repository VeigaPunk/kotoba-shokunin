Result: DONE — Codex’s documented instruction mechanism is directory-walk scoped, not a matching-file rule file; the fetched page is preserved as S104.page.

## Findings and gates

- W0’s `CensusCodex.md` classifies Codex as NOT ELIGIBLE: its `AGENTS.md` instruction chain follows directories, and `~/.codex/rules/` is command execpolicy rather than instruction scoping. This is a reviewer row, not a C1 measurement.
- Read `verifiers/check_scoped_rules.py` before drafting. Its frozen C1 rule requires a documented instruction rule file applying only to matching files; the Codex directory walk does not meet that condition. I did not run the counter or any build/test gate. The experimental execpolicy classification below is from the inspected W0 census report; this assignment’s fetch was the `agents-md.md` page only.
- Snapshot evidence: `.ufo/waves/round-60/snapshots/S104.page:12`. Quote is a contiguous, unshaped excerpt; inline-code marks and punctuation are retained.

### Fetch record

Exact executed sequence:

```sh
date -u; mkdir -p /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots; timeout 60 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' -w '\nHTTP %{http_code} %{url_effective}\n' -o /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page https://learn.chatgpt.com/docs/agent-configuration/agents-md.md; r=$?; printf 'curl_exit=%s\n' "$r"; wc -c /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page
```

Observed output:

```text
Fri 23 Oct 2026 12:08:21 PM UTC
HTTP 200 https://learn.chatgpt.com/docs/agent-configuration/agents-md.md
curl_exit=0
9149 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page
9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page
```

The saved file is the response body written by curl (`-o`); no response bytes were transformed. Curl exit status was 0; HTTP status was 200. The byte-count and hash commands printed the output above; their individual exit statuses were not captured.

### Quote evidence

Executed `sed -n '12p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-60/snapshots/S104.page`; output:

```text
2. **Project scope:** Starting at the project root (typically the Git root), Codex walks down to your current working directory. If Codex cannot find a project root, it only checks the current directory. In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`. Codex includes at most one file per directory.
```

Executed `printf '%s\n' 'In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`.' | wc -w`; output: `18`. The command’s individual exit status was not captured. This is the exact contiguous quote excerpt used below.

## Exact text for integration

### SOURCES.md row S104

```markdown
| S104 | OpenAI Learn — Custom instructions with AGENTS.md — https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | docs | A | Codex instruction-file discovery: global and project locations, project-root-to-current-directory walking, filename order and one file per directory (vendor documentation; not a runtime test) | § How Codex discovers guidance (`S104.page:9-15`); project directory walk (`S104.page:12`); fetched 2026-10-23T12:08:21Z, HTTP 200, 9,149 B, sha256 `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e`; exact bytes `.ufo/waves/round-60/snapshots/S104.page` | re-opens S044 — Codex walks from the project root to the current directory, checks AGENTS.override.md, AGENTS.md and fallback names at each directory, and includes at most one file per directory | mined | 2026-10-23 | 90d | corpus/knowledge/scoped-rules-round60.md |
```

The `re-opens S044 —` prefix is required because this is the S044 base URL. The row carries the full fetched SHA-256.

### Gate line for `corpus/lessons/round-60.md`

```markdown
- **S104 Codex** — https://learn.chatgpt.com/docs/agent-configuration/agents-md.md — accessed Fri 23 Oct 2026 12:08:21 PM UTC (HTTP 200, 9,149 bytes, sha256 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e) — `.ufo/waves/round-60/snapshots/S104.page:12`: "In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`."
```

### SKILL.md row

```markdown
| Codex | no scoped rule file: AGENTS.md instructions are discovered by directory walk (S104 :12) | none (the project-root-to-current-directory walk determines loaded instructions, S104 :12) | Use nested AGENTS.override.md/AGENTS.md for directory-specific instructions, not matching-file rules (S104 :12) |
```

The Rule files cell intentionally starts with plain text, not a backticked path token; this is a non-eligible reviewer row.

### Two-line entry note

```text
Codex is not eligible: AGENTS.override.md/AGENTS.md files are selected along the project-root-to-current-directory walk, not by matching-file pattern (S104 :12).
~/.codex/rules/ is a separate experimental command execpolicy, not instruction-file scoping (W0 census: .ufo/waves/round-60/w0/CensusCodex.md).
```

## Touched surfaces and limits

- Created only `.ufo/waves/round-60/snapshots/S104.page` from the fetched body and this report at `.ufo/waves/round-60/build/SrcCodex.md`.
- The proposed SOURCES row, Gate line, SKILL row, and entry note above are report text for the L1 integrator; I did not edit `corpus/SOURCES.md`, `corpus/lessons/round-60.md`, `corpus/knowledge/scoped-rules-round60.md`, or `SKILL.md`.
- No tools were installed. No counter, tests, build, or C1 measurement was run. The snapshot has a recorded HTTP status, byte count, and SHA-256; live-page suitability as an eligible C1 source is not claimed.
