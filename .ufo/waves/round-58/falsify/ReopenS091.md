Result: MIXED — S091 row, its receipt, and every fact in the SKILL.md VS Code row and the entry bullet hold against the live page; the one defect is the quote note's "no other byte is changed" claim, which is false (newlines were rewritten to spaces), a Q42 shaping-disclosure violation.

# Re-open of S091 (VS Code prompt-files page)

URL: https://code.visualstudio.com/docs/agent-customization/prompt-files.md
Fetch, this seat:

```
$ date -u
Fri 23 Oct 2026 08:26:36 AM UTC
$ curl -sS -o s091.md -w 'HTTP %{http_code} bytes=%{size_download}\n' -A 'Mozilla/5.0 ...' <URL>
HTTP 200 bytes=13729
$ wc -c s091.md   →   13729
$ sha256sum s091.md   →   4ad1b2bcaf78c9166b1609610f354d9cb8b1ff9c9e7cf643c443fad04dac6685
```

Fetched copy: `/fast/scratch/hyaku/kotoba-r58/ReopenS091/s091.md`.

## SOURCES row (`corpus/SOURCES.md:104`)

- Recorded receipt: HTTP 200, 13,729 B, sha256 `4ad1b2bc…6685`, fetched 2026-10-23T08:08:16Z — **holds**; my re-fetch 18 min later returns the identical body (same bytes, same sha).
- `§ Prompt file locations (prompt-files.md:19-28)` — **holds** (`:19` heading, `:28` last line of section).
- `§ Prompt file format (:33-49)` — **holds** (`:33` heading, `:49` body sentence closes the section).
- `input syntax (:69-70)` — **holds** (`:69` `> [!TIP]`, `:70` the `${input:variableName}` sentence).
- Gist column (Local workspace default `.github/prompts`; `.prompt.md` Markdown with optional frontmatter; slash names default to filenames; input hints/placeholders guide/gather user context) — **holds** (`:25`, `:35-44`, `:40`, `:41`/`:70`).

## Quote verbatim + Q42 note (entry `corpus/knowledge/command-files-round58.md:37`, note `:29-30`)

Decoded (`&#124;`→`|`) quote: `that the Local harness uses for prompt files. | Scope | Default file location | |-------|-----------------------| | Workspace | \`.github/prompts\` folder |`

Byte comparison against the fetched span `s091.md:21-25`:

- After `&#124;` → `|` decoding and collapsing each `\n` run to a single space, the quote is **byte-identical** to the page span (verified programmatically; separator dash counts `:24` = `|-------|-----------------------|` exact).
- **FINDING (low, Q42)**: the note says "its table pipes are written as `&#124;` to keep them inside one cell — **no other byte is changed**". False: the quote drops two newline bytes (the `\n\n` between `:21` and `:23`, i.e. the blank line is removed entirely) and replaces the `\n` at the end of `:23` and `:24` with spaces — 4 newline bytes rewritten/removed, not disclosed. Q42 requires the note to name exactly which bytes were removed; this note claims none were. The shaping itself is disclosed in spirit (it "spans a Markdown table"), and the word content is intact, but the literal claim "no other byte is changed" is inaccurate — the fix is to add "newlines collapsed to spaces" (or use the unshaped `:25` row alone).
- Row-rule check: the quote does name `.github/prompts` in the page's own bytes — holds.

## Fact-by-fact, SKILL.md `Custom command files` row (`SKILL.md:115`)

`Command files` cell — `.github/prompts` (workspace; user files in the profile):
- workspace `.github/prompts`: **holds** (`:25`, `| Workspace | \`.github/prompts\` folder |`)
- user files in the profile: **holds** (`:26` `| User profile | Your user data (specific to your VS Code profile) |`); page names no path, cell names none either.

`What a file sets` cell:
- `.prompt.md` Markdown: **holds** (`:35` "Prompt files are Markdown files with the `.prompt.md` extension.")
- optional `description`: **holds** (`:39`, Required = No)
- `name` (after `/`, defaults to the file name): **holds** (`:40`, Required = No; "used after typing `/` in chat. If not specified, the file name is used.")
- `argument-hint`: **holds** (`:41`, Required = No)
- `agent`: **holds** (`:42`, Required = No)
- `model`: **holds** (`:43`, Required = No)
- `tools`: **holds** (`:44`, Required = No)
- field list completeness (all six, nothing missed): **holds** (`:37-44` is the entire field table; all six rows marked `No`)
- `${input:…}`: **holds** (`:70` "a syntax like `${input:variableName}`, `${input:variableName:placeholder}`")
- cited line refs `(S091 \`:35,39-44,69-70\`)`: **holds** — every ref points at the text it summarizes.

`Action` cell — "Local harness only: for other harnesses write an agent skill":
- **holds** (`:17` IMPORTANT: "Prompt files run only in **Local** harness sessions… For reusable workflows in other harnesses, create an [agent skill]…"). Page also offers "convert an existing prompt file to a skill" — the cell's phrasing is an action recommendation, not a misquote; no defect.

## Fact-by-fact, entry `What a file sets` bullet (`command-files-round58.md:49-51`)

- `.prompt.md` Markdown files (`:35`): **holds** (`:35`).
- optional frontmatter `description`, `name`, `argument-hint`, `agent`, `model`, `tools` (`:39-44`): **holds** (`:37-44`; six fields, all `No`).
- `name` follows `/` and defaults to the file name (`:40`): **holds** (`:40` verbatim-supporting).
- `${input:…}` variables (`:69-70`): **holds** (`:70`; `:69` is the TIP marker).
- user-level files live in the profile folder: **holds-with-nit** — page `:26` says "Your user data (specific to your VS Code profile)" and `:126` "user profile"; the page deliberately names no folder/path (seat SrcVSCode noted the same, build/SrcVSCode.md:8). "profile folder" is a fair paraphrase of "profile"/"user data" but slightly implies a filesystem folder the page does not name; cosmetic at most.
- Intro claim "prompt files run only in Local harness sessions, and its page sends reusable workflows for other harnesses to an agent skill (S091 `prompt-files.md:17`)" (`:17-18` of entry): **holds** (`:17`).

## Findings

1. **Low (Q42)**: quote note at `command-files-round58.md:29-30` asserts "no other byte is changed" while the quote collapses/removes 4 newline bytes from `prompt-files.md:21-25`. Word/pipe content is exact; only the disclosure is wrong. Suggested correction: append "newlines collapsed to single spaces, blank line between the prose and table dropped".

2. **Cosmetic**: "profile folder" (entry `:51`) names a folder where the page says only "user data (specific to your VS Code profile)" (`:26`). Not a factual error; the seat's own build report already hedged to "profile data".

## Residual risk / gaps

- Page is vendor docs served as Markdown; a CDN variant or locale could differ — my fetch returned the recorded bytes exactly, so drift risk is nil as of 08:26Z.
- The `Action` cell omits the page's "convert an existing prompt file to a skill" path (`:17`); an editorial choice, not an error.
- I did not re-verify non-VS-Code rows, S028, or the counter; out of this item's scope.
