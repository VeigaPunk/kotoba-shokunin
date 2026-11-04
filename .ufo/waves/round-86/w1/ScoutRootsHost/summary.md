# ScoutRootsHost — where the 132 base-missing names live on this host (round 86, w1)

Inputs: fixture `verifiers/fixtures/omp-catalogue-r86/catalogue.json` (entries, `template_hex`,
`cache_rows`), 132 `MISS … not-discovered` lines in `.ufo/waves/round-86/receipts/c1-K0-base.txt`.
Scoring used the lane's own `parse_frontmatter`, `preview` and `omp_key` from
`verifiers/verify_harness_claims.py` (imported read-only). "Render match" means `preview(desc)`
equals the fixture render, or `omp_key(template, name, desc)` is a fixture cache row whose
description equals the render (cache hit). Render time: 2026-11-04T21:55:22.890Z.
Full table: `host-map.tsv` (1933 candidate rows; columns name, candidate_path, render_match,
cache_hit, mtime, ctime, match_via, before_render, realpath, note).

## Result

- All 132 names classified, all 132 have at least one reproducing candidate; 0 names unreproducible.
- 1128 reproducing candidate paths (996 distinct real files); every one has mtime and ctime
  before the render (0 `POST`).
- **The root omp reads is `~/.omp/plugins/node_modules/ecc-pi-core/skills`**: exactly 132 entries,
  all 132 reproduce (112 by preview and cache, 20 by cache hit only). `ecc-pi-core` is a symlink
  (created 2026-10-25T05:03:07Z) to `/home/vgpnk/.ecc/pi/core`. Its `package.json` declares
  `"pi": {"skills": ["./skills"]}`, and `~/.omp/plugins/omp-plugins.lock.json` lists it as
  enabled at version 2.2.3. The SKILL.md files have mtime and ctime between 2026-10-25T02:30:16.249Z and .254Z.
  It is the only root whose names are exactly the 132 missing names. No other root matches that set.

## Roots with reproducing candidates, ranked (root = SKILL.md grandparent)

| count | root | note |
|---:|---|---|
| 132 | `/home/vgpnk/.omp/plugins/node_modules/ecc-pi-core/skills` | omp plugin root (symlink → `~/.ecc/pi/core/skills`) |
| 132 | `/home/vgpnk/.ecc/pi/core/skills` | realpath of the row above |
| 132 | `/home/vgpnk/.zcode/cli/plugins/cache/ecc/ecc/2.2.3/pi/core/skills` | zcode copy of ECC 2.2.3, not an omp root |
| 132 | `/home/vgpnk/.zcode/cli/plugins/marketplaces/ecc/pi/core/skills` | zcode copy |
| 131 | `/home/vgpnk/.ecc/skills` | full ECC tree (311 dirs); lacks `ecc-council` |
| 131 | `/home/vgpnk/.zcode/cli/plugins/cache/ecc/ecc/2.2.3/skills` | zcode copy |
| 131 | `/home/vgpnk/.zcode/cli/plugins/marketplaces/ecc/skills` | zcode copy |
| 25 | `~/.ecc/.kiro/skills` (+2 zcode copies, 25 each) | ECC per-harness port |
| 16 | `~/.ecc/.agents/skills` (+2 zcode copies) | ECC repo-local, not `~/.agents/skills` |
| 10 | `~/.ecc/docs/ja-JP/skills` (+2 zcode copies) | translated docs whose render happens to match |
| 9 | `~/.ecc/docs/tr/skills` (+2 zcode copies) | " |
| 6 | `~/.ecc/docs/zh-TW/skills` (+2 zcode copies) | " |
| 2 | `~/.ecc/.cursor/skills` (+2 zcode copies) | " |
| 1 | `~/.ecc/docs/zh-CN/skills` (+2 zcode copies) | " |

A first-match brute-force walk would also reach the decoys (`~/.ecc/skills`, `~/.zcode/…`). Only
the `~/.omp/plugins/node_modules/*/skills` root has code support in the ELF (below).

## ELF source (omp 18.15.0, `/home/vgpnk/.local/bin/omp`, read via mmap)

- `// packages/coding-agent/src/discovery/omp-plugins.ts` @ 173914407: provider `omp-plugins`, and
  `uie` loads skills from `dir: Zo.join(R.path, "skills")` (verbatim at offset 173914936, unique),
  with `requireDescription: true` for every root `R` returned by `X9`.
- `// packages/coding-agent/src/discovery/omp-extension-roots.ts`: `X9` merges explicit and
  configured extension roots with `XQ(u)`. `XQ` calls `AP(u.cwd, {home})` → `UQ` → `eD($o(home), lock, "user")`.
  `$o` is `getPluginsDir` and `Pu` is `getPluginsNodeModules`. The verbatim text
  `function Pu(p) {\n  return h.join($o(p), "node_modules");` occurs once at offset 166892466, and
  `Pu as getPluginsNodeModules` occurs once at 189719663. The lock file name `omp-plugins.lock.json` occurs at 166892625.
- The quote `Sub-discovery (skills, hooks, tools, commands, rules, prompts, .mcp.json) inside extension packages`
  occurs twice, at 114492956 and in omp-plugins.ts. The locator requires >= 12 chars verbatim, not uniqueness.
- [INFERENCE] `eD` enumerates `~/.omp/plugins/node_modules/<pkg>` for packages in the lock file. I did not read `eD`
  line by line. The observed plugin set matches it: `ecc-pi-core` and `unreal-engine-skills-omp` are both in the lock file and in `node_modules`.

## Names with no reproducing candidate

None. All 132 reproduce from the omp plugin root.

These 20 names reproduce **only through a cache hit**. Their `preview(desc)` differs from the
render, so the render is the cached LLM compression keyed by `omp_key`: coding-standards,
dart-flutter-patterns, dashboard-builder, django-celery, django-tdd, docker-patterns,
dotnet-patterns, ecc-council, golang-testing, kotlin-coroutines-flows, kotlin-exposed-patterns,
liquid-glass-design, motion-patterns, nestjs-patterns, perl-patterns, prisma-patterns,
python-testing, pytorch-patterns, react-performance, security-review. A model that runs where
the fixture's `cache_rows` are not available would reach these 20 lines only if the cache rows reach it.

805 candidate rows do not match. They come from translated docs (`docs/ja-JP`, `zh-CN`, `es`,
`tr`, `ko-KR`), harness ports (`.kiro`, `.agents`) and one OpenBot synced plugin. Their descriptions differ from the
render (styles: plain 718, quoted 54, `>` 30, `>-` 3; first 60 chars of the preview are in the
`note` column).

## Search coverage

- Pass 1: `find /home/vgpnk -xdev` with `/home/vgpnk/Projects/shokunin` pruned, `-maxdepth 12`, without following symlinks
  and without skipping node_modules: 5839 SKILL.md files. One permission error (`~/Projects/eimo/packages/infra/.secrets`).
- Pass 2: the same search with `find -L`, `-maxdepth 9`. It prunes the fleet root, `~/.local/state/fnm_multishells`,
  every `node_modules`, `~/.cache` and `~/.local/share/fnm`, because those are symlink fan-out and loops.
  It found 4240 files. An unpruned `-L` pass was stopped after it fanned out through `fnm_multishells`.
  It had produced 55,678 paths there and none elsewhere.
- Pass 3: `find -L ~/.omp/plugins/node_modules -maxdepth 4`, 132 files. This puts back the node_modules
  symlink root that pass 2 pruned.
