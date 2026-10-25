# RevEntryVersion — round-67 wave 2

## Attack and axes

Attacks the refusal of staged S123's `document version 2026/08/18` claim and the falsifiability of its flip condition. Axes: **source fidelity** (what the served bytes actually carry) and **checkability** (whether a later round can execute the flip test).

Measured landed revision: `da86c03e482a6aef433c34d733726b37c7cf6607` (HEAD; the reviewed lesson and entry were unmodified in the working tree). The independent source capture was in temporary sandbox `/tmp/rev-entry-version.html`, not at either Git revision.

## Finding — High: the refusal is falsified, and its flip condition is already satisfied

The **narrow** main-text observation survives, but the refusal based on it does not:

- The staged row really says `document version 2026/08/18` (`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:7`).
- The lesson refuses that identifier because it is absent from fetched main text, then permits a flip if it appears on a versioned permalink or in page metadata (`corpus/lessons/round-67.md:46-53`). M105 broader still calls it an identifier the source does not carry (`:93-101`). The entry repeats the main-text rationale (`corpus/knowledge/instruction-authority-ladder-round67.md:14-16`).
- The scout expressly scoped its result to extracted main text and left raw HTML/metadata uninspected (`.ufo/waves/round-67/w1/logs/ScoutModelSpec.log:121-123`). That evidence cannot support the broader refusal or evaluate the flip disjuncts.
- An independent `curl -L` fetch of the cited URL returned HTTP 200 without redirecting to another URL, 2,662,295 bytes, SHA-256 `72db50e5063c3c8942671c3ce6e30d0dd643de558eefd690aab127ec53bf4e5a`. Its raw HTML line 5 is exactly:

  ```html
  <title>Model Spec (2026/08/18)</title>
  ```

  The literal occurs **once** in the served HTML. A second fetch of the same canonical URL returned the same byte count and digest, again with one occurrence and one exact title tag.
- The same capture carries `<body data-model-spec-version="2026-08-18">` at line 1401 and `<div class="date-value">August 18, 2026</div>` at line 1869. A stdlib HTML text extraction excluding script/style/svg found zero `2026/08/18` occurrences in visible body text and one `August 18, 2026`, consistent with the scout's narrow report.

Thus the page itself supplies the exact slash-form identifier in its document title on the cited versioned permalink. The rendered body date is not wrong; the inference that the source does not carry the staged version string is wrong. At minimum the first flip disjunct, “appears verbatim on a versioned permalink,” is already true. The `<head>` document title also supplies the literal under the natural reading of “the page's own metadata,” but the verdict does not depend on resolving that terminology.

**Recommended verdict:** attack succeeds; the refusal does not hold. The existing flip rule supports an appended correction now rather than continued refusal. This is a review recommendation, not an admission or an integration.

## Is the flip condition checkable later?

**Yes as a predicate, but not by the main-text-only method documented in the scout log.** A later round can fetch the raw response from `https://model-spec.openai.com/2026-08-18` and search the served HTML/document title for the exact literal. That test is positive in this attack, so the condition is not merely a future hypothetical.

The condition is operationally under-specified in one respect: it does not say to inspect raw HTML or name `<title>`. A later round using only extracted main text could repeat the false negative. Naming the raw response and `<title>` would remove that ambiguity; no such ambiguity rescues the current refusal, because the literal is already on the versioned page.

## Residual risk and verification gaps

- The two raw fetches establish current, reproducible served bytes, not the identity of the scout's earlier FetchURL extraction. They do not overturn that extraction's reported body-text absence; they overturn the broader refusal.
- No browser/JavaScript execution was needed for the decisive evidence: the title is directly in the raw HTML. The body-text extraction was a scoped corroboration, not a claim about every possible client rendering.
- The lane has no durable raw-HTML receipt in this seat's allowed output scope. The temporary capture can disappear and the live page can drift; the digest, exact tag, URL, and line locations above are the durable evidence in this report.
