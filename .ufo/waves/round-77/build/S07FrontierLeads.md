# S07FrontierLeads — frontier ground leads for round 78+ (LEADS, not SOURCES rows)

Base: lane HEAD 6523aced1ee0ebe07dca996213bdc645a6acbd1e. All pages opened 2026-10-27 (UTC) with
`curl -sL -m 60 -A 'Mozilla/5.0'`; bytes were in my scratch dir (removed before yield; nothing
under scratch is citable, the URL+sha256 below is the re-open handle). Read first:
corpus/README.md `## Frontier`, PROVINCE.md `## Frontier`, corpus/SOURCES.md `## Leads (unopened)`.

Common finding: the lane holds *what reaches the model at offer time* (listing thresholds r54, S053/S055/S056/S058/S059/S063/S064, overlap levers r51)
and *where instructions live* (r53/r56/r58/r59/r60). It holds NOTHING about what happens to a skill body
AFTER it is loaded and the context is compacted. That is the one coherent hole the three leads below
come from (L1/L2), plus one prompt-altitude lead (L3). A fourth candidate (Vercel) is REFUSED below.

## L1 (rank 1) — Claude Code: invoked-skill content across auto-compaction

- URL: https://code.claude.com/docs/en/skills.md — HTTP 200, 117,982 B, fetched 2026-10-27T19:45:04Z,
  sha256 0fdcb266021ca13437dda9ea1137a53319b3f4dec703ff3164f9db94968ad286.
- Located quote (20 words, verified present in the fetched body; § "Skill content lifecycle", line 611):
  "Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each."
  Second span (9 words, same paragraph): "Re-attached skills share a combined budget of 25,000 tokens."
  Corroborating span, § troubleshooting line 1220: "put the most important instructions near the top of `SKILL.md`" (copy exact from page when minting).
- Not covered (sweeps, run at the base tree; the two files excluded by the grep -v filter, `harness-router-models-round9.md` and
  `opencode-offer-trace-round8.md`, each contain one "compact" hit about router models, not skill bodies):
  `grep -rnEi 'compaction|compacted|auto-compact' corpus/knowledge SKILL.md | grep -v 'harness-router-models-round9\|opencode-offer-trace-round8'` → 0 lines printed;
  `grep -rnEi 'Skill content lifecycle|re-attach|25,000' …` → 0 lines (grep exit 1);
  `grep -rnEi 'standing instructions' …` → one hit, resident-index-and-rungs-round72.md:31, which is the rung rule, not compaction.
  The page's URL is already held (S022/S053/S065) for other sections (listing cap, invocation form); this lead is a NEW SECTION on a held URL, so it needs a new row/anchor
  (S0xx "§ Skill content lifecycle"), not a recheck of S053. The SKILL.md `5,000` hit (line 175) is Cursor's body-size warning, unrelated.
- Craft rule it could ground: front-load the instructions that must survive; assume a body past ~5,000 tokens loses its tail after compaction in this client
  (documentary; no client run). Counterable as a claim: a counter that checks the quote/location on the committed snapshot and that the SKILL.md rule row cites it.
- PROVINCE scope check: IN (SKILL.md body craft, "what a skill author does", cf. Core rows for r54 thresholds and r74 body craft). Refuse: the compaction algorithm itself and long-context
  recall measurement — sibling kengaku (capability measurement; the lane already refused the Vercel/Chroma context-rot entry on exactly that ground, lessons/round-72.md) and, for memory/context
  tooling beyond the skill body, no listed sibling owns it, so report to the orchestrator.
- Risks: vendor-documented single client (tier A, docs); numbers can change per release (recheck short, e.g. 30d); a `--fetch` counter must tolerate the markdown-vs-HTML request profile (S049 errata).

## L2 (rank 2) — Agent Skills client-implementation guide, Step 5: protect and deduplicate skill content

- URL: https://agentskills.io/client-implementation/adding-skills-support.md — HTTP 200, 20,446 B, fetched 2026-10-27T19:45:05Z,
  sha256 07511caadbe1bad84d81477d0efce87bc2c7eaff562179522c083910586dfb06.
- Located quote (19 words; § "Protect skill content from context compaction", line 322, verified present):
  "Skill instructions are durable behavioral guidance — losing them mid-conversation silently degrades the agent's performance without any visible error."
  Neighbouring section "Deduplicate activations" (line 329): track activated skills and skip re-injection.
- Not covered: the URL is S002's page but S002's anchor is "§ Handling malformed YAML, § Lenient validation" only (corpus/SOURCES.md S002 row);
  `grep -rnEi 'exempt skill|Protect skill content|durable behavioral' corpus/knowledge SKILL.md` → 0 lines (grep exit 1);
  `grep -rnEi 'adding-skills-support' corpus/knowledge SKILL.md` → 0 lines (the SOURCES row exists; no knowledge entry or SKILL.md row cites the page).
- Why it pairs with L1: L2 is the spec's client-side rule (what a conforming client SHOULD do), L1 is one client's documented actual behaviour. Together they
  support a "what the client does to your body after load" table (spec rule vs Claude Code budget), with the honest gap stated: only one client documents numbers.
- PROVINCE scope check: IN as author-facing guidance and as the spec's reading of client duty; refuse the harness implementation guidance itself (writing a client = not SKILL.md/AGENTS.md craft;
  nearest sibling for harness/agent code is kumitate [INFERENCE from the adjacent-lane list; I did not re-read kumitate's PROVINCE.md]).
- Risk: guidance-level SHOULD, not a behaviour claim; tier A spec page, content may be revised (recheck 30–90d).

## L3 (rank 3, weakest) — Anthropic Engineering: "right altitude" for system prompts

- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents → 308 → https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
  (final HTTP 200, 241,154 B, fetched 2026-10-27T19:45:04Z, sha256 ec0eb251214b8b7d830518a033fd50626e7f5c7a21c1ec5c3551ca11f1e5b961; the HTML is one line, so a located quote
  needs a heading/anchor, not a line number — a counter must use a text anchor "The anatomy of effective context").
- Located quote (12 words, verified present): "The right altitude is the Goldilocks zone between two common failure modes."
  Context: hardcoded brittle logic vs vague high-level guidance; plus "striving for the minimal set of information that fully outlines your expected behavior (… minimal does not necessarily mean short)".
- Not covered: `grep -rnEi 'altitude|Goldilocks' corpus/knowledge SKILL.md` → 0 lines (grep exit 1). It is already named in SOURCES `## Leads (unopened)` (Anthropic Engineering — Effective context engineering) but never opened.
- Overlap warning (why rank 3): the r74 entry (spec-skill-creation-craft-round74.md) already holds "instructions graded by task fragility" and "a default instead of a menu" (S223); the altitude rule is the
  Anthropic-side restatement, so a claim here must name what it adds beyond S223 (a second independent vendor, tier A engineering post vs spec page) or it duplicates.
- PROVINCE scope check: IN for prompt craft; the page's compaction/memory/long-horizon sections are OUT (agent-runtime design; capability, not authoring) — refuse them, cite only the system-prompt anatomy section.

## Refused candidate — Vercel "AGENTS.md outperforms skills in our agent evals"

- Opened: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals — HTTP 200, 899,578 B, 2026-10-27T19:45:05Z, sha256
  e88f41ab03ac24795814d1e20069e4d97e3063eeb4adbd4c46429db3dc9c3744. Today the page DOES carry the spans the round-68 refusal could not locate (lessons/round-68.md:103, S168 "payload-absent"):
  "In 56% of eval cases, the skill was never invoked." and the 53% / 79% / 100% pass-rate table (verified present).
- Refused for round 78+ by the lane's own standing reason: substance is measured pass rate on one vendor's Next.js evals = capability measurement, sibling kengaku's ground (lessons/round-72.md "Rejected … (1)";
  flip condition there: "a craft rule that cannot be stated without the figure"). Nothing found today meets that flip. Recorded so a later round does not reopen it on "the page is now reachable".
  Note it is also not a documentary vendor-behaviour claim (no client doc), so it would be tier B/C at best.

## Recommendation

Round 78 claim shape: one entry "what a skill body keeps after compaction" on L1+L2 (counter: quote+snapshot+row-cited, same family as check_spec_craft/check_cn_vendor_surfaces; documentary evidence only).
L3 only if a delta over S223 is stated in the claim. These are leads, not registry rows; no SOURCES.md/README/PROVINCE edit was made.
