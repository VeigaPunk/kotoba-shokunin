# ScoutRootsHost report (round 86, w1)

Scope: map the 132 `not-discovered` names in `c1-K0-base.txt` to SKILL.md files on this host. Read-only outside `w1/ScoutRootsHost/`.

Files: `w1/ScoutRootsHost/host-map.tsv` (1933 rows, sha256 `34382908e2b27a17c79bfcb3ca6f0de061106ed05ef90cc0c361fe8413a66807`)
and `w1/ScoutRootsHost/summary.md`.

## Findings

1. All 132 names are classified and all 132 reproduce. There are 0 unreproducible names. 1128 reproducing paths (996 real files) were found, and every one has mtime and ctime before 2026-11-04T21:55:22.890Z.
2. The root omp reads is `~/.omp/plugins/node_modules/ecc-pi-core/skills`, with 132 of 132 names. `ecc-pi-core` is a symlink to `~/.ecc/pi/core`.
   The package is enabled in `~/.omp/plugins/omp-plugins.lock.json` at 2.2.3, and its `package.json` has `pi.skills: ["./skills"]`. Its name set is exactly the 132 missing names.
3. ELF support: `discovery/omp-plugins.ts` has `dir: Zo.join(R.path, "skills")` (unique, offset 173914936). The roots come from `X9` → `XQ` → `AP`/`UQ` → `eD($o(home), …)`.
   `function Pu(p) {\n  return h.join($o(p), "node_modules");` is unique at 166892466, and `Pu as getPluginsNodeModules` is unique at 189719663.
   The ledger needs a pattern such as `~/.omp/plugins/node_modules/*/skills`. The ledger owner (ExecModel) chooses the quote.
4. Decoy roots reproduce almost as many names: `~/.ecc/skills` 131, `~/.zcode/cli/plugins/{cache/ecc/ecc/2.2.3,marketplaces/ecc}/{skills,pi/core/skills}` 131 or 132 each,
   and `.kiro`, `.agents` and translated `docs/*` roots 1 to 25 each. None of them is an omp root, so a brute-force first-match walk would land on unsourced roots.
5. 20 names reproduce only through a fixture cache hit, because `preview` differs from the render. The list is in `summary.md`.
   A model reaches those 20 lines only if the scored run can consult the cache rows.

## Evidence

- `find /home/vgpnk -xdev` with the fleet root pruned and `-maxdepth 12` found 5839 SKILL.md files.
- A bounded `find -L` pass found 4240, after pruning `fnm_multishells`, `node_modules`, `.cache` and `fnm`.
- `find -L ~/.omp/plugins/node_modules -maxdepth 4` found 132.
- The mapping run printed `1933 rows; 132 names reproduced`. For the omp-plugin rows the tally was `('yes','yes','preview+cache','pre'): 112, ('yes','yes','cache','pre'): 20`.
- `awk` over the TSV: 132 distinct names, 132 names with `render_match=yes`, 0 reproducing rows after the render.

## Risks

- I did not read `eD` line by line [INFERENCE], so `node_modules/<pkg>` enumeration comes from the call chain and the observed plugin set.
- The unpruned symlink pass was stopped. Roots reachable only through the pruned symlink farms were not searched.
- I installed no tools.
