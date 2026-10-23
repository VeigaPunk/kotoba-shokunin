Result: BREAKS — the independent R5 self-test audit killed 258 of 387 one-at-a-time mutations; 129 survived, including real-result-changing guards and the final CLI predicate.
# Independent frozen C1 counter mutation audit
## Provenance and detector
- Target: `verifiers/check_plugin_manifests.py` from freeze commit `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`; rule/claim: `plans/round-57.md:31-40` (especially R5 at line 40).
- Pristine counter SHA-256, actually printed by `--self-test`: `2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b`. Source size: 74,479 bytes.
- Run checkout: sandbox `ee50d8fa7b5d260fff8bc332f4a90513bee518ff` (`/fast/scratch/hyaku/kotoba-r57/MutC1Counter`). Receipt/definitions commit, made after all runs: sandbox `0d2fbd73db79572758799fdeaaf421d87990f5c7` (`/fast/scratch/hyaku/kotoba-r57/MutC1Counter`). Never pushed.
- **No revision was measured by `--rev`: this assignment audits `--self-test`, not a C1 live-page predicate control.** No real C1 entry/table, network request, C2 fix, lane Git/JJ write, or tool install/update was made. Only the named report/raw receipt were written in the lane.
- Axes: exhaustive production guard/comparison census; detector discrimination; exact-byte isolation/restoration.
- Identical bounded command for every pristine, mutated and restored run:

```sh
timeout 120 env TMPDIR=/fast/scratch/hyaku/kotoba-r57/MutC1Counter/mutation-probe/tmp python3 -B /fast/scratch/hyaku/kotoba-r57/MutC1Counter/mutation-probe/verifiers/check_plugin_manifests.py --self-test
```
- Expected result: pristine/restored exit 0, `self-test: 0 failure(s) over 184 assertions`. Final sequential pass: **387 mutations, 383 distinct mutant byte hashes; 258 killed, 129 survived, zero inconclusive**. Kills: 255 exit 1, two exit 2, one timeout exit 124. The two usage-error kills are detection by process failure, not completed assertion failures.
- M243 deleted the not-found escape in `token_at_boundary` and did not terminate. The same 120-second bound killed it (exit 124; raw receipt at its table link); it is not counted as an assertion failure or a survivor.
- There were 775 completed final detector invocations: one initial baseline, 387 mutants, 387 restorations. Each restoration also serves as the next pristine baseline. All restoration runs passed and printed the pristine hash.
- An earlier non-pty exploratory pass was discarded after tool auto-backgrounding at M243. Only owned job `bg_6315` was cancelled. The entire sweep was then repeated with synchronous completion enforced; **only the repeated pass is tabulated**. The raw receipt discloses the incomplete output and cancellation.
- Raw receipt: `MutC1Counter.txt`; per-mutant rows link to its exact starting line. It includes before/mutant/restored hashes, full actual tool outputs, exit codes and restoration outputs. Sandbox `mutation-probe/manifest.json` reconstructs every edit; `strict-records.json` holds the completed results.
## Scope and census
The independent census covers every production `if` and `while` test and each comparison operator in the backed/found/new-ground call graph, including the real `main` orchestration. It also mutates every production boolean gate, ternary choice, comprehension filter, `not`, typed exception handler and explicit `.lower()`/`.casefold()` normalizer, plus the listed constant/regex/character-boundary sites. Each case replaces one smallest AST/text span in a separate probe copy. No mutation changes a self-test assertion or fixture. Excluded: `self_test`, its three fixture helpers (`held_world`, `_outcome`, `_self_git`) and the Python module-entry `__name__` dispatch; these are not the claimed measurement logic. This is one declared mutation per operator/site, not a claim to enumerate infinitely many possible rewrites.
| Mutation class | Runs |
|---|---:|
| boolean | 45 |
| boundary-drop | 23 |
| case-preserve | 11 |
| casefold-match | 3 |
| choice-negate | 13 |
| comparison | 81 |
| constant-boundary | 7 |
| exception-guard | 6 |
| filter-delete | 12 |
| grammar-boundary | 13 |
| guard-delete | 112 |
| loop-boundary | 5 |
| negation-delete | 37 |
| targeted | 19 |

The production rejection/selection inventory is enumerated, with exact expressions, in the following table: revision/Git/lane guards (244-290); table/section/source parsers (298-440); tracker/host/path/token/foreign guards (452-527); quote/Gate/source/backed guards (536-679); page/token/redirect/size/found guards (719-791); blob/protocol/held guards (799-904); summary/threshold/distinct-ground logic (911-934); CLI input, fetch/count/ground/output/exit logic (1527-1594). Table line numbers refer to the untouched frozen file, not hunk-shifted copies.
## Mutation results
`killed` means the completed bounded detector rejected the mutation. `survived` means exit 0 and all 184 assertions passed. Duplicate final byte strings from distinct syntactic edit spans were deliberately run separately; their identical SHA values are visible in the raw receipt.
| Mutant (one replacement) | Frozen line | Self-test killed/survived | Raw output |
|---|---:|---|---|
| M001 TARGET: <code>5</code> → <code>(5) + (1)</code> | 169 | killed (exit 1) | [raw](MutC1Counter.txt#L19) |
| M002 NEW_TARGET: <code>3</code> → <code>(3) + (1)</code> | 170 | killed (exit 1) | [raw](MutC1Counter.txt#L44) |
| M003 MIN_WORDS: <code>3</code> → <code>(3) + (1)</code> | 171 | killed (exit 1) | [raw](MutC1Counter.txt#L69) |
| M004 MAX_WORDS: <code>25</code> → <code>(25) + (-1)</code> | 172 | killed (exit 1) | [raw](MutC1Counter.txt#L94) |
| M005 MAX_BYTES: <code>5 * 1024 * 1024</code> → <code>(5 * 1024 * 1024) + (-1)</code> | 174 | survived | [raw](MutC1Counter.txt#L119) |
| M006 FETCH_TIMEOUT: <code>30</code> → <code>(30) + (1)</code> | 175 | survived | [raw](MutC1Counter.txt#L141) |
| M007 CHUNK: <code>256</code> → <code>(256) + (1)</code> | 176 | survived | [raw](MutC1Counter.txt#L163) |
| M008 REV_RE: <code>r&quot;^[0-9a-fA-F]{40}$&quot;</code> → <code>&#x27;[0-9a-fA-F]{40}$&#x27;</code> | 210 | survived | [raw](MutC1Counter.txt#L185) |
| M009 REV_RE: <code>r&quot;^[0-9a-fA-F]{40}$&quot;</code> → <code>&#x27;^[0-9a-fA-F]{40}&#x27;</code> | 210 | killed (exit 1) | [raw](MutC1Counter.txt#L207) |
| M010 TOKEN_RE: <code>r&quot;^(~/&#124;\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$&quot;</code> → <code>&#x27;(~/&#124;\\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$&#x27;</code> | 211 | survived | [raw](MutC1Counter.txt#L232) |
| M011 TOKEN_RE: <code>r&quot;^(~/&#124;\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$&quot;</code> → <code>&#x27;^(~/&#124;\\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?&#x27;</code> | 211 | killed (exit 1) | [raw](MutC1Counter.txt#L254) |
| M012 TOKEN_RE: <code>r&quot;^(~/&#124;\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$&quot;</code> → <code>&#x27;^.*$&#x27;</code> | 211 | killed (exit 1) | [raw](MutC1Counter.txt#L279) |
| M013 SID_RE: <code>r&quot;^&#96;?(S\d{3,})&#96;?$&quot;</code> → <code>&#x27;^&#96;?(S\\d{2,})&#96;?$&#x27;</code> | 216 | survived | [raw](MutC1Counter.txt#L304) |
| M014 SID_RE: <code>r&quot;^&#96;?(S\d{3,})&#96;?$&quot;</code> → <code>&#x27;^&#96;?(S\\d{3,})&#96;?&#x27;</code> | 216 | survived | [raw](MutC1Counter.txt#L326) |
| M015 SID_RE: <code>r&quot;^&#96;?(S\d{3,})&#96;?$&quot;</code> → <code>&#x27;^&#96;?([Ss]\\d{3,})&#96;?$&#x27;</code> | 216 | survived | [raw](MutC1Counter.txt#L348) |
| M016 SID_RE: <code>r&quot;^&#96;?(S\d{3,})&#96;?$&quot;</code> → <code>&#x27;&#96;?(S\\d{3,})&#96;?$&#x27;</code> | 216 | survived | [raw](MutC1Counter.txt#L370) |
| M017 SOURCES_ROW_RE: <code>r&quot;^\&#124;[ \t]*S[0-9]{3,}[ \t]*\&#124;&quot;</code> → <code>&#x27;\\&#124;[ \\t]*S[0-9]{3,}[ \\t]*\\&#124;&#x27;</code> | 218 | survived | [raw](MutC1Counter.txt#L392) |
| M018 SOURCES_ROW_RE: <code>r&quot;^\&#124;[ \t]*S[0-9]{3,}[ \t]*\&#124;&quot;</code> → <code>&#x27;^\\&#124;[ \\t]*S[0-9]{2,}[ \\t]*\\&#124;&#x27;</code> | 218 | survived | [raw](MutC1Counter.txt#L414) |
| M019 SOURCES_ROW_RE: <code>r&quot;^\&#124;[ \t]*S[0-9]{3,}[ \t]*\&#124;&quot;</code> → <code>&#x27;^\\&#124;[ \\t]*[Ss][0-9]{3,}[ \\t]*\\&#124;&#x27;</code> | 218 | survived | [raw](MutC1Counter.txt#L436) |
| M020 PLUGIN_WORD_RE: <code>r&quot;\b(?:plugins?&#124;extensions?)\b&quot;</code> → <code>&#x27;(?:plugins?&#124;extensions?)&#x27;</code> | 219 | survived | [raw](MutC1Counter.txt#L458) |
| M021 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&quot; \t\r\n&#96;&#x27;([&quot;)</code> | 221 | killed (exit 1) | [raw](MutC1Counter.txt#L480) |
| M022 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \r\n&#96;&quot;\&#x27;([&#x27;)</code> | 221 | survived | [raw](MutC1Counter.txt#L505) |
| M023 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\n&#96;&quot;\&#x27;([&#x27;)</code> | 221 | survived | [raw](MutC1Counter.txt#L527) |
| M024 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\r\n&quot;\&#x27;([&#x27;)</code> | 221 | killed (exit 1) | [raw](MutC1Counter.txt#L549) |
| M025 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\r\n&#96;&quot;([&#x27;)</code> | 221 | survived | [raw](MutC1Counter.txt#L574) |
| M026 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\r\n&#96;&quot;\&#x27;(&#x27;)</code> | 221 | killed (exit 1) | [raw](MutC1Counter.txt#L596) |
| M027 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\r\n&#96;&quot;\&#x27;[&#x27;)</code> | 221 | killed (exit 1) | [raw](MutC1Counter.txt#L621) |
| M028 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27; \t\r&#96;&quot;\&#x27;([&#x27;)</code> | 221 | survived | [raw](MutC1Counter.txt#L646) |
| M029 BOUNDARY_PREV: <code>frozenset(&quot; \t\r\n&#96;\&quot;&#x27;([&quot;)</code> → <code>frozenset(&#x27;\t\r\n&#96;&quot;\&#x27;([&#x27;)</code> | 221 | killed (exit 1) | [raw](MutC1Counter.txt#L668) |
| M030 ASCII_ALNUM: <code>frozenset(string.ascii_letters + string.digits)</code> → <code>(frozenset(string.ascii_letters + string.digits)) - frozenset(&#x27;0&#x27;)</code> | 223 | survived | [raw](MutC1Counter.txt#L696) |
| M031 ASCII_ALNUM: <code>frozenset(string.ascii_letters + string.digits)</code> → <code>(frozenset(string.ascii_letters + string.digits)) - frozenset(&#x27;A&#x27;)</code> | 223 | survived | [raw](MutC1Counter.txt#L718) |
| M032 ASCII_ALNUM: <code>frozenset(string.ascii_letters + string.digits)</code> → <code>(frozenset(string.ascii_letters + string.digits)) - frozenset(&#x27;a&#x27;)</code> | 223 | survived | [raw](MutC1Counter.txt#L740) |
| M033 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&quot;&#96;&#x27;([&lt;/~=&quot;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L762) |
| M034 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&quot;\&#x27;([&lt;/~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L787) |
| M035 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;([&lt;/~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L813) |
| M036 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;(&lt;/~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L838) |
| M037 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;([/~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L863) |
| M038 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;([&lt;/=&#x27;)</code> | 224 | survived | [raw](MutC1Counter.txt#L888) |
| M039 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;([&lt;/~&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L910) |
| M040 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;([&lt;~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L935) |
| M041 HELD_PREV: <code>frozenset(&quot;&#96;\&quot;&#x27;([&lt;/~=&quot;)</code> → <code>frozenset(&#x27;&#96;&quot;\&#x27;[&lt;/~=&#x27;)</code> | 224 | killed (exit 1) | [raw](MutC1Counter.txt#L962) |
| M042 HELD_NEXT_BAD: <code>frozenset(string.ascii_letters + string.digits + &quot;_-&quot;)</code> → <code>(frozenset(string.ascii_letters + string.digits + &quot;_-&quot;)) - frozenset(&#x27;-&#x27;)</code> | 225 | killed (exit 1) | [raw](MutC1Counter.txt#L987) |
| M043 HELD_NEXT_BAD: <code>frozenset(string.ascii_letters + string.digits + &quot;_-&quot;)</code> → <code>(frozenset(string.ascii_letters + string.digits + &quot;_-&quot;)) - frozenset(&#x27;_&#x27;)</code> | 225 | killed (exit 1) | [raw](MutC1Counter.txt#L1012) |
| M044 lane_dir: <code>here.name == &quot;verifiers&quot;</code> → <code>here.name != &quot;verifiers&quot;</code> | 244 | survived | [raw](MutC1Counter.txt#L1037) |
| M045 lane_dir: <code>here.name == &quot;verifiers&quot;</code> → <code>False</code> | 244 | survived | [raw](MutC1Counter.txt#L1059) |
| M046 lane_dir: <code>(cand / &quot;SKILL.md&quot;).is_file() and (cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file()</code> → <code>((cand / &quot;SKILL.md&quot;).is_file()) or ((cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file())</code> | 248 | survived | [raw](MutC1Counter.txt#L1081) |
| M047 lane_dir: <code>(cand / &quot;SKILL.md&quot;).is_file() and (cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file()</code> → <code>False</code> | 248 | survived | [raw](MutC1Counter.txt#L1103) |
| M048 lane_dir: <code>(cand / &quot;SKILL.md&quot;).is_file() and (cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file()</code> → <code>((cand / &quot;SKILL.md&quot;).is_file()) or ((cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file())</code> | 253 | survived | [raw](MutC1Counter.txt#L1125) |
| M049 lane_dir: <code>(cand / &quot;SKILL.md&quot;).is_file() and (cand / &quot;corpus&quot; / &quot;SOURCES.md&quot;).is_file()</code> → <code>False</code> | 253 | survived | [raw](MutC1Counter.txt#L1147) |
| M050 git: <code>OSError</code> → <code>RuntimeError</code> | 268 | survived | [raw](MutC1Counter.txt#L1169) |
| M051 rev_ok: <code>bool(rev) and REV_RE.match(rev) is not None</code> → <code>(bool(rev)) or (REV_RE.match(rev) is not None)</code> | 274 | killed (exit 1) | [raw](MutC1Counter.txt#L1191) |
| M052 rev_ok: <code>REV_RE.match(rev) is not None</code> → <code>REV_RE.match(rev) is None</code> | 274 | killed (exit 1) | [raw](MutC1Counter.txt#L1231) |
| M053 verify_rev: <code>r.returncode != 0</code> → <code>r.returncode == 0</code> | 280 | killed (exit 1) | [raw](MutC1Counter.txt#L1262) |
| M054 verify_rev: <code>r.returncode != 0</code> → <code>False</code> | 280 | killed (exit 1) | [raw](MutC1Counter.txt#L1288) |
| M055 git_show: <code>r.returncode != 0</code> → <code>r.returncode == 0</code> | 286 | killed (exit 1) | [raw](MutC1Counter.txt#L1313) |
| M056 git_show: <code>r.returncode != 0</code> → <code>False</code> | 286 | killed (exit 1) | [raw](MutC1Counter.txt#L1339) |
| M057 git_show: <code>&quot;does not exist&quot; in err or &quot;exists on disk, but not in&quot; in err</code> → <code>(&quot;does not exist&quot; in err) and (&quot;exists on disk, but not in&quot; in err)</code> | 288 | killed (exit 1) | [raw](MutC1Counter.txt#L1364) |
| M058 git_show: <code>&quot;does not exist&quot; in err</code> → <code>&quot;does not exist&quot; not in err</code> | 288 | killed (exit 1) | [raw](MutC1Counter.txt#L1389) |
| M059 git_show: <code>&quot;does not exist&quot; in err or &quot;exists on disk, but not in&quot; in err</code> → <code>False</code> | 288 | killed (exit 1) | [raw](MutC1Counter.txt#L1414) |
| M060 git_show: <code>&quot;exists on disk, but not in&quot; in err</code> → <code>&quot;exists on disk, but not in&quot; not in err</code> | 288 | survived | [raw](MutC1Counter.txt#L1439) |
| M061 cells: <code>not (s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;)) or len(s) &lt; 2</code> → <code>(not (s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;))) and (len(s) &lt; 2)</code> | 298 | survived | [raw](MutC1Counter.txt#L1461) |
| M062 cells: <code>not (s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;)) or len(s) &lt; 2</code> → <code>False</code> | 298 | survived | [raw](MutC1Counter.txt#L1483) |
| M063 cells: <code>not (s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;))</code> → <code>(s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;))</code> | 298 | killed (exit 1) | [raw](MutC1Counter.txt#L1505) |
| M064 cells: <code>s.startswith(&quot;&#124;&quot;) and s.endswith(&quot;&#124;&quot;)</code> → <code>(s.startswith(&quot;&#124;&quot;)) or (s.endswith(&quot;&#124;&quot;))</code> | 298 | survived | [raw](MutC1Counter.txt#L1563) |
| M065 cells: <code>len(s) &lt; 2</code> → <code>len(s) &lt;= 2</code> | 298 | survived | [raw](MutC1Counter.txt#L1585) |
| M066 clean: <code>re.sub(r&quot;[&#96;*]&quot;, &quot;&quot;, cell).strip().lower()</code> → <code>(re.sub(r&quot;[&#96;*]&quot;, &quot;&quot;, cell).strip())</code> | 305 | killed (exit 1) | [raw](MutC1Counter.txt#L1607) |
| M067 is_separator: <code>bool(row) and all(SEPARATOR_RE.fullmatch(x) for x in row)</code> → <code>(bool(row)) or (all(SEPARATOR_RE.fullmatch(x) for x in row))</code> | 314 | killed (exit 1) | [raw](MutC1Counter.txt#L1665) |
| M068 tables: <code>not block</code> → <code>False</code> | 322 | killed (exit 1) | [raw](MutC1Counter.txt#L1723) |
| M069 tables: <code>not block</code> → <code>(block)</code> | 322 | killed (exit 1) | [raw](MutC1Counter.txt#L1769) |
| M070 tables: <code>not c or is_separator(c)</code> → <code>(not c) and (is_separator(c))</code> | 328 | survived | [raw](MutC1Counter.txt#L1815) |
| M071 tables: <code>not c or is_separator(c)</code> → <code>False</code> | 328 | survived | [raw](MutC1Counter.txt#L1837) |
| M072 tables: <code>not c</code> → <code>(c)</code> | 328 | killed (exit 1) | [raw](MutC1Counter.txt#L1859) |
| M073 tables: <code>ln.strip().startswith(&quot;&#124;&quot;)</code> → <code>False</code> | 335 | killed (exit 1) | [raw](MutC1Counter.txt#L1917) |
| M074 tables: <code>got is not None</code> → <code>got is None</code> | 339 | killed (exit 1) | [raw](MutC1Counter.txt#L1975) |
| M075 tables: <code>got is not None</code> → <code>False</code> | 339 | survived | [raw](MutC1Counter.txt#L2016) |
| M076 tables: <code>got is not None</code> → <code>got is None</code> | 342 | killed (exit 1) | [raw](MutC1Counter.txt#L2038) |
| M077 tables: <code>got is not None</code> → <code>False</code> | 342 | killed (exit 1) | [raw](MutC1Counter.txt#L2096) |
| M078 section_lines: <code>m</code> → <code>False</code> | 353 | killed (exit 1) | [raw](MutC1Counter.txt#L2154) |
| M079 section_lines: <code>ln.rstrip() == heading</code> → <code>ln.rstrip() != heading</code> | 354 | killed (exit 1) | [raw](MutC1Counter.txt#L2211) |
| M080 section_lines: <code>ln.rstrip() == heading</code> → <code>False</code> | 354 | killed (exit 1) | [raw](MutC1Counter.txt#L2269) |
| M081 section_lines: <code>inside and len(m.group(1)) &lt;= level</code> → <code>(inside) or (len(m.group(1)) &lt;= level)</code> | 357 | killed (exit 1) | [raw](MutC1Counter.txt#L2326) |
| M082 section_lines: <code>inside and len(m.group(1)) &lt;= level</code> → <code>False</code> | 357 | survived | [raw](MutC1Counter.txt#L2383) |
| M083 section_lines: <code>len(m.group(1)) &lt;= level</code> → <code>len(m.group(1)) &lt; level</code> | 357 | survived | [raw](MutC1Counter.txt#L2405) |
| M084 section_lines: <code>inside</code> → <code>False</code> | 360 | killed (exit 1) | [raw](MutC1Counter.txt#L2427) |
| M085 skill_rows: <code>not sec</code> → <code>False</code> | 370 | survived | [raw](MutC1Counter.txt#L2484) |
| M086 skill_rows: <code>not sec</code> → <code>(sec)</code> | 370 | killed (exit 1) | [raw](MutC1Counter.txt#L2506) |
| M087 skill_rows: <code>tuple(clean(x) for x in head[:len(SKILL_HEADER)]) == SKILL_HEADER</code> → <code>tuple(clean(x) for x in head[:len(SKILL_HEADER)]) != SKILL_HEADER</code> | 373 | killed (exit 1) | [raw](MutC1Counter.txt#L2563) |
| M088 skill_rows: <code>tuple(clean(x) for x in head[:len(SKILL_HEADER)]) == SKILL_HEADER</code> → <code>False</code> | 373 | killed (exit 1) | [raw](MutC1Counter.txt#L2621) |
| M089 entry_rows: <code>tuple(clean(x) for x in head[:len(ENTRY_HEADER)]) == ENTRY_HEADER</code> → <code>tuple(clean(x) for x in head[:len(ENTRY_HEADER)]) != ENTRY_HEADER</code> | 382 | killed (exit 1) | [raw](MutC1Counter.txt#L2678) |
| M090 entry_rows: <code>tuple(clean(x) for x in head[:len(ENTRY_HEADER)]) == ENTRY_HEADER</code> → <code>False</code> | 382 | killed (exit 1) | [raw](MutC1Counter.txt#L2735) |
| M091 sources_table: <code>SOURCES_ROW_RE.match(ln)</code> → <code>False</code> | 393 | killed (exit 1) | [raw](MutC1Counter.txt#L2791) |
| M092 sources_table: <code>len(c) == 13</code> → <code>len(c) != 13</code> | 395 | killed (exit 1) | [raw](MutC1Counter.txt#L2847) |
| M093 sources_table: <code>len(c) == 13</code> → <code>False</code> | 395 | killed (exit 1) | [raw](MutC1Counter.txt#L2903) |
| M094 source_ids: <code>SOURCES_ROW_RE.match(ln)</code> → <code>True</code> | 401 | survived | [raw](MutC1Counter.txt#L2959) |
| M095 urls_of: <code>u</code> → <code>False</code> | 409 | killed (exit 1) | [raw](MutC1Counter.txt#L2981) |
| M096 url_key: <code>not url</code> → <code>False</code> | 418 | killed (exit 1) | [raw](MutC1Counter.txt#L3036) |
| M097 url_key: <code>not url</code> → <code>(url)</code> | 418 | killed (exit 1) | [raw](MutC1Counter.txt#L3061) |
| M098 url_key: <code>(u.hostname or &quot;&quot;).lower()</code> → <code>(u.hostname or &quot;&quot;)</code> | 421 | survived | [raw](MutC1Counter.txt#L3121) |
| M099 url_key: <code>u.hostname or &quot;&quot;</code> → <code>(u.hostname) and (&quot;&quot;)</code> | 421 | killed (exit 1) | [raw](MutC1Counter.txt#L3143) |
| M100 url_key: <code>host.startswith(&quot;www.&quot;)</code> → <code>False</code> | 422 | killed (exit 1) | [raw](MutC1Counter.txt#L3171) |
| M101 url_key: <code>urllib.parse.unquote(u.path or &quot;&quot;).lower()</code> → <code>(urllib.parse.unquote(u.path or &quot;&quot;))</code> | 424 | killed (exit 1) | [raw](MutC1Counter.txt#L3196) |
| M102 url_key: <code>u.path or &quot;&quot;</code> → <code>(u.path) and (&quot;&quot;)</code> | 424 | killed (exit 1) | [raw](MutC1Counter.txt#L3223) |
| M103 url_key: <code>path.endswith(&quot;/&quot;)</code> → <code>False</code> | 426 | killed (exit 1) | [raw](MutC1Counter.txt#L3267) |
| M104 url_key: <code>path.endswith(&quot;.md&quot;)</code> → <code>False</code> | 428 | killed (exit 1) | [raw](MutC1Counter.txt#L3292) |
| M105 url_key: <code>path.endswith(&quot;/&quot;)</code> → <code>False</code> | 430 | survived | [raw](MutC1Counter.txt#L3319) |
| M106 base_url_keys: <code>SOURCES_ROW_RE.match(ln)</code> → <code>False</code> | 438 | killed (exit 1) | [raw](MutC1Counter.txt#L3341) |
| M107 base_url_keys: <code>len(c) &gt; 2</code> → <code>len(c) &gt;= 2</code> | 440 | survived | [raw](MutC1Counter.txt#L3367) |
| M108 base_url_keys: <code>len(c) &gt; 2</code> → <code>False</code> | 440 | killed (exit 1) | [raw](MutC1Counter.txt#L3389) |
| M109 url_is_tracker: <code>urllib.parse.unquote(urllib.parse.urlsplit(url).path or &quot;&quot;).lower()</code> → <code>(urllib.parse.unquote(urllib.parse.urlsplit(url).path or &quot;&quot;))</code> | 452 | survived | [raw](MutC1Counter.txt#L3415) |
| M110 url_is_tracker: <code>urllib.parse.urlsplit(url).path or &quot;&quot;</code> → <code>(urllib.parse.urlsplit(url).path) and (&quot;&quot;)</code> | 452 | killed (exit 1) | [raw](MutC1Counter.txt#L3437) |
| M111 url_is_tracker: <code>seg in TRACKER_SEGMENTS</code> → <code>seg not in TRACKER_SEGMENTS</code> | 453 | killed (exit 1) | [raw](MutC1Counter.txt#L3463) |
| M112 url_is_tracker: <code>seg</code> → <code>True</code> | 453 | survived | [raw](MutC1Counter.txt#L3519) |
| M113 host_ok: <code>(u.hostname or &quot;&quot;).lower()</code> → <code>(u.hostname or &quot;&quot;)</code> | 458 | survived | [raw](MutC1Counter.txt#L3541) |
| M114 host_ok: <code>u.hostname or &quot;&quot;</code> → <code>(u.hostname) and (&quot;&quot;)</code> | 458 | killed (exit 1) | [raw](MutC1Counter.txt#L3563) |
| M115 host_ok: <code>any(seg in (&quot;.&quot;, &quot;..&quot;) for seg in urllib.parse.unquote(path).split(&quot;/&quot;))</code> → <code>False</code> | 459 | killed (exit 1) | [raw](MutC1Counter.txt#L3621) |
| M116 host_ok: <code>seg in (&quot;.&quot;, &quot;..&quot;)</code> → <code>seg not in (&quot;.&quot;, &quot;..&quot;)</code> | 459 | killed (exit 1) | [raw](MutC1Counter.txt#L3646) |
| M117 host_ok: <code>p</code> → <code>False</code> | 463 | killed (exit 1) | [raw](MutC1Counter.txt#L3704) |
| M118 host_ok: <code>host == h and (path == prefix or path.startswith(prefix + &quot;/&quot;))</code> → <code>(host == h) or (path == prefix or path.startswith(prefix + &quot;/&quot;))</code> | 465 | killed (exit 1) | [raw](MutC1Counter.txt#L3729) |
| M119 host_ok: <code>host == h</code> → <code>host != h</code> | 465 | survived | [raw](MutC1Counter.txt#L3754) |
| M120 host_ok: <code>host == h and (path == prefix or path.startswith(prefix + &quot;/&quot;))</code> → <code>False</code> | 465 | killed (exit 1) | [raw](MutC1Counter.txt#L3776) |
| M121 host_ok: <code>path == prefix or path.startswith(prefix + &quot;/&quot;)</code> → <code>(path == prefix) and (path.startswith(prefix + &quot;/&quot;))</code> | 465 | killed (exit 1) | [raw](MutC1Counter.txt#L3801) |
| M122 host_ok: <code>path == prefix</code> → <code>path != prefix</code> | 465 | killed (exit 1) | [raw](MutC1Counter.txt#L3826) |
| M123 host_ok: <code>host == h or host.endswith(&quot;.&quot; + h)</code> → <code>(host == h) and (host.endswith(&quot;.&quot; + h))</code> | 467 | killed (exit 1) | [raw](MutC1Counter.txt#L3851) |
| M124 host_ok: <code>host == h</code> → <code>host != h</code> | 467 | killed (exit 1) | [raw](MutC1Counter.txt#L3908) |
| M125 host_ok: <code>host == h or host.endswith(&quot;.&quot; + h)</code> → <code>False</code> | 467 | killed (exit 1) | [raw](MutC1Counter.txt#L3954) |
| M126 token_well_formed: <code>not token or not TOKEN_RE.match(token)</code> → <code>(not token) and (not TOKEN_RE.match(token))</code> | 476 | killed (exit 1) | [raw](MutC1Counter.txt#L4011) |
| M127 token_well_formed: <code>not token or not TOKEN_RE.match(token)</code> → <code>False</code> | 476 | killed (exit 1) | [raw](MutC1Counter.txt#L4036) |
| M128 token_well_formed: <code>not token</code> → <code>(token)</code> | 476 | killed (exit 1) | [raw](MutC1Counter.txt#L4061) |
| M129 token_well_formed: <code>not TOKEN_RE.match(token)</code> → <code>(TOKEN_RE.match(token))</code> | 476 | killed (exit 1) | [raw](MutC1Counter.txt#L4123) |
| M130 token_well_formed: <code>s</code> → <code>True</code> | 478 | survived | [raw](MutC1Counter.txt#L4186) |
| M131 token_well_formed: <code>any(MARKETPLACE in s.lower() for s in segs)</code> → <code>False</code> | 479 | killed (exit 1) | [raw](MutC1Counter.txt#L4208) |
| M132 token_well_formed: <code>MARKETPLACE in s.lower()</code> → <code>MARKETPLACE not in s.lower()</code> | 479 | killed (exit 1) | [raw](MutC1Counter.txt#L4234) |
| M133 token_well_formed: <code>s.lower()</code> → <code>(s)</code> | 479 | survived | [raw](MutC1Counter.txt#L4296) |
| M134 token_well_formed: <code>w.lower()</code> → <code>(w)</code> | 481 | survived | [raw](MutC1Counter.txt#L4318) |
| M135 token_well_formed: <code>w</code> → <code>True</code> | 481 | survived | [raw](MutC1Counter.txt#L4340) |
| M136 token_well_formed: <code>w in PLUGIN_WORDS</code> → <code>w not in PLUGIN_WORDS</code> | 482 | killed (exit 1) | [raw](MutC1Counter.txt#L4362) |
| M137 foreign_marker: <code>(token or &quot;&quot;).lower()</code> → <code>(token or &quot;&quot;)</code> | 487 | killed (exit 1) | [raw](MutC1Counter.txt#L4390) |
| M138 foreign_marker: <code>token or &quot;&quot;</code> → <code>(token) and (&quot;&quot;)</code> | 487 | killed (exit 1) | [raw](MutC1Counter.txt#L4415) |
| M139 foreign_marker: <code>other != client and MARKERS[other] in low</code> → <code>(other != client) or (MARKERS[other] in low)</code> | 489 | killed (exit 1) | [raw](MutC1Counter.txt#L4443) |
| M140 foreign_marker: <code>other != client</code> → <code>other == client</code> | 489 | killed (exit 1) | [raw](MutC1Counter.txt#L4502) |
| M141 foreign_marker: <code>other != client and MARKERS[other] in low</code> → <code>False</code> | 489 | killed (exit 1) | [raw](MutC1Counter.txt#L4563) |
| M142 foreign_marker: <code>MARKERS[other] in low</code> → <code>MARKERS[other] not in low</code> | 489 | killed (exit 1) | [raw](MutC1Counter.txt#L4591) |
| M143 normalise: <code>not token</code> → <code>False</code> | 496 | killed (exit 1) | [raw](MutC1Counter.txt#L4652) |
| M144 normalise: <code>not token</code> → <code>(token)</code> | 496 | killed (exit 1) | [raw](MutC1Counter.txt#L4688) |
| M145 normalise: <code>t.startswith(pre)</code> → <code>False</code> | 500 | killed (exit 1) | [raw](MutC1Counter.txt#L4729) |
| M146 normalise: <code>t.endswith(&quot;/&quot;)</code> → <code>False</code> | 503 | killed (exit 1) | [raw](MutC1Counter.txt#L4756) |
| M147 token_span: <code>not token</code> → <code>False</code> | 510 | survived | [raw](MutC1Counter.txt#L4785) |
| M148 token_span: <code>not token</code> → <code>(token)</code> | 510 | killed (exit 1) | [raw](MutC1Counter.txt#L4807) |
| M149 token_span: <code>not form</code> → <code>False</code> | 514 | survived | [raw](MutC1Counter.txt#L4841) |
| M150 token_span: <code>not form</code> → <code>(form)</code> | 514 | killed (exit 1) | [raw](MutC1Counter.txt#L4863) |
| M151 token_span: <code>text.find(form)</code> → <code>text.casefold().find(form.casefold())</code> | 516 | killed (exit 1) | [raw](MutC1Counter.txt#L4897) |
| M152 token_span: <code>i &lt; 0</code> → <code>i &lt;= 0</code> | 517 | survived | [raw](MutC1Counter.txt#L4923) |
| M153 token_span: <code>i &lt; 0</code> → <code>False</code> | 517 | killed (exit 1) | [raw](MutC1Counter.txt#L4945) |
| M154 token_span: <code>best is None or i &lt; best[0]</code> → <code>(best is None) and (i &lt; best[0])</code> | 519 | killed (exit 1) | [raw](MutC1Counter.txt#L4972) |
| M155 token_span: <code>best is None</code> → <code>best is not None</code> | 519 | killed (exit 1) | [raw](MutC1Counter.txt#L5007) |
| M156 token_span: <code>best is None or i &lt; best[0]</code> → <code>False</code> | 519 | killed (exit 1) | [raw](MutC1Counter.txt#L5042) |
| M157 token_span: <code>i &lt; best[0]</code> → <code>i &lt;= best[0]</code> | 519 | survived | [raw](MutC1Counter.txt#L5076) |
| M158 plugin_word_outside: <code>m.end() &lt;= start or m.start() &gt;= end</code> → <code>(m.end() &lt;= start) and (m.start() &gt;= end)</code> | 527 | killed (exit 1) | [raw](MutC1Counter.txt#L5098) |
| M159 plugin_word_outside: <code>m.end() &lt;= start</code> → <code>m.end() &lt; start</code> | 527 | survived | [raw](MutC1Counter.txt#L5154) |
| M160 plugin_word_outside: <code>m.end() &lt;= start or m.start() &gt;= end</code> → <code>False</code> | 527 | killed (exit 1) | [raw](MutC1Counter.txt#L5176) |
| M161 plugin_word_outside: <code>m.start() &gt;= end</code> → <code>m.start() &gt; end</code> | 527 | survived | [raw](MutC1Counter.txt#L5232) |
| M162 strip_quotes: <code>len(s) &gt;= 2 and s.startswith(a) and s.endswith(b)</code> → <code>(len(s) &gt;= 2) or (s.startswith(a)) or (s.endswith(b))</code> | 536 | killed (exit 1) | [raw](MutC1Counter.txt#L5254) |
| M163 strip_quotes: <code>len(s) &gt;= 2</code> → <code>len(s) &gt; 2</code> | 536 | survived | [raw](MutC1Counter.txt#L5279) |
| M164 strip_quotes: <code>len(s) &gt;= 2 and s.startswith(a) and s.endswith(b)</code> → <code>False</code> | 536 | killed (exit 1) | [raw](MutC1Counter.txt#L5301) |
| M165 quote_in_gate: <code>ws(quote) in gate_raw or ws(quote.replace(&quot;&#96;&quot;, &quot;&quot;)) in gate_plain</code> → <code>(ws(quote) in gate_raw) and (ws(quote.replace(&quot;&#96;&quot;, &quot;&quot;)) in gate_plain)</code> | 547 | survived | [raw](MutC1Counter.txt#L5327) |
| M166 quote_in_gate: <code>ws(quote) in gate_raw</code> → <code>ws(quote) not in gate_raw</code> | 547 | killed (exit 1) | [raw](MutC1Counter.txt#L5349) |
| M167 quote_in_gate: <code>ws(quote.replace(&quot;&#96;&quot;, &quot;&quot;)) in gate_plain</code> → <code>ws(quote.replace(&quot;&#96;&quot;, &quot;&quot;)) not in gate_plain</code> | 547 | killed (exit 1) | [raw](MutC1Counter.txt#L5376) |
| M168 entry_row_verdict: <code>m</code> → <code>not (m)</code> | 563 | killed (exit 1) | [raw](MutC1Counter.txt#L5403) |
| M169 entry_row_verdict: <code>not sid</code> → <code>False</code> | 564 | killed (exit 1) | [raw](MutC1Counter.txt#L5474) |
| M170 entry_row_verdict: <code>not sid</code> → <code>(sid)</code> | 564 | killed (exit 1) | [raw](MutC1Counter.txt#L5499) |
| M171 entry_row_verdict: <code>not MIN_WORDS &lt;= n &lt;= MAX_WORDS</code> → <code>False</code> | 569 | killed (exit 1) | [raw](MutC1Counter.txt#L5554) |
| M172 entry_row_verdict: <code>not MIN_WORDS &lt;= n &lt;= MAX_WORDS</code> → <code>(MIN_WORDS &lt;= n &lt;= MAX_WORDS)</code> | 569 | killed (exit 1) | [raw](MutC1Counter.txt#L5580) |
| M173 entry_row_verdict: <code>MIN_WORDS &lt;= n &lt;= MAX_WORDS</code> → <code>MIN_WORDS &lt; n &lt;= MAX_WORDS</code> | 569 | survived | [raw](MutC1Counter.txt#L5635) |
| M174 entry_row_verdict: <code>MIN_WORDS &lt;= n &lt;= MAX_WORDS</code> → <code>MIN_WORDS &lt;= n &lt; MAX_WORDS</code> | 569 | survived | [raw](MutC1Counter.txt#L5657) |
| M175 entry_row_verdict: <code>token</code> → <code>False</code> | 571 | killed (exit 1) | [raw](MutC1Counter.txt#L5679) |
| M176 entry_row_verdict: <code>span is None</code> → <code>span is not None</code> | 573 | killed (exit 1) | [raw](MutC1Counter.txt#L5706) |
| M177 entry_row_verdict: <code>span is None</code> → <code>False</code> | 573 | killed (exit 1) | [raw](MutC1Counter.txt#L5754) |
| M178 entry_row_verdict: <code>not plugin_word_outside(q_plain, span[0], span[1])</code> → <code>False</code> | 576 | killed (exit 1) | [raw](MutC1Counter.txt#L5800) |
| M179 entry_row_verdict: <code>not plugin_word_outside(q_plain, span[0], span[1])</code> → <code>(plugin_word_outside(q_plain, span[0], span[1]))</code> | 576 | killed (exit 1) | [raw](MutC1Counter.txt#L5825) |
| M180 entry_row_verdict: <code>not quote_in_gate(quote, gate_raw, gate_plain)</code> → <code>False</code> | 578 | killed (exit 1) | [raw](MutC1Counter.txt#L5880) |
| M181 entry_row_verdict: <code>not quote_in_gate(quote, gate_raw, gate_plain)</code> → <code>(quote_in_gate(quote, gate_raw, gate_plain))</code> | 578 | killed (exit 1) | [raw](MutC1Counter.txt#L5905) |
| M182 entry_row_verdict: <code>sid</code> → <code>False</code> | 580 | killed (exit 1) | [raw](MutC1Counter.txt#L5960) |
| M183 entry_row_verdict: <code>sid in at_base</code> → <code>sid not in at_base</code> | 581 | killed (exit 1) | [raw](MutC1Counter.txt#L5997) |
| M184 entry_row_verdict: <code>sid in at_base</code> → <code>False</code> | 581 | killed (exit 1) | [raw](MutC1Counter.txt#L6052) |
| M185 entry_row_verdict: <code>not s</code> → <code>False</code> | 584 | killed (exit 1) | [raw](MutC1Counter.txt#L6077) |
| M186 entry_row_verdict: <code>not s</code> → <code>(s)</code> | 584 | killed (exit 1) | [raw](MutC1Counter.txt#L6123) |
| M187 entry_row_verdict: <code>s[2] != &quot;docs&quot;</code> → <code>s[2] == &quot;docs&quot;</code> | 587 | killed (exit 1) | [raw](MutC1Counter.txt#L6196) |
| M188 entry_row_verdict: <code>s[2] != &quot;docs&quot;</code> → <code>False</code> | 587 | killed (exit 1) | [raw](MutC1Counter.txt#L6251) |
| M189 entry_row_verdict: <code>s[3] != &quot;A&quot;</code> → <code>s[3] == &quot;A&quot;</code> | 589 | killed (exit 1) | [raw](MutC1Counter.txt#L6276) |
| M190 entry_row_verdict: <code>s[3] != &quot;A&quot;</code> → <code>False</code> | 589 | killed (exit 1) | [raw](MutC1Counter.txt#L6331) |
| M191 entry_row_verdict: <code>s[7] != &quot;mined&quot;</code> → <code>s[7] == &quot;mined&quot;</code> | 591 | killed (exit 1) | [raw](MutC1Counter.txt#L6356) |
| M192 entry_row_verdict: <code>s[7] != &quot;mined&quot;</code> → <code>False</code> | 591 | killed (exit 1) | [raw](MutC1Counter.txt#L6411) |
| M193 entry_row_verdict: <code>s[8] not in OPENED</code> → <code>s[8] in OPENED</code> | 593 | killed (exit 1) | [raw](MutC1Counter.txt#L6436) |
| M194 entry_row_verdict: <code>s[8] not in OPENED</code> → <code>False</code> | 593 | killed (exit 1) | [raw](MutC1Counter.txt#L6491) |
| M195 entry_row_verdict: <code>urls</code> → <code>not (urls)</code> | 596 | killed (exit 1) | [raw](MutC1Counter.txt#L6516) |
| M196 entry_row_verdict: <code>not url</code> → <code>False</code> | 597 | killed (exit 1) | [raw](MutC1Counter.txt#L6578) |
| M197 entry_row_verdict: <code>not url</code> → <code>(url)</code> | 597 | killed (exit 1) | [raw](MutC1Counter.txt#L6603) |
| M198 entry_row_verdict: <code>url_key(url) in base_urls</code> → <code>url_key(url) not in base_urls</code> | 600 | killed (exit 1) | [raw](MutC1Counter.txt#L6659) |
| M199 entry_row_verdict: <code>url_key(url) in base_urls</code> → <code>False</code> | 600 | killed (exit 1) | [raw](MutC1Counter.txt#L6714) |
| M200 entry_row_verdict: <code>not host_ok(url, HOSTS[client])</code> → <code>False</code> | 602 | killed (exit 1) | [raw](MutC1Counter.txt#L6740) |
| M201 entry_row_verdict: <code>not host_ok(url, HOSTS[client])</code> → <code>(host_ok(url, HOSTS[client]))</code> | 602 | killed (exit 1) | [raw](MutC1Counter.txt#L6765) |
| M202 entry_row_verdict: <code>url_is_tracker(url)</code> → <code>False</code> | 604 | killed (exit 1) | [raw](MutC1Counter.txt#L6820) |
| M203 judge: <code>client_name(r[0]) == client</code> → <code>client_name(r[0]) != client</code> | 626 | killed (exit 1) | [raw](MutC1Counter.txt#L6845) |
| M204 judge: <code>client_name(r[0]) == client</code> → <code>True</code> | 626 | killed (exit 1) | [raw](MutC1Counter.txt#L6900) |
| M205 judge: <code>len(smine) != 1</code> → <code>len(smine) == 1</code> | 627 | killed (exit 1) | [raw](MutC1Counter.txt#L6957) |
| M206 judge: <code>len(smine) != 1</code> → <code>False</code> | 627 | killed (exit 1) | [raw](MutC1Counter.txt#L7014) |
| M207 judge: <code>smine</code> → <code>not (smine)</code> | 630 | killed (exit 1) | [raw](MutC1Counter.txt#L7039) |
| M208 judge: <code>spans[0]</code> → <code>spans[-1]</code> | 632 | survived | [raw](MutC1Counter.txt#L7095) |
| M209 judge: <code>spans</code> → <code>not (spans)</code> | 632 | killed (exit 1) | [raw](MutC1Counter.txt#L7117) |
| M210 judge: <code>token is None</code> → <code>token is not None</code> | 633 | killed (exit 1) | [raw](MutC1Counter.txt#L7174) |
| M211 judge: <code>token is None</code> → <code>False</code> | 633 | killed (exit 1) | [raw](MutC1Counter.txt#L7231) |
| M212 judge: <code>not token_well_formed(token)</code> → <code>False</code> | 635 | killed (exit 1) | [raw](MutC1Counter.txt#L7256) |
| M213 judge: <code>not token_well_formed(token)</code> → <code>(token_well_formed(token))</code> | 635 | killed (exit 1) | [raw](MutC1Counter.txt#L7281) |
| M214 judge: <code>other</code> → <code>False</code> | 641 | killed (exit 1) | [raw](MutC1Counter.txt#L7337) |
| M215 judge: <code>len(words) &lt; 3</code> → <code>len(words) &lt;= 3</code> | 645 | survived | [raw](MutC1Counter.txt#L7362) |
| M216 judge: <code>len(words) &lt; 3</code> → <code>False</code> | 645 | killed (exit 1) | [raw](MutC1Counter.txt#L7384) |
| M217 judge: <code>client_name(r[0]) == client</code> → <code>client_name(r[0]) != client</code> | 647 | killed (exit 1) | [raw](MutC1Counter.txt#L7409) |
| M218 judge: <code>client_name(r[0]) == client</code> → <code>True</code> | 647 | survived | [raw](MutC1Counter.txt#L7465) |
| M219 judge: <code>not row_why</code> → <code>False</code> | 654 | killed (exit 1) | [raw](MutC1Counter.txt#L7487) |
| M220 judge: <code>not row_why</code> → <code>(row_why)</code> | 654 | killed (exit 1) | [raw](MutC1Counter.txt#L7542) |
| M221 judge: <code>er[2].strip() or &quot;-&quot;</code> → <code>(er[2].strip()) and (&quot;-&quot;)</code> | 657 | survived | [raw](MutC1Counter.txt#L7598) |
| M222 judge: <code>not emine</code> → <code>False</code> | 658 | killed (exit 1) | [raw](MutC1Counter.txt#L7620) |
| M223 judge: <code>not emine</code> → <code>(emine)</code> | 658 | killed (exit 1) | [raw](MutC1Counter.txt#L7645) |
| M224 judge: <code>picked is None</code> → <code>picked is not None</code> | 660 | killed (exit 1) | [raw](MutC1Counter.txt#L7701) |
| M225 judge: <code>picked is None</code> → <code>False</code> | 660 | killed (exit 1) | [raw](MutC1Counter.txt#L7746) |
| M226 judge: <code>picked</code> → <code>not (picked)</code> | 663 | killed (exit 1) | [raw](MutC1Counter.txt#L7791) |
| M227 judge: <code>picked</code> → <code>not (picked)</code> | 664 | killed (exit 1) | [raw](MutC1Counter.txt#L7830) |
| M228 judge: <code>picked</code> → <code>not (picked)</code> | 665 | killed (exit 1) | [raw](MutC1Counter.txt#L7869) |
| M229 judge: <code>not why</code> → <code>(why)</code> | 667 | killed (exit 1) | [raw](MutC1Counter.txt#L7908) |
| M230 gate_section: <code>line.startswith(&quot;## &quot;)</code> → <code>False</code> | 676 | killed (exit 1) | [raw](MutC1Counter.txt#L7963) |
| M231 gate_section: <code>line.rstrip() == &quot;## Gate&quot;</code> → <code>line.rstrip() != &quot;## Gate&quot;</code> | 677 | killed (exit 1) | [raw](MutC1Counter.txt#L8021) |
| M232 gate_section: <code>inside</code> → <code>False</code> | 679 | killed (exit 1) | [raw](MutC1Counter.txt#L8079) |
| M233 _plain: <code>page_plain(s).lower()</code> → <code>(page_plain(s))</code> | 696 | killed (exit 1) | [raw](MutC1Counter.txt#L8137) |
| M234 norm_page: <code>norm_page_case(s).lower()</code> → <code>(norm_page_case(s))</code> | 714 | killed (exit 1) | [raw](MutC1Counter.txt#L8163) |
| M235 boundary_ok: <code>idx == 0</code> → <code>idx != 0</code> | 719 | killed (exit 1) | [raw](MutC1Counter.txt#L8189) |
| M236 boundary_ok: <code>idx == 0</code> → <code>False</code> | 719 | killed (exit 1) | [raw](MutC1Counter.txt#L8221) |
| M237 boundary_ok: <code>text[idx - 1] in BOUNDARY_PREV</code> → <code>text[idx - 1] not in BOUNDARY_PREV</code> | 721 | killed (exit 1) | [raw](MutC1Counter.txt#L8246) |
| M238 token_at_boundary: <code>not token</code> → <code>False</code> | 731 | survived | [raw](MutC1Counter.txt#L8284) |
| M239 token_at_boundary: <code>not token</code> → <code>(token)</code> | 731 | killed (exit 1) | [raw](MutC1Counter.txt#L8306) |
| M240 token_at_boundary: <code>True</code> → <code>False</code> | 734 | killed (exit 1) | [raw](MutC1Counter.txt#L8339) |
| M241 token_at_boundary: <code>text.find(token, start)</code> → <code>text.casefold().find(token.casefold(), start)</code> | 735 | killed (exit 1) | [raw](MutC1Counter.txt#L8381) |
| M242 token_at_boundary: <code>i &lt; 0</code> → <code>i &lt;= 0</code> | 736 | killed (exit 1) | [raw](MutC1Counter.txt#L8406) |
| M243 token_at_boundary: <code>i &lt; 0</code> → <code>False</code> | 736 | killed (120-s timeout, exit 124) | [raw](MutC1Counter.txt#L8431) |
| M244 token_at_boundary: <code>j &gt;= len(text) or not (text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;)</code> → <code>(j &gt;= len(text)) and (not (text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;))</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8455) |
| M245 token_at_boundary: <code>j &gt;= len(text)</code> → <code>j &gt; len(text)</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8502) |
| M246 token_at_boundary: <code>not (text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;)</code> → <code>(text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;)</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8548) |
| M247 token_at_boundary: <code>not (text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;)</code> → <code>True</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8583) |
| M248 token_at_boundary: <code>text[j] in ASCII_ALNUM or text[j] in &quot;_-&quot;</code> → <code>(text[j] in ASCII_ALNUM) and (text[j] in &quot;_-&quot;)</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8610) |
| M249 token_at_boundary: <code>text[j] in ASCII_ALNUM</code> → <code>text[j] not in ASCII_ALNUM</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8637) |
| M250 token_at_boundary: <code>text[j] in &quot;_-&quot;</code> → <code>text[j] not in &quot;_-&quot;</code> | 739 | killed (exit 1) | [raw](MutC1Counter.txt#L8670) |
| M251 token_at_boundary: <code>boundary_ok(text, i) and right_ok</code> → <code>(boundary_ok(text, i)) or (right_ok)</code> | 740 | killed (exit 1) | [raw](MutC1Counter.txt#L8704) |
| M252 token_at_boundary: <code>boundary_ok(text, i) and right_ok</code> → <code>False</code> | 740 | killed (exit 1) | [raw](MutC1Counter.txt#L8738) |
| M253 token_at_boundary: <code>boundary_ok(text, i) and right_ok</code> → <code>boundary_ok(text, i)</code> | 740 | killed (exit 1) | [raw](MutC1Counter.txt#L8771) |
| M254 token_at_boundary: <code>boundary_ok(text, i) and right_ok</code> → <code>right_ok</code> | 740 | killed (exit 1) | [raw](MutC1Counter.txt#L8798) |
| M255 token_forms: <code>not token</code> → <code>False</code> | 749 | killed (exit 1) | [raw](MutC1Counter.txt#L8829) |
| M256 token_forms: <code>not token</code> → <code>(token)</code> | 749 | killed (exit 1) | [raw](MutC1Counter.txt#L8875) |
| M257 token_forms: <code>f and f not in forms</code> → <code>(f) or (f not in forms)</code> | 754 | survived | [raw](MutC1Counter.txt#L8924) |
| M258 token_forms: <code>f and f not in forms</code> → <code>False</code> | 754 | killed (exit 1) | [raw](MutC1Counter.txt#L8946) |
| M259 token_forms: <code>f not in forms</code> → <code>f in forms</code> | 754 | killed (exit 1) | [raw](MutC1Counter.txt#L8973) |
| M260 fetch: <code>MAX_BYTES + 1</code> → <code>MAX_BYTES</code> | 773 | survived | [raw](MutC1Counter.txt#L9000) |
| M261 fetch: <code>pins is not None and not host_ok(final, pins)</code> → <code>(pins is not None) or (not host_ok(final, pins))</code> | 774 | survived | [raw](MutC1Counter.txt#L9022) |
| M262 fetch: <code>pins is not None</code> → <code>pins is None</code> | 774 | survived | [raw](MutC1Counter.txt#L9044) |
| M263 fetch: <code>pins is not None and not host_ok(final, pins)</code> → <code>False</code> | 774 | survived | [raw](MutC1Counter.txt#L9066) |
| M264 fetch: <code>not host_ok(final, pins)</code> → <code>(host_ok(final, pins))</code> | 774 | survived | [raw](MutC1Counter.txt#L9088) |
| M265 fetch: <code>base_keys is not None and url_key(final) in base_keys</code> → <code>(base_keys is not None) or (url_key(final) in base_keys)</code> | 776 | survived | [raw](MutC1Counter.txt#L9110) |
| M266 fetch: <code>base_keys is not None</code> → <code>base_keys is None</code> | 776 | survived | [raw](MutC1Counter.txt#L9132) |
| M267 fetch: <code>base_keys is not None and url_key(final) in base_keys</code> → <code>False</code> | 776 | survived | [raw](MutC1Counter.txt#L9154) |
| M268 fetch: <code>url_key(final) in base_keys</code> → <code>url_key(final) not in base_keys</code> | 776 | survived | [raw](MutC1Counter.txt#L9176) |
| M269 fetch: <code>len(data) &gt; MAX_BYTES</code> → <code>len(data) &gt;= MAX_BYTES</code> | 778 | survived | [raw](MutC1Counter.txt#L9198) |
| M270 fetch: <code>len(data) &gt; MAX_BYTES</code> → <code>False</code> | 778 | survived | [raw](MutC1Counter.txt#L9220) |
| M271 fetch: <code>Exception</code> → <code>RuntimeError</code> | 781 | survived | [raw](MutC1Counter.txt#L9242) |
| M272 fetch: <code>last</code> → <code>not (last)</code> | 783 | survived | [raw](MutC1Counter.txt#L9264) |
| M273 found_on_page: <code>not quote or norm(quote) not in norm_page(page_text)</code> → <code>(not quote) and (norm(quote) not in norm_page(page_text))</code> | 788 | killed (exit 1) | [raw](MutC1Counter.txt#L9286) |
| M274 found_on_page: <code>not quote or norm(quote) not in norm_page(page_text)</code> → <code>False</code> | 788 | killed (exit 1) | [raw](MutC1Counter.txt#L9311) |
| M275 found_on_page: <code>not quote</code> → <code>(quote)</code> | 788 | killed (exit 1) | [raw](MutC1Counter.txt#L9336) |
| M276 found_on_page: <code>not quote or norm(quote) not in norm_page(page_text)</code> → <code>not quote</code> | 788 | killed (exit 1) | [raw](MutC1Counter.txt#L9363) |
| M277 found_on_page: <code>norm(quote) not in norm_page(page_text)</code> → <code>norm(quote) in norm_page(page_text)</code> | 788 | killed (exit 1) | [raw](MutC1Counter.txt#L9388) |
| M278 ls_tree_blobs: <code>r.returncode != 0</code> → <code>r.returncode == 0</code> | 799 | killed (exit 1) | [raw](MutC1Counter.txt#L9416) |
| M279 ls_tree_blobs: <code>r.returncode != 0</code> → <code>False</code> | 799 | survived | [raw](MutC1Counter.txt#L9445) |
| M280 ls_tree_blobs: <code>not rec</code> → <code>False</code> | 804 | killed (exit 1) | [raw](MutC1Counter.txt#L9467) |
| M281 ls_tree_blobs: <code>not rec</code> → <code>(rec)</code> | 804 | killed (exit 1) | [raw](MutC1Counter.txt#L9496) |
| M282 ls_tree_blobs: <code>not sep or len(parts) != 3</code> → <code>(not sep) and (len(parts) != 3)</code> | 808 | survived | [raw](MutC1Counter.txt#L9525) |
| M283 ls_tree_blobs: <code>not sep or len(parts) != 3</code> → <code>False</code> | 808 | survived | [raw](MutC1Counter.txt#L9547) |
| M284 ls_tree_blobs: <code>not sep</code> → <code>(sep)</code> | 808 | killed (exit 1) | [raw](MutC1Counter.txt#L9569) |
| M285 ls_tree_blobs: <code>len(parts) != 3</code> → <code>len(parts) == 3</code> | 808 | killed (exit 1) | [raw](MutC1Counter.txt#L9598) |
| M286 ls_tree_blobs: <code>kind != b&quot;blob&quot;</code> → <code>kind == b&quot;blob&quot;</code> | 811 | killed (exit 1) | [raw](MutC1Counter.txt#L9627) |
| M287 ls_tree_blobs: <code>kind != b&quot;blob&quot;</code> → <code>False</code> | 811 | killed (exit 1) | [raw](MutC1Counter.txt#L9652) |
| M288 ls_tree_blobs: <code>p == &quot;.ufo&quot; or p.startswith(UFO_PREFIX)</code> → <code>(p == &quot;.ufo&quot;) and (p.startswith(UFO_PREFIX))</code> | 814 | killed (exit 1) | [raw](MutC1Counter.txt#L9677) |
| M289 ls_tree_blobs: <code>p == &quot;.ufo&quot;</code> → <code>p != &quot;.ufo&quot;</code> | 814 | killed (exit 1) | [raw](MutC1Counter.txt#L9702) |
| M290 ls_tree_blobs: <code>p == &quot;.ufo&quot; or p.startswith(UFO_PREFIX)</code> → <code>False</code> | 814 | killed (exit 1) | [raw](MutC1Counter.txt#L9727) |
| M291 parse_batch: <code>pos &lt; n</code> → <code>pos &lt;= n</code> | 824 | killed (exit 1) | [raw](MutC1Counter.txt#L9752) |
| M292 parse_batch: <code>pos &lt; n</code> → <code>False</code> | 824 | killed (exit 1) | [raw](MutC1Counter.txt#L9792) |
| M293 parse_batch: <code>nl &lt; 0</code> → <code>nl &lt;= 0</code> | 826 | survived | [raw](MutC1Counter.txt#L9819) |
| M294 parse_batch: <code>nl &lt; 0</code> → <code>False</code> | 826 | survived | [raw](MutC1Counter.txt#L9841) |
| M295 parse_batch: <code>len(parts) != 3 or parts[1] != &quot;blob&quot;</code> → <code>(len(parts) != 3) and (parts[1] != &quot;blob&quot;)</code> | 830 | killed (exit 1) | [raw](MutC1Counter.txt#L9863) |
| M296 parse_batch: <code>len(parts) != 3</code> → <code>len(parts) == 3</code> | 830 | killed (exit 1) | [raw](MutC1Counter.txt#L9888) |
| M297 parse_batch: <code>len(parts) != 3 or parts[1] != &quot;blob&quot;</code> → <code>False</code> | 830 | killed (exit 1) | [raw](MutC1Counter.txt#L9929) |
| M298 parse_batch: <code>parts[1] != &quot;blob&quot;</code> → <code>parts[1] == &quot;blob&quot;</code> | 830 | killed (exit 1) | [raw](MutC1Counter.txt#L9965) |
| M299 parse_batch: <code>len(body) != size</code> → <code>len(body) == size</code> | 834 | killed (exit 1) | [raw](MutC1Counter.txt#L9997) |
| M300 parse_batch: <code>len(body) != size</code> → <code>False</code> | 834 | survived | [raw](MutC1Counter.txt#L10037) |
| M301 read_blobs: <code>not shas</code> → <code>False</code> | 842 | survived | [raw](MutC1Counter.txt#L10059) |
| M302 read_blobs: <code>not shas</code> → <code>(shas)</code> | 842 | killed (exit 1) | [raw](MutC1Counter.txt#L10081) |
| M303 read_blobs: <code>r.returncode != 0</code> → <code>r.returncode == 0</code> | 846 | killed (exit 1) | [raw](MutC1Counter.txt#L10106) |
| M304 read_blobs: <code>r.returncode != 0</code> → <code>False</code> | 846 | survived | [raw](MutC1Counter.txt#L10135) |
| M305 held_in_text: <code>not token</code> → <code>False</code> | 854 | survived | [raw](MutC1Counter.txt#L10157) |
| M306 held_in_text: <code>not token</code> → <code>(token)</code> | 854 | killed (exit 1) | [raw](MutC1Counter.txt#L10179) |
| M307 held_in_text: <code>True</code> → <code>False</code> | 858 | killed (exit 1) | [raw](MutC1Counter.txt#L10220) |
| M308 held_in_text: <code>line.find(token, start)</code> → <code>line.casefold().find(token.casefold(), start)</code> | 859 | killed (exit 1) | [raw](MutC1Counter.txt#L10261) |
| M309 held_in_text: <code>i &lt; 0</code> → <code>i &lt;= 0</code> | 860 | killed (exit 1) | [raw](MutC1Counter.txt#L10287) |
| M310 held_in_text: <code>i &lt; 0</code> → <code>False</code> | 860 | killed (exit 1) | [raw](MutC1Counter.txt#L10315) |
| M311 held_in_text: <code>i == 0 or line[i - 1].isspace() or line[i - 1] in HELD_PREV</code> → <code>(i == 0) and (line[i - 1].isspace()) and (line[i - 1] in HELD_PREV)</code> | 863 | killed (exit 1) | [raw](MutC1Counter.txt#L10351) |
| M312 held_in_text: <code>i == 0</code> → <code>i != 0</code> | 863 | killed (exit 1) | [raw](MutC1Counter.txt#L10392) |
| M313 held_in_text: <code>i == 0 or line[i - 1].isspace() or line[i - 1] in HELD_PREV</code> → <code>True</code> | 863 | killed (exit 1) | [raw](MutC1Counter.txt#L10421) |
| M314 held_in_text: <code>line[i - 1] in HELD_PREV</code> → <code>line[i - 1] not in HELD_PREV</code> | 863 | killed (exit 1) | [raw](MutC1Counter.txt#L10447) |
| M315 held_in_text: <code>left and held_right_ok(line, j)</code> → <code>(left) or (held_right_ok(line, j))</code> | 864 | killed (exit 1) | [raw](MutC1Counter.txt#L10484) |
| M316 held_in_text: <code>left and held_right_ok(line, j)</code> → <code>False</code> | 864 | killed (exit 1) | [raw](MutC1Counter.txt#L10516) |
| M317 held_in_text: <code>left and held_right_ok(line, j)</code> → <code>left</code> | 864 | killed (exit 1) | [raw](MutC1Counter.txt#L10557) |
| M318 held_right_ok: <code>j &gt;= len(line)</code> → <code>j &gt; len(line)</code> | 872 | killed (exit 1) | [raw](MutC1Counter.txt#L10587) |
| M319 held_right_ok: <code>j &gt;= len(line)</code> → <code>False</code> | 872 | killed (exit 1) | [raw](MutC1Counter.txt#L10626) |
| M320 held_right_ok: <code>c in HELD_NEXT_BAD</code> → <code>c not in HELD_NEXT_BAD</code> | 875 | killed (exit 1) | [raw](MutC1Counter.txt#L10665) |
| M321 held_right_ok: <code>c in HELD_NEXT_BAD</code> → <code>False</code> | 875 | killed (exit 1) | [raw](MutC1Counter.txt#L10697) |
| M322 held_right_ok: <code>c == &quot;.&quot; and j + 1 &lt; len(line) and line[j + 1] in ASCII_ALNUM</code> → <code>(c == &quot;.&quot;) or (j + 1 &lt; len(line)) or (line[j + 1] in ASCII_ALNUM)</code> | 877 | killed (exit 1) | [raw](MutC1Counter.txt#L10725) |
| M323 held_right_ok: <code>c == &quot;.&quot;</code> → <code>c != &quot;.&quot;</code> | 877 | killed (exit 1) | [raw](MutC1Counter.txt#L10764) |
| M324 held_right_ok: <code>c == &quot;.&quot; and j + 1 &lt; len(line) and line[j + 1] in ASCII_ALNUM</code> → <code>False</code> | 877 | killed (exit 1) | [raw](MutC1Counter.txt#L10790) |
| M325 held_right_ok: <code>j + 1 &lt; len(line)</code> → <code>j + 1 &lt;= len(line)</code> | 877 | killed (exit 1) | [raw](MutC1Counter.txt#L10816) |
| M326 held_right_ok: <code>line[j + 1] in ASCII_ALNUM</code> → <code>line[j + 1] not in ASCII_ALNUM</code> | 877 | killed (exit 1) | [raw](MutC1Counter.txt#L10855) |
| M327 held_in_blob: <code>b&quot;\0&quot; in data</code> → <code>b&quot;\0&quot; not in data</code> | 884 | killed (exit 1) | [raw](MutC1Counter.txt#L10881) |
| M328 held_in_blob: <code>b&quot;\0&quot; in data</code> → <code>False</code> | 884 | killed (exit 1) | [raw](MutC1Counter.txt#L10906) |
| M329 held_in_base: <code>t</code> → <code>True</code> | 891 | survived | [raw](MutC1Counter.txt#L10931) |
| M330 held_in_base: <code>not pending</code> → <code>False</code> | 893 | survived | [raw](MutC1Counter.txt#L10953) |
| M331 held_in_base: <code>not pending</code> → <code>(pending)</code> | 893 | killed (exit 1) | [raw](MutC1Counter.txt#L10975) |
| M332 held_in_base: <code>held_in_blob(body, t)</code> → <code>False</code> | 900 | killed (exit 1) | [raw](MutC1Counter.txt#L11000) |
| M333 held_in_base: <code>not pending</code> → <code>False</code> | 903 | survived | [raw](MutC1Counter.txt#L11025) |
| M334 held_in_base: <code>not pending</code> → <code>(pending)</code> | 903 | survived | [raw](MutC1Counter.txt#L11047) |
| M335 summary_line: <code>fetching</code> → <code>False</code> | 911 | killed (exit 1) | [raw](MutC1Counter.txt#L11069) |
| M336 predicate: <code>not fetching</code> → <code>False</code> | 923 | killed (exit 1) | [raw](MutC1Counter.txt#L11094) |
| M337 predicate: <code>not fetching</code> → <code>(fetching)</code> | 923 | killed (exit 1) | [raw](MutC1Counter.txt#L11119) |
| M338 predicate: <code>found &gt;= TARGET and ground &gt;= NEW_TARGET</code> → <code>(found &gt;= TARGET) or (ground &gt;= NEW_TARGET)</code> | 925 | killed (exit 1) | [raw](MutC1Counter.txt#L11145) |
| M339 predicate: <code>found &gt;= TARGET and ground &gt;= NEW_TARGET</code> → <code>not (found &gt;= TARGET and ground &gt;= NEW_TARGET)</code> | 925 | killed (exit 1) | [raw](MutC1Counter.txt#L11171) |
| M340 predicate: <code>found &gt;= TARGET</code> → <code>found &gt; TARGET</code> | 925 | killed (exit 1) | [raw](MutC1Counter.txt#L11198) |
| M341 predicate: <code>ground &gt;= NEW_TARGET</code> → <code>ground &gt; NEW_TARGET</code> | 925 | killed (exit 1) | [raw](MutC1Counter.txt#L11223) |
| M342 new_ground: <code>{t.casefold() for t in norms if t and not held.get(t)}</code> → <code>[t.casefold() for t in norms if t and not held.get(t)]</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11248) |
| M343 new_ground: <code>t.casefold()</code> → <code>(t)</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11273) |
| M344 new_ground: <code>t and not held.get(t)</code> → <code>(t) or (not held.get(t))</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11298) |
| M345 new_ground: <code>t and not held.get(t)</code> → <code>True</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11323) |
| M346 new_ground: <code>not held.get(t)</code> → <code>(held.get(t))</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11348) |
| M347 new_ground: <code>held.get(t)</code> → <code>held.get(t.casefold())</code> | 934 | killed (exit 1) | [raw](MutC1Counter.txt#L11375) |
| M348 main: <code>OSError</code> → <code>RuntimeError</code> | 1527 | survived | [raw](MutC1Counter.txt#L11400) |
| M349 main: <code>args.self_test</code> → <code>False</code> | 1530 | killed (exit 2) | [raw](MutC1Counter.txt#L11422) |
| M350 main: <code>args.rev or args.fetch or args.json</code> → <code>(args.rev) and (args.fetch) and (args.json)</code> | 1531 | survived | [raw](MutC1Counter.txt#L11448) |
| M351 main: <code>args.rev or args.fetch or args.json</code> → <code>False</code> | 1531 | survived | [raw](MutC1Counter.txt#L11470) |
| M352 main: <code>not args.rev</code> → <code>False</code> | 1534 | survived | [raw](MutC1Counter.txt#L11492) |
| M353 main: <code>not args.rev</code> → <code>(args.rev)</code> | 1534 | killed (exit 2) | [raw](MutC1Counter.txt#L11514) |
| M354 main: <code>not rev_ok(args.rev)</code> → <code>False</code> | 1536 | killed (exit 1) | [raw](MutC1Counter.txt#L11537) |
| M355 main: <code>not rev_ok(args.rev)</code> → <code>(rev_ok(args.rev))</code> | 1536 | killed (exit 1) | [raw](MutC1Counter.txt#L11562) |
| M356 main: <code>git_show(lane, args.rev, SKILL) or &quot;&quot;</code> → <code>(git_show(lane, args.rev, SKILL)) and (&quot;&quot;)</code> | 1543 | survived | [raw](MutC1Counter.txt#L11587) |
| M357 main: <code>git_show(lane, args.rev, ENTRY) or &quot;&quot;</code> → <code>(git_show(lane, args.rev, ENTRY)) and (&quot;&quot;)</code> | 1544 | survived | [raw](MutC1Counter.txt#L11609) |
| M358 main: <code>git_show(lane, args.rev, SOURCES) or &quot;&quot;</code> → <code>(git_show(lane, args.rev, SOURCES)) and (&quot;&quot;)</code> | 1545 | survived | [raw](MutC1Counter.txt#L11631) |
| M359 main: <code>git_show(lane, args.rev, LESSON) or &quot;&quot;</code> → <code>(git_show(lane, args.rev, LESSON)) and (&quot;&quot;)</code> | 1546 | survived | [raw](MutC1Counter.txt#L11653) |
| M360 main: <code>git_show(lane, BASE, SOURCES) or &quot;&quot;</code> → <code>(git_show(lane, BASE, SOURCES)) and (&quot;&quot;)</code> | 1547 | survived | [raw](MutC1Counter.txt#L11675) |
| M361 main: <code>(EnvError, UnicodeDecodeError, OSError)</code> → <code>RuntimeError</code> | 1548 | survived | [raw](MutC1Counter.txt#L11697) |
| M362 main: <code>if r[&quot;backed&quot;]</code> → <code>if True</code> | 1553 | survived | [raw](MutC1Counter.txt#L11719) |
| M363 main: <code>r[&quot;backed&quot;]</code> → <code>True</code> | 1553 | survived | [raw](MutC1Counter.txt#L11741) |
| M364 main: <code>if r[&quot;in_k&quot;]</code> → <code>if True</code> | 1554 | survived | [raw](MutC1Counter.txt#L11763) |
| M365 main: <code>r[&quot;in_k&quot;]</code> → <code>True</code> | 1554 | survived | [raw](MutC1Counter.txt#L11785) |
| M366 main: <code>args.fetch</code> → <code>False</code> | 1556 | survived | [raw](MutC1Counter.txt#L11807) |
| M367 main: <code>found_on_page(fetch(r[&quot;url&quot;], HOSTS[r[&quot;client&quot;]],\n                                                 base_url_keys(base_sources)),\n                                           r[&quot;quote&quot;], r[&quot;token&quot;])</code> → <code>True</code> | 1559 | survived | [raw](MutC1Counter.txt#L11829) |
| M368 main: <code>Exception</code> → <code>RuntimeError</code> | 1562 | survived | [raw](MutC1Counter.txt#L11851) |
| M369 main: <code>False</code> → <code>True</code> | 1563 | survived | [raw](MutC1Counter.txt#L11873) |
| M370 main: <code>1 if r[&quot;found&quot;] else 0</code> → <code>1</code> | 1565 | survived | [raw](MutC1Counter.txt#L11895) |
| M371 main: <code>r[&quot;found&quot;]</code> → <code>not (r[&quot;found&quot;])</code> | 1565 | survived | [raw](MutC1Counter.txt#L11917) |
| M372 main: <code>if r.get(&quot;found&quot;)</code> → <code>if True</code> | 1566 | survived | [raw](MutC1Counter.txt#L11939) |
| M373 main: <code>r.get(&quot;found&quot;)</code> → <code>True</code> | 1566 | survived | [raw](MutC1Counter.txt#L11961) |
| M374 main: <code>args.fetch</code> → <code>not (args.fetch)</code> | 1566 | survived | [raw](MutC1Counter.txt#L11983) |
| M375 main: <code>args.fetch</code> → <code>False</code> | 1568 | survived | [raw](MutC1Counter.txt#L12005) |
| M376 main: <code>if r[&quot;norm&quot;]</code> → <code>if True</code> | 1569 | survived | [raw](MutC1Counter.txt#L12027) |
| M377 main: <code>r[&quot;norm&quot;]</code> → <code>True</code> | 1569 | survived | [raw](MutC1Counter.txt#L12049) |
| M378 main: <code>(EnvError, UnicodeDecodeError, OSError)</code> → <code>RuntimeError</code> | 1572 | survived | [raw](MutC1Counter.txt#L12071) |
| M379 main: <code>[r[&quot;norm&quot;] for r in counted]</code> → <code>[r[&quot;norm&quot;] for r in backed]</code> | 1577 | survived | [raw](MutC1Counter.txt#L12093) |
| M380 main: <code>args.json</code> → <code>False</code> | 1578 | survived | [raw](MutC1Counter.txt#L12115) |
| M381 main: <code>not r[&quot;backed&quot;]</code> → <code>False</code> | 1585 | survived | [raw](MutC1Counter.txt#L12137) |
| M382 main: <code>not r[&quot;backed&quot;]</code> → <code>(r[&quot;backed&quot;])</code> | 1585 | survived | [raw](MutC1Counter.txt#L12159) |
| M383 main: <code>args.fetch</code> → <code>False</code> | 1589 | survived | [raw](MutC1Counter.txt#L12181) |
| M384 main: <code>r.get(&quot;found&quot;)</code> → <code>not (r.get(&quot;found&quot;))</code> | 1590 | survived | [raw](MutC1Counter.txt#L12203) |
| M385 main: <code>r.get(&quot;found&quot;)</code> → <code>False</code> | 1591 | survived | [raw](MutC1Counter.txt#L12225) |
| M386 main: <code>r.get(&quot;held&quot;)</code> → <code>not (r.get(&quot;held&quot;))</code> | 1592 | survived | [raw](MutC1Counter.txt#L12247) |
| M387 main: <code>predicate(args.fetch, found, ground)</code> → <code>0</code> | 1594 | survived | [raw](MutC1Counter.txt#L12269) |

## Every survivor: claim impact and one-line killing arm
**Impact assessments and proposed arms below are [INFERENCE], from the frozen code and the observed surviving mutation; these extra arms were not run or added.** “Yes F/G” means the mutation can change the corresponding value or the claimed exit on suitable actual inputs; it does not claim that a real sourced table was built or that a C1 `--fetch` control won. Boundary/held examples require the described input/base occurrence. Git-protocol and error-shape cases distinguish healthy real inputs from malformed/environmental inputs. `tok` denotes `.claude-plugin/plugin.json`; `skill`, `entry`, `sources`, `lesson`, `base` refer to the existing synthetic fixtures at frozen lines 1165-1190. Proposed CLI worlds are **hermetic test fixtures**, supplying revision bytes/fake page responses/base blobs to the actual `main`, not stubbing out its F/G outputs.
A proposed arm states the pristine expected result and must fail under the mutant. Some survivors are equivalent or unreachable with the remaining guards: no honest semantic killing arm exists for them, which is stated explicitly rather than fabricating a coverage defect. Helper-only, out-of-domain, diagnostic or performance arms are labeled and are not recommendations to expand the claim.
| Survivor | Can change real claim result (F,G)? | One-line arm that would kill it / equivalence reason |
|---|---|---|
| M005 (`174`) | Yes F: an exactly 5-MiB valid page is newly rejected. | Fake HTTP response of exactly 5*1024*1024 bytes must be accepted by fetch(). |
| M006 (`175`) | Yes F: changes the pinned timeout; a 30-to-31-second response can change found. | Intercept urlopen and assert timeout == 30 (not the mutable FETCH_TIMEOUT constant). |
| M007 (`176`) | No F/G: chunk-size change preserves the complete scan on successful Git reads. | With 257 blobs, spy that read_blobs batches contain at most 256 IDs; performance/spec arm only. |
| M008 (`210`) | No: removing ^ is equivalent because every consumer uses re.match, which is already start-anchored. | None exists for this equivalent regex/consumer pair; do not count it as a missing semantic arm. |
| M010 (`211`) | No: removing ^ is equivalent because every consumer uses re.match, which is already start-anchored. | None exists for this equivalent regex/consumer pair; do not count it as a missing semantic arm. |
| M013 (`216`) | No F/G with the remaining guards: two-digit IDs still cannot enter sources_table(). | Assert SID_RE.match("S90") is None; local grammar arm, not an end-to-end claim change. |
| M014 (`216`) | Yes F: a source cell such as S901 extra is accepted as S901. | Existing synthetic world with Gemini entry source "S901 extra" must back only Claude Code. |
| M015 (`216`) | No F/G: lowercase entry IDs still have no lowercase row in sources_table(). | Assert SID_RE.match("s901") is None; local grammar arm. |
| M016 (`216`) | No: removing ^ is equivalent because every consumer uses re.match, which is already start-anchored. | None exists for this equivalent regex/consumer pair; do not count it as a missing semantic arm. |
| M017 (`218`) | No: removing ^ is equivalent because every consumer uses re.match, which is already start-anchored. | None exists for this equivalent regex/consumer pair; do not count it as a missing semantic arm. |
| M018 (`218`) | No F/G against the fixed well-formed base: SID_RE still rejects two-digit cited IDs. | Assert sources_table(a syntactically complete S90 row) == {}; local parser arm. |
| M019 (`218`) | No F/G against the fixed uppercase-ID base: SID_RE still rejects lowercase cited IDs. | Assert sources_table(a syntactically complete s901 row) == {}; local parser arm. |
| M020 (`219`) | Yes F: nonwords containing plugin/extension outside the token satisfy the quote rule. | Quote "unpluginsX .claude-plugin/plugin.json exists" must not back Claude Code even when copied to Gate. |
| M022 (`221`) | No F/G: norm_page_case converts tab/CR/LF to spaces before the boundary helper. | Assert token_at_boundary(C + tok, tok) is True for the removed tab/CR/LF C; helper-only arm. |
| M023 (`221`) | No F/G: norm_page_case converts tab/CR/LF to spaces before the boundary helper. | Assert token_at_boundary(C + tok, tok) is True for the removed tab/CR/LF C; helper-only arm. |
| M025 (`221`) | Yes F: tokens immediately after a single quote are falsely rejected. | Assert token_at_boundary("'" + tok, tok) is True. |
| M028 (`221`) | No F/G: norm_page_case converts tab/CR/LF to spaces before the boundary helper. | Assert token_at_boundary(C + tok, tok) is True for the removed tab/CR/LF C; helper-only arm. |
| M030 (`223`) | Yes F/G: a 0 suffix can become a valid found boundary, and .0 can become held. | Assert token_at_boundary(tok + "0", tok) is False. |
| M031 (`223`) | Yes F/G: an A suffix can become a valid found boundary, and .A can become held. | Assert token_at_boundary(tok + "A", tok) is False. |
| M032 (`223`) | Yes F/G: an a suffix can become a valid found boundary, and .a can become held. | Assert token_at_boundary(tok + "a", tok) is False. |
| M038 (`224`) | Yes G if a held occurrence uses bare ~ immediately before the token; current test uses ~/ and exercises / instead. | Assert held_in_text("~" + tok, tok) is True. |
| M044 (`244`) | No F/G in the installed verifiers/ layout with no nested lane markers: the ancestor search rediscovers the same repository. | Create conflicting complete markers inside verifiers/ and its parent; assert lane_dir() chooses the parent (layout-policy arm). |
| M045 (`244`) | No F/G in the installed verifiers/ layout with no nested lane markers: the ancestor search rediscovers the same repository. | Create conflicting complete markers inside verifiers/ and its parent; assert lane_dir() chooses the parent (layout-policy arm). |
| M046 (`248`) | Can change repository selection, hence F/G, for the supported relocated-copy layout with a partial-marker ancestor. | A partial-marker directory below a complete clone root must not stop the upward search; assert the complete root is selected. |
| M047 (`248`) | Can change F/G for a supported nested/relocated copy by falling back to the lane instead of finding its clone; no effect at root/verifiers/. | Place the copy under clone/nested/verifiers with no nested markers; assert lane_dir() resolves to clone. |
| M048 (`253`) | Can select an invalid/other repository with one marker; healthy installed layout is unchanged. | With only one marker at every candidate and no valid fallback, lane_dir() must raise EnvError. |
| M049 (`253`) | Yes to claim result: every real measurement loses its repository and exits 2; F/G are not computed. | In an ordinary complete clone, assert lane_dir() returns that clone instead of raising EnvError. |
| M050 (`268`) | No numeric F/G: changes OSError-to-EnvError conversion and error reporting only. | Make subprocess.run raise OSError; assert git() raises EnvError, not OSError. |
| M060 (`288`) | Yes on a real Git failure: most non-missing-path errors become missing files; blank base sources can remove rejection checks. | Mock git show rc=1 with stderr "fatal: bad object"; git_show must raise EnvError, not return None. |
| M061 (`298`) | Yes F: malformed pipe rows without a closing &#124; can be interpreted as valid headers/data. | Assert cells("&#124; Client &#124; Plugin manifest &#124; What a plugin can ship &#124; Action X") == []. |
| M062 (`298`) | Yes F: malformed pipe rows without a closing &#124; can be interpreted as valid headers/data. | Assert cells("&#124; Client &#124; Plugin manifest &#124; What a plugin can ship &#124; Action X") == []. |
| M064 (`298`) | Yes F: malformed pipe rows without a closing &#124; can be interpreted as valid headers/data. | Assert cells("&#124; Client &#124; Plugin manifest &#124; What a plugin can ship &#124; Action X") == []. |
| M065 (`298`) | No F/G: only the empty single-cell row &#124;&#124; changes; it cannot name a frozen client or header. | Assert cells("&#124;&#124;") == [""]; parser-only arm. |
| M070 (`328`) | No F/G on well-formed tables; malformed rows can instead reach r[0] and crash the judge. | Assert list(tables("&#124; h &#124;\n&#124; broken\n")) == [(["h"], [])]; malformed-row arm. |
| M071 (`328`) | No F/G on well-formed tables; malformed rows can instead reach r[0] and crash the judge. | Assert list(tables("&#124; h &#124;\n&#124; broken\n")) == [(["h"], [])]; malformed-row arm. |
| M075 (`339`) | Yes F: a table flushed before EOF is dropped. | Append a blank line and prose after the valid synthetic SKILL table; skill_rows must still return both rows. |
| M082 (`357`) | Yes F: a table under the next same-level heading can leak into the target section. | Target heading followed immediately by "### Other" and a valid table must produce skill_rows == []. |
| M083 (`357`) | Yes F: a table under the next same-level heading can leak into the target section. | Target heading followed immediately by "### Other" and a valid table must produce skill_rows == []. |
| M085 (`370`) | No: deleting the empty-section early return is equivalent to iterating zero tables. | None exists: tables("") yields no tables, so the final return remains []. |
| M094 (`401`) | Yes to claim result: real SOURCES prose/blank lines cause IndexError instead of valid F/G. | Assert source_ids("# Sources\n" + base) == {"S001"}. |
| M098 (`421`) | No F/G with the pinned DNS hosts: hostname already lowercases them; scoped IPv6 is outside the allowed hosts. | Assert url_key("http://[fe80::1%25ZONE]/p") == "//fe80::1%25zone/p"; scoped-IPv6 helper-only arm. |
| M105 (`430`) | Yes F: URL aliases whose pre-.md part ends in / no longer normalize to the held URL. | Assert url_key("https://cursor.com/docs/plugins/.md") == url_key("https://cursor.com/docs/plugins"). |
| M107 (`440`) | No: SOURCES_ROW_RE already requires two pipes, so every matching line has at least three split cells. | None exists with the unchanged row regex; a two-cell match is unreachable. |
| M109 (`452`) | Yes F: case variants such as /ISSUES/ stop being rejected as tracker URLs. | Assert url_is_tracker("https://github.com/anthropics/claude-code/ISSUES/1") is True. |
| M112 (`453`) | No: empty path segments are not in TRACKER_SEGMENTS, so retaining them changes no result. | None exists: membership of the empty string in the pinned tracker set is False. |
| M113 (`458`) | No F/G with the pinned DNS hosts: hostname already lowercases those; only a custom scoped-IPv6 pin exposes the redundant conversion. | Assert host_ok("http://[fe80::1%25ZONE]/p", ("fe80::1%25zone",)) is True; outside-HOSTS helper arm. |
| M119 (`465`) | Yes F: wrong hosts with a pinned repository path are accepted; alternate GitHub/raw pins mask the positive test. | Assert host_ok("https://evil.example/anthropics/claude-code/x", HOSTS["Claude Code"]) is False. |
| M130 (`478`) | No: empty segments contain neither marketplace nor plugin words. | None exists: retaining empty segments is semantically inert with the remaining filters. |
| M133 (`479`) | Yes F: uppercase MARKETPLACE segments bypass marketplace rejection. | Assert token_well_formed(".x/plugins/MARKETPLACE.json") is False. |
| M134 (`481`) | Yes F: uppercase PLUGINS/EXTENSIONS token segments are falsely rejected. | Assert token_well_formed("PLUGINS/x.json") is True. |
| M135 (`481`) | No: retained empty words never belong to PLUGIN_WORDS. | None exists with the pinned nonempty plugin-word set. |
| M147 (`510`) | No: after deleting this guard, both empty/None forms are still skipped by the inner guard. | None exists for str-or-None inputs; the inner not-form guard preserves the result. |
| M149 (`514`) | No F/G: the judge only calls token_span for nonempty well-formed tokens, whose forms are nonempty. | Assert token_span("x", "/") is None; outside-token-grammar helper arm. |
| M152 (`517`) | Yes F: a token at quote position zero is falsely treated as absent. | Assert token_span(tok + " plugins exist", tok) == (0, len(tok)). |
| M157 (`519`) | No F/G: a same-start normalized form may have a shorter span, but only a prefix/trailing slash changes and no plugin-word interval changes sides. | Assert token_span("plugins/", "plugins/") == (0, 8); span-choice arm. |
| M159 (`527`) | Yes F: an outside plugin word ending exactly at the token start is falsely rejected. | Assert plugin_word_outside("plugins" + tok, 7, 7 + len(tok)) is True. |
| M161 (`527`) | Yes F: an outside plugin word starting exactly after a trailing-slash token is falsely rejected. | Assert plugin_word_outside("plugins/plugins", 0, 8) is True. |
| M163 (`536`) | No F/G: only empty paired quotes change stripping, and both spellings fail the minimum word count. | Assert strip_quotes(chr(34) * 2) == ""; helper-only arm. |
| M165 (`547`) | Yes F: Gate evidence with different backtick decoration is wrongly required to match both forms. | Assert quote_in_gate("plugin `x` lives", "plugin x lives", "plugin x lives") is True. |
| M173 (`569`) | Yes F: quotes of exactly three words are falsely rejected by the actual entry guard. | Replace Gemini quote and Gate quote with "extensions use gemini-extension.json"; both synthetic clients must remain backed. |
| M174 (`569`) | Yes F: quotes of exactly 25 words are falsely rejected by the actual entry guard. | Use a 25-word Gemini quote containing extensions and gemini-extension.json in both entry and Gate; both clients must remain backed. |
| M208 (`632`) | Yes F: using the last instead of first backticked span can bypass a malformed first token. | Gemini manifest cell "`package.json` then `gemini-extension.json`" must still reject Gemini. |
| M215 (`645`) | Yes F: exactly-three-word actions are falsely rejected. | Replace Gemini action with "read this first"; both synthetic clients must remain backed. |
| M218 (`647`) | Yes F: a differently named entry row can back the client if its other fields fit. | Rename only the Gemini entry Client cell to Nobody; backed() must contain only Claude Code. |
| M221 (`657`) | No F/G: changes only the diagnostic source-ID label. | An invalid entry with empty source ID must report a reason prefixed "entry row -:". |
| M238 (`731`) | No F/G: token_forms removes empty tokens before calling token_at_boundary. | Assert token_at_boundary(" ", "") is False; helper-only arm. |
| M257 (`754`) | No F/G: duplicate forms only repeat the same any() checks; empty forms are rejected by token_at_boundary. | Assert token_forms("plugins") == ["plugins"]; canonicalization/performance arm. |
| M260 (`773`) | Yes F: oversized pages are truncated to the limit and accepted instead of rejected. | Fake a 5-MiB-plus-one response with a valid quote near the start; fetch must raise the size error. |
| M261 (`774`) | Yes F: every ordinary call provides pins/base_keys, so the or condition rejects all pages. | Fake a fresh pinned URL with a small body and empty base-key set; fetch must return that body. |
| M262 (`774`) | Yes F: a redirect to an unpinned host is accepted. | Fake a response whose final URL is https://evil.example/x with nonempty client pins; fetch must raise OSError. |
| M263 (`774`) | Yes F: a redirect to an unpinned host is accepted. | Fake a response whose final URL is https://evil.example/x with nonempty client pins; fetch must raise OSError. |
| M264 (`774`) | Yes F: the host guard rejects pinned destinations and accepts off-host ones. | Fake a small response at its original pinned final URL; fetch must return its body. |
| M265 (`776`) | Yes F: every ordinary call provides pins/base_keys, so the or condition rejects all pages. | Fake a fresh pinned URL with a small body and empty base-key set; fetch must return that body. |
| M266 (`776`) | Yes F: redirected base SOURCES URLs are no longer rejected. | Fake a final URL in the supplied base-key set on a pinned host; fetch must raise OSError. |
| M267 (`776`) | Yes F: redirected base SOURCES URLs are no longer rejected. | Fake a final URL in the supplied base-key set on a pinned host; fetch must raise OSError. |
| M268 (`776`) | Yes F: fresh pages are rejected and base URLs are allowed. | Fake a fresh pinned final URL not in the supplied base-key set; fetch must return its body. |
| M269 (`778`) | Yes F: an exactly-5-MiB response is falsely rejected. | Fake a response of exactly 5*1024*1024 bytes; fetch must return it. |
| M270 (`778`) | Yes F: the read overflow byte is accepted instead of triggering the size guard. | Fake a 5-MiB-plus-one response; fetch must raise OSError. |
| M271 (`781`) | Yes F: the documented retry disappears for ordinary OSError/network failures. | Fake urlopen raising OSError once then returning a pinned small response; fetch must succeed on the second attempt. |
| M272 (`783`) | No F/G: after two failures either version throws; only error type/message changes. | Fake both attempts raising ValueError("sentinel"); assert fetch ultimately raises that ValueError, not fallback OSError. |
| M279 (`799`) | Yes G on a Git failure: an empty stdout is treated as a successful empty scan, falsely making held tokens new. | Fake the relevant ls-tree/cat-file command returning rc=1 and empty stdout; require EnvError, never empty results. |
| M282 (`808`) | No on well-formed Git output; malformed protocol records can bypass the required could-not-evaluate rejection. | Fake ls-tree stdout b"100644 blob abc\0" without its tab/path; ls_tree_blobs must raise EnvError. |
| M283 (`808`) | No on well-formed Git output; malformed protocol records can bypass the required could-not-evaluate rejection. | Fake ls-tree stdout b"100644 blob abc\0" without its tab/path; ls_tree_blobs must raise EnvError. |
| M293 (`826`) | No on well-formed Git output: only an impossible empty cat-file header changes. | Assert parse_batch(b"\n") == []; protocol-only arm. |
| M294 (`826`) | No on well-formed Git output; truncated headers can hang instead of rejecting. | A cat-file header b"abc missing" without newline must raise EnvError within a bounded one-second child run. |
| M300 (`834`) | No on well-formed Git output; truncated blob data can become an incomplete held scan instead of a rejection. | Assert parse_batch(b"abc blob 3\na") raises EnvError. |
| M301 (`842`) | No F/G on healthy Git: an unnecessary empty cat-file request still returns []. | Spy on git and assert read_blobs(lane, []) returns [] without invoking git; optimization arm. |
| M304 (`846`) | Yes G on a Git failure: an empty stdout is treated as a successful empty scan, falsely making held tokens new. | Fake the relevant ls-tree/cat-file command returning rc=1 and empty stdout; require EnvError, never empty results. |
| M305 (`854`) | No F/G: held_in_base filters empty tokens before this helper is called. | Assert held_in_text(" ", "") is False; helper-only arm. |
| M329 (`891`) | No F/G: empty tokens remain never-held and new_ground filters them anyway. | Assert held_in_base(valid_repo, rev, {""}) == {}; helper-map-shape arm. |
| M330 (`893`) | No F/G on healthy Git: the empty-token scan does unnecessary work but returns the same empty map. | With no tokens, spy that ls_tree_blobs is never called; optimization arm. |
| M333 (`903`) | No F/G on successful reads: scanning after all tokens are held cannot change True back to False. | With 257 blobs and every token held in the first batch, assert read_blobs is called once; optimization arm. |
| M334 (`903`) | Yes G: unresolved tokens after the first batch stop the scan before later held occurrences. | Use 257 blobs with the only held occurrence in blob 257; held_in_base must return True for that token. |
| M348 (`1527`) | No numeric F/G: changes unreadable-own-file handling from controlled exit 2 to a traceback. | Make self_sha raise OSError; main must return 2 and emit could-not-evaluate, without traceback. |
| M350 (`1531`) | No F/G for measurement invocations: only the mutually-exclusive self-test CLI rule changes. | Assert main(["--self-test", "--fetch"]) raises SystemExit(2). |
| M351 (`1531`) | No F/G for measurement invocations: only the mutually-exclusive self-test CLI rule changes. | Assert main(["--self-test", "--fetch"]) raises SystemExit(2). |
| M352 (`1534`) | No F/G: missing --rev is still rejected with code 2 by rev_ok(None), but no argparse usage error. | Assert main([]) raises SystemExit(2), rather than returning 2; CLI error-shape arm. |
| M356 (`1543`) | Yes F: a nonempty measured SKILL/entry/SOURCES/Gate file is replaced with the empty string. | The hermetic five-backed/five-found world with three new tokens must print F=5,G=3 and exit 0. |
| M357 (`1544`) | Yes F: a nonempty measured SKILL/entry/SOURCES/Gate file is replaced with the empty string. | The hermetic five-backed/five-found world with three new tokens must print F=5,G=3 and exit 0. |
| M358 (`1545`) | Yes F: a nonempty measured SKILL/entry/SOURCES/Gate file is replaced with the empty string. | The hermetic five-backed/five-found world with three new tokens must print F=5,G=3 and exit 0. |
| M359 (`1546`) | Yes F: a nonempty measured SKILL/entry/SOURCES/Gate file is replaced with the empty string. | The hermetic five-backed/five-found world with three new tokens must print F=5,G=3 and exit 0. |
| M360 (`1547`) | Yes F: erases all base IDs and base URLs and can admit an old source as new. | World with four new found rows and one base-ID row must print F=4 and exit 1, not count the base row. |
| M361 (`1548`) | No successful F/G are produced on the affected failures; changes controlled exit 2 into an uncaught exception. | Inject EnvError in the corresponding revision-read/base-scan stage; main must return 2 without traceback. |
| M362 (`1553`) | Yes F/G: rejected but otherwise fetchable rows are put in the backed/fetch/ground pipeline. | Four valid found rows plus a fifth with a two-word action must remain F=4 and exit 1 even if its page matches. |
| M363 (`1553`) | Yes F/G: rejected but otherwise fetchable rows are put in the backed/fetch/ground pipeline. | Four valid found rows plus a fifth with a two-word action must remain F=4 and exit 1 even if its page matches. |
| M364 (`1554`) | No F/G or predicate change: only denominator K is inflated; K has no threshold. | World with five well-formed client tokens and two absent rows must print "5 of 5", not "5 of 7". |
| M365 (`1554`) | No F/G or predicate change: only denominator K is inflated; K has no threshold. | World with five well-formed client tokens and two absent rows must print "5 of 5", not "5 of 7". |
| M366 (`1556`) | Yes F: --fetch no longer fetches anything, leaving F=0. | The hermetic five-found/three-new-token world must exit 0 and print F=5,G=3. |
| M367 (`1559`) | Yes F: fabricates found=True for every backed row without fetching any page. | Five backed rows with only four matching live pages must print F=4 and exit 1. |
| M368 (`1562`) | Can change a passing result to an uncaught failure if five rows are found and a sixth fetch raises a normal OSError. | Six backed rows, five matching pages, one OSError, and G=3 must still print F=5 and exit 0. |
| M369 (`1563`) | Yes F: a fetch exception counts as live-page evidence. | Five backed rows with four matching pages and one OSError must print F=4 and exit 1. |
| M370 (`1565`) | Yes F: missing live-page evidence no longer prevents the found increment. | Five backed rows with four matching pages and one quote-absent page must print F=4 and exit 1. |
| M371 (`1565`) | Yes F: counts not-found instead of found, rejecting a genuine five-found world. | Five backed rows all found, G=3, must print F=5 and exit 0. |
| M372 (`1566`) | Yes G: non-found backed tokens contribute new ground and can turn F=5,G=2 into G=3. | Five found rows using two distinct new tokens plus an unfound backed third token must stay G=2 and exit 1. |
| M373 (`1566`) | Yes G: non-found backed tokens contribute new ground and can turn F=5,G=2 into G=3. | Five found rows using two distinct new tokens plus an unfound backed third token must stay G=2 and exit 1. |
| M374 (`1566`) | Yes G: a --fetch measurement never computes its actual new ground, leaving G=0. | Five found rows spanning three new tokens must print G=3 and exit 0. |
| M375 (`1568`) | Yes G: a --fetch measurement never computes its actual new ground, leaving G=0. | Five found rows spanning three new tokens must print G=3 and exit 0. |
| M376 (`1569`) | No F/G: every backed row has a nonempty norm; even an injected empty value is later filtered by held_in_base/new_ground. | No claim-result arm exists; a helper spy can assert the tokens passed to held_in_base omit empty strings on an injected malformed report. |
| M377 (`1569`) | No F/G: every backed row has a nonempty norm; even an injected empty value is later filtered by held_in_base/new_ground. | No claim-result arm exists; a helper spy can assert the tokens passed to held_in_base omit empty strings on an injected malformed report. |
| M378 (`1572`) | No successful F/G are produced on the affected failures; changes controlled exit 2 into an uncaught exception. | Inject EnvError in the corresponding revision-read/base-scan stage; main must return 2 without traceback. |
| M379 (`1577`) | Yes G: non-found backed tokens contribute new ground and can turn F=5,G=2 into G=3. | Five found rows using two distinct new tokens plus an unfound backed third token must stay G=2 and exit 1. |
| M380 (`1578`) | No F/G/predicate change: only --json output selection is lost. | A valid --json run must emit a parseable JSON result with found/new_ground fields. |
| M381 (`1585`) | No F/G/predicate change: only reject/BACKED detail labeling changes. | For an absent client row, require a reject line; for a backed client, require a BACKED line. |
| M382 (`1585`) | No F/G/predicate change: only reject/BACKED detail labeling changes. | For an absent client row, require a reject line; for a backed client, require a BACKED line. |
| M383 (`1589`) | No F/G/predicate change: only fetch detail fields are omitted. | A found new client in a --fetch run must have "found=yes held-at-base=no" in its BACKED detail. |
| M384 (`1590`) | No F/G/predicate change: detail yes/no is reversed without changing stored found or the counts. | For a found client assert its detail says found=yes; for an unfound backed client assert found=no. |
| M385 (`1591`) | No F/G/predicate change: the held-at-base detail is omitted. | A found client must have a held-at-base=yes/no detail field. |
| M386 (`1592`) | No F/G/predicate change: held-at-base detail is reversed without changing G. | For a newly found token with no held occurrence, require detail held-at-base=no. |
| M387 (`1594`) | Yes: exits 0 for a valid empty revision with F=0,G=0, and also violates non-fetch-always-1. | Hermetic empty valid revision with --fetch must print F=0,G=0 and return 1 (also require a non-fetch run to return 1). |

## Highest-value gaps
- **CLI end-to-end path:** M387 (`main`, line 1594) replaces the terminal predicate call with literal `0`; all 184 assertions still pass. [INFERENCE] a valid empty revision would still print F=0,G=0 yet exit 0, directly breaking the claimed iff. This was not scored as an actual live C1 control. M367 similarly survives when every backed row is fabricated as found without calling fetch.
- **Found/fetch guards:** M260-M272 all survive: overflow-byte read, pinned-host redirect, base-URL redirect, size-limit equality/deletion, retry/error handling. Existing found helper tests never call `fetch`.
- **Inclusive boundaries in the actual backed judge:** M173/M174 reject exactly 3/25 quote words, and M215 rejects exactly three action words, while the self-test passes. The self-test has direct constant-expression word-count assertions but not these actual judge boundary paths.
- **Held scan completeness:** M334 reverses the pending-token stop condition and survives because the fixture fits in one batch. [INFERENCE] a token first held in blob 257 can be counted as new.
- The 129 survivors are **not 129 demonstrated claim exploits**: several are redundant guards, denominator/detail-only changes, or helper/error-domain differences. The survivor table distinguishes these from F/G-changing cases. The original author’s 54-mutant table may still describe those 54 runs; it does not establish every guard/operator has a discriminating arm.
## Restoration and bounds
Final observed `sha256sum` (exit 0, UTC `2026-10-23T04:34:49Z`):

```text
2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b  verifiers/check_plugin_manifests.py
2ac51d2a2f50d85590c307e6ef5aab05a0b660de42a33e5657011ecc05d6305b  mutation-probe/verifiers/check_plugin_manifests.py
```
The original tracked counter was never edited. The separate probe copy was restored in a `finally` block after every mutant, including the timeout; every restored detector printed the same hash and passed. Runs were in the owned clone with `TMPDIR` underneath it; no source byte in a sibling/lane was mutated. No integration, counter redesign, real plugin content, C2 change, package transaction, service restart or extra runtime/model call was performed. No further checks claimed.
