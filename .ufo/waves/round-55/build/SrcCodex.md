Result: DONE — Codex’s named-skill prompt form is grounded in a distinct official OpenAI Developers page; evidence and integration drafts follow.

## Finding

The selected official page documents a user prompt that names one skill with a `$` prefix. The exact fetched-byte quote is 11 words and includes the form token:

> “Use the $setup-demo-app skill to create the project in this directory.” — `eval-skills.md:148`, within the `codex exec` prompt string.

At `eval-skills.md:171-172`, the page describes this as an explicit-invocation prompt that names the skill directly and checks whether Codex can invoke it when asked. The same page distinguishes explicit from implicit invocation at `:171-183`.

## Drafts for integration

SOURCES row (11 cells; `S0NN` placeholder as requested):

```text
| S0NN | OpenAI Developers — Testing Agent Skills Systematically with Evals — https://developers.openai.com/blog/eval-skills.md | docs | A | Codex explicit named-skill invocation in a user prompt | § 3, “Manually trigger the skill to expose hidden assumptions,” prompt example (`eval-skills.md:144-149`); fetched 2026-10-22T23:13:16Z; SHA-256 `6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2` | A prompt example uses `$setup-demo-app` to create the project. | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md |
```

Entry row:

```text
| Codex | S0NN | "Use the $setup-demo-app skill to create the project in this directory." | `eval-skills.md:148` (inside the `codex exec` prompt string) | Names the skill in the prompt, which the page says lets Codex invoke it when asked. |
```

SKILL.md decision-table row:

```text
| Codex | `$setup-demo-app` | Names and invokes the skill directly in a Codex prompt. | Set this turn aside when measuring implicit activation. |
```

The form cell token exactly matches the token in the entry quote. The action applies the Frontier rule: an explicit name-invocation turn is not evidence of implicit, description-routed activation.

## Implicit-invocation control

The selected Evals page does **not** document a setting that blocks implicit invocation while retaining explicit invocation. Its explicit/implicit discussion is about test prompts (`eval-skills.md:171-183`); a search of the downloaded page for `allow_implicit_invocation|implicit_invocation|enabled = false|disable|implicit invocation|implicitly` returned only the implicit-test lines `:174-175`, with no disabling setting.

A separate, already-cited official page does document that control. The markdown page fetched through `https://developers.openai.com/codex/skills.md` redirected to `https://learn.chatgpt.com/docs/build-skills.md`; it shows `policy:` / `allow_implicit_invocation: false` at lines 206-208 and says at line 218: “When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works.” This is the existing Build skills page (S013, S021, S054 in the current SOURCES file), so I used the distinct Evals page for the new row instead.

## Provenance and checks

Primary source fetch (ordinary `curl`; `.md` route):

```text
Command: timeout 120s bash -lc 'date -u; curl -L --max-time 90 --silent --show-error --output /fast/scratch/hyaku/kotoba-r55/SrcCodex/eval-skills.md --write-out "HTTP %{http_code}\nbytes %{size_download}\neffective %{url_effective}\n" https://developers.openai.com/blog/eval-skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCodex/eval-skills.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCodex/eval-skills.md'
Exit: 0
Thu Oct 22 11:13:16 PM UTC 2026
HTTP 200
bytes 19356
effective https://developers.openai.com/blog/eval-skills.md
6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2  /fast/scratch/hyaku/kotoba-r55/SrcCodex/eval-skills.md
19356 /fast/scratch/hyaku/kotoba-r55/SrcCodex/eval-skills.md
```

Source-selection checks:

- Exact-URL search in the lane `corpus/SOURCES.md` for `https://developers.openai.com/blog/eval-skills` returned no matches. The new draft therefore cites a page not already listed there.
- Fetch of `https://developers.openai.com/codex/skills.md` used `timeout 120s bash -lc 'date -u; curl -L --max-time 90 --silent --show-error --output /fast/scratch/hyaku/kotoba-r55/SrcCodex/developers-skills.md --write-out "HTTP %{http_code}\nbytes %{size_download}\neffective %{url_effective}\n" https://developers.openai.com/codex/skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCodex/developers-skills.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCodex/developers-skills.md'` (exit 0). Output: `date -u` = `Thu Oct 22 11:12:58 PM UTC 2026`; HTTP 200; 11,035 bytes; effective URL `https://learn.chatgpt.com/docs/build-skills.md`; SHA-256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`. This existing page states the `$` mention and `$skill-creator` form (`build-skills.md:95-117`) and explicit-only setting above.
- Fetch of Codex repository docs at `https://raw.githubusercontent.com/openai/codex/main/docs/skills.md` used `timeout 120s bash -lc 'date -u; curl -L --max-time 90 --silent --show-error --output /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.md --write-out "HTTP %{http_code}\nbytes %{size_download}\neffective %{url_effective}\n" https://raw.githubusercontent.com/openai/codex/main/docs/skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.md; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.md'` (exit 0). Output: `date -u` = `Thu Oct 22 11:12:58 PM UTC 2026`; HTTP 200; 115 bytes; effective URL is the requested raw URL; SHA-256 `e59789d09692310bbf94e2ef8db0aaf00d97f2226982c8c5330d2d260583a97d`. Its only content is a pointer to developer docs (`codex-skills.md:1-3`), not an invocation form.
- Fetch of `https://github.com/openai/codex/commits/main/docs/skills.md.atom` used `timeout 120s bash -lc 'date -u; curl -L --max-time 90 --silent --show-error --output /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.atom --write-out "HTTP %{http_code}\nbytes %{size_download}\neffective %{url_effective}\n" https://github.com/openai/codex/commits/main/docs/skills.md.atom; sha256sum /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.atom; wc -c /fast/scratch/hyaku/kotoba-r55/SrcCodex/codex-skills.atom'` (exit 0). Output: `date -u` = `Thu Oct 22 11:12:58 PM UTC 2026`; HTTP 200; 3,353 bytes; SHA-256 `9bb2e9453d04a7c8a22d28ec731e36a873d5e8e5c3bd5a551323b75b5d427864`. Its latest listed docs/skills change is commit `d281bcfcd4c32341eddadc447ed1af168e20d23e`, “Point skills docs to developer documentation site” (`codex-skills.atom:7-14`).

Sandbox setup command: `timeout 180s bash -lc 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/SrcCodex && git -C /fast/scratch/hyaku/kotoba-r55/SrcCodex checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c0'` (exit 0; no stdout). The clone was checked out at the plan commit. In that clone:

```text
Command: timeout 120s bash -lc 'set +e; python3 -B /fast/scratch/hyaku/kotoba-r55/SrcCodex/verifiers/check_explicit_invocation.py --self-test; rc=$?; printf "command exit %s\n" "$rc"; exit "$rc"'
self-test: 0 failure(s) over 29 assertions
command exit 0
Exit: 0
```

## Surfaces and limits

- Lane surface written: `.ufo/waves/round-55/build/SrcCodex.md` only. Fetched pages and the self-test were in the permitted sandbox clone; no product, corpus, verifier, counter, lesson, or SKILL.md files were edited. No tools were installed.
- C1 `--rev ... --fetch` was not run: these are source and row drafts for the integrator, not integrated lane changes. This report does not claim the C1 predicate passed, or claim that Codex behavior was executed or measured.
- C2 gates and the other six C1 clients were out of scope.
