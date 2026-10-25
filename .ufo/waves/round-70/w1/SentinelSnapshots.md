# SentinelSnapshots — round 70 wave 1 security/hygiene review

**Verdict: CLEAN — no findings at any severity.** Base `7d51253f`, tip `16b212a3`. I did not modify any committed lane file. I made a scratch directory, `/tmp/k70w1-SentinelSnapshots.lf3b`, and deleted it before returning. I installed no tools.

Axes: credential/secret exposure, private/session/tracking URLs, pin integrity (sha256), oversized files.

## 1. Snapshot sha256 matches the pins in `verifiers/check_skill_evals.py` SNAPSHOTS (lines 46–57)

Command: `sha256sum .ufo/waves/round-70/snapshots/*` (working tree), plus `git show 16b212a3:.ufo/waves/round-70/snapshots/$f | sha256sum` (the committed blob, which is what the verifier hashes at line 95):

| file | working tree = tip blob | pin |
|---|---|---|
| S209-evaluating-skills.md (16973 B) | a799805f…fb684 | a799805f…fb684 ✔ |
| S210-optimizing-descriptions.md (13403 B) | 7cc54fbb…bd837 | 7cc54fbb…bd837 ✔ |
| S211-run_eval.py.txt (11464 B) | 43e3b8f8…8657f | 43e3b8f8…8657f ✔ |

- `git diff --stat 16b212a3 -- .ufo/waves/round-70/snapshots/` printed nothing, so the working tree has no drift from the tip.
- Provenance: the snapshots and the three pin lines both come from the same commit, `53de0ac` ("frozen plan, two counters … pinned source snapshots"). This is the freeze commit, shown by `git log $B..$R -- .ufo/waves/round-70/snapshots/` and by `git log -L46,58:verifiers/check_skill_evals.py`. No later commit touches either.
- Live upstream cross-check: `curl -fsSL --max-time 30 <url> | sha256sum` on all three pinned URLs returned byte-identical hashes today: a799805f…, 7cc54fbb…, 43e3b8f8…. S211's URL is commit-pinned (`anthropics/skills/dbd4588f…/skills/skill-creator/scripts/run_eval.py`), so it cannot change upstream.
- Modes are `100644` for all three (`git ls-tree`). S211 is stored as `.txt` and is not executable.

## 2. Snapshot content: credentials, private/session URLs, tracking tokens

- URL inventory (`rg -o 'https?://…' snapshots/`) found 10 URLs. All are public docs: `agentskills.io/llms.txt`, `agentskills.io/specification.md#…`, `agentskills.io/skill-creation/{evaluating-skills,using-scripts}.md`, `github.com/anthropics/skills/tree/main/skills/skill-creator`, and `platform.claude.com/docs/en/agent-sdk/typescript#sdk-task-notification-message`. None carries a query string, signature, session id or `utm_`.
- Secret regex over the snapshots (`token|secret|op://|bearer|api[_-]?key|password|sk-…|ghp_|github_pat_|xox[bap]-|AKIA…|BEGIN … PRIVATE|utm_|[?&](sig|signature|X-Amz|key|auth|session|sid)=`) matched only S209 lines 68, 116, 120, 127, 226, 231, 236, 242 and 256. Every hit is an LLM *token count* in prose or example JSON (e.g. `"total_tokens": 84852`). These are false positives.
- `rg '/home/|/Users/|<email>|localhost|127.0.0.1' snapshots/` returned NONE, so there are no local paths, emails or hosts.
- All three files are valid UTF-8 (`iconv`) with no CR characters.
- Note (not a defect): S211:83 forwards `os.environ` minus `CLAUDECODE` to a `claude` subprocess. That is upstream code kept as inert data, and the lane never executes it.

## 3. `git diff 7d51253f..16b212a3 --stat`: size and secret-shaped strings

- 42 files, +3447/−87. `git diff --numstat | awk '$1=="-"'` printed nothing, so there are no binaries.
- Sizes from `git cat-file -s <tip>:<path>` for every changed path: the largest is `LOG.md` at 552,839 B, followed by `SCORECARD.md` at 197,225 B and `corpus/SOURCES.md` / the validate copy at 147,827 B. **Nothing exceeds 1 MiB (1,048,576 B).**
- I scanned the requested pattern `rg -i 'token|secret|op://|bearer'` over the 3040 added lines (from `git diff -U0`). There were 36 hits, all in prose: census-token and citation-token rules, `skills.max_context_tokens`, "(5 tokens)" quote lengths, LOG token-resolution lines, plus the nine S209 hits above. None has a secret value.
- I also ran a strict credential-shape regex (`sk-[ant-]…{20,}`, `ghp_`, `github_pat_`, `gho_`, `xox?-`, `AKIA…`, `AIza…`, PEM private key, `Bearer <16+ chars>`, `op://\S+`, JWT `eyJ….….`, `(api_key|secret|password|token)\s*[:=]\s*<12+ chars>`). It matched 2 lines, both false positives:
  - `validate/corpus/README.md` (diff line 668) mentions "the `op://`-literal rule with no placeholder exception". This is a prose reference to a policy and contains no 1Password item reference.
  - S209:127 matches only because the docs URL is next to `` `total_tokens` ``.
- No URL with a query string appears anywhere in the added lines (`rg -o 'https?://…\?…'` returned nothing).

## Smallest remediation

None required.
