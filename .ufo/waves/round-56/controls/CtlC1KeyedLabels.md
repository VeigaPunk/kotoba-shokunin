Result: DONE — All 20 sandbox controls were scored with the frozen C1 bytes; none met the predicate, although repeated paths and fenced structures pass the preliminary BACKED checks.

Seat: CtlC1KeyedLabels (critic). Assigned axes: depth (the C1 learning claim), provenance/identity consistency, and calibration (do not confuse BACKED with the live predicate). No admission or canonical judgment is made here.
Freeze: 0f58a469b0e3c4fcefaa11d2a01648b2e88cb257.
Sandbox: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels.
First recorded UTC: Fri 23 Oct 2026 02:25:36 AM UTC.
Plan read: plans/round-56.md:19-45,78-91. Counter docstring read first: verifiers/check_agent_definitions.py:2-107.
Observed command: timeout 10 sha256sum verifiers/check_agent_definitions.py
Observed output: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
Counter bytes were also hashed immediately before each recorded predicate run and required to equal that digest. Counter files were never changed. Every synthetic commit has the freeze commit as parent; git object/index writes occurred only in the sandbox.

Findings and smallest safe corrections

1. Repetition defeats the preliminary outside-path language check, but NOT the frozen live predicate in this control.
Counterexample: dd97b088794bc15f220b32c3c72834014cf603c4:corpus/knowledge/agent-definition-files-round56.md:5-11 contains only three repetitions of the path in each quote, e.g. ".control-0/agents .control-0/agents .control-0/agents". All occurrences of the word agents are inside paths. The counter reports all seven clients BACKED, then found=no: F=0, G=0, exit 1. The two-repetition control is rejected only for two words; the single-path three-word control is rejected for lacking an outside agent word.
Evidence: verifiers/check_agent_definitions.py:452-467,521-532 selects the first path span, then allows an agents word in the second path span. Frozen non-fetch JSON diagnostics also record backed=7 for the three-repetition world; those diagnostics always exit 1 and are not the predicate.
Impacted axes: depth, provenance/semantic calibration. Smallest safe correction, if the intended rule is a language word outside every path: exclude all path-token spans before searching for the agent word. This is a fixable preliminary-parser defect, not a demonstrated MET world; do not silently change the frozen counter or declare C1 broken from BACKED alone.

2. Fences are not a structural boundary for Gate, SKILL tables, or SOURCES rows.
Counterexample: 4be7085f0cfd4349c2ff2f72385cb6d5dceb9f42:corpus/lessons/round-56.md:3-13 puts the entire ## Gate heading and quotes inside a code fence. It still backs all seven clients. 64a4295e69b527b83f85c1392953c97abb9c69db puts the SKILL table inside a code block; db096746c193efdf092de35b8773506289cfc5be puts the SOURCES registry rows inside one. Each also backs all seven. Each declared --fetch run remains F=0, G=0, exit 1.
Evidence: verifiers/check_agent_definitions.py:271-316,343-351,617-627 has no fence state. Fixture bytes are saved under .control-evidence/<world>/<repo-path> in this sandbox.
Impacted axes: provenance/structural consistency and calibration. Smallest safe correction if rendered section/table identity is required: recognize headings/registry tables only outside fences, reusing the existing repository fence convention rather than inventing a competing grammar. A quote inside a code block under a real Gate still literally records that quote; a later real ## Gate is also a Gate. Those two requested controls are accepted structurally, but are not independently a skip-learning shortcut under the frozen wording. Do not relabel that tradeoff as a predicate break.

3. Tier/status/date labels do not override the parsed URL host; duplicate SKILL clients and aliases do not increase the count.
All six off-pin/lookalike/userinfo-before-@/pin-in-path worlds reject all seven rows specifically for the host. A/mined/2026-10-23 labels alone do not bypass this guard. Exact duplicate SKILL rows give K=0. VSCode and Copilot are not recognized as VS Code and Copilot CLI, so that world has K=5, backed=5 from the other five synthetic clients, not seven; changing every client name yields K=0. Duplicate entry rows are explicitly allowed by the implementation and its self-test, which selects a passing entry row; that is different from duplicate SKILL authority.
Evidence: verifiers/check_agent_definitions.py:262-264,395-408,535-556,576-607,859-865 and the per-world stdout below. No correction is justified by these off-pin/duplicate/alias results. Obtaining five genuine, correctly quoted documented locations for the remaining exact client names would do real C1 work, not create a shortcut; that line was stopped without doing it.

4. Host scope is initial parsed authority, not an assertion about every redirect destination.
The proper-subdomain control admits only the Cursor row at https://www.cursor.com/; this is consistent with the frozen host_ok descendant rule. In userinfo-offpin-at-pinned the actual parsed host is pinned, so it is not the inverse off-pin attack. Separate ordinary root reopens observed https://code.claude.com/ redirecting to https://claude.com/product/claude-code, a host not listed for Claude Code. This is a provenance-boundary observation, not a successful live quote/path world.
Evidence: verifiers/check_agent_definitions.py:395-408,691-705 checks the original URL and follows urllib redirects without inspecting the final host; direct source receipts below give the observed effective URLs. If the intended identity rule applies to the final source as well, the smallest correction is to check the final response URL against the same pins (only through a pre-data erratum). No off-host live-predicate success was observed here.

Limits: These are deliberately fabricated, non-admitted fixtures: seven distinct .control-N/agents forms; fabricated A/mined/opened labels; synthetic action text; and fake quotes. They skip all actual C1 learning. Every declared predicate run printed F=0 and G=0 and exited 1. Preliminary admission is not a measured claim success. No happy baseline of genuine new documentation was built because that would perform the real claim work, not the assigned shortcut control. Ordinary reopens below log their own fetched bytes; the frozen counter does not expose HTTP status, final URL or body hashes, so these are not represented as byte-identity logs of its separate requests. No client is claimed silent or to document nothing. No model calls, browser challenges, tool installations, counter edits, lane code execution, or lane git writes occurred. All started runs were finite and timeout-capped; the scoring runner completed and no service was started.

World construction: timeout 600 python3 -B .control-runner.py (sandbox cwd). It creates four synthetic document blobs per commit using an isolated sandbox index, retains every other frozen tree blob, scores each with timeout 180, and saves full output in .control-evidence/results.json. Additional --json without --fetch diagnostics use timeout 30 and are explicitly not predicate runs. No predicate run timed out or was left unrun.

Summary (name; BACKED diagnostic; declared predicate exit):
fresh-labels-off-pin; 0 of 7; exit 1; NOT MET
suffix-lookalike; 0 of 7; exit 1; NOT MET
dashed-prefix-lookalike; 0 of 7; exit 1; NOT MET
subdomain-suffix-lookalike; 0 of 7; exit 1; NOT MET
userinfo-pinned-at-offpin; 0 of 7; exit 1; NOT MET
pin-mentioned-only-in-path; 0 of 7; exit 1; NOT MET
duplicate-exact-skill-clients; 0 of 0; exit 1; NOT MET
duplicate-entry-clients; 7 of 7; exit 1; NOT MET
VSCode-Copilot-variants; 5 of 5; exit 1; NOT MET
all-client-name-variants; 0 of 0; exit 1; NOT MET
Gate-quotes-only-in-code-block; 7 of 7; exit 1; NOT MET
Gate-quotes-only-under-later-Gate; 7 of 7; exit 1; NOT MET
Gate-heading-and-quotes-inside-code-block; 7 of 7; exit 1; NOT MET
quote-three-repeated-paths; 7 of 7; exit 1; NOT MET
quote-two-repeated-paths; 0 of 7; exit 1; NOT MET
agent-word-only-in-single-path; 0 of 7; exit 1; NOT MET
SKILL-table-only-in-code-block; 7 of 7; exit 1; NOT MET
SOURCES-rows-only-in-code-block; 7 of 7; exit 1; NOT MET
userinfo-offpin-at-pinned; 7 of 7; exit 1; NOT MET
proper-subdomain-Cursor-only; 1 of 7; exit 1; NOT MET

Per-world frozen-predicate receipts (full stdout)

World: fresh-labels-off-pin
Sandbox commit hash: 891ac9d2a90d75e3654297e7eff8c55f62fc9a6a
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/fresh-labels-off-pin/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 891ac9d2a90d75e3654297e7eff8c55f62fc9a6a --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://example.invalid/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://example.invalid/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://example.invalid/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://example.invalid/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://example.invalid/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://example.invalid/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://example.invalid/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 891ac9d2a90d75e3654297e7eff8c55f62fc9a6a --json; exit 1

World: suffix-lookalike
Sandbox commit hash: c2c75e2936d38afee975c3cce23f3a3b12b08e47
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/suffix-lookalike/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev c2c75e2936d38afee975c3cce23f3a3b12b08e47 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://code.claude.com.evil.invalid/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://developers.openai.com.evil.invalid/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://code.visualstudio.com.evil.invalid/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://docs.github.com.evil.invalid/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://geminicli.com.evil.invalid/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://cursor.com.evil.invalid/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://opencode.ai.evil.invalid/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev c2c75e2936d38afee975c3cce23f3a3b12b08e47 --json; exit 1

World: dashed-prefix-lookalike
Sandbox commit hash: fbac27067abfa3882bd3f761d38eb07ca330a2cc
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/dashed-prefix-lookalike/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev fbac27067abfa3882bd3f761d38eb07ca330a2cc --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://evil-code.claude.com/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://evil-developers.openai.com/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://evil-code.visualstudio.com/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://evil-docs.github.com/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://evil-geminicli.com/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://evil-cursor.com/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://evil-opencode.ai/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev fbac27067abfa3882bd3f761d38eb07ca330a2cc --json; exit 1

World: subdomain-suffix-lookalike
Sandbox commit hash: 0639955e0ec057856f542dc952e0e45f6297e158
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/subdomain-suffix-lookalike/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 0639955e0ec057856f542dc952e0e45f6297e158 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://docs.code.claude.com.evil.invalid/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://docs.developers.openai.com.evil.invalid/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://docs.code.visualstudio.com.evil.invalid/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://docs.docs.github.com.evil.invalid/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://docs.geminicli.com.evil.invalid/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://docs.cursor.com.evil.invalid/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://docs.opencode.ai.evil.invalid/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 0639955e0ec057856f542dc952e0e45f6297e158 --json; exit 1

World: userinfo-pinned-at-offpin
Sandbox commit hash: 1d50d4d554c19aa247b89ad3617f28b2908348be
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/userinfo-pinned-at-offpin/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 1d50d4d554c19aa247b89ad3617f28b2908348be --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://code.claude.com@example.invalid/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://developers.openai.com@example.invalid/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://code.visualstudio.com@example.invalid/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://docs.github.com@example.invalid/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://geminicli.com@example.invalid/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://cursor.com@example.invalid/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://opencode.ai@example.invalid/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 1d50d4d554c19aa247b89ad3617f28b2908348be --json; exit 1

World: pin-mentioned-only-in-path
Sandbox commit hash: 972b105fcce8c488390b05425e271bad2c298111
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/pin-mentioned-only-in-path/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 972b105fcce8c488390b05425e271bad2c298111 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://example.invalid/code.claude.com/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://example.invalid/developers.openai.com/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://example.invalid/code.visualstudio.com/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://example.invalid/docs.github.com/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://example.invalid/geminicli.com/control' is not on a pinned host
Cursor       no     entry row S905: S905 URL 'https://example.invalid/cursor.com/control' is not on a pinned host
opencode     no     entry row S906: S906 URL 'https://example.invalid/opencode.ai/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 972b105fcce8c488390b05425e271bad2c298111 --json; exit 1

World: duplicate-exact-skill-clients
Sandbox commit hash: 340162686ea27837110a440cc21570d88973608c
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/duplicate-exact-skill-clients/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 340162686ea27837110a440cc21570d88973608c --fetch
Full stdout:
agent-definition locations found on the live page 0 of 0; new ground 0
Claude Code  no     SKILL.md rows naming client: 2 (need exactly 1)
Codex        no     SKILL.md rows naming client: 2 (need exactly 1)
VS Code      no     SKILL.md rows naming client: 2 (need exactly 1)
Copilot CLI  no     SKILL.md rows naming client: 2 (need exactly 1)
Gemini CLI   no     SKILL.md rows naming client: 2 (need exactly 1)
Cursor       no     SKILL.md rows naming client: 2 (need exactly 1)
opencode     no     SKILL.md rows naming client: 2 (need exactly 1)
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 0; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 340162686ea27837110a440cc21570d88973608c --json; exit 1

World: duplicate-entry-clients
Sandbox commit hash: f238a03e8836bb00bd85af4aaac2b03df17fd293
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/duplicate-entry-clients/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev f238a03e8836bb00bd85af4aaac2b03df17fd293 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev f238a03e8836bb00bd85af4aaac2b03df17fd293 --json; exit 1

World: VSCode-Copilot-variants
Sandbox commit hash: ed7d545483eb711cf9a7efd3c657647feca23356
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/VSCode-Copilot-variants/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev ed7d545483eb711cf9a7efd3c657647feca23356 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 5; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 5 of 5; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev ed7d545483eb711cf9a7efd3c657647feca23356 --json; exit 1

World: all-client-name-variants
Sandbox commit hash: 3a3575e58b22549971e77ce6d46c143f4db66b0e
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/all-client-name-variants/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 3a3575e58b22549971e77ce6d46c143f4db66b0e --fetch
Full stdout:
agent-definition locations found on the live page 0 of 0; new ground 0
Claude Code  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Codex        no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
VS Code      no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 0; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 3a3575e58b22549971e77ce6d46c143f4db66b0e --json; exit 1

World: Gate-quotes-only-in-code-block
Sandbox commit hash: c37bf67badab978696ff8e1be638444c2fd6956a
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/Gate-quotes-only-in-code-block/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev c37bf67badab978696ff8e1be638444c2fd6956a --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev c37bf67badab978696ff8e1be638444c2fd6956a --json; exit 1

World: Gate-quotes-only-under-later-Gate
Sandbox commit hash: 26765e533bc32719bb608f0495278d97ddac6883
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/Gate-quotes-only-under-later-Gate/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 26765e533bc32719bb608f0495278d97ddac6883 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 26765e533bc32719bb608f0495278d97ddac6883 --json; exit 1

World: Gate-heading-and-quotes-inside-code-block
Sandbox commit hash: 4be7085f0cfd4349c2ff2f72385cb6d5dceb9f42
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/Gate-heading-and-quotes-inside-code-block/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 4be7085f0cfd4349c2ff2f72385cb6d5dceb9f42 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 4be7085f0cfd4349c2ff2f72385cb6d5dceb9f42 --json; exit 1

World: quote-three-repeated-paths
Sandbox commit hash: dd97b088794bc15f220b32c3c72834014cf603c4
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/quote-three-repeated-paths/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev dd97b088794bc15f220b32c3c72834014cf603c4 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev dd97b088794bc15f220b32c3c72834014cf603c4 --json; exit 1

World: quote-two-repeated-paths
Sandbox commit hash: 0872933fb920be7db74ab0582f3f1d38dfd60d31
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/quote-two-repeated-paths/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 0872933fb920be7db74ab0582f3f1d38dfd60d31 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: quote holds 2 words (need 3-25)
Codex        no     entry row S901: quote holds 2 words (need 3-25)
VS Code      no     entry row S902: quote holds 2 words (need 3-25)
Copilot CLI  no     entry row S903: quote holds 2 words (need 3-25)
Gemini CLI   no     entry row S904: quote holds 2 words (need 3-25)
Cursor       no     entry row S905: quote holds 2 words (need 3-25)
opencode     no     entry row S906: quote holds 2 words (need 3-25)
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 0872933fb920be7db74ab0582f3f1d38dfd60d31 --json; exit 1

World: agent-word-only-in-single-path
Sandbox commit hash: 4a21947ccbb7543453caff6ef85649ff0be894a3
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/agent-word-only-in-single-path/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 4a21947ccbb7543453caff6ef85649ff0be894a3 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: quote holds no agent word outside the path token
Codex        no     entry row S901: quote holds no agent word outside the path token
VS Code      no     entry row S902: quote holds no agent word outside the path token
Copilot CLI  no     entry row S903: quote holds no agent word outside the path token
Gemini CLI   no     entry row S904: quote holds no agent word outside the path token
Cursor       no     entry row S905: quote holds no agent word outside the path token
opencode     no     entry row S906: quote holds no agent word outside the path token
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 0 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 4a21947ccbb7543453caff6ef85649ff0be894a3 --json; exit 1

World: SKILL-table-only-in-code-block
Sandbox commit hash: 64a4295e69b527b83f85c1392953c97abb9c69db
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/SKILL-table-only-in-code-block/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 64a4295e69b527b83f85c1392953c97abb9c69db --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 64a4295e69b527b83f85c1392953c97abb9c69db --json; exit 1

World: SOURCES-rows-only-in-code-block
Sandbox commit hash: db096746c193efdf092de35b8773506289cfc5be
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/SOURCES-rows-only-in-code-block/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev db096746c193efdf092de35b8773506289cfc5be --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev db096746c193efdf092de35b8773506289cfc5be --json; exit 1

World: userinfo-offpin-at-pinned
Sandbox commit hash: 04f10ed3ed456198a64ab23834567fddfc1448a3
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/userinfo-offpin-at-pinned/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev 04f10ed3ed456198a64ab23834567fddfc1448a3 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  BACKED token=.control-0/agents norm=.control-0/agents found=no
Codex        BACKED token=.control-1/agents norm=.control-1/agents found=no
VS Code      BACKED token=.control-2/agents norm=.control-2/agents found=no
Copilot CLI  BACKED token=.control-3/agents norm=.control-3/agents found=no
Gemini CLI   BACKED token=.control-4/agents norm=.control-4/agents found=no
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     BACKED token=.control-6/agents norm=.control-6/agents found=no
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 7 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev 04f10ed3ed456198a64ab23834567fddfc1448a3 --json; exit 1

World: proper-subdomain-Cursor-only
Sandbox commit hash: c037120960e658059b67d043b8577a31741f7e63
Fixture bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/proper-subdomain-Cursor-only/
sha256sum of counter bytes run: 1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py
cwd: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels
Command: timeout 180 python3 -B verifiers/check_agent_definitions.py --rev c037120960e658059b67d043b8577a31741f7e63 --fetch
Full stdout:
agent-definition locations found on the live page 0 of 7; new ground 0
Claude Code  no     entry row S900: S900 URL 'https://example.invalid/control' is not on a pinned host
Codex        no     entry row S901: S901 URL 'https://example.invalid/control' is not on a pinned host
VS Code      no     entry row S902: S902 URL 'https://example.invalid/control' is not on a pinned host
Copilot CLI  no     entry row S903: S903 URL 'https://example.invalid/control' is not on a pinned host
Gemini CLI   no     entry row S904: S904 URL 'https://example.invalid/control' is not on a pinned host
Cursor       BACKED token=.control-5/agents norm=.control-5/agents found=no
opencode     no     entry row S906: S906 URL 'https://example.invalid/control' is not on a pinned host
Full stderr: (empty)
exit 1
C1 predicate: --fetch exit 0 (F>=5, G>=2) — NOT MET
Separate non-predicate diagnostic: BACKED 1 of 7; timeout 30 python3 -B verifiers/check_agent_definitions.py --rev c037120960e658059b67d043b8577a31741f7e63 --json; exit 1

Ordinary direct-source access receipts
These are independent curl reopens, not quoted authorities for any learning claim. No external source text is quoted or markdown-stripped here. Off-pin .invalid URLs rejected before backing are not opened. The userinfo decoy after the scheme is recorded in the URL exactly as tested.
Root-fetch command template: timeout 25 curl --location --silent --show-error --max-time 20 --output <body_path> --write-out %{json} <URL>. Each access records a separate timeout 5 date -u observation. Byte digests hash the saved response body.

URL: https://code.claude.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://claude.com/product/claude-code
Byte count: 630032
sha256: 8690e9fbd35a48b4c8a5ea01332872e98c8f0c8a7e98731906b3d42182919420
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-550631f98ba3.bytes
curl exit 0
stderr: (empty)

URL: https://code.visualstudio.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://code.visualstudio.com/
Byte count: 248475
sha256: 72448e59abc99f0d39e0f08b02b2fa8be4fd6df700e25738e8053d48850f1491
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-177f0934751b.bytes
curl exit 0
stderr: (empty)

URL: https://cursor.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://cursor.com/
Byte count: 620134
sha256: 769fec0fe7e1cd7e9d7ad9212c66e2dbc75050b4f2b5ca85ba1a89845569c9db
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-bbba856f6f33.bytes
curl exit 0
stderr: (empty)

URL: https://developers.openai.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://developers.openai.com/
Byte count: 360318
sha256: a872fa96e67ae8ed8f24c75676e2928ab5a64508a4f9fe3ed4406e27a8fa5773
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-3183bfc53aaf.bytes
curl exit 0
stderr: (empty)

URL: https://docs.github.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://docs.github.com/en
Byte count: 56682
sha256: e836d79f33a20dc43ad83a4bd35e50605636f8a920fa9d8abd64561c709a817d
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-a5e87fdc2aae.bytes
curl exit 0
stderr: (empty)

URL: https://geminicli.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://geminicli.com/
Byte count: 27739
sha256: 09a20609698c50e33b03cb0175585bcd27586a4f2695ab12101b47c64800797b
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-0141b617730f.bytes
curl exit 0
stderr: (empty)

URL: https://opencode.ai/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://opencode.ai/
Byte count: 70370
sha256: 4a574450fb4c99fc274bfbeb42129d4060618db951e63ba1e95910ae229fb724
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-d4108b708f72.bytes
curl exit 0
stderr: (empty)

URL: https://www.cursor.com/
date -u: Fri Oct 23 02:28:09 AM UTC 2026
HTTP status: 200
Effective URL: https://cursor.com/
Byte count: 620134
sha256: 769fec0fe7e1cd7e9d7ad9212c66e2dbc75050b4f2b5ca85ba1a89845569c9db
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-abf0e5309a4f.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@code.claude.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://claude.com/product/claude-code
Byte count: 630032
sha256: 311379e6c9015c2176a017fef84a13cbe1aa25f49006ca84d0fe4a21d5f19272
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-0.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@developers.openai.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://developers.openai.com/
Byte count: 360318
sha256: a872fa96e67ae8ed8f24c75676e2928ab5a64508a4f9fe3ed4406e27a8fa5773
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-1.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@code.visualstudio.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://code.visualstudio.com/
Byte count: 248475
sha256: 72448e59abc99f0d39e0f08b02b2fa8be4fd6df700e25738e8053d48850f1491
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-2.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@docs.github.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://docs.github.com/en
Byte count: 56682
sha256: e836d79f33a20dc43ad83a4bd35e50605636f8a920fa9d8abd64561c709a817d
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-3.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@geminicli.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://geminicli.com/
Byte count: 27739
sha256: 09a20609698c50e33b03cb0175585bcd27586a4f2695ab12101b47c64800797b
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-4.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@cursor.com/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://cursor.com/
Byte count: 620134
sha256: 769fec0fe7e1cd7e9d7ad9212c66e2dbc75050b4f2b5ca85ba1a89845569c9db
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-5.bytes
curl exit 0
stderr: (empty)

URL: https://example.invalid@opencode.ai/
date -u: Fri Oct 23 02:29:48 AM UTC 2026
HTTP status: 200
Effective URL: https://opencode.ai/
Byte count: 70370
sha256: 4a574450fb4c99fc274bfbeb42129d4060618db951e63ba1e95910ae229fb724
Saved bytes: /fast/scratch/hyaku/kotoba-r56/CtlC1KeyedLabels/.control-evidence/source-userinfo-6.bytes
curl exit 0
stderr: (empty)

Tool installs/updates: none.
Report: .ufo/waves/round-56/controls/CtlC1KeyedLabels.md
