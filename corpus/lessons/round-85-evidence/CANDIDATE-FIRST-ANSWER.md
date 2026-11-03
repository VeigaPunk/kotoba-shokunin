# Kotoba round85: first complete candidate answer

Inputs: the four fictional tasks in corpus/lessons/round-85-freeze/candidate/NEUTRAL-INPUTS.md at parent-reported freeze ba8716a9baaf91951f395ebba6ba72ae71d9ee8d. Applied the frozen candidate METHOD.md and SOURCE-NOTES.md. No scenario action was executed. This is an authored instruction-editing exercise, not measured model performance. No baseline answers, hidden expectations or reviewer rubric were read. The prior disclosed development work remains prior work, not a fresh blind baseline.

## H1 — Export desk

### Replacement body

Before packaging, clarify any missing destination or unreadable field selection. Classify the export as a partner bundle if destination is `partner` OR the selected fields contain `partner_token`; either condition suffices. Otherwise use the normal CSV download action.

For a partner bundle, obtain current approval for this destination before packaging begins. Read `references/partners.md` for the partner formatting table and apply it when packaging, then download. If approval is missing or not current, or required formatting cannot be read, stop packaging and resolve the missing prerequisite.

### Detail placement and reasoning

Keep the OR classifier, missing-input rule and pre-packaging approval in the body. Leave the long formatting table in `references/partners.md`, loaded only on the partner branch before packaging. The condition is now decidable without opening the withheld reference. It is a repair of the circular existing body against the task's explicit behavior, not a claim that the old sentence already expressed a sufficient classifier.

State replay: either partner indicator leads to the approved partner path; neither leads to ordinary CSV. An unreadable selection or missing destination is not permission to infer an ordinary export, even when another indicator is available. No packaging may precede clarification and applicable approval. The task does not specify an approval lookup mechanism or formatting fallback, so neither is invented.

## H2 — Simulation desk

### Replacement body

Prepare local simulations only; never submit them. Reuse a saved simulation result only if its input digest AND rules version both match the current request. A missing digest or version is not a match. Otherwise create a fresh local simulation.

Preserve the result's status: only READY may be labeled ready for operator review. REVIEW and UNKNOWN must retain those exact statuses and stop without submission. If a status needs explanation, read `references/status-examples.md`; examples never override these status rules.

Use plain text when no theme ID is supplied. When a theme ID is supplied, read `references/theme.md` before applying its formatting. If the requested theme cannot be resolved, ask for clarification rather than silently substituting a different theme. Formatting does not change status or authorize submission.

### Detail placement and reasoning

Keep the local-only boundary, both cache-match conditions, missing-metadata behavior and status gate visible once in this shared procedure. Keep the fifty explanatory examples conditional on a need to explain a status, rather than loading them to discover what READY permits. Theme detail loads only for a supplied ID; plain text needs no theme file.

Delete repeated wording only if each of the six original sections reaches this shared procedure before reusing, creating or labeling a result. If they are independent entrypoints, retain an explicit mandatory pointer at each rather than leaving any entrypoint unguarded.

State replay: two known matches permit reuse; one mismatch or missing value requires a fresh local simulation. READY permits a readiness label, never submission. REVIEW and UNKNOWN preserve their status and stop. Assumption: saved results carry a usable result status; missing or unrecognized saved status does not justify a READY label and needs clarification. No status conversion or new submission route is inferred.

## H3 — Two-stage release exercise

### Replacement body

Keep the entire exercise simulated. Preview is harmless and separate from the irreversible simulated release; approval of a preview alone never authorizes release.

Before simulated release, verify operator approval for the current artifact's specific digest and read and complete `references/release-checks.md`. Do not release if the approved digest does not match, approval is absent, or the required checklist cannot be completed. If the artifact changes after checking, verify both its digest authorization and the checklist again before release.

If the release response is lost, look up the receipt using that operation's ID before considering any retry. An absent or ambiguous receipt means stop for operator reconciliation. A receipt showing the release already occurred does not authorize repeating it. Do not infer permission to retry merely because the response was lost; any permitted retry must still satisfy the current artifact's release prerequisites.

### Detail placement and reasoning

Leave the detailed compatibility checklist in `references/release-checks.md`; the body requires its load before release, not merely after an error. Keep preview-versus-release authorization, digest binding, artifact-change invalidation and uncertain-outcome reconciliation in the body. These small rules determine whether the long checklist or a retry is reachable lawfully.

State replay: preview-only approval never reaches release. A matching approved digest plus completed checks permits the simulated release. Artifact change invalidates both earlier checks, not just the checksum comparison. Lost response leads first to receipt lookup; absent or ambiguous receipt stops for the operator. A lost operation ID likewise cannot satisfy lookup and requires reconciliation, not a guessed replacement ID.

The input gives no definitive-failure receipt schema or independent retry grant. The replacement deliberately does not invent either. Repetition in the eight paragraphs may be removed only where these guards remain reachable from every affected entrypoint.

## H4 — Conflicting selector

### Replacement body

Check the client before selecting a flag. Client B is unsupported: hand off without inventing flags. For client A, use the supplied version; if it is missing, query the installed version read-only. If discovery fails, ask for the version before selecting a flag. Use `compact` for version1 and `dense` for version2. For any other or unresolved version, obtain supported-version guidance instead of guessing a flag.

Use the default layout when no style ID is supplied. With a supplied style ID, read `references/styles.md` before formatting; if that style cannot be resolved, ask for clarification rather than inventing its rules.

Read the troubleshooting table in `references/errors.md` only when an actual error code is returned, and use the matching entry. Do not infer an error code from uncertainty about the client, version or style. If the code has no usable entry, report that limitation rather than inventing recovery steps.

### Detail placement and reasoning

Keep client support, version discovery, the two explicit version-to-flag mappings and the missing-style default in the body. Both branch classifiers are available before flag selection or formatting. Style rules remain conditional on a supplied style ID; the sixty-message troubleshooting table remains conditional on an observed error code. Neither reference is needed for the ordinary no-style, no-error path.

State replay: B hands off before flag selection; A with version1 selects compact, version2 selects dense, missing version uses allowed read-only discovery, failed discovery asks rather than guesses. Missing style chooses default; supplied style loads its rules. Actual error activates troubleshooting; absence of an error does not.

The fictional guide supplies no command syntax, handoff recipient, unsupported-A-version policy beyond supporting1and2, or invalid-style fallback. These instructions therefore do not manufacture executable commands, recipients or a substitute style. Repeated explanations can be replaced by this shared procedure only if every original entrypoint still reaches its relevant guard.

## Scope of this answer

The replacement bodies are intended to preserve the supplied fictional behavior while making its guards reachable and leaving long optional or branch-specific material conditional. Conservative handling of unspecified situations is identified above rather than presented as quoted policy. File existence, word counts and repeated keywords cannot establish the semantic comparison; the independent reviewer owns that judgment. No comparative improvement or round admission is self-awarded here.
