Result: BREAKS — the Events check trims captured spans before applying the frozen regex, so a malformed span can pass; the other requested conjuncts match the frozen plan.

## Findings

### Medium — Events span validation accepts surrounding whitespace

`plans/round-59.md:43` requires at least two distinct backticked spans, each matching `^[A-Za-z][A-Za-z0-9_.:-]*$`. In `verifiers/check_hook_files.py:705-724`, `event_spans()` applies `span.strip()` before `events_cell_why()` tests `EVENT_RE`. Therefore a raw span such as `` ` PreToolUse ` `` does not match the required regex, but is accepted as `PreToolUse`; subsequent page checks search the stripped name (`:1042-1054`). This is a conformance bypass, though the referenced page must still carry the resulting event names.

Evidence: standalone reproduction of the same extraction/validation sequence, command exit 0:
```
python3 -B -c 'import re; backtick=re.compile(r"`([^`]+)`"); event=re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]*$"); cell="` PreToolUse ` `SessionStart`"; spans=[]
for raw in backtick.findall(cell):
 s=raw.strip()
 if s and s not in spans: spans.append(s)
print("raw spans:", backtick.findall(cell)); print("validated spans:", spans); print("regex pass:", [bool(event.match(s)) for s in spans]); print("count:", len(spans))'
```
Output:
```
raw spans: [' PreToolUse ', 'SessionStart']
validated spans: ['PreToolUse', 'SessionStart']
regex pass: [True, True]
count: 2
```

## Conjunct review

| Plan conjunct | Counter code | Result |
|---|---|---|
| Events: >=2 distinct spans, each matching regex; page hits case-sensitive and not inside a longer identifier (`plans/round-59.md:43, 49-52`) | `event_spans`/`events_cell_why`: `verifiers/check_hook_files.py:705-725`; page boundary: `:743-763`, used by `page_why` at `:1051-1054` | Diverges only because captured spans are stripped before regex validation (finding above). Distinct-name count and the frozen `[A-Za-z0-9_]` page boundary are otherwise implemented. |
| Snapshot path and sha256 source: committed `.ufo/waves/round-59/snapshots/<S###>.page`; compare to sha256 in SOURCES row; quote/token/events present (`plans/round-59.md:44-50`) | Path: `:252, 395-397`; first labelled full digest: `:306, 510-517`; committed bytes read with `git show`: `:377-393, 2377-2379`; digest compare and page checks: `:848-865` | Matches. `row_sha()` searches the row’s joined cells for the first `sha256`-labelled 64-hex run; it requires a full run, and the snapshot comparison hashes raw committed bytes. |
| `--fetch`: curl `-sSL`, browser User-Agent, up to 3 attempts (`plans/round-59.md:51-52`) | Curl argv and trailer: `:1058-1082`; `FETCH_ATTEMPTS = 3`: `:260`; retry loop and HTTP-200 requirement: `:1085-1109` | Matches; each attempt includes the browser UA and Accept header, and fetch retries failures up to three times. |
| Pinned host on effective URL (`plans/round-59.md:51-52`) | `curl` writes `%{url_effective}`: `:318-319, 1065-1082`; redirect result checked against client pins: `:1095-1100`; host matcher: `:580-593`; pin map: `:265-282` | Matches. The source URL is pinned as well (`:840-841`), and the post-redirect effective URL is checked. |
| G over FOUND rows only; casefold/normalise distinctness and base exclusions (`plans/round-59.md:53-55`) | FOUND filter and base scan: `:2398-2409`; `.ufo/` exclusion and case-insensitive held test: `:1114-1129, 1170-1229`; distinct count: `:1254-1262` | Matches. `counted` contains only backed rows with `found=True`; without fetch it is empty and G remains zero. |
| Exit 2 cases / predicate (`plans/round-59.md:58-62`; frozen spec `:208-213`) | Invalid hash and setup/read failures: `:2351-2382`; base-tree scan failure: `:2400-2406`; predicate: `:1245-1253, 2423-2425` | Matches the named cases: invalid full hash, non-commit, git/read failures, missing SKILL.md, or unreadable file return 2 without traceback. Fetch failures are row failures, not evaluation failures. With frozen targets, only `--fetch` can return 0, and only when F and G meet their targets. |
| Printed line equals plan sentence (`plans/round-59.md:53-55`) | `summary_line`: `verifiers/check_hook_files.py:1232-1241`; call: `:2410` | Matches exactly for `--fetch`; without fetch it prints `live not run` and G is 0. Frozen `TARGET=4`, `NEW_TARGET=5` are at `:253-254`. |

## Residual risk and verification gaps

The identified false acceptance is limited to whitespace inside a backticked Events span; this review found no other divergence among the requested conjuncts. Review was static/read-only; the full counter and live fetch were not run. Freeze source identity was checked with `git --no-optional-locks show 4b2125c91ea1868a83b7b28eb4bbbacc35f469fe:verifiers/check_hook_files.py | sha256sum` (exit 0): `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  -`.