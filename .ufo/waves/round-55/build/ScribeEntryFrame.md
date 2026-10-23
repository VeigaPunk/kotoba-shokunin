Result: DONE — drafted the requested C1 entry frame and Round 55 Frontier note as report text for L1 integration; no lane product file was changed.

## Behavior and gates

This seat supplies the frame, not the per-client evidence or final C1 verdict. The proposed entry says why explicitly invoked turns must be separated from an implicit-trigger measure, and bounds the counter to the checks and output documented by the frozen instrument. No gate, test, self-test, source fetch, or shell command was run. The recheck command below is proposed text, not an execution result.

The frozen predicate is `python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch`; the plan states exit 0 iff the output has F ≥ 4 and G ≥ 2. The counter documentation specifies that it checks sourced table records and live-page quote presence, and does not judge whether a form is actually explicit invocation or test client behaviour (plan `plans/round-55.md:18-41`; counter `verifiers/check_explicit_invocation.py:20-68,298-368,528-536`). No predicate result is claimed here.

## Draft entry text

```markdown
# Explicit invocation by client (round 55)

The Frontier row *Implicit-intent fidelity* (`../README.md` § Frontier) concerns whether a skill activates implicitly when the user's request does not name it. A turn on which the user explicitly invokes a skill must be set aside from an implicit-trigger measure; otherwise a deliberate invocation is counted alongside activations attributed to implicit intent. This entry frames a source-backed inventory of client-documented invocation forms for that separation. It does not measure which turns were explicit or how clients behave.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|

## Findings

1. **Client forms and their documentation.**
2. **Use of the forms in separating explicit turns from implicit-intent measurement.**

## Limits

The counter does not judge whether a form is truly an explicit invocation rather than a listing or management command; that is reviewer reading. It does not check client behaviour, and it covers only Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, Cursor, and opencode.

recheck: python3 -B verifiers/check_explicit_invocation.py --rev <rev> --fetch
```

The `## Per-client record` header is exactly the counter's required header; the table contains no client rows, as assigned. The findings are headings for L1's evidence-led completion, not results asserted by this seat.

## Draft README Frontier append-only note

```markdown
**Round 55 (append-only note on the Implicit-intent fidelity row):** *Implicit-intent fidelity* — the C1 `--fetch` counter reports `explicit invocation forms found on the live page F of K; new ground G` (`python3 -B ../verifiers/check_explicit_invocation.py --rev <rev> --fetch`). This records the counter's live-page count among backed client records and its new-ground count; it does not measure implicit intent, classify individual user turns, test client behaviour, or cover clients beyond the seven.
```

This describes the counter's output shape, not a measured F/K/G result. It does not claim that any client is silent or that the frontier is held.

## Provenance and limits

Read-only basis: `plans/round-55.md:18-41`; template `corpus/knowledge/skill-listing-thresholds-round54.md:1-14,36-39,60-67`; `corpus/QUALITY.md:23-25,37,41-42`; `corpus/README.md:87-98,120-125`; and `verifiers/check_explicit_invocation.py:20-68,298-368,528-536`. Q12 calls for an opening `source:` with S### plus URL/anchor and `verified-at:`. Those cannot be supplied from this frame without the source seats' actual row identifiers, anchors, and access records; L1 must add them from those records rather than use guessed values. No external source was fetched, so there is no access timestamp, HTTP status, byte count, or fetched-content hash to report. No negative source claim was made, so no Q30 silence sweep is claimed. No numeric count claim was added, so Q13 count prose is not introduced.

## Touched surfaces and out of scope

Only this report file was written: `.ufo/waves/round-55/build/ScribeEntryFrame.md`. `corpus/knowledge/explicit-invocation-round55.md` and `corpus/README.md` were read, not edited; both proposed texts are reproduced above for L1 integration. No source research, per-client rows, SKILL.md table, lesson/SOURCES entry, verifier change, C1/C2 execution, or counter modification was performed. No tools were installed.
