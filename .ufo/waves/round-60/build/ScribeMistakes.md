Result: MIXED — three draft entries and their evidence are complete; the observed Git time for the A1 commit differs by two seconds from the supplied time.

# ScribeMistakes — Round 60

## Proposed `## Mistakes` entries

- **M86 `word-count-without-command`** · Round 59's Gate called the Gemini hooks-overview span “29 words” (`corpus/lessons/round-59.md:27`; `sed -n '94,97p' hooks.md | wc -w` → `29`, exit 0), although cutting at `.gemini/settings.json` gives `25` (``sed -n '94,97p' hooks.md | tr '\n' ' ' | sed -E 's/^.*Hooks/Hooks/; s/(`\.gemini\/settings\.json`).*/\1/' | wc -w`` → `25`, exit 0; `.ufo/waves/round-60/w0/ExecR1Recount.md:35-49`). The same cited line's “25-word” and “10-word” forms are supported by `sed -n '94,97p' hooks.md | wc -w` → `29` (exit 0), the cut command above → `25` (exit 0), and `sed -n '413p' best-practices.md | wc -w` → `10` (exit 0). · captured-by: round-59 verifier spot-check R1 and `ExecR1Recount` · fix: use the `verifiers/check_word_counts.py` guard from `ExecWordCountCheck` and require each stated word count to carry its counting command · shown able to fail: `python3 -B verifiers/check_word_counts.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af --file corpus/lessons/round-59.md` → checker exit 1; output:
  ```
  corpus/lessons/round-59.md:27: stated word count (29 words, 25-word, 10-word) with no `wc -w` command on this line or the next 2
      - **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap (`CensusGeminiCLI`); the best-practices page carries a 10-word quote.
  stated word counts without a counting command: 1 of 1 claimed lines
  ```
  The command ran in `/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/sandbox` at the named revision. The tested checker copy had sha256 `10323e55eefdd61d7e723f4d159acb7c83785cdbccd503e82b64c5c1a4a3b644`; it was read from the `ExecWordCountCheck` working tree, not claimed as integrated or as that seat's final artifact.

- **M87 `future-dated-timestamp`** · Round 59 R3 recorded “Closed 10:12Z” after its report commit at 10:10:35Z (`corpus/lessons/round-59-verifier-spotcheck.md:36-37,203-204`); the error recurred in the A1 header: `git show bfe8cc2b:plans/round-60.md | grep -n 10:36Z` → `47:**Draft amendment A1 (10:36Z, before the freeze, before any control or C1 data; the rule is tightened, never loosened).**`, exit 0. `git log -1 --format=%cI bfe8cc2b` → `2026-10-23T07:33:42-03:00`, exit 0; `date -u -d '2026-10-23T07:33:42-03:00' '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-23T10:33:42Z`. At freeze, the header instead used the commit reference (`git show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:plans/round-60.md | grep -n -E 'Draft amendment A1|10:36Z|bfe8cc2b'` → ``47:**Draft amendment A1 (committed `bfe8cc2b`; before the freeze, before any control or C1 data; the rule is tightened, never loosened).**``, exit 0). · captured-by: round-59 non-author verifier spot-check R3 and the round-60 freeze review · fix: use the amendment commit reference at freeze; any stated wall-clock must be captured no later than the shipping commit · shown able to fail: the `git show ... | grep -n 10:36Z` and `git log -1 --format=%cI bfe8cc2b` commands above return the future header and earlier recorded commit time.

- **M88 `semantic-rule-wrong-key-pass`** · The pre-A1 Scope-key draft let Cursor's printed-but-wrong `description` pass at line 65 (backticked table cell plus `globs`) and line 99 (`description:` plus `patterns`) (`plans/round-60.md:35-44,48-60`; `.ufo/waves/round-60/w0/CensusCursor.md:94-108`). The draft-predicate replay below returns True on both fetched lines. · captured-by: `CensusCursor` before the freeze · fix: A1 removes the table-cell and loose glob/pattern-word alternatives; K must stand in key form, and its value's first token must be a `*` path pattern (or the first item of a block value) (`plans/round-60.md:54-60`) · shown able to fail: ``timeout 20 bash -o pipefail -c 'python3 -c '\''import re; lines=open("/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/rules.md",encoding="utf-8").read().splitlines(); p=r"\b(?:glob|globs|pattern|patterns)\b"; print("line 65: table-cell + loose-word alternative =", bool(re.search(r"\|\s*`description`\s*\|", lines[64]) and re.search(p, lines[64]))); print("line 99: key-form + loose-word alternative =", bool(re.search(r"(?<![A-Za-z0-9_-])description(?![A-Za-z0-9_-])\s*[:=]", lines[98]) and re.search(p, lines[98])))'\''; rc=$?; printf "exit=%s\\n" "$rc"; test "$rc" -eq 0'`` → `line 65: table-cell + loose-word alternative = True`; `line 99: key-form + loose-word alternative = True`; exit 0.

## Behavior

Copy-ready M86–M88 entries are supplied for L1 to append under `corpus/lessons/round-60.md` `## Mistakes`. The target lesson file was not found on my initial read, and I did not create or edit it; this seat wrote only this report in the lane.

## Gates

No lane gate, C1 counter, build, or test suite was run. The assigned word-count checker evidence command was run once in my sandbox clone; the M88 replay is a read-only evidence command, not a run of the historical counter. No tool was installed or upgraded.

## Touched surfaces

- Lane: `.ufo/waves/round-60/build/ScribeMistakes.md` only.
- Own scratch: fetched source files and the sandbox clone under `/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/`.

## Out of scope

No edits to `corpus/lessons/round-60.md`, `corpus/lessons/round-59.md`, `plans/round-60.md`, `SKILL.md`, SOURCES, verifiers, or any lane Git/jj state. No commit or push.

## Findings and evidence

- Gemini source fetch (ordinary curl): `date -u` → `Fri Oct 23 12:09:28 PM UTC 2026`; `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' -o hooks.md -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}\n' https://geminicli.com/docs/hooks.md` → `status=200 bytes=8341 url=https://geminicli.com/docs/hooks.md`; `sha256sum hooks.md` → `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`. The two counting commands and outputs are recorded in M86. `ExecR1Recount.md:21` says there is no committed round-59 snapshot of this page; my fetched bytes match the report's digest.
- Gemini best-practices source fetch: `date -u` → `Fri Oct 23 12:20:10 PM UTC 2026`; `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' -o best-practices.md -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}\n' https://geminicli.com/docs/hooks/best-practices.md` → `status=200 bytes=17650 url=https://geminicli.com/docs/hooks/best-practices.md`; `sha256sum best-practices.md` → `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc`; `sed -n '413p' best-practices.md` → ``When you open a project with hooks defined in `.gemini/settings.json`:``; `sed -n '413p' best-practices.md | wc -w` → `10`, exit 0.
- Cursor source fetch: `date -u` → `Fri Oct 23 12:11:18 PM UTC 2026`; `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' -H 'Accept: text/markdown' -o rules.md -w 'status=%{http_code} bytes=%{size_download} url=%{url_effective}\n' https://cursor.com/docs/rules` → `status=200 bytes=17403 url=https://cursor.com/docs/rules`; `sha256sum rules.md` → `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`. This matches `CensusCursor.md:9-12`. `sed -n '65p;99p' rules.md` → ``| `alwaysApply` | `description` | `globs`  | Behavior                                                         |`` and `description: RPC service conventions and patterns for the backend`, exit 0; both are the fetched lines tested by the M88 replay.
- Amendment chronology commands were run read-only in the lane with `timeout 20`, `bash -o pipefail`, and `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin`. Results and exit codes are embedded in M87. **Verbatim conflict:** the task supplied `10:33:44Z` for `bfe8cc2b`; the executed `%cI` command returned `2026-10-23T07:33:42-03:00`, and the executed UTC conversion returned `2026-10-23T10:33:42Z`. Both precede the header's `10:36Z`; I have not replaced either timestamp with the other.
- The checker test sandbox was cloned from the lane and checked out at `31092dc6f875370bddd6eb1e4da4ca0d210c56af`; `git rev-parse HEAD` printed that exact revision. The checker copy and run were confined to that clone. No sandbox commit was made.

## Artifact paths

- Report: `.ufo/waves/round-60/build/ScribeMistakes.md`
- Own scratch: `/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/{hooks.md,best-practices.md,rules.md,sandbox/}`
- Tested checker copy: `/fast/scratch/hyaku/kotoba-r60/ScribeMistakes/sandbox/verifiers/check_word_counts.py` (sha256 `10323e55eefdd61d7e723f4d159acb7c83785cdbccd503e82b64c5c1a4a3b644`)
- Checker source read from the executor's working tree: `/fast/scratch/hyaku/kotoba-r60/ExecWordCountCheck/verifiers/check_word_counts.py`; integration/final artifact not claimed.
