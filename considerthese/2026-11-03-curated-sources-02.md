# kotoba: second curated source to consider after hyaku

Date: 2026-11-03

**Status: unassimilated future candidate after hyaku.** Reading proposal only: no training, execution, assimilation, dependency adoption or external changes. Earlier notes remain unchanged.

## Guidance: separating syntactic constraints from prompt meaning

- Primary source: <https://github.com/guidance-ai/guidance/tree/21b1d90dfbebff4b141df70c714c8af15aa5f4af>
- Domain fit and new gap: Adds a contract-design angle beyond context organization and Promptfoo regression declarations: regex, finite choices and JSON schemas can constrain output form, while semantic correctness remains a separate obligation. Unit tests include malformed integers and unsatisfiable bounds.
- Precise reading: README.md — Guarantee output syntax with constrained generation; Debug grammars offline; Generating JSON; tests/unit/library/json/test_json.py — TestInteger.test_bad_integer; test_unsatisfiable_min_max.
- Future question: Which parts of a skill’s response contract are syntax, and which require semantic judgment?
- Proposed later evaluation (original lane-specific design): After hyaku, split one response contract into a syntax checklist and meaning checklist. Propose positive, malformed, schema-valid-but-wrong, and impossible-schema examples, including a refusal case that must not be forced into a success-only schema. Compare paper expectations for prose-only and constrained-output variants without claiming any installed client supports the backend.
- Limitations: Grammar guarantees depend on backend support; schema-valid output can be factually wrong. This is not a replacement for skill-trigger discovery or evidence about client loading. No provider calls, dependency adoption or prompt optimizer work.
- License/reuse: MIT; official pinned license read at <https://raw.githubusercontent.com/guidance-ai/guidance/21b1d90dfbebff4b141df70c714c8af15aa5f4af/LICENSE.md>. Preserve applicable notices; dependencies and external data need separate review.
- Version/timestamp: Official API returned 21b1d90dfbebff4b141df70c714c8af15aa5f4af with committer timestamp 2026-05-21T17:08:00Z. Commit snapshot, not a release assertion or proof of latest maintenance. Fetched 2026-11-03.
- Deduplication: All supplied lane existing-context files, including published first-batch notes, and existing-urls.json. Repository aliases and source-family names checked. Not a claim about unprovided historical files. No exact-URL or source-family match found. DSPy/GEPA remain excluded as already queued.

### Verification links

- <https://api.github.com/repos/guidance-ai/guidance/commits/21b1d90dfbebff4b141df70c714c8af15aa5f4af>
- <https://raw.githubusercontent.com/guidance-ai/guidance/21b1d90dfbebff4b141df70c714c8af15aa5f4af/README.md>
- <https://raw.githubusercontent.com/guidance-ai/guidance/21b1d90dfbebff4b141df70c714c8af15aa5f4af/LICENSE.md>
- <https://raw.githubusercontent.com/guidance-ai/guidance/21b1d90dfbebff4b141df70c714c8af15aa5f4af/tests/unit/library/json/test_json.py>

