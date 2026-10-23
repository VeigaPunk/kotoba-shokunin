Result: DONE — Cursor’s official skills documentation identifies `/skill-name` as explicit invocation and documents a setting that prevents automatic application.

## Findings

- **C1 source and invocation form.** The official skills page documents manual invocation by typing `/` in Agent chat and searching for a skill name; it says the invocation attaches to one message (`cursor-skills.md:29`). Its `disable-model-invocation` field row gives the explicit named form and says the agent will not apply the skill automatically based on context (`cursor-skills.md:175`). The automatic-invocation section also describes typing `/skill-name` in chat (`cursor-skills.md:212-214`).
- **Byte-exact source quote (22 words; no Markdown was stripped):** “When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context.” — `cursor-skills.md:175`. The table row is the `disable-model-invocation` field. This documents both the named explicit form and a way to suppress implicit application while retaining explicit invocation: set `disable-model-invocation: true`.
- **Release-note corroboration.** Cursor’s release notes state: “A skill slash entry attaches once when you press Enter” (9 words; `cursor-release.md:1811`).

## Fetch evidence

The skills page and release notes were fetched with `curl` in the sandbox clone. The exact `date -u` output immediately before both fetches was:

```text
Thu 22 Oct 2026 11:12:21 PM UTC
```

- URL: `https://cursor.com/docs/skills.md`; final HTTP status `200`; `18,477` bytes; SHA-256 `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d`. Fetched bytes: `/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcCursor/cursor-skills.md`.
- URL: `https://cursor.com/docs/release-notes.md`; final HTTP status `200`; `301,193` bytes; SHA-256 `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd`. Fetched bytes: `/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcCursor/cursor-release.md`.
- Fetch commands (from that clone directory):
  - `timeout 900s curl -sS -L --max-time 60 -D cursor-skills.headers -o cursor-skills.md -w 'skills HTTP=%{http_code}\n' https://cursor.com/docs/skills.md` → `skills HTTP=200`; `wc -c cursor-skills.md` → `18477`; `sha256sum cursor-skills.md` → `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d  cursor-skills.md`.
  - `timeout 900s curl -sS -L --max-time 60 -D cursor-release.headers -o cursor-release.md -w 'release HTTP=%{http_code}\n' https://cursor.com/docs/release-notes.md` → `release HTTP=200`; `wc -c cursor-release.md` → `301193`; `sha256sum cursor-release.md` → `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd  cursor-release.md`.
- The lane `corpus/SOURCES.md` search for `cursor.com/docs/skills` returned `No matches found`; the release-notes URL is already cited in the lane as S058.

## Draft C1 rows

Draft SOURCES row (11 cells; `S0NN` is the requested placeholder):

```text
| S0NN | Cursor Docs — Agent Skills — https://cursor.com/docs/skills.md | docs | A | Cursor's documented named-skill slash invocation in Agent chat and the automatic-invocation control | § How skills work (`cursor-skills.md:29`); § SKILL.md file format, `disable-model-invocation` row (`:175`); § Disabling automatic invocation (`:212-214`); fetched 2026-10-22T23:12:21Z (HTTP 200, 18,477 B, sha256 `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d`) | With `disable-model-invocation: true`, a skill is included only after explicit `/skill-name` invocation, not automatically based on context | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md |
```

Draft entry row:

```text
| Cursor | S0NN | "When `true`, the skill is only included when explicitly invoked via `/skill-name`. The agent will not automatically apply it based on context." | Cursor Docs — Agent Skills, `cursor-skills.md:175` | The `disable-model-invocation` row says the skill is included only on explicit `/skill-name` invocation and is not automatically applied based on context. |
```

Draft SKILL.md decision row:

```text
| Cursor | `/skill-name` | With `disable-model-invocation: true`, the skill is included in context only when invoked explicitly; the agent will not automatically apply it based on context. | Set aside turns that use this form from implicit-activation counts; they were explicitly invoked. |
```

## Gate, surfaces, and limits

- **Gate run:** in the sandbox clone checked out at plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`, `timeout 900s python3 -B /fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcCursor/verifiers/check_explicit_invocation.py --self-test` printed `self-test: 0 failure(s) over 29 assertions`; exit code `0`.
- **Touches:** only this report was written in the lane. The SOURCES row, knowledge entry, and SKILL.md decision row above are drafts in this report and were not applied. Page bytes, headers, and the cloned verifier are in `/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcCursor/`.
- **Out of scope / limits:** no product code, verifier, or lane Git/JJ state was edited; no tools were installed. The C1 live `--fetch` predicate was not run, so this source report and the requested self-test do not establish that predicate. The documentation is evidence of Cursor’s documented behavior, not a measurement of runtime behavior. Since an explicit form was found, the Q30 three-part silence sweep does not apply.
