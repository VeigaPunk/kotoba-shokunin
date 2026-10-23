# Round 61 — RevC3Bleed report (C3 cross-domain bleed audit)

Seat: `RevC3Bleed` (reviewer, adjacency). Date: 2026-10-23 (UTC). Scope: audit the C3 import for cross-domain bleed — read the kama source and the ScribeC3 draft (landed at `.ufo/waves/round-61/wave/ScribeC3.md`); kotoba must cite kama's practice, not absorb kama's domain content (endpoint/serving specifics); the entry must be useful for prompt-craft self-assessment. Read-only; no writes outside this report.

## Verdict

**`bleed clean`** — the drafted S117 row, knowledge entry, and README coverage-map row are practice-level borrowing only. No kama domain content, findings, measurements, implementation, parser rules, source data, or conclusions are imported. Two boundaries checked:

- **Boundary 1 — domain-content boundary (cite practice, do not absorb kama's domain):** the borrowed material is limited to (a) the writing-revision calibration principle and (b) the six statement-class labels P/H/N/C/T/Q used as a classification *pattern*. None of kama's artifact-specific content is imported.
- **Boundary 2 — usefulness boundary (the entry must serve kotoba's prompt-craft self-assessment):** the entry lands the borrowed practice on kotoba's own self-assessment surfaces (`SKILL.md`, `SCORECARD.md`) as a craft recommendation, with an explicit "pattern to consider, not implemented" hedge; it does not restate kama's calibration results.

## Evidence read

| Artifact | Path | What it established |
|---|---|---|
| kama source | `/home/vgpnk/Projects/shokunin/kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` | The actual borrowed file: entry head line 5; calibration principle line 7; six classes lines 9–16; correction-format prescription line 18; base receipt numbers line 20; extractor bound line 22; failure-meaning note lines 24–33 |
| kama province | `/home/vgpnk/Projects/shokunin/kama-shokunin/PROVINCE.md` | Kama's domain is **local model serving & endpoint health** (baseURL drift, served-model reconciliation, probe conventions, llama-server, ports 8080/34113, GGUF). Nothing from this domain appears in the C3 drafts |
| kotoba province | `/home/vgpnk/Projects/shokunin/kotoba-shokunin/PROVINCE.md` | Kotoba's domain: prompt & skill craft; confirms `SKILL.md`, `SCORECARD.md`, `SHONEN.md` are kotoba's own surfaces (entry's mapping target) |
| ScribeC3 draft | `kotoba-shokunin/.ufo/waves/round-61/wave/ScribeC3.md` | The three draft artifacts under audit: S117 row, `corpus/knowledge/writing-revision-calibration-round61.md`, corpus README coverage-map row |
| SOURCES contract | `/home/vgpnk/Projects/shokunin/CORPUS.md` § SOURCES.md | kind/tier/scope/anchor/teaches rules; `own-work` = "a repo path or command" |
| Plan C3 text | `kotoba-shokunin/plans/round-61.md` | Frozen C3 scope: tier B scoped to "writing-revision calibration for prompt-craft self-assessment", kind `own-work`, anchor "the entry head", status queued, opened 2026-10-23, recheck 180d, used-by the entry |

## Boundary 1 — domain-content check (line-by-line against the source)

O scan of the three drafted artifacts (S117 row, entry, README row) for kama-domain tokens — `llama|endpoint|probe|serving|GGUF|baseURL|8080|34113|model_id|/v1/models|/health|/props|/slots|connection-refused|DEAD|consumer|qwen|systemd` — returned **zero matches** (grep over `.ufo/waves/round-61/wave/ScribeC3.md`, 2026-10-23). The only kama-identifying strings in the drafts are the citation itself (`../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md`) and the six class labels, both required by the frozen scope.

What the entry borrows vs. what it leaves behind:

| Draft section | Borrows (practice) | Leaves behind (kama domain/mechanics) |
|---|---|---|
| § Borrowed practice | The *idea*: bind each statement to its writing revision and check support against the evidence state at that revision, separating a then-present calibration error from later drift | `git blame --line-porcelain`, `W` acquisition, the `git merge-base --is-ancestor` commit test, `%ct` committer-time mechanics, the P/H/N/C/T/Q check details (path/blob rules, hex windows, exclusion tokens `llama.cpp`/`upstream`/`ufo-fsd`/`@`) |
| § Claim-shape taxonomy | The six class *labels* P/H/N/C/T/Q as a pattern for classifying claims in `SKILL.md`/`SCORECARD.md` | The concrete parser rules per class; the correction-row format (`SA29:<sid>`, byte-prefix rule); the "frozen base files" concept |
| § Boundary | Explicit scope statement: practice-level borrowing only, tier B, not sole support | The base receipt numbers (69 extracted / 11 mismatched / 0 valid / 11 unresolved), `before/c1-base.json`, the w1 critic/Confirm-seat failure discussion |

Two words deserve explicit note so they are not misread as silently imported domain content:
- **"drift"** in the entry ("drift that happened afterward") is generic claim-state drift, the calibration concept itself — not kama's endpoint-drift detection domain.
- **"revision"/"class"** are used in their generic craft sense; the entry does not adopt kama's `W` notation, its class definitions, or its artifact names.

The entry does not paraphrase-claim kama's results; its § Boundary explicitly disclaims "no kama domain content, findings, measurements, implementation, parser rules, source data, or conclusions" — and the scan confirms that sentence is accurate.

## Boundary 2 — usefulness for prompt-craft self-assessment

- The entry's §1 states the calibration principle in implementation-agnostic terms and ties it to the self-assessment question that matters for craft: "whether a claim was grounded when authored rather than merely whether it still matches today's state."
- The entry's §2 makes a concrete, actionable recommendation for kotoba: classify claims in `SKILL.md`/`SCORECARD.md` by shape (P/H/N/C/T/Q as labels), then ask what evidence would support each kind at its writing revision. This is a usable prompt-craft lever, not a description of kama's checker.
- The hedge "a taxonomy pattern to consider, not a claim that kotoba's documents already implement these checks" is honest and prevents any silent overclaim.
- The `teaches` cell is grounded in the source's demonstrated content (line 7's before/after distinction) and stays within the scoped tier-B claim.

The entry is useful for prompt-craft self-assessment. It is thinner on "how to implement" than on "what to consider" — a depth preference, not a bleed defect.

## Findings (severity order)

1. **Low — Gate quote not verbatim (fidelity nit).** The draft's located quote (ScribeC3.md line 15) is:
   `"evaluates the statement against the committed tree/history at W, not just against the current tip."`
   Source line 7 reads: `The check then evaluates the statement against the committed tree/history at `W`, not just against the current tip.`
   The draft omits the backticks around `W`; the opening words ("The check then") are dropped, which is a legitimate truncation, but the backtick removal makes the span not strictly verbatim. Word count 15 is correct and the quote is located at `:7`. Recommendation: keep the backticks in the landed Gate line (`corpus/lessons/round-61.md` § Gate) so the quote is byte-verbatim; the plan's counting gate (`grep -c 'self-assessment-at-writing'`) is unaffected.
2. **Info — `kind=own-work` for a sibling-lane artifact is semantically stretched** (contract v1: `own-work` = "a repo path or command", and every precedent own-work row S009/S010/S015/S020 is the lane's own gate). The plan froze `own-work` and `ExecC3Row` is tasked with recording the kind/tier rationale; flagging for the L1 that the rationale should note why `own-work` is chosen over `docs`/`code` for a sibling's primary artifact. This is a classification-honesty question, not bleed.
3. **Info — positive observation:** kotoba already runs `trigger.citation_resolves` (rounds 16/17) on claim citations in its self-report files; the borrowed writing-revision calibration complements that existing claim-citation check. The entry does not tie the two together — optional enrichment, not a defect.

## Residual risk and verification gaps

- **No pinned hash/commit for the kama file** in the draft (ScribeC3 states this itself). I read the file at the host's current checkout; I did not capture a commit pin either. If the kama file changes before integration, the Gate quote and row must be re-verified. `ScoutAdjacency` is the seat tasked with reflecting kama-file updates; my verdict is against the bytes I read on 2026-10-23.
- Integration gates (`grep -c 'self-assessment-at-writing' corpus/SOURCES.md` → 1, `test -f` on the entry, README row presence) are L1 integration measures, not run by this seat; the draft correctly does not claim them passed.
- No measurement was performed in this audit (read-only review); the only "measurement" evidence above is the grep sweep and file reads, all 2026-10-23.

Installs: no installs.
Blockers: none.
Produced: C3 bleed audit — verdict `bleed clean` with the two boundaries (domain-content, usefulness) checked line-by-line against the kama source and the ScribeC3 draft; one low-severity quote-fidelity nit and two informational notes filed.
