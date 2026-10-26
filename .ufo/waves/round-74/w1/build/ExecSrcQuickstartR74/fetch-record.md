# Fetch record — agentskills.io/skill-creation/quickstart (opened 2026-10-25, round 74 wave 1)

Seat `ExecSrcQuickstartR74`. All commands run 2026-10-25 (`date -I` → `2026-10-25`).

## Site fetches

| item | command | observed |
|---|---|---|
| `.md` form | `curl -sL --max-time 60 -A 'Mozilla/5.0' -o page_quickstart_md.raw -w 'http=%{http_code} final=%{url_effective} bytes=%{size_download}\n' https://agentskills.io/skill-creation/quickstart.md` | `http=200 final=https://agentskills.io/skill-creation/quickstart.md bytes=4080` (no redirect) |
| no-`.md` form | same curl against `https://agentskills.io/skill-creation/quickstart` | `http=200 final=https://agentskills.io/skill-creation/quickstart bytes=271472`; the HTML carries the same two sentences (`grep -c 'agents/skills/'` → 4; literal `VS Code looks for skills in <code>.agents/skills/</code> by default` present; `Roll dice using a random number generator` present) |
| sha256 of the `.md` bytes | `sha256sum page_quickstart_md.raw` | `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb` |
| size/lines | `wc -lc page_quickstart_md.raw` | `83 4080` |

Snapshot saved verbatim (no reshaping): `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/snapshot.md`
= the `.md` bytes; pin in `snapshot.sha256` = `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb  snapshot.md`.

## Upstream source file

| item | command | observed |
|---|---|---|
| repo head | `git ls-remote https://github.com/agentskills/agentskills refs/heads/main` | `69ef37e9424c0a7ea9dd2293b559e43ec8176379	refs/heads/main` |
| commits touching the docs path | `curl -sL 'https://api.github.com/repos/agentskills/agentskills/commits?path=docs/skill-creation/quickstart.mdx&per_page=3'` | newest `8aeff476971ff1d4eb87a49568678c3f71c38f68` 2026-04-19 ("Remove link to `what-are-skills.mdx`…"); then `d7dba49` 2026-03-23; `3fccd70` 2026-03-16 |
| ancestry | `curl -sL 'https://api.github.com/repos/agentskills/agentskills/compare/8aeff47...69ef37e'` | `status ahead, ahead_by 36, behind_by 0` — the path's last commit is an ancestor of the head |
| mdx at the head | `curl -sL https://raw.githubusercontent.com/agentskills/agentskills/69ef37e/docs/skill-creation/quickstart.mdx` | `http=200`, 3 844 B, sha256 `a6614e814e19fb505b2e45a39a61643d62ac4ebee0515ceb913d09512d8489db` |
| mdx at the path's last commit | same raw URL at `8aeff47` | `http=200`, 3 844 B, sha256 `a6614e81…d8489db` — **identical**, so the file has not changed since 2026-04-19 |

`69ef37e` is therefore still the head of the repository *and* the bytes of
`docs/skill-creation/quickstart.mdx` at `69ef37e` are the bytes of the path's last change.

## Site text vs upstream mdx (modulo markup)

Mapping applied to the mdx (each step is site markup, no prose change):

1. frontmatter `title:`/`description:` → `# Quickstart` plus a `> Create your first Agent Skill and see it work in VS Code.` blockquote;
2. the site's three-line `> ## Documentation Index …` blockquote prepended (site chrome, not page text);
3. `<Note>…</Note>` → `> [!NOTE]` / `>` / `> …` callout form;
4. list markers `- ` → `* `;
5. fence info string gains ` theme={null}`;
6. site-relative links `/skill-creation/x` → `https://agentskills.io/skill-creation/x.md`.

Command: a Python normaliser (`mdx_as_site.md`) then string equality against the fetched `.md`.
Observed: `NORMALIZED_EQUAL: site page text == upstream mdx after the documented markup mapping`;
`sha256sum mdx_as_site.md page_quickstart_md.raw` → both
`7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb`.

Raw `diff /tmp/k74qs_69ef37e.mdx page_quickstart_md.raw` shows 41 changed lines, all of them the six
markup classes above (frontmatter, index blockquote, two callouts, bullet markers, fence attribute, link
targets) — no sentence differs.

## Lane probes (base `1e03d19`)

| probe | command | observed |
|---|---|---|
| lane holds the page? | `grep -rn 'skill-creation/quickstart' corpus/ SKILL.md PROVINCE.md README.md \| wc -l` | `0` |
| page carries script-bundling rules? | `grep -nE 'scripts/\|500 lines\|1024' snapshot.md` | `0` hits (only `progressive disclosure` on line 74 matches nothing else) |
| lane holds the `.agents/skills/` root elsewhere | `grep -rn '\.agents/skills' SKILL.md PROVINCE.md corpus/` | many hits (e.g. `SKILL.md:50`), none citing this page — the root is held as observed client behaviour, not as the tutorial's default |

## Staged material re-grounded

`grep -nE '^\| S2(31|32|36|37) ' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` → four rows;
the quickstart row is `S237`, status `mined`, opened `2026-10-23`, used-by
`corpus/knowledge/spec-script-craft-rules.md`. Staged size claim "`.md` 4 080 B" matches today's fetch
exactly; the staged quotes are located (see the report's grounding table).
