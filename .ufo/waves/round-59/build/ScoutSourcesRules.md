Result: DONE — S096–S101 are free ids; the only census URL already in `corpus/SOURCES.md` is Gemini's extensions reference (S083), and reusing it as a row's first URL raises W04 or E04 depending on scope.

# Evidence

- Contract: `/home/vgpnk/Projects/shokunin/CORPUS.md:64-156` (SOURCES-CONTRACT-v1, frozen). Maintained parser note at `:150-155`: 0–3 leading spaces count; 4+ are indented code and are ignored. Frozen manual `awk` examples assume column zero and do not implement W04.
- Validator: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`. Header `:1-38`. Row rules `:600-674` (`url_of`, E01–E12, W01–W04). Used-by disk check `:538-570`. `--file` sets the lane dir to the parent of `corpus/` (`:497-502`), so used-by paths are lane-relative.
- Registry observed: `kotoba-shokunin/corpus/SOURCES.md` `## Registry` rows S001–S095, 94 data rows, no duplicate ids, only gap **S092**. Header at line 12. S089–S095 style at lines 102–107. `## Paths` starts line 109.
- Validate, read-only, `--today 2026-10-23 --file` that registry: exit 0, eight existing W04 lines (S018, S019, S021, S054, S055, S056, S065, S086), then `file	ok`. Warnings do not fail the lane (`sources-census.sh:32-33,738-745,805`).
- `corpus/knowledge/hook-files-round59.md` and `corpus/lessons/round-59.md` are absent on disk now. A `mined` row whose `used-by` names either path is E11 until that path exists.
- No tools installed.

URL key (`url_of`, `:600-605`), first `https?://` in the **source** cell only:

1. Strip the fragment (`#` through end).
2. Strip one trailing `/` (a second slash remains).
3. Strip the scheme. `http` and `https` compare equal.
4. Lowercase the host only. Path case, query string, and a trailing `.md` are kept.
5. `www.` is not stripped. A redirect is not followed, so `developers.openai.com/codex/hooks.md` and `learn.chatgpt.com/docs/hooks.md` are different keys.

W04 (`:644-645`): that key was already seen and this row's scope string is new. Same scope does not W04. E04 (`:646-649`): same key and same scope, this row is not `rejected`, an earlier non-rejected row holds that pair, and `teaches` does not match `supersedes S[0-9]{3}`. Observed escape: S039 teaches opens `supersedes S024` with the same scope as S024, and validate emitted neither E04 nor W04 for it. S086 teaches opens `supersedes S080` but the scope string differs, so validate emitted W04 anyway. Rejection of the later row suppresses E04; it does not stop the URL from being seen.

# Rules a new row must meet

Census-enforced (exit 1 on any E; W leaves exit 0):

| Check | Rule | Where |
|---|---|---|
| Place | Inside `## Registry`, before `## Paths`. A row under Paths or the search log is E12. 0–3 leading spaces only. | script `:609-623`; contract shape `:76-84` |
| Columns | Exactly 11 cells, awk `NF==13`. A raw pipe inside any cell is E01 and skips the other checks for that row. The entity `&#124;` is not a pipe. | script `:635-638`; contract `:89` |
| id | `S` + 3 or more digits. S096–S101 match and are unused. Duplicate id is E03. A gap is not an error: S092 is unused and the script does not require contiguous ids. Contract text says "the next unused" (`CORPUS.md:89`); the frozen seat assignment is S096–S101. | script `:640-642` |
| source | First URL in this cell is the only URL the duplicate checks see. Later supporting-page URLs do not raise W04 or E04. Own-work with no URL is skipped. | script `:600-605,629,644-654`; contract `:90` |
| kind | One of `spec` `docs` `paper` `code` `tool` `dataset` `talk` `book` `community` `own-work`. Else E05. S089–S095 are `docs`. | script `:655-656`; contract `:91-92` |
| tier | `A`, `B`, or `C` only. Else E06. Scoped to the scope cell, not global. `community` at `A` is E10. Official docs are contract tier A (`CORPUS.md:93-97`). The script does not check that a `docs` row is A. | script `:657,668` |
| scope | Free text, trimmed. It is the W04/E04 discriminator. Two rows may share a URL when the scope strings differ (W04, exit 0) or when the later `teaches` matches `supersedes S###` (same scope: no E04). Copying one scope sentence onto two hook rows is E04. | script `:643-649`; contract `:98` |
| anchor | Not census-enforced. Contract: section, heading, page, or line plus a revision; never a bare homepage (`:99-100`). | contract only |
| teaches | Not enum-checked. Contract: one grounded benefit (`:101-102`). Rejected rows should read `REJECTED: <reason>; flip: <what would change the verdict>`. W02 if `rejected` and `teaches` is under 8 characters. The E04 escape is the substring `supersedes S` plus at least three digits. | script `:648,671-672` |
| status | `queued`, `mined`, or `rejected`. `watch` is E07. `mined` means cited by at least one `used-by` path. | script `:658-659`; contract `:103-104` |
| opened | Real ISO date `YYYY-MM-DD`, not after `--today` (default UTC today). `2026-10-23` passes a run dated 2026-10-23. A future date or an impossible date is E08. A time-of-day is rejected. | script `:660-662,49-63` |
| recheck | A calendar-valid ISO date (a past date is not E09), or `NNd` (`90d`, `180d`), or a symbolic token `^[A-Za-z][A-Za-z0-9 _-]*$` (`on-release`, `on-commit`). Empty, `90 d`, and `90days` are E09. S089–S095 use `90d`. `overdue` mode prints `cadence` for every `NNd` and symbolic row and flags a row only on or after its due date (opened + N days, or the ISO recheck date). That is not a validate error. | script `:663-666,675-685`; contract `:105-106` |
| used-by | `mined` and exactly `—` (U+2014, the glyph on S005) is W03. `queued` plus that glyph is quiet. Any other mined value is split on commas only (not semicolons; the frozen manual awk also splits on `;`, the script does not) and each trimmed path must exist under the lane root or E11. A hyphen-minus or en dash is not that glyph: on a mined row it is E11, not W03. Tier `C` plus `mined` plus a real path is W01. | script `:669-674,558-568`; contract `:107-108` |

Contract rules the script does not score, still binding (`CORPUS.md:110-129`):

1. Open the source in this round. The round lesson `## Gate` records the URL, the access date, and a quote of at most 25 words locating `teaches`.
2. Append-only. Do not edit older rows except `status`, `recheck`, and `used-by`, each logged old to new in the lesson. A correction is a new row whose `teaches` opens `supersedes S0NN —`.
3. No credential, session, private, or `op://` URL.
4. Do not copy the QUALITY method or the chousa method into the row.

Not this validator: the C1 counter's 64-hex sha256 cell, hook-event quotes, and `url_key` (which drops a trailing `.md`). `hooks` and `hooks.md` are different W04 keys.

# Census URL vs this registry

Exact normalized match of every `https?://` token in `.ufo/waves/round-59/w0/Census*.md` against every URL token in `corpus/SOURCES.md`.

Primary pages the seats fetched for the six eligible clients are absent. Putting one of these first in a new source cell does not W04 against today's registry:

| Id | Client | Lead page (absent from SOURCES.md) |
|---|---|---|
| S096 | Claude Code | `https://code.claude.com/docs/en/hooks.md` (`CensusClaudeCode.md:13`) |
| S097 | Codex | `https://learn.chatgpt.com/docs/hooks.md` (`CensusCodex.md:9`). The 308 source `https://developers.openai.com/codex/hooks.md` is also absent and is a different key. |
| S098 | VS Code | `https://code.visualstudio.com/docs/agent-customization/hooks.md` (`CensusVSCode.md:8`). `migrate-customizations.md` is also absent. |
| S099 | Copilot CLI | `https://docs.github.com/en/copilot/concepts/customizations/hooks.md` (`CensusCopilotCLI.md:11`). Also absent: `hooks-reference.md`, `use-hooks.md`, `copilot-cli-hooks.md`, `cli-config-dir-reference.md`. |
| S100 | Gemini CLI | `https://geminicli.com/docs/hooks/best-practices.md` and `https://geminicli.com/docs/hooks.md` (`CensusGeminiCLI.md:10-11`). Also absent: the writing-hooks page, `docs/hooks/`, and `docs/reference/configuration.md`. |
| S101 | Cursor | `https://cursor.com/docs/hooks.md` (`CensusCursor.md:7`). Bare `https://cursor.com/docs/hooks` is a different key and is also absent. |

Would raise W04 or E04: `https://geminicli.com/docs/extensions/reference.md`, first URL of mined S083 (`SOURCES.md:96`). Scope text: `Gemini CLI extension manifest location and documented extension contents (vendor documentation; not runtime behavior)`. Teaches does not contain `supersedes`.

- New row, that URL first, any other scope: W04, exit 0 if nothing else fails. The line names the new id.
- New row, that URL first, that same scope, not `rejected`, teaches without `supersedes S###`: E04, exit 1.
- Same URL only as a later URL in the source cell: the script does not see it. No W04 from that placement.

Opencode is not an eligible row. None of `Censusopencode.md`'s URLs (served `opencode.ai/docs/plugins.md`, `config.md`, or the `74f8d486` raw pins) occur in this registry. S085 and S087 are different commits of plugin docs. Reusing either of those existing first URLs follows the same W04/E04 rule as S083.

The eight W04s already in the file stay. A clean new-row check is "no new W04 or E line whose id is S096–S101", not "validate prints nothing".

# Checklist (L1, after the six rows are in the registry)

Run from anywhere. Read-only. `--today` keeps E08 stable.

```sh
F=/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-23 --file "$F"
echo exit:$?
```

Pass:

1. Exit 0, and a final `file	ok` line. Any E line fails, including E04 and E11.
2. No W04, E04, or E01–E12 line whose id is S096, S097, S098, S099, S100, S101, or S102.
3. Pre-existing W04 ids only: S018, S019, S021, S054, S055, S056, S065, S086. Re-diff against a validate captured before the edit.
4. Each new row: `NF==13` (11 cells), id matches `^S09[6-9]$` or `^S10[01]$`, kind `docs` unless the page is not vendor docs, tier `A` (not `community`), status one of `queued` `mined` `rejected`, opened `2026-10-23`, recheck `90d` or another legal cadence, no raw pipe.
5. `mined` means `used-by` is one or more comma-separated paths that exist under `kotoba-shokunin/`, not the em dash. `queued` means used-by is the em dash, not a hyphen.
6. The first URL of each new source cell is distinct from every earlier first URL, including the other new rows. Do not put `geminicli.com/docs/extensions/reference.md` first.
7. A same-URL correction, if any, uses a new id and `teaches` matching `supersedes S[0-9]{3}`. The same scope without that substring is E04.
8. Contract, not the script: the lesson `## Gate` has the URL, the access date, and a quote of at most 25 words for each new row; the anchor is a section plus a revision, not a bare home page; no private URL.

```sh
python3 - << 'PY'
import re
p="/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md"
text=open(p).read().split("## Paths",1)[0]
def url_of(s):
    m=re.search(r"https?://[^\s|]+", s)
    if not m: return ""
    u=re.sub(r"#[^ ]*$","",m.group(0)); u=re.sub(r"/$","",u); u=re.sub(r"^[A-Za-z]+://","",u)
    n=u.find("/"); return (u[:n].lower()+u[n:]) if n>=0 else u.lower()
seen={}
new={"S096","S097","S098","S099","S100","S101","S102"}
for line in text.splitlines():
    if not line.startswith("| S"): continue
    c=[x.strip() for x in line.split("|")]
    if not re.match(r"S[0-9]{3,}", c[1]): continue
    u=url_of(c[2]); seen.setdefault(u,[]).append((c[1], c[5], c[8], c[7][:40]))
for u,rows in seen.items():
    ids=[r[0] for r in rows]
    if any(i in new for i in ids) and len(rows)>1:
        print(u)
        for r in rows: print(" ", r)
PY
```

Empty output means no new first-URL collides with an earlier row. That is the W04/E04 candidate check.
