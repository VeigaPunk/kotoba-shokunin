# SiblingOverlapScan — round 51 build (connector, read-only)

Result: NO sibling owns the overlap-lever ground. It stays kotoba's (prompt and skill craft).
Two sibling facts bear on C2 and should be cited, not absorbed: kumitate's name-keyed skill
precedence for kimi, and kagi's last-match-wins ordering for opencode `permission` rules.

Seat: `KotobaR51.SiblingOverlapScan`, 2026-10-22T14:18:53Z to 14:23Z. Lane base `43ca0bfb`.
Nothing installed or updated. Nothing was written except this file.

## Scope note

The assignment asked for each sibling's `master`. Seven siblings have no `master` branch:
audio, game-dev-2d, game-dev-3d, kaidoku, kotodama, lore, revenger. For those I scanned `main`.

## Table — every hit of the prescribed regex (17 lines in 7 lanes)

Ground owner: "own" means the lane's own province. In every row the topic is not kotoba's.

| lane @ commit | path:line | what the line is about | ground | bears on C2? |
|---|---|---|---|---|
| kagi @ 899c50b4 | `corpus/claim-ledger.tsv:33` | credential checklist "policy deny-list" | kagi own (credential hygiene) | no |
| kagi @ 899c50b4 | `corpus/knowledge/config-layering.md:18` (section `:35-38`) | opencode 1.18.31 agent `permission` ruleset, "evaluated last-match-wins" (`:36-37`), janitor handler | kagi own (janitor isolation) | yes: opencode row. Cite only |
| kake @ f1ffb817 | `corpus/lessons/round-6-aggregator-audit.md:129` | systemd timer `disabled` | kake own | no |
| kake @ f1ffb817 | `corpus/lessons/round-8-aggregator-box3-coldrun.md:76` | timer "loaded + disabled" | kake own | no |
| kumitate @ 8eea5608 | `corpus/README.md:74` | index row: swarm/tower mutual exclusion, permission-mode enum | kumitate own (orchestration runtime) | no. It is skill doctrine, not a client lever |
| tabi @ e3cf4e0d | `corpus/knowledge/interaction-approval-table.md:59`, `:93` | default-deny for third-party reads | tabi own | no |
| tabi @ e3cf4e0d | `corpus/evidence/w4-erb-b-append-proof/pre/interaction-approval-table.md:59`, `:93` | copy of the row above | tabi own | no |
| tabi @ e3cf4e0d | `corpus/evidence/w4-t4-3-sweep/pins.log:51` | Chrome `Preferences` JSON (`disable_reasons`, permissions) | tabi own | no |
| tabi @ e3cf4e0d | `corpus/knowledge/external-class-fixture-v2.md:1` and 2 copies under `corpus/evidence/w6-aud-b6-scratch/note-rev/` | "U7 default-deny holds" | tabi own | no |
| tsukuroi @ 4de2b6b1 | `SKILL.md:2161` | seat policy: "Only the exact `skill://godspeed` URI is an approved skill read" | tsukuroi own (seat boundary) | no. Lane policy, not a client lever |
| tsukuroi @ 4de2b6b1 | `corpus/knowledge/journal-boot-plane.md:299` | `ls /boot` Permission denied | tsukuroi own | no |
| game-dev-3d @ 89dd182b (main) | `corpus/knowledge/unreal-mcp/executability/gameplay-gas.md:123` | no plugin "enable/disable contract" | game-dev-3d own | no |
| kaidoku @ cd32264f (main) | `corpus/knowledge/2026-10-13-r2-skill-references-deep.md:107` | Codex sandbox "preserved rather than silently disabled" | kaidoku own (REA client launch) | no |

These lanes returned no lines (git grep exit 1): chousa, kama, kasegi, kengaku, mado, mori, souji
and tameshi on `master`; audio, game-dev-2d, kotodama, lore and revenger on `main`.

## Supplementary scan (wider lever terms the prescribed regex misses)

I also searched for `user-invocable`, `enabledSkills`, `permission.skill`, `"skill":`,
`first-found-wins`, and skill near shadow, precedence or collision. It found one relevant hit:

| lane @ commit | path:line | content | ground | bears on C2? |
|---|---|---|---|---|
| kumitate @ 8eea5608 (same lines at kotoba's pin `fac39171`) | `corpus/knowledge/kimi-skills-plugins.md:319`, `:334`, `:345`; `SKILL.md:554-558` | kimi listing rule "Project overrides User overrides Extra overrides Built-in" when scopes "define a skill with the same name". The roots are "merged by name". The tie-break is "rule-derived, not observed" | kumitate own (Kimi Code substrate rows K1-K5, kumitate `PROVINCE.md:14`) | yes: an analogue. Kimi is not one of the 7 clients |

Everything else was noise: Godot binary fixtures in game-dev-2d, and Hyprland config precedence
in mado. The other hits used "precedence" or "hidden" in unrelated senses (game-dev-3d, kake,
kama, kotodama, mori, tabi, tsukuroi).

## Proposed move (one, bounded)

**Evidence.** Kumitate's entry shows that scope precedence settles which of two skills *with the
same name* survives. It never chooses between two skills with different names whose descriptions
overlap. The build spec still names that kind of precedence as a lever to look for. The
`SrcCopilotCli` prompt says "first-found-wins precedence at :415" (`build-spec.json`).
`S022`, `S025`, `S026` and `S029` also name same-name or precedence sections ("Resolve skills
that share a name", "duplicate names", "Precedence and aliases").

The `LeverGuard` mutants are listed in its prompt: row removed, row unmined, `used-by` missing,
key term absent from the quote, key term containing "description", duplicate client, entry
citing a different S###, table absent, unknown client. None of them rejects a precedence-only row.

**Move.** Add one admission rule to the C2 table and one mutant to `check_overlap_levers.py`:

- Rule: a row whose key term is only a same-name precedence rule does not count for that client.
  Examples are "first-found-wins", "overrides" and "precedence". Such a rule stops a skill only
  when the user renames a skill to collide on purpose.
- A row counts only if its lever removes a named skill from model choice or from loading. Examples
  are a disable or deny key, `disable-model-invocation`, `user-invocable`, a permission rule, or
  a `/skills` toggle.
- Mutant: a client's key term is swapped for its page's precedence phrase. The counter must lower K.
- The entry may cite kumitate `kimi-skills-plugins.md:319,345` at `8eea5608` as a measured example
  of name-keyed resolution. That is kumitate ground, so the entry cites it and does not restate it.

**Second-order effect, the opencode row.** If the opencode lever is a `permission` skill deny,
its effect depends on rule order. Kagi measured "evaluated last-match-wins" for opencode 1.18.31
agent `permission` rules (`config-layering.md:36-37`). A deny followed by a wildcard allow would
not hold. The row should cite kagi for that ordering and not re-derive it.

Kotoba `PROVINCE.md:41` says "the opencode config group owner is unresolved and stays with the
integrator". Writing the row therefore touches an unruled boundary, and the L1 should say so in
the lesson and not rule on it.

**Affected axes.** Depth improves, because the 7 of 7 cannot be met by same-name precedence alone.
Adjacency improves, because two sibling facts are cited at pinned commits and none is absorbed.
Freshness and operability are unchanged.

**Risks.**
- The count may fall below 7 for a client whose page documents only precedence. That is the real
  value, not a harm. Under the rule's own wording this is [INFERENCE] for Copilot CLI, if its
  disable lines (spec: "lines near 20-33") turn out not to be about skills.
- Kagi's ordering is from opencode 1.18.31 on 2026-09-28. Kotoba pins opencode 1.19.3 (S015) and
  the docs describe the current release (S024). The cite must carry kagi's version bound.

**Verification.** The main agent should run `check_overlap_levers.py --self-test` with the new
mutant. On the base it must print `overlap levers backed 0 of 7 clients`. A precedence-swapped
fixture must print fewer than 7.

## Does kaidoku's round-26 evidence-ID identity entry bear on SOURCES keying?

Yes, as an analogy, and it is bounded. The entry is kaidoku `ae8bcd86`
`corpus/knowledge/2026-10-22-r26-native-reader-evidence-id-identity.md`. It finds that an evidence
id is stable when it is minted from content (the subject's sha256) and changes when the path enters
the hashed projection. It also finds that two verbs which call one operation share one id, so
"An id alone therefore does not tell which of the two verbs produced it".

Kotoba keys `SOURCES.md` rows by a sequential S### label, and fetch identity lives inside the
anchor text. At `43ca0bfb` four sources have twin rows: S001/S018 and S003/S019 are both `mined`
on the same URL, and S010/S020 and S013/S021 differ in status. S018, S019, S020 and S021 each say
"supersedes" the older row.

The C2 counter accepts any `mined` row whose `used-by` names the entry. A superseded twin that is
still `mined` (S001, S003) could therefore back a client. That is the "unlabelled twin" laundering
D7 carries.

Kaidoku's lesson maps onto this: bind each quote to the content it was read from (URL plus fetched
sha256) and not only to the label, and treat a superseded row as non-canonical. Concretely, the
counter can reject a cited row that a later row supersedes, and flag two `mined` rows on one URL
and sha256. This is [INFERENCE]: kaidoku's finding is about REA 6.5.0 id minting, not about
SOURCES rows, so kotoba would cite it as a design analogy only.

## Pin drift seen in passing (kotoba `PROVINCE.md:36-56` against current heads)

The pins have moved for 9 lanes: kaidoku, kake, kama, kotodama, kumitate, mado, mori, tameshi and
tsukuroi. Kumitate moved from `fac39171` to `8eea5608`, and the kumitate lines cited above are
identical at both commits. This is not a C2 action. It is input for `check_sibling_census.py`.

## Evidence (commands, exit codes)

- Prescribed regex per lane, run as `git -C <lane> grep -niE '<regex>' $(git rev-parse master|main) -- corpus SKILL.md PROVINCE.md`.
  Exit 0 with hits: kagi 2, kake 2, kumitate 1, tabi 8, tsukuroi 2, game-dev-3d 1, kaidoku 1 (17 lines).
  Exit 1 for the other 13 lanes.
- `git rev-parse master` failed for the 7 main-only lanes (they are marked NO-MASTER in the loop).
  `git branch -a` shows `main` for each.
- Supplementary wider regex, same pathspec: exit 0. Matching lines: game-dev-2d 7 (all binary),
  game-dev-3d 3, kagi 1, kaidoku 3, kake 1, kama 1, kotodama 3, kumitate 7, mado 3, mori 1, tabi 2, tsukuroi 4.
- `git -C kumitate-shokunin show <rev>:corpus/knowledge/kimi-skills-plugins.md | grep -n ...`:
  lines 319, 334 and 345 at both `fac39171` and `8eea5608`, exit 0.
- `git -C kagi-shokunin show 899c50b4:corpus/knowledge/config-layering.md | grep -n last-match-wins`: lines 36-37, exit 0.
- `git -C kaidoku-shokunin log -1 ae8bcd86`: commit "round-26: final receipts at 16307c47"; the entry has 135 lines.
- Kotoba `SOURCES.md` at `43ca0bfb` has 29 S### rows, with twin URLs at S001/S018, S003/S019,
  S010/S020 and S013/S021 (Python parse of the registry, exit 0).
