Result: DONE — Copilot CLI and VS Code already contrast hooks with instruction text on the pages S099 and S098 will cite; Claude’s deterministic/advisory lines are on other pinned-host docs and need a new row; Codex, Gemini CLI, and Cursor did not show that contrast on the pages opened.

Seat ScoutInstructionVsHook. No tools installed. No lane file edited except this report. Fetches used the counter’s header set (`verifiers/check_hook_files.py` `CURL_UA` Chrome/130 and `Accept: text/markdown, text/plain;q=0.9, */*;q=0.8`), `curl -sSL --max-time 30`. Word counts are `str.split()` of the quoted slice (backticks kept). No bytes stripped inside a quote unless the line says so. Saved bodies: `/fast/scratch/hyaku/kotoba-r59/ScoutInstructionVsHook/`. These quotes do not contain the hook-config token, so they cannot replace the entry Quote cells.

## On the pages S096–S101 will cite

Census and the control seats pin S096 `https://code.claude.com/docs/en/hooks.md`, S097 `https://learn.chatgpt.com/docs/hooks.md`, S098 `https://code.visualstudio.com/docs/agent-customization/hooks.md`, S099 `https://docs.github.com/en/copilot/concepts/customizations/hooks.md`, S100 `https://geminicli.com/docs/hooks/best-practices.md`, S101 `https://cursor.com/docs/hooks` (the `.md` route 404s under this header set).

### Copilot CLI — on S099, prefer this

- URL: `https://docs.github.com/en/copilot/concepts/customizations/hooks.md`
- `date -u` immediately before the batch: `Fri 23 Oct 2026 09:36:19 AM UTC`
- HTTP 200, 8428 bytes, sha256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` (same sha as the census)
- Line 15, first sentence, 15 words, no bytes stripped:

Unlike custom instructions, hooks run code rather than asking the model to follow a rule.

The rest of the line is an example and is not needed. This is the sentence to ground the intro.

A different page, `https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions.md` (same batch, HTTP 200, 14669 bytes, sha256 `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933`), line 14, says Copilot may not follow custom instructions and does not mention hooks. Not a hook contrast. Would be a new row if used. Do not prefer it over line 15.

### VS Code — on S098, usable; a sharper page would be a new row

- URL: `https://code.visualstudio.com/docs/agent-customization/hooks.md`
- same `date -u`: `Fri 23 Oct 2026 09:36:19 AM UTC`
- HTTP 200, 15152 bytes, sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` (same sha as the census)
- Line 6, second sentence, 25 words, no bytes stripped:

Use them to add context, validate a tool call, run a formatter, or record an event without relying on the model to request the action.

It does not say “instructions”. It does say the hook runs without the model requesting the action. On the S098 page, so no new row.

Line 208 of the same page is the other direction and should not ground the intro: “Hooks and instructions are not substitutes for enforced permissions, sandboxing, or enterprise controls.”

Sharper, not on S098, would need its own row (do not spend the only spare id on it while line 6 exists):

- `https://code.visualstudio.com/docs/agents/concepts/customization` — batch `Fri 23 Oct 2026 09:37:09 AM UTC`, HTTP 200, 10754 bytes, sha256 `133bca60d59138bacc0ef9872566451d18b3fb27c56e68798c18f2dc4ac9d962`. Line 77, second sentence, 17 words:

A hook configured for the corresponding lifecycle event runs regardless of whether the model remembers the instruction.

The preceding sentence on that line is 22 words: `For example, an instruction that says "run the formatter after editing a file" asks the model to remember and perform that action.`

- `https://code.visualstudio.com/learn/customizations/5-hooks` — same batch, HTTP 200, 6363 bytes, sha256 `ad091a4a1b7b68cdec2d74e00018ad6dea41caf0a2323fd2319bd650f1340acc`. Line 93, both sentences, 23 words. The apostrophe in “don’t” is U+2019, not ASCII 0x27:

Unlike prompts, instructions, or even skills, hooks don’t require you to explicitly trigger them. They run automatically when the right conditions are met.

### Claude Code — not on S096

Re-fetched `https://code.claude.com/docs/en/hooks.md` at `Fri 23 Oct 2026 09:37:09 AM UTC`, HTTP 200, 274129 bytes, sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`. No “deterministic” or “advisory” contrast. Closest lines are a different claim (static text vs a script), line 1137, 22 words for the whole line:

For instructions that never change, prefer [CLAUDE.md](/docs/en/memory.md). It loads without running a script and is the standard place for static project conventions.

The vendor sentences that match the plan (“deterministic, not text the model may ignore”; “a rule that must hold every time” out of the prompt) are on other `code.claude.com` docs. Each URL is a new SOURCES row. S102 can cover only one.

Prefer S102 = `https://code.claude.com/docs/en/best-practices` if the intro keeps the word “deterministic”:

- batch `Fri 23 Oct 2026 09:36:19 AM UTC`, HTTP 200, 36360 bytes, sha256 `b225977e2892002cc91ff4dfe2d6a7e2324fd455aa6325c889cecb009ca76052`
- Line 227, second sentence, 14 words, no bytes stripped:

Unlike CLAUDE.md instructions which are advisory, hooks are deterministic and guarantee the action happens.

- Line 225 is a blockquote. The sentence after the `> ` marker (bytes U+003E U+0020 not included), 12 words: `Use hooks for actions that must happen every time with zero exceptions.`

Use `https://code.claude.com/docs/en/features-overview` instead if the intro says “prompt instruction” (same batch, HTTP 200, 27348 bytes, sha256 `e1f0ae3d6465f43cc18b3fc1cdab43b4ca10455ddbe5917ef11d79d86b64ab82`):

- Line 189, last sentence, 16 words:

If a rule must hold every time, make it a hook rather than a prompt instruction.

- Line 189, middle sentence, 17 words: `An instruction like "never edit `.env`" in CLAUDE.md or a skill is a request, not a guarantee.`
- Line 181 is a table row, not one sentence. The two cells, 7 words each: `Fires on its event without Claude deciding` and `Claude interprets the instructions; outcome can vary`.

`https://code.claude.com/docs/en/hooks-guide` (same batch, HTTP 200, 62917 bytes, sha256 `004ded2fd87af2deee93d4ce7f47216a82b5e22fc76f345ea654eeb51b2bee3c`) line 9, second sentence, is 30 words, over the cap. Contiguous 20-word slice, no bytes removed inside the slice:

which gives you deterministic control: certain actions always happen rather than relying on the LLM to choose to run them.

### Codex — not on S097, not found on the other pages opened

- `https://learn.chatgpt.com/docs/hooks.md` — `Fri 23 Oct 2026 09:36:19 AM UTC`, HTTP 200, 47133 bytes, sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`. The only “advisory” hit is line 718, about `SessionEnd` hook output, not about instruction files.
- `https://learn.chatgpt.com/docs/agent-configuration/agents-md.md` — `Fri 23 Oct 2026 09:37:09 AM UTC`, HTTP 200, 9149 bytes, sha256 `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e`. Discovery and truncation only. No “may not follow”.
- Docs index `https://learn.chatgpt.com/docs/llms.txt` — same 09:36:19Z batch, HTTP 200, 33447 bytes, sha256 `fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943`. No deterministic/unlike blurb.
- `https://api.github.com/search/code?q=repo:openai/codex+deterministic+hooks` returned HTTP 401 (unauthenticated code search). The repo tree was not walked. Not a silence claim.

### Gemini CLI — not on S100, no vendor docs sentence found

S100 bytes were not re-fetched this seat. A search of the control snapshot `/fast/scratch/hyaku/kotoba-r59/CtlFabSnapshot/.ufo/waves/round-59/snapshots/S100.page` (the control receipt’s sha256 `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc`) found no unlike/deterministic/GEMINI.md-vs-hooks sentence. Own fetches:

- `https://geminicli.com/docs/hooks.md` — `Fri 23 Oct 2026 09:36:19 AM UTC`, HTTP 200, 8341 bytes, sha256 `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`. Line 9 says hooks run synchronously in the agent loop. It does not mention instructions.
- `https://geminicli.com/docs/extensions/writing-extensions.md` — same batch, HTTP 200, 12407 bytes, sha256 `4c981cc62340163051ded660bc1d9b650b34f3674e04b16899045aa2198fef98`. The feature table (lines 22 and 24) says a `GEMINI.md` is instructions loaded into the model’s context (“CLI provides to model”) and hooks are “Invoked by: CLI”. That is who runs them, not “the model may not follow”. Not the intro sentence.
- Changelogs, later batches: `https://geminicli.com/docs/changelogs/latest.md` (`Fri 23 Oct 2026 09:37:09 AM UTC`, HTTP 200, 4140 bytes, sha256 `f38215087f7adabbd9d52831ceeb1def13bc98eb4b62181c518f295e399dd68f`), `https://geminicli.com/docs/changelogs.md` (`Fri 23 Oct 2026 09:38:21 AM UTC`, HTTP 200, 69617 bytes, sha256 `e8fb2a25f450de8ed4cc1db23c0c48d269853cd05b375399e7a4e47d834f423a`), `https://geminicli.com/docs/changelogs/preview.md` (same batch, HTTP 200, 6038 bytes, sha256 `c186463197c0cb2d65eece11cc0b69a567d7a2b4967443447cf8488b40d06593`). No hook-vs-instruction line. `raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/hooks.md` was HTTP 404 at `Fri 23 Oct 2026 09:39:24 AM UTC`.
- `https://github.com/google-gemini/gemini-cli/issues/2779` is a pinned host but a tracker (the counter rejects it) and the body is a feature request by GitHub user `coygeek` (API `Fri 23 Oct 2026 09:38:52 AM UTC`, HTTP 200, issue JSON sha256 `fbbe9b9137de33216df74c4b6dd4c46be7a57d673e0cc3917a1b64caead01a5d`). Not a vendor sentence. Not a row.

### Cursor — not on S101, not found on the other pages opened

- `https://cursor.com/docs/hooks` — `Fri 23 Oct 2026 09:36:19 AM UTC`, HTTP 200, 69145 bytes, sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`. No unlike/deterministic/instruction contrast. Command hooks vs prompt hooks (line 176) is a different split.
- `https://cursor.com/docs/hooks.md` — same batch, HTTP 404, 389 bytes, sha256 `4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`. Same failure mode the controls recorded.
- `https://cursor.com/docs/rules` — `Fri 23 Oct 2026 09:37:09 AM UTC`, HTTP 200, 17403 bytes, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`. Line 28, second sentence, 16 words, is rules-as-guidance and does not mention hooks: `This gives the AI consistent guidance for generating code, interpreting edits, or helping with workflows.` Line 186 says the agent decides whether to apply a rule when `alwaysApply` is false. Not the requested contrast. `.md` on this path was HTTP 404, same 389-byte sha as the hooks `.md` 404.
- `https://cursor.com/help/customization/rules` — same batch, HTTP 200, 6285 bytes, sha256 `c6d2b0697e0b8f51d0d9ad7701a850cd81c389ec075e24b15e24bbd4e5afcdfc`. No contrast needles.
- `https://cursor.com/docs/cli/changelog` — `Fri 23 Oct 2026 09:38:21 AM UTC`, HTTP 200, 56159 bytes, sha256 `70d57616d76ddfa089d42b23a149fad68436ecd8711a94b33c13c3c64795167b`. No hook-vs-instruction line. `https://cursor.com/docs/release-notes` — same batch, HTTP 200, 301193 bytes, sha256 `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd`. Hooks and rules are named as settings, not contrasted.

## What the intro can stand on

Ground the intro from S099 line 15 and S098 line 6 with no new row. Add one new row only if the intro uses Claude’s words. S102 should be `https://code.claude.com/docs/en/best-practices` for “Unlike CLAUDE.md instructions which are advisory, hooks are deterministic…”, or `https://code.claude.com/docs/en/features-overview` for “make it a hook rather than a prompt instruction”. Not both. Codex, Gemini CLI, and Cursor are not checked to a “documents nothing” verdict: lane `corpus/` had no match for these phrases, and the pages above were opened, but the Codex and Cursor docs trees were not fully walked.

## Corpus

`grep` of `/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` for `Unlike custom instructions`, `without relying on the model`, `hooks are deterministic`, and `deterministic control` returned no matches.
