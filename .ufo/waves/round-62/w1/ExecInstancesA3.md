# Round 62 W1 — E2 / E2b concrete instances

## Scope and result

Produced two E2 (`A3(a)`) rejection instances, three accepted E2 normalization controls, two E2b (`A3(b)`) rendering-alias rejection instances, and one accepted E2b distinct-path control. Each was passed to the named arm-level function loaded from `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py` in the scratch probe. The E2 probe also called `url_key` for the base and candidate URLs.

The observed results match the expected verdicts below. E2's locale and `.mdx` divergences return the existing generic “no base row with this URL” reason; `/rules`, trailing slash, and query variants normalize to the base key and return `[]`. E2b rejects the locale and `@latest` renderings with the A3 alias reason, while a distinct path returns `[]`.

## Frozen instance literals

`input` is the positional argument tuple for the named guard; it can be frozen as `guard(*input)`. E2's `base_rows` and `base_lines` are included in each tuple so the instance is self-contained.

### E2 — A3(a) `url_key` identity through `reopen_why`

```python
[
    {
        "id": "E2-locale-segment-reject",
        "guard": "reopen_why",
        "input": (
            ["S118", "", "", "", "", "", "re-opens S112 — locale URL"],
            "https://docs.example.com/ja/rules",
            "paths",
            {"S112": ["S112", "https://docs.example.com/rules.md"]},
            {"S112": ""},
        ),
        "expected_verdict": "REJECT",
        "expected_reason_substring": "re-open names no base row with this URL",
    },
    {
        "id": "E2-mdx-suffix-reject",
        "guard": "reopen_why",
        "input": (
            ["S118", "", "", "", "", "", "re-opens S112 — suffix URL"],
            "https://docs.example.com/rules.mdx",
            "paths",
            {"S112": ["S112", "https://docs.example.com/rules.md"]},
            {"S112": ""},
        ),
        "expected_verdict": "REJECT",
        "expected_reason_substring": "re-open names no base row with this URL",
    },
    {
        "id": "E2-md-drop-accept",
        "guard": "reopen_why",
        "input": (
            ["S118", "", "", "", "", "", "re-opens S112 — md omission"],
            "https://docs.example.com/rules",
            "paths",
            {"S112": ["S112", "https://docs.example.com/rules.md"]},
            {"S112": ""},
        ),
        "expected_verdict": "ACCEPT",
        "expected_reason_substring": None,  # expected reasons == []
    },
    {
        "id": "E2-trailing-slash-accept",
        "guard": "reopen_why",
        "input": (
            ["S118", "", "", "", "", "", "re-opens S112 — trailing slash"],
            "https://docs.example.com/rules/",
            "paths",
            {"S112": ["S112", "https://docs.example.com/rules.md"]},
            {"S112": ""},
        ),
        "expected_verdict": "ACCEPT",
        "expected_reason_substring": None,  # expected reasons == []
    },
    {
        "id": "E2-query-accept",
        "guard": "reopen_why",
        "input": (
            ["S118", "", "", "", "", "", "re-opens S112 — query variation"],
            "https://docs.example.com/rules?view=print",
            "paths",
            {"S112": ["S112", "https://docs.example.com/rules.md"]},
            {"S112": ""},
        ),
        "expected_verdict": "ACCEPT",
        "expected_reason_substring": None,  # expected reasons == []
    },
]
```

### E2b — A3(b) `alias_why` for fresh rows

```python
[
    {
        "id": "E2b-ja-locale-reject",
        "guard": "alias_why",
        "input": (
            "https://docs.example.com/ja/rules",
            [("S113", "https://docs.example.com/rules")],
        ),
        "expected_verdict": "REJECT",
        "expected_reason_substring": "rendering alias of the committed row",
    },
    {
        "id": "E2b-at-latest-reject",
        "guard": "alias_why",
        "input": (
            "https://docs.example.com/rules/@latest",
            [("S113", "https://docs.example.com/rules")],
        ),
        "expected_verdict": "REJECT",
        "expected_reason_substring": "rendering alias of the committed row",
    },
    {
        "id": "E2b-distinct-path-accept",
        "guard": "alias_why",
        "input": (
            "https://docs.example.com/guides/advanced",
            [("S113", "https://docs.example.com/rules")],
        ),
        "expected_verdict": "ACCEPT",
        "expected_reason_substring": None,  # expected reasons == []
    },
]
```

## Exact scratch evidence

Scratch script: `/fast/scratch/hyaku/kotoba-r62/ExecInstancesA3/probe.py` (outside the lane). It loaded the counter with `runpy.run_path` and called `url_key`, `reopen_why`, and `alias_why` directly.

Command:

```sh
date -u; python3 -B /fast/scratch/hyaku/kotoba-r62/ExecInstancesA3/probe.py; rc=$?; printf 'exit code: %s\n' "$rc"; exit "$rc"
```

Pasted output:

```text
Fri 23 Oct 2026 08:50:46 PM UTC
E2: url_key + reopen_why
E2-locale-segment-reject: url_key(base)='//docs.example.com/rules'; url_key(reopen)='//docs.example.com/ja/rules'; reasons=['re-open names no base row with this URL']
E2-mdx-suffix-reject: url_key(base)='//docs.example.com/rules'; url_key(reopen)='//docs.example.com/rules.mdx'; reasons=['re-open names no base row with this URL']
E2-md-drop-accept: url_key(base)='//docs.example.com/rules'; url_key(reopen)='//docs.example.com/rules'; reasons=[]
E2-trailing-slash-accept: url_key(base)='//docs.example.com/rules'; url_key(reopen)='//docs.example.com/rules'; reasons=[]
E2-query-accept: url_key(base)='//docs.example.com/rules'; url_key(reopen)='//docs.example.com/rules'; reasons=[]
E2b: alias_why
E2b-ja-locale-reject: reasons=["A3: URL 'https://docs.example.com/ja/rules' is a rendering alias of the committed row S113 URL 'https://docs.example.com/rules'"]
E2b-at-latest-reject: reasons=["A3: URL 'https://docs.example.com/rules/@latest' is a rendering alias of the committed row S113 URL 'https://docs.example.com/rules'"]
E2b-distinct-path-accept: reasons=[]
exit code: 0
```

## Risks and blockers

Risk: this is direct arm-level evidence for the requested E2/E2b cases; it does not measure integration into the full absorption instrument. No other checks were run. No blocker.

Files changed: `.ufo/waves/round-62/w1/ExecInstancesA3.md` only. Scratch probe is outside the lane. No installs.

Installs: no installs.
Blockers: none.
Produced: froze two E2 rejects, three E2 controls, two E2b rejects, and one E2b control with direct guard outputs.
