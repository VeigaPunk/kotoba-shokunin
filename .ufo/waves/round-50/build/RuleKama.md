# RuleKama — D3 fact base (kama vs kotoba on instruction artifacts)

Result: **HOLDS-BOUNDED** — kama's census row `adjacent` holds on the pinned bytes under both
stated precedences. The bound: kama `consumer-registry.md:111` records a truth verdict whose object
is a sibling SKILL.md's endpoint claim; it flips to `contested` only under a widened reading of
precedence (b) (any instrument at all over instruction artifacts), not under (b) as stated.

Pin `c808ba07f09c4be55413d3d6516c542ab69b64f8`; tip `1560e4d83f42b04f40336357de6f9637eafa0f4b`
(branch `master`). All quotes verbatim from `git show <rev>:<path>`; I read copies at
`/fast/scratch/hyaku/kotoba-r50/build/RuleKama/{pin,tip}/`. No language server answers Markdown or
git blobs, so this is literal reading, not semantic LSP proof.

## 1. Does kama's committed scope claim to write or audit other lanes' SKILL.md, prompts, AGENTS.md-class files, or instruments over them?

No craft claim, no write claim, no audit-of-wording claim. It claims one measurement over that file
class: local endpoint pins.

- `SKILL.md:3` (frontmatter): "Domain specialist — local model serving & endpoint health — scopes
  local LLM endpoints, baseURL drift, model-id reconciliation."
- `SKILL.md:8-9`: "This lane answers exactly one question: **is the thing at this baseURL the model
  this config believes it is, right now.**"
- `SKILL.md:18-19` (Domain): "`baseURL` values declared by consumer configs that point at a loopback
  port (OpenCode provider blocks, agent frontmatter, shell scripts, systemd units)." — agent prompt
  files enter scope only as declarations of a URL/model id.
- `PROVINCE.md:40`: "**Refuses:** model quality/eval (kengaku), credential material & auth flows
  (kagi), dispatch/route mechanism (kumitate), remote web surfaces (kake)." Instruction craft is
  never refused, never claimed.
- `PROVINCE.md:45`: "**Write boundary (hard):** kama never writes to `~/.config`, `~/.omp`, or
  systemd units."
- `corpus/knowledge/cross-lane-scope.md:3`: "That does not transfer ownership of the consumer's
  credentials, evaluation, route-selection mechanism, or instruction text to kama."
- `PROVINCE.md:15` claims the instrument: "| endpoint-consumers cross-lane registry |
  `corpus/knowledge/consumer-registry.md`, `cross-lane-scope.md` |".

What that registry actually does to instruction artifacts (the three cited anchors):

- `consumer-registry.md:91-92` (rows 2-3, `~/.config/opencode/agents/janitor.md`, `distiller.md`):
  endpoint verdicts FOREIGN_SERVICE, consuming lane named "`kotoba` [INFERENCE] (agent-instruction
  surface)". Purpose: endpoint verification; the wording owner is assigned away.
- `consumer-registry.md:111-112` (rows 22-23, kengaku): row 22 is
  "`~/projects/shokunin/kengaku-shokunin/SKILL.md:322-323`" with verdict "records FOREIGN_SERVICE on
  8080 / MODEL_OK on 34113 | kengaku"; row 23 is kengaku `PROVINCE.md:14` with "**MODEL_OK** ✅".
  This is a verdict on the truth of a sibling SKILL.md's endpoint statement — the only anchor whose
  judged object is a sibling SKILL.md.
- `consumer-registry.md:325-326`: absence sweep rows for `~/.config/opencode/skills`, `tools/`,
  `plugin/`, `agent/`, `command/` and "`~/.agents/` (skills + godspeed-core + AGENTS.md)" → both
  "**no matches** (exit 1)". Purpose: measurement (prove no endpoint pin exists), not audit.
- `consumer-registry.md:332`: sweeps "`~/projects/shokunin/kumitate-shokunin`, `kotoba-shokunin`,
  `kake-shokunin`, `kasegi-shokunin`, `.ufo/` (as *config*)" → "**no config pins**; every hit is
  prose/evidence in `corpus/**.md`". Again endpoint absence evidence across sibling trees.

No committed kama instrument over prompt text as a fixture method or craft check: `git grep -qE
'check_sibling_census|verify_skill_checklist|verify_dispatch_prompts|trigger-fidelity|floors-registry'`
at the pin, excluding `.ufo`, exits 1 (no match). kama has `tools/`, `tests/`, `registry/` but none
of them read a SKILL.md.

## 2. Does either side state a split covering the same artifact or function?

Yes, both sides, and they agree on the same sentence.

- kama `corpus/knowledge/cross-lane-scope.md:29`: "**Kotoba** owns the instruction/agent surface and
  its model/fallback wording; **kama** owns independent verification of the target endpoint."
  Same artifact class, same function (a model/fallback statement in an agent file vs truth about the
  service).
- `cross-lane-scope.md:13`: "**Kotoba:** agent/instruction surface, including the model and
  no-fallback claims."
- `cross-lane-scope.md:41` (handoff to kotoba): "kama has not edited those instructions."
- `cross-lane-scope.md:49-52` (Adjacency rule): out-of-domain predicates include "instruction
  content"; kama "MUST NOT absorb that domain's source edits".
- kotoba `SKILL.md:4-5`: "Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
  dispatch prompts / system prompts for trigger fidelity and decision density."
- kotoba `SKILL.md:10-12`: "Sibling boundary: the five `*-shokunin` domain skills (kagi, kake,
  kasegi, kengaku, kumitate) own their own SKILL.md content — this skill audits and reports; fixes
  route to the owning lane."
- kotoba `PROVINCE.md:44` (kama row) restates kama's split verbatim and carries the open note:
  "open: kama `corpus/knowledge/consumer-registry.md:91-92, 111-112, 325-326` audits agent prompt text
  and records a verdict on a sibling SKILL.md, which read literally could be `contested` — recorded
  for the integrator, not ruled here".
- kotoba's kotoba-core instruments are enumerated at `PROVINCE.md:14`: "Executable instruments over
  those surfaces — `verifiers/verify_skill_checklist.py`, `verifiers/verify_surfaces.py`, …". kama
  references none of them (same exit-1 grep as above).

Note for the D3 ruling: the kotoba census's own note at `sibling-overlap-census-round49.md:185-186`
says "The rule gives no precedence between the `contested` and `adjacent` arms; recorded for the
integrator, row stays `adjacent`." The same phrase "audits agent prompt text" overstates rows
325-326, which are absence sweeps; the only judging row is 111.

## 3. Did anything relevant change between pin and tip?

No. Seven commits between them; the two cited files are byte-identical.

- `consumer-registry.md`: 413 lines at pin and at tip; `diff -u` exit 0, 0 lines.
- `cross-lane-scope.md`: `diff -u` exit 0, 0 lines.
- `git diff --stat <pin>..HEAD -- SKILL.md PROVINCE.md MINT.md corpus`: SKILL.md 34 lines (all
  context-capacity / mutation-count rows), plus corpus `QUALITY.md`, `README.md`, `SOURCES.md`,
  `knowledge/context-capacity.md`, `knowledge/gguf-declared-identity.md`, `lessons/round-25*`;
  `PROVINCE.md` and `MINT.md` unchanged.
- Added corpus lines pin→tip mention only kama's own `SKILL.md` rows; none asserts a claim over a
  sibling instruction artifact (`git diff <pin>..HEAD -- corpus | grep '^+' | grep -iE
  'kotoba|SKILL\.md|AGENTS\.md|instruction surface|prompt craft'` → 5 lines, all self-references).
- `git grep -c 'kotoba'` per file: identical at pin and tip (MINT.md 2; consumer-registry.md 4;
  cross-lane-scope.md 3; listener-census.md 1). kama `SKILL.md` and `PROVINCE.md` contain no
  "kotoba" at either revision (`git grep -q` exit 1).

## 4. Rulings

**(a) A stated split covering the same function decides `adjacent` → `adjacent`.**
The split exists on both sides and is the same split, quoted at kama `cross-lane-scope.md:29` and
restated at kotoba `PROVINCE.md:44`. kama's registry does the half the split gives it (endpoint
truth) and names the wording owner in the same row. Nothing in kama's surfaces claims the wording
half, edits it, or instruments its quality. Confidence: high.

**(b) Any claim over kotoba-core instruments decides `contested` → `adjacent` as stated.**
"Kotoba-core instruments" are the verifier set at kotoba `PROVINCE.md:14`; kama references none
(grep exit 1). kama claims its own registry, which sweeps agent prompt text for endpoint pins. It
becomes `contested` only if (b) is widened from "kotoba-core instruments" to "any instrument that
touches instruction artifacts at all"; under that widening rows 325-326 and 332 qualify, though their
unit of analysis is endpoint absence, not instruction quality. If the integrator must pick one
precedence for the census entry, (a) is the one with committed text on both sides; (b) as written
adds nothing here beyond (a).

Residual unknown: I found no kama instrument, checklist or corpus statement that judges instruction
wording, prompt format or decision density; if one exists outside the paths swept (`SKILL.md`,
`PROVINCE.md`, `corpus/`, `tools/`, `tests/`, `registry/`), it would change answer 1.

## Evidence (commands, exit codes verbatim)

```
git -C kama-shokunin rev-parse HEAD                      -> 1560e4d83f42b04f40336357de6f9637eafa0f4b   (0)
git -C kama-shokunin rev-parse c808ba07f09c4be...69b64f8 -> c808ba07f09c4be55413d3d6516c542ab69b64f8 (0)
diff -u pin/.../consumer-registry.md tip/.../consumer-registry.md    -> 0 lines, exit 0
diff -u pin/.../cross-lane-scope.md   tip/.../cross-lane-scope.md    -> 0 lines, exit 0
git diff --stat <pin>..HEAD -- SKILL.md PROVINCE.md MINT.md corpus   -> 8 files, exit 0
git grep -qE 'check_sibling_census|verify_skill_checklist|verify_dispatch_prompts|trigger-fidelity|floors-registry' <pin> -- . ':!.ufo' -> exit 1
git grep -q 'kotoba' <pin> -- SKILL.md PROVINCE.md        -> exit 1
git grep -q 'kotoba' HEAD  -- SKILL.md PROVINCE.md        -> exit 1
git show <pin>:corpus/knowledge/consumer-registry.md | wc -l -> 413
git show <tip>:corpus/knowledge/consumer-registry.md | wc -l -> 413
```

No tools installed or upgraded this seat. Writes: only this report and the scratch copies under
`/fast/scratch/hyaku/kotoba-r50/build/RuleKama/` (no patch; nothing in the lane was edited).
