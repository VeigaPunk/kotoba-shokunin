Result: HOLDS — the C1 v2 predicate (`--fetch` exit 0, F>=4, G>=2) re-runs true at the tip `f0e6b695` (`found on the live page 5 of 5; new ground 4`, exit 0), the v2 counter is confirmed strictly stricter than v1 at the tip (backed set {Claude Code, Codex, Copilot CLI, Cursor, opencode} ⊂ all 7 under v1), and every counted quote was re-verified verbatim on its live page with byte counts and sha256 matching the SOURCES receipts; two disclosed narrowness observations noted, no defect found.

Seat: W2RerunC1. Sandbox: `/fast/scratch/hyaku/kotoba-r55/W2RerunC1`, cloned 2026-10-23T00:09:24Z, checked out `f0e6b695b746775823b65a8c45de7d50ea33e84f`. Counter bytes used: `verifiers/check_explicit_invocation.py` (v2) at the tip, sha256 `e13eb88d8cfc32fc8975968280aa5a0055416fb07e43facbf1f585d951787e5a`; v1 bytes `git show a10240c0:verifiers/check_explicit_invocation.py > verifiers/cei_v1.py`, sha256 `4fc6e01ad576531c95265c7dcd2440b0b2bda0cd3520a0b317c46cd78b3ff5e5` (540 lines). All runs from the sandbox clone root; `date -u` printed by the shell immediately before and after each run.

## 1. v2 counter (`--fetch`) at the five revisions — verbatim output

### f0e5de82 (base)
`Fri 23 Oct 2026 12:11:32 AM UTC` / `Fri 23 Oct 2026 12:11:33 AM UTC`, `python3 -B verifiers/check_explicit_invocation.py --rev f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c --fetch`, exit 1:
```
Claude Code  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Codex        no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
VS Code      no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Copilot CLI  no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Gemini CLI   no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
Cursor       no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
opencode     no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)
user-typed invocation forms found on the live page 0 of 0; new ground 0
```
Matches the v2 control receipt (`C1-v2-controls.txt`: base → `0 of 0`, exit 1).

### a10240c0 (plan)
`Fri 23 Oct 2026 12:11:32 AM UTC` / `12:11:33`, `--rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c0 --fetch`, exit 1:
```
(seven identical "no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)" lines)
user-typed invocation forms found on the live page 0 of 0; new ground 0
```

### b04a9005 (erratum 1, counter v2 commit)
`Fri 23 Oct 2026 12:11:32 AM UTC` / `12:11:33`, `--rev b04a9005 --fetch`, exit 1:
```
(seven identical "no SKILL.md rows naming client: 0 (need 1); entry rows naming client: 0 (need 1)" lines)
user-typed invocation forms found on the live page 0 of 0; new ground 0
```
The counter bytes at `b04a9005` are identical to the tip (`git show` of both → sha256 `e13eb88d…`); the 0-of-0 here scores pre-content revisions, not a counter defect.

### 96155796 (C1 content)
`Fri 23 Oct 2026 12:11:32 AM UTC` / `12:11:33`, `--rev 96155796 --fetch`, exit 0:
```
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
```

### f0e6b695 (tip) — the declared predicate
`Fri 23 Oct 2026 12:11:32 AM UTC` / `12:11:33`, `--rev f0e6b695b746775823b65a8c45de7d50ea33e84f --fetch`, exit 0:
```
Claude Code  BACKED token=/skill-name new=False found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      no quote does not contain the word skill
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   no SKILL.md form cell has no backticked invocation token
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
user-typed invocation forms found on the live page 5 of 5; new ground 4
```
Predicate check: F=5 ≥ 4 and G=4 ≥ 2 → exit 0. **C1 predicate HOLDS at the tip.** The identical result at `96155796` is explained by `git diff 96155796 f0e6b695 -- corpus/lessons/round-55.md SKILL.md corpus/SOURCES.md corpus/knowledge/explicit-invocation-round55.md`: only the lesson changed (+34 lines: Rejected, Mistakes, routed-defect sections); the Gate quotes the counter reads were not touched [INFERENCE: identical output is consistent with that diff].

## 2. v1 counter (`--fetch`) at 96155796 and f0e6b695 — verbatim output

Both runs (`Fri 23 Oct 2026 12:12:41 AM UTC` / `12:12:42`), `python3 -B verifiers/cei_v1.py --rev <rev> --fetch`, identical output, exit 0:
```
Claude Code  BACKED token=/skill-name new=True found=True
Codex        BACKED token=$setup-demo-app new=True found=True
VS Code      BACKED token=/webapp-testing new=True found=True
Copilot CLI  BACKED token=/frontend-design new=True found=True
Gemini CLI   BACKED token=activate_skill new=True found=True
Cursor       BACKED token=/skill-name new=True found=True
opencode     BACKED token=@skill-id new=True found=True
explicit invocation forms found on the live page 7 of 7; new ground 7
```

## 3. Erratum claim: v2 strictly stricter than v1 — VERIFIED (rule inspection + observed behavior)

Docstring v2 line 79-80: "v2 is strictly stricter than v1: every client it backs, v1 also backs; every rule below only adds a failure condition."

- **Observed at the tip**: backed(v2) = {Claude Code, Codex, Copilot CLI, Cursor, opencode} ⊂ backed(v1) = all 7. VS Code dropped by the quote-needs-`skill` rule; Gemini CLI dropped because `activate_skill` fails v2's user-typed TOKEN_RE. Inclusion is strict, not just ⊆.
- **Rule inspection** (`diff verifiers/cei_v1.py verifiers/check_explicit_invocation.py`): every difference adds a rejection, none relaxes one — TOKEN_RE narrowed to `/` `$` `@` sigils, one segment, `[A-Za-z0-9<>_-]` after the head char (v1 allowed `#`, `.*`, and bare `_` tool names); BUILTINS exclusion added; quote must contain `skill`; page normalisation strips style/script/comments (and keeps `<letter` tags only); `new_ground` case-folds and adds the base-URL exclusion; `ground` counted per distinct case-folded token (v1 summed per client). Backed(v2) ⊆ backed(v1) holds by construction: every v2 condition is a v1 condition plus more.
- **New-ground direction verified**: Claude Code's `/skill-name` flips new=True (v1) → new=False (v2) because its row URL `code.claude.com/docs/en/skills.md` normalises to a key already held by base rows S022/S053 (base SOURCES lines 35, 66); the four True clients' URLs are absent at base (base grep exit 1 for `cursor.com/docs/skills`, `developers.openai.com/blog/eval-skills`, the Copilot how-to URL, the anomalyco/opencode raw URL, the gemini tutorial URL). v1's ground 7 vs v2's 4 is the per-client sum vs distinct-token-and-URL rule working as the erratum describes.

## 4. Independent live-page verification (falsify: the `found=True` values are real)

Independent `curl` fetch 2026-10-23T00:15:49–50Z, all HTTP 200; byte counts and sha256 equal the SOURCES row receipts exactly (all five pages byte-stable since the seats fetched them):

| client | URL | HTTP | bytes | sha256 | quote verbatim at |
|---|---|---|---|---|---|
| Claude Code | `https://code.claude.com/docs/en/skills.md` | 200 | 112,748 | `909dd50a…c737` | line 547 |
| Codex | `https://developers.openai.com/blog/eval-skills.md` | 200 | 19,356 | `6cf414bb…3a2` | line 148 (inside a `codex exec` prompt string) |
| Copilot CLI | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md` | 200 | 10,057 | `989af498…1a0` | line 128 |
| Cursor | `https://cursor.com/docs/skills.md` | 200 | 18,477 | `a642fa96…602d` | line 175 |
| opencode | `https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx` | 200 | 9,187 | `931b5425…7b` | line 201 |

Each `grep -nF` of the entry quote against the fetched bytes matched (exit 0) at the line the SOURCES row cites; quotes are byte-exact (opencode's entry notes it strips the backticks around `@skill-id`, matching the counter's normalisation).

## 5. Supporting checks

- Could-not-evaluate path: `--rev 1111111111111111111111111111111111111111 --fetch` → `could-not-evaluate: revision '1111…' is not a commit`, **exit 2** (2026-10-23T00:16:30Z).
- Self-tests (2026-10-23T00:17:36Z): v2 `self-test: 0 failure(s) over 44 assertions` exit 0; v1 `0 failure(s) over 29 assertions` exit 0.
- Counter frozen: `git diff --stat b04a9005 f0e6b695 -- verifiers/check_explicit_invocation.py` empty; both `git show` sha256 `e13eb88d…`.
- The summary-line denominator is `len(backed)`, so `found on the live page 5 of 5` does not claim all seven clients; the two misses print above it — no saturation inflation.
- Run wall time ~1.1 s for fetch runs is plausible: the five pages total ~160 KB of markdown over warm connections (independent curl of all five took ~1 s).

## 6. Observations (disclosed by the work; not counter defects; nothing new routed)

1. **Margin is 5, not 6.** The entry claims six clients document user-typed forms, but VS Code's counted-row quote (`agent-skills.md:287`) holds the token without the word `skill`, so v2 rejects it while v1 backed it. The lesson's Rejected table already records this ("admitted as S067, but the v2 counter does not count it"), so it is disclosed; the claim still passes because F=5 ≥ 4, with no headroom for a second loss.
2. **Claude Code is backed on a base page.** S065 is a new row id but its URL equals base rows S022/S053 (`code.claude.com/docs/en/skills`), so it cannot be new ground under either counter; the `S###`-not-at-base rule the claim states is satisfied (S065 absent at base; base grep found only S022/S053 on that URL). Ground margin is 4 vs the 2 minimum because Codex, Copilot CLI, Cursor and opencode sit on genuinely new URLs.

Tooling: no installs. Verdict: **C1 numbers and the erratum strictness claim hold at the tip; predicate verified end-to-end including live pages.**
