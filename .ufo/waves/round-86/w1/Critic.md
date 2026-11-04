# Critic — round 86 W1 report (C1 shortcut worlds, Q71 disclosure)

Full tables, answers and corrections are in `.ufo/waves/round-86/w1/Critic/worlds.md`. Receipts are in
`.ufo/waves/round-86/w1/Critic/receipts/` (15 runs on the frozen counter, 15 `a1-*` runs on addendum-1). Generators,
ledgers and digests are in `.ufo/waves/round-86/w1/Critic/worlds/`.

## Results (N of 215 / exit)

| world | frozen counter (`ecfad51f`) | amended counter (`b9ee5484`) |
|---|---|---|
| W-brute, 107 roots, find order: no ledger / fragment ledger | 141 / 1 ; 141 / 1 | 141 / 1 ; 141 / 1 (G4 FAIL) |
| W-alpha: no ledger / fragment ledger | 143 / 1 ; 143 / 1 | 143 / 1 ; 143 / 1 (G4 FAIL) |
| W-cover + `*` ledger | **215 / 0** | 215 / 1 (G4 FAIL) |
| W-base+1 (`~/.ecc/pi/core/skills`) + fragment ledger | **215 / 0** | 215 / 1 (G4 FAIL) |
| cheapest: base + 1 `.zcode` line + `*` | **215 / 0** (became addendum-1 K3) | 215 / 1 |
| W-dotbrute (39 aliased roots, junk ELF quotes containing the dot segment): find / alpha / cover | n/a | **212 / 0 ; 214 / 0 ; 215 / 0** |
| cheapest-a1: base + 1 line `~/.omp/plugins/node_modules/ecc-pi-core/skills` + 3 junk-quote rows | 215 / 1 (no ledger) | **215 / 0** |
| W-candidate (`903bd78` content) | n/a | **215 / 0** |

## Answers

- **(a) Yes, on both counters.** The amended counter is still passed by worlds that never read
  omp's loaders. The find-order dot-brute world reaches 212 and draws about 41 lines from roots
  omp does not read (`omp-gamedev`, `OpenBot`, `devin`; 0 ELF hits).
- **(b) The cheapest world is one appended root line** plus a 2-row ledger (frozen) or a 3-row
  ledger (amended).
- **(c) No.** The candidate's 215 lines come from `~/.omp/plugins/node_modules/ecc-pi-core/skills`
  (132) and `~/.agents/skills` (83), and both are source-packet rows. Its other roots contribute 0
  lines and the counter does not exercise them.

## Open findings

- **F5:** the dot rule checks spelling, not reading.
- **F6:** N and the root-to-name attribution of the candidate are identical to the brute world's.
- **F7:** the dot rule rejects the actual loader quotes.
- **F4:** walk-up roots cannot be scored.
- **Candidate note:** the sandbox scores the candidate's no-registry fallback.

The correction is in worlds.md: pin the loader-quote offsets from the source packet, and bind back
the plugin registry files.
