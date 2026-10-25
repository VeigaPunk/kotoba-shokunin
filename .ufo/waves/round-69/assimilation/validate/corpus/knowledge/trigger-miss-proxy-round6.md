# Literal-trigger miss proxy & the always-on coverage hole

Sourced 2026-09-28 (round 6), L1-measured. Extends
`skill-activation-telemetry.md` — the round-5 join recipe applied to a first
fidelity measurement. Store: `~/.local/share/opencode/opencode.db` (sqlite,
readonly). Denominators: 398 sessions with user text, 415 `tool='skill'`
calls, 216 sessions with ≥1 load.

## Method

1. Per-session skill loads: `part` rows where `$.tool='skill'`, skill name at
   `$.state.input.name`.
2. Per-session user intent text: `part(type='text')` joined
   `message_id → message(role='user')`, then **cleaned**: slash-command
   tokens stripped (`/skill:godspeed`, `/ufo`, … — these are invocation
   verbs, not router intent) and injected directive blobs removed
   ("You are a Godspeed-enabled subagent …" appears verbatim in dispatched
   prompts and caused a 60-session false cluster for the token `ufo`).
3. Literal-trigger session = intent text contains a trigger token for skill
   X. Miss = trigger present, X never loaded in that session.

### Query recipe (re-runnable)

```sql
-- loads
select p.session_id, json_extract(p.data,'$.state.input.name')
from part p where json_extract(p.data,'$.tool')='skill';
-- intent text
select m.session_id, json_extract(p.data,'$.text') from part p
join message m on p.message_id=m.id
where json_extract(m.data,'$.role')='user' and json_extract(p.data,'$.type')='text';
```

## Measured results (cleaned intent text)

| Skill | Loaded (sess) | Literal-trigger sess | Misses | Miss rate |
|-------|--------------|---------------------|--------|-----------|
| wwkd (`wwkd`, `karpathy`) | 51 | 3 | 0 | 0% |
| ufo (`ufo`) | 47 | 13 | 5 | 38.5% |
| xbrd-ask (`xbrd-ask`, `xask`) | 8 | 1 | 1 | 100% |
| sekhmet-l3 (`sekhmet`, `xbrd-spark`) | 4 | 0 | — | n/a |
| omarchy (`omarchy`) | 4 | 0 | — | n/a |
| bailian family (`百炼`,`bailian`,`dashscope`) | 16 | 2 | 0 | 0% |
| godspeed (`godspeed`) | 205 | 18 | 5 | 27.8% |
| kimi-webbridge (`webbridge`) | 0 | 0 | — | n/a (no literal-intent sessions) |

## Read

- **Unique-token triggers work.** Skills whose trigger strings are
  domain-exclusive (wwkd, bailian terms, sekhmet) show 0 literal misses —
  when a user names the thing, it loads.
- **Ambiguous tokens produce apparent misses.** All 5 `ufo` misses are
  domain references, not invocations ("16 ufo-format agents", "ufo-sighting"
  tmux issue, "doesn't work with ufo"). The skill correctly did not fire —
  the misses say more about trigger-token ambiguity than router failure.
  `xask` similarly appeared inside a delegated prompt ("xask the-revenger…")
  where the parent already consumed the dispatch.
- **Always-on skills leak.** godspeed's description demands activation "on
  every prompt"; measured coverage is 205/398 = **51.5%** of sessions, and
  even sessions whose prompt says `| godspeed` or names the skill loaded it
  only ~72% of the time. Where godspeed did load, opencode.db often shows a
  slash-command or directive-driven route; the rest of the fleet relies on
  harness-side always-on injection (AGENTS.md godspeed banner) that isn't
  per-skill — the router's always-on verdicts aren't observable per prompt.
- **Phantom `customize-opencode`** (27 calls, no SKILL.md in surveyed roots)
  is confirmed in this window too — an activation source outside the file
  survey set.

## Limits — what this proxy cannot say

- **Implicit-intent fidelity is still unmeasured.** "帮我写个 prompt" carrying
  no literal token is invisible to this proxy; needs intent classification
  (labeling pass, future round).
- **Per-prompt ≠ per-session.** A session counts as hit if the skill loaded
  on *any* prompt; multi-prompt sessions blur attribution (398 sessions vs
  560 text parts — most sessions are single-prompt, so blur is bounded).
- **opencode.db ≠ omp.** The `| godspeed` dispatch fleets run under omp
  (`~/.omp/agent/sessions/*.jsonl`, 5609 files); this proxy measures the
  opencode-side store only. Cross-store dedupe is future work.
- **N/A ≠ healthy.** kimi-webbridge has zero literal-intent sessions —
  untested, not clean.

## Craft consequence (new rule candidate)

For skills whose name doubles as a domain term (ufo, omarchy), the literal
trigger surface must carry *invocation-shaped* triggers (`/ufo`, quoted
imperative contexts), not just the bare noun — otherwise both the router
*and* the measurement proxy cannot separate reference from intent.
