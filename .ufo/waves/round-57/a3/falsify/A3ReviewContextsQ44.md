Result: MIXED — w0 and both falsify waves carry the process-hygiene bound verbatim in their contexts; the controls call carries it by reference only (M63 right about that), but M63's claim that the build contexts carry it verbatim is false (they carry a lowercase paraphrase; the build files' grep hit comes from the ScribeMistakes item prompt, so the round's only presence check false-passes the build wave).

Checked 2026-10-23, `date -u` at verification: Fri 23 Oct 2026 07:01:26 AM UTC. All greps run in `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/`; JSON context fields extracted with python (read-only). No tool installs (tooling directive: nothing to record). No lane writes except this report.

## 1. `grep -c 'Kill only by the PIDs you started'` per record (command run on all 12 files at once; exit 0)

| record | count | matching line(s) | what the match is |
|---|---|---|---|
| w0-call.json | 1 | :2 | the context — bounds inlined verbatim |
| controls-call.json | 0 | — | no match (re-run alone: prints `0`, exit 1 — M63's cited behavior reproduced) |
| build-spec.json | 1 | :170 | ScribeMistakes item prompt quoting M61's grep command; the context (line 12) does NOT match |
| build-dispatch.json | 1 | :462 | same item prompt; context line 367 does NOT match |
| build-taskcall-sent.json | 1 | :97 | same; context line 2 does NOT match |
| falsify-spec.json (a1) | 2 | :13 context, :261 Q44 item prompt | context verbatim + the Q44 assignment quoting the grep |
| falsify-dispatch.json (a1) | 2 | :376 context, :526 | same |
| falsify-taskcall-sent.json (a1) | 2 | :2 context, :152 | same |
| a3/falsify-spec.json | 2 | :13 context, :292 | same |
| a3/falsify-dispatch.json | 2 | :444 context, :614 | same |
| a3/falsify-taskcall-sent.json | 2 | :2 context, :172 | same |
| bounds.md (canonical) | 1 | :6 | the bound itself |

Case-insensitive `grep -ic 'kill only by the pids you started'` adds only: controls-call.json 1 (the lowercase paraphrase) and the three build files 2 each (context paraphrase + item prompt).

## 2. Is the 4-process/120 s cap present?

| record | full form "at most 4 concurrent processes and 120 s wall time" | short form "4 processes/120 s" | verdict |
|---|---|---|---|
| w0-call.json | 1 | 0 | full cap, in context (bounds bullet verbatim) |
| controls-call.json | 0 | 0 | ABSENT. Context says only "kill only by the PIDs you started; contention tests capped" — no numbers. The file's only "120 s" is MutC1Counter's mutation discipline ("timeout 120 s each", :37), not the contention cap |
| build-spec/build-dispatch/build-taskcall-sent | 0 each | 1 each | numbers only, as a short paraphrase in the context ("contention tests capped at 4 processes/120 s"); the bounds sentence itself is absent from all three files |
| falsify-spec/dispatch/taskcall-sent (a1) | 1 each | 1 each | full cap in context; short form additionally in the sentinel item ("beyond 4 processes/120 s") |
| a3/falsify-* (3 files) | 1 each | 1 each | same shape as a1 |
| bounds.md | 1 | 0 | canonical full form |

## 3. Which carry the bound verbatim, which by reference only

Context-level checks (character presence in the parsed JSON `context` string; spec/dispatch/taskcall contexts within each wave are byte-identical — verified all six sibling pairs):

- **Verbatim (bounds.md text inlined, capital-K sentence + full cap):** w0-call.json (whole bounds.md inline, every line); falsify-spec.json, falsify-dispatch.json, falsify-taskcall-sent.json (a1 — whole bounds.md inline, every line); a3/falsify-spec.json, a3/falsify-dispatch.json, a3/falsify-taskcall-sent.json (bounds inlined; exactly two wave-parameterized bullets updated to a3 values — message target `agent://KotobaR57A3`, sandbox path `/fast/scratch/hyaku/kotoba-r57a3/<YourSeatName>`; the process-hygiene bullet is byte-verbatim). Root bounds.md itself still carries the a1 values (bounds.md:2), so a byte-diff against today's bounds.md flags those two a3 bullets — substitution, not omission.
- **By reference only:** controls-call.json — context at char ~1548: "Read /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-57/bounds.md FIRST — it is binding", plus a lowercase summary without the cap numbers.
- **Paraphrase with numbers, not verbatim:** the three build files — context at char ~3931: "kill only by the PIDs you started, never pkill -f; contention tests capped at 4 processes/120 s". killHi=False, killLo=True in all three contexts.
- **Spurious verbatim hits:** the build files' `grep -c` = 1 comes only from the ScribeMistakes item prompt (build-spec.json:170, build-dispatch.json:462, build-taskcall-sent.json:97), which embeds M61's check command `grep -c 'Kill only by the PIDs you started' …/round-56/build-spec.json`. The file-level grep therefore cannot distinguish a verbatim context from an item prompt that merely quotes the check.

## 4. Is lesson M63 accurate? Clause by clause (corpus/lessons/round-57.md:101-104)

1. "the pre-freeze control call's context named `bounds.md`" — TRUE (controls-call.json context, char ~1548 window quoted above).
2. "and summarised the kill bound in lower case" — TRUE (char ~1756; case-insensitive count 1, case-sensitive 0).
3. "so `grep -c 'Kill only by the PIDs you started' .ufo/waves/round-57/controls-call.json` prints 0" — TRUE; reproduced, exit 1; r7-bound-grep.txt:6 agrees (frozen 04:37:44Z, receipt committed at 27af04a).
4. "while the w0 and build contexts carry it verbatim" — **FALSE for build.** w0: TRUE (context inlines bounds.md verbatim). Build: the contexts carry only the lowercase paraphrase; the capital-K sentence appears in the three build files only inside the ScribeMistakes item prompt. Upstream error: build/ScoutReportR1.md:17 says the build "context at char 3948 has the full form … (both 5,382 B)" — the length and byte-identity are right (context len 5,382 in all three), but the text at char 3931+ is the paraphrase, not the bounds sentence. build-spec.json has exactly one commit (27af04a, 2026-10-23T01:46:10-03:00 = 04:46:10Z) and a clean working copy, so the committed bytes ScoutReportR1 describes after 04:46Z are the bytes measured here; its "full form" wording is wrong against them, and M63 hardened it into "verbatim".
5. fix "every later context inlines `bounds.md`" — TRUE as applied: falsify a1 and a3 contexts inline the full bounds text.
6. fix "the falsify call's grep is recorded in the report" — not satisfied by any pre-existing artifact: the a1 reportDir `.ufo/waves/round-57/falsify` (falsify-spec.json:12) was never created (absent on disk — the a1 wave died with the orchestrator), and a3/falsify/ held only swarm-registry.json before this report. This report records it (section 1). [INFERENCE] the clause anticipated the falsify-wave Q44 report; the a1 Q44 seat never delivered one, so M63's "captured-by: Q44 (this round)" is realized only by this attempt-3 re-run.

## 5. Findings

- **F1 (lesson text wrong on build; fix proposed).** M63's contrast clause (lesson :103) is false for the build contexts. Exact old→new for the L1 (old = corpus/lessons/round-57.md:101-104, hard-wrapped; new unwrapped, L1 may rewrap):
  - OLD: `- **M63 \`bound-carried-by-reference\`** · the pre-freeze control call's context named \`bounds.md\` and summarised the kill bound in lower case, so \`grep -c 'Kill only by the PIDs you started' .ufo/waves/round-57/controls-call.json\` prints 0 (\`.ufo/waves/round-57/r7-bound-grep.txt\`) while the w0 and build contexts carry it verbatim · captured-by: Q44 (this round) · fix: every later context inlines \`bounds.md\`; the falsify call's grep is recorded in the report.`
  - NEW: `- **M63 \`bound-carried-by-reference\`** · the pre-freeze control call's context named \`bounds.md\` and summarised the kill bound in lower case without the cap numbers, so \`grep -c 'Kill only by the PIDs you started' .ufo/waves/round-57/controls-call.json\` prints 0 (\`.ufo/waves/round-57/r7-bound-grep.txt\`); the w0 context and both falsify waves' contexts carry the bounds text verbatim, while the build contexts carry only the paraphrase "kill only by the PIDs you started, never pkill -f; contention tests capped at 4 processes/120 s" and each build file's grep count 1 comes from the \`ScribeMistakes\` item quoting M61's grep command, not from the context · captured-by: Q44 (attempt-1 seat died before reporting; re-verified attempt 3, \`.ufo/waves/round-57/a3/falsify/A3ReviewContextsQ44.md\`) · fix: every later context inlines \`bounds.md\` (falsify attempts 1 and 3 do); the falsify call's grep is recorded in the attempt-3 report.`
- **F2 (presence check false-passes the build wave).** Q44's criterion (build/ScribeQuality.md:10: "a context check must fail when either bound is absent") is not implemented anywhere as a context check. The only existing grep (M61's, and the Q44 assignments') counts whole files, so it returns 1 for every build record even though no build context contains the verbatim bound — the exact controls-call failure M63 records would score as "present" on the build records. Recommendation (no counter added without a routed item): if a presence check is kept, extract the context field first (`jq -r '.context' … | grep -c`), or state the check as file-scoped in the lesson.
- **F3 (report/bytes inconsistency, no edit proposed).** build/ScoutReportR1.md:17 "full form … byte-identical (both 5,382 B)" is wrong on "full form" (see 4.4). Per round-56 precedent the fleet/seat report is not edited; F1's M63 rewrite is the correction surface.
- **F4 (provenance, not a defect).** `git --no-optional-locks status --porcelain=v1` (lane): `?? .ufo/waves/round-57/a3/`, `?? falsify-dispatch.json`, `?? falsify-spec.json`, `?? falsify-taskcall-sent.json`. The a1 falsify records and the whole a3/ dir (incl. the untrusted a2-candidate.patch) are untracked working-copy files; the w0/controls/build records and bounds.md are tracked and clean. Sections 1–4 therefore describe working-copy bytes read today for the falsify records, committed bytes for the rest.
- **F5 (minor, by design).** bounds.md:2 still carries the a1 message target (`agent://KotobaR57`); a3 seats are bound via the a3 context's substituted bullets (verified: `agent://KotobaR57A3`, `kotoba-r57a3` present in a3 context). No action; noted so a future grep of bounds.md alone is not read as the a3 seat's target.

## Residual risk and verification gaps

- I did not re-run any wave or check any seat behavior; this is a records audit only.
- The frozen receipt r7-bound-grep.txt (04:37:44Z) predates build-spec.json's commit (04:46:10Z) by 9 minutes; that the "1" it printed for build-spec/build-dispatch is the same ScribeMistakes line is [INFERENCE] from the file having a single commit and a clean working copy — pre-commit working bytes are unverifiable.
- Character offsets (3931, 1756, 1548) are 0-based python indices into the parsed context strings; ScoutReportR1's "char 3948"/"char 1773" used its own origin (differences ≤ 25 chars, same text).
- Whether bounds.md was byte-identical at the w0 dispatch (its context inlines it) was not checked against the ee50d8f blob; w0/controls/build records are clean against HEAD, which is the state this audit covers.

Report: .ufo/waves/round-57/a3/falsify/A3ReviewContextsQ44.md
