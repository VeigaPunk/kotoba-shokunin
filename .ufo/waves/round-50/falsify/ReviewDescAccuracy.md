# ReviewDescAccuracy: sibling clauses in kotoba's SKILL.md description (round 50 falsify)

VERDICT: FAILS for one clause. The clause "kengaku owns measured effects of prompt format" (SKILL.md:13) asserts more than kengaku's own bytes, which limit that ownership to measured capability effects. Applies to kotoba at 956ee1676e4c18480bce8ac3993541462be76e11, checked against the census pins. The other clauses: chousa HOLDS, kama HOLDS, kotodama HOLDS, tameshi HOLDS-BOUNDED, five-lane sentence HOLDS-BOUNDED.

Scope: the six sibling clauses in the description (SKILL.md:10-15), each checked against the sibling's bytes at its census pin, plus the census round-50 sentence that vouches for them (census lines 236-239). Not covered (other seats): the C1 and C2 counters, D1-D6, S024-S029.

Pins (all resolve with `rev-parse`, rc 0): chousa 6c5eb146, kama c808ba07, kengaku 1f3b0f1e, tameshi 3b20f073, kotodama 35f0d49f, kagi 899c50b4, kake e73d48bb, kasegi 1fafde8f, kumitate fac39171.

## Findings

### F1 MEDIUM: kengaku clause drops "capability" and "only"; census sentence overstates (Q26)

- Clause (SKILL.md:13): "kengaku owns measured effects of prompt format".
- kengaku SKILL.md:3 (pin): "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)".
- kengaku PROVINCE.md:30-32 (pin): "kotoba: prompt- and skill-craft rules, render/trigger behaviour — this lane keeps the *measured* effect of prompt format on capability and hands the reusable craft implication out."
- kengaku PROVINCE.md:138 (pin): "measured capability effects of prompt format stay here".
- kotoba's own PROVINCE.md:46 keeps the qualifier: "kengaku keeps measured capability effects of prompt format".
- Why it matters: the clause as written gives kengaku every measured effect of prompt format. That includes render and trigger behaviour, which kengaku's PROVINCE.md:30 assigns to kotoba and which kotoba's own description claims (SKILL.md:4-5, "trigger fidelity"). The description is the matching input, so a trigger-effect request would route to the wrong lane.
- Census overstatement: sibling-overlap-census-round49.md:237-239 says the four lanes added this round "state only the side the census already admits (... kengaku's measured effects of prompt format ...)". The census's own admitted kengaku quote is "kengaku keeps only measured capability effects" (census line 276). The census test is lexical (census lines 236-237 say so), so no counter turns on the ownership wording. Q26 (corpus/QUALITY.md:37) requires every clause of a headline to be turned on by a counter or a cited guard. This clause is not. Q26 fails for that sentence.
- Direction (not applied): restore kengaku's own words, "measured capability effects of prompt format" (PROVINCE.md:138), in the description, and correct the census sentence to match.

### F2 LOW: tameshi clause is supported, but kotoba's two surfaces disagree; the guard does not read boundary text

- Clause (SKILL.md:13-14): "tameshi owns the fixture and mutation method".
- tameshi SKILL.md:3 (pin): "Verification-fixture craft for 'hermetic suites', 'mutation testing', and 'gate fixtures'."
- tameshi PROVINCE.md:3-5 (pin): "verification-fixture craft — the reusable method of honest checks: hermetic suites, mutation testing, ..."
- tameshi PROVINCE.md:14-17 bounds the claim: "every lane's gate remains its own; tameshi owns only the reusable craft (a pattern is admitted from evidence in TWO independent lanes before it is claimed general)."
- kotoba's own PROVINCE.md:55 says "tameshi owns the fixture method", with no mutation. The description is wider than PROVINCE.md. The guard skips boundary text (PROVINCE.md:31-32: "the boundary text is not checked").
- Residual (conduct, not a clause error): the round's C2 instrument, verifiers/box_proof_case_deletion.py, is a deletion-mutation counter (docstring lines 2-11, 21-33). It does not cite tameshi. The description routes "the mutation method" to tameshi, so the integrator should decide whether kotoba's use on its own gate is intended. tameshi PROVINCE.md:14-17 would allow it.

### F3 LOW: five-lane sentence; bytes hold, but the census text does not cite them

- Clause (SKILL.md:10-11): "kagi, kake, kasegi, kengaku and kumitate own their own SKILL.md content".
- kagi: corpus/lessons/round-5-aggregator-mirror-bare-path-and-unclosed-prereq.md:3 "owner of the file cited below; the owning lane corrects `SKILL.md`". Also PROVINCE.md:50 and :53, where its checklist and self-count gates are bound to its own SKILL.md.
- kake: corpus/lessons/round-5-aggregator-mirror-pathless-cli-invocation.md:3 and :5 "Aggregator-owned file; the owning lane corrects `SKILL.md`."
- kasegi: corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:3 and :5 (same words). Also corpus/lessons/round-1-aggregator-audit.md:7 "`SKILL.md`/`LOG.md` are lane-owned".
- kengaku: corpus/lessons/round-1-aggregator-audit.md:6-7 "lane-owned `SKILL.md`/`LOG.md`/`PROVINCE.md` were not edited".
- kumitate: corpus/README.md:62 "against this lane's `SKILL.md`". Also PROVINCE.md:15 "registry: `SKILL.md` §Gate registry".
- Bounds:
  (a) Four of the five supports are aggregator-written text inside the lane's corpus, not the lane's own declaration.
  (b) The census does not cite these lines. Its kagi split is the `$HOME/.config/opencode` owner row (census lines 125-128; kagi corpus/README.md:96). Its kengaku basis is SKILL.md:3, which gives "skill craft" to kotoba, not content to kengaku (census line 276).
  (c) kengaku's text says "craft" and the description says "content". The description does not reconcile the two nouns.
  (d) The line "**Owns:** the domain knowledge, playbooks, error patterns, and checklists above." (kagi PROVINCE.md:5, kake :5, kasegi :24, kumitate :5, kengaku :5) points at nothing above it in PROVINCE.md. Reading it as SKILL.md ownership is an inference.

### F4 no finding: chousa clause HOLDS

- Clause (SKILL.md:12): "chousa owns the research method".
- chousa SKILL.md:3 (pin): "Deep-research method (調査) — question framing, source hierarchy, citation chaining, claim-vs-source verification."
- chousa SKILL.md:8-9: "the reusable METHOD of source research".
- chousa PROVINCE.md:3: "Domain: deep-research method (調査) — the reusable craft of source research."
- chousa MINT.md:24: "No province absorbs the research method."
- Bound, chousa corpus/README.md:876-877: "No promotion, outside spot-check or province expansion beyond deep-research method is self-awarded here."
- Other siblings state the same ownership: kagi PROVINCE.md:67, kake PROVINCE.md:34, kasegi PROVINCE.md:44, kumitate PROVINCE.md:27, kengaku PROVINCE.md:137. kotoba's own PROVINCE.md:38 says "the research method stays chousa's".
- Basis note: the census basis for chousa is kotoba-side only ("no chousa-side split was cited", census round-50 precedence section). chousa's bytes never name kotoba. The clause rests on kotoba's routing, and chousa's domain line supports it.

### F5 no finding: kama clause HOLDS

- Clause (SKILL.md:12-13): "kama owns endpoint verification".
- kama corpus/knowledge/cross-lane-scope.md:29 (pin), verbatim: "**kama** owns independent verification of the target endpoint." This is the census-admitted split.
- kama SKILL.md:8-9: "Local model serving & endpoint health. This lane answers exactly one question: is the thing at this baseURL the model this config believes it is, right now."
- kama SKILL.md:27-29 refuses model quality (kengaku), credentials (kagi), routing (kumitate) and web surfaces (kake).
- Caveat: "verification" is corpus-side wording; kama's SKILL.md says "health". kengaku contradicts itself on serving-plane ownership: PROVINCE.md:24-25 says "the model-serving plane ... no lane owns it", while PROVINCE.md:136 says kama "owns serving-plane health/detection and endpoint identity". The kotoba clause follows the kama side.

### F6 no finding: kotodama clause HOLDS

- Clause (SKILL.md:14-15): "kotodama owns naming and language for fictional worlds despite the similar name".
- kotodama SKILL.md:8-9: "...connects languages, cultures, myths, symbolisms, and eras to their linguistics and costumes for a fictional world".
- kotodama SKILL.md:26: "Name entities (people, places, gods, items) | naming-systems → phonotactics + morphology of the naming language".
- kotodama PROVINCE.md:3-7: "...naming systems — for fictional worlds, feeding the world bible."
- kotodama MINT.md:20-21: "kotoba owns prompt/skill craft despite its name."
- The clause is narrower than kotodama's own domain, so it does not over-assert.

## Evidence (commands and exit codes)

- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/lane`, then `git -C <lane> checkout -q 956ee1676e4c18480bce8ac3993541462be76e11`, then `git -C <lane> rev-parse HEAD`: rc 0; HEAD = 956ee1676e4c18480bce8ac3993541462be76e11.
- `git -C /home/vgpnk/Projects/shokunin/<lane>-shokunin rev-parse --verify <pin>^{commit}`, nine lanes: rc 0 each.
- `git -C <repo> show <pin>:<file>` for SKILL.md, PROVINCE.md, AGENTS.md and README.md of the nine lanes, plus 9 further scope files (MINT.md, corpus lessons and knowledge files cited above): rc 0 each. Copies are in /fast/scratch/hyaku/kotoba-r50/falsify/ReviewDescAccuracy/sib/.
- `git -C <repo> grep -n -i -E <pattern> <pin> -- . ':(exclude).ufo' ':(exclude)reports' ':(exclude)LOG.md' ':(exclude)SCORECARD.md' ':(exclude)*.json' ':(exclude)*.log' ':(exclude)*.jsonl' ':(exclude)*.tsv'`, one run per clause keyword and lane: rc 0; matches quoted above.
- `git -C <lane> grep -c -i -w kotoba` (scope surfaces, counts): kagi 27 hits in 13 files; kengaku 92 hits in 26 files; kasegi 3 in 1; kake 2 in 1; kumitate 2 in 2.
- `git -C <lane> grep -n -i -E "tameshi|mutation" 956ee1676e4c18480bce8ac3993541462be76e11 -- verifiers/box_proof_case_deletion.py`: rc 1 (no match).
- `git -C <lane> grep -n -E "^\| Q2[4-7] |Q25|Q26" -- corpus/QUALITY.md`: rc 0. Q25 is at line 36 and Q26 at line 37.
- Not run by this seat: `verifiers/check_sibling_census.py`. The C1 counter belongs to another seat; census line numbers were read from the pinned file.
- No web sources opened. Tools installed or updated: none.
- Writes: this report file only in the lane checkout. All other scratch is under /fast/scratch/hyaku/kotoba-r50/falsify/ReviewDescAccuracy/.

## Residual risk and gaps

- Whether the round's own source sweeps (S024-S029) count as chousa's "research method" (PROVINCE.md:38 says kotoba "never re-derives it"): [INFERENCE], not assessed.
- For long SKILL.md files I read the first 33 lines and searched the rest with `git grep` at each pin. Keyword hits outside those searches were not checked.
- Not checked here: the description's 1,024-character cap and the C1 count (other seats).
