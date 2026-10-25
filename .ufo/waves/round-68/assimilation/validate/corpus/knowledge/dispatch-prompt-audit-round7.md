# Dispatch-prompt surface audit — round 7

Sourced 2026-09-28 (round 7), L2 executor lanes `ExecDispatchChecklist`
(drafted the checklist below, applied it to all 43 `.ufo/prompts/*.md`) and
`ExecResolvability` (reference/command sweep over the same 43 + 3
`~/.config/opencode/command/*.md` + the generator `scripts/shokunin-watchdog.sh`).
Lane artifacts: `/tmp/kotoba-r7/executor-dispatch-checklist.md`,
`/tmp/kotoba-r7/executor-resolvability.md`. All defects are **cross-domain**
(main-repo/driver owned) — reported, not fixed.

## Dispatch-prompt fidelity checklist (drafted + applied)

Checkable by reading the file; DP- prefix. 12 items:

1. **Shape matches mode** — spawn `*-L1.md` 9–12 non-blank lines w/ all 6
   stanzas; round `*-round-N.md` 3–4 lines.
2. **Spawn stanza order** — role+dir → context → job → L2 map → report+fence →
   `| godspeed`; report stanza after routing.
3. **`| godspeed` literal final line.**
4. **Report path literal** — `.ufo/reports/round-<N>/<id>.md` with no `<…>`
   placeholder or unsubstituted variable.
5. **Report filename = lane id, matches landed files** — prior-round refs must
   resolve.
6. **Round files carry delta only** — no restated L2 map, domain essay, or
   verification commands.
7. **Spawn carries the L2 routing map** when the lane dispatches L2s; aliases
   must equal the current MISSION.md bucket.
8. **Self-containment** — no deictic refs ("as before", "the other lane")
   without a named antecedent; paths absolute or cwd-resolvable.
9. **Embedded paths/commands resolve** on disk / PATH.
10. **No escape leakage or duplicated body** — no literal `\n`, no verbatim
    repeated stanza blocks.
11. **Round token coherent** — `<N>` equal across filename, role line, report
    dir; ≤ `.ufo/state/<id>.round`.
12. **Scope fence explicit** — names a MUST-NOT-write target + the writable dir.

## Application result: 37/43 files fail ≥1 item

| Item | Files failing | Worst instance |
|---|---|---|
| 6 delta-only (round restates L2 map) | 30/35 round files | every `*-round-*.md` except `protocol-round-4..8` |
| 4 `<lane>` placeholder | 6 `*-L1.md` | `.ufo/reports/round-1/<lane>.md` never substituted; cost `kake` and `kengaku` their round-1 canonical names (`web-properties-publishing.md`, `kengaku-shokunin.md` — `ls .ufo/reports/round-1/`) |
| 7 stale routing aliases | 6 spawn files | `reviewer m_composer / connector m_antigravity / sentinel m_grok` vs current `m_zfl`/`m_lunamax` buckets |
| 5 filename mismatch | 5 | `AGGREGATE.md` refs vs landed `aggregator.md` |
| 10 literal `\n` + duplicated body | 6 `*-L1.md` | lines 6–10 byte-repeat 1–5 with `\| godspeed` glued (`md5sum` recipe in lane file §1) |
| 9 dead path | 1 | `kengaku-L1.md:5` → `/home/vgpnk/wikillm/llm-wiki` ENOENT |

Items 3, 8, 11, 12: **0 fails** — the terminator, self-containment, round
token, and scope fence hold everywhere. Clean files: `kagi-L1.md`,
`protocol-round-4..8.md`.

## Cross-surface defects (resolvability sweep, 46 files + generator)

- **Generator-vs-artifact split**: on-disk prompts are all pre-v3
  (mtimes 15:57–16:55 < `shokunin-watchdog.sh` mtime 16:57). The v3 generator
  already emits the correct MISSION.md bucket + 8-L2 minimum + `git push`
  rule; the 38-file stale-routing defect is a regeneration/commit problem,
  not a live template bug. `git show ccc7217` proves only `m_kcode→m_flash`
  was ever fixed.
- **Driver contract bugs** (`scripts/shokunin-watchdog.sh`, integrator-owned):
  `:39` `report_of()` accepts `<lane>-shokunin.md`, contradicting
  PROTOCOL.md:101-102 — and still misses `web-properties-publishing.md`
  (kake round-1 report invisible to the driver); `:59` protocol heredoc
  numbering starts at `2.` (step 1 dropped); `:49` emits
  `round-<N-1>/AGGREGATE.md` read paths that never existed (ledger landed
  once, at `round-2/AGGREGATE.md`, while prompts write `aggregator.md` —
  three-way definition divergence).
- **Command-file defects**: `command/sekhmet.md:9` sources
  `~/.xbgst/env.l3-sekhmet.sh` — ENOENT (dead live-run gate; same literal at
  `sekhmet-l3/SKILL.md:48,57`); `command/ufo.md:11` bans `general`/`explore`
  agents absent on this host (`ls ~/.omp/agent/agents | grep -c
  'general\|explore'` → 0); `ufo.md:9` says "Task tool" — host tool is `task`.
- **Ambiguity findings worth keeping** (affect checklist wording):
  A2 — scope fence is *allowed* durable-policy restatement in round mode
  (exempt it from item 6); A3 — the L2 map has no durable home, so "delta
  only" vs "respawned lane needs the map" is a real tension (resolved by the
  round-7 MISSION.md steer: lanes re-read MISSION.md, so the map has a home);
  A8 — `.ufo/state/<id>.round` holds the lane's *latest* round, not the
  file's round: equality is wrong, `≤` bound is right.
- **Drift vs round-4 corpus claims**: round-prompt population 6→35;
  "round prompts omit the routing map" now false for 30/35 (the map is
  restated, with 3 stale aliases).
