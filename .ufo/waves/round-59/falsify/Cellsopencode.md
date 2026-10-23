Result: MIXED — both Events spans are genuine, correctly cited V2 tool-hook events and the module-routing claims hold, but the unqualified opencode row hides a V1/V2 API boundary explicitly documented on its cited page.

## Scope and axes

Seat: `KotobaR59.Cellsopencode`; sole recipient/integrator: `KotobaR59`.

Reviewed `SKILL.md:133` and `corpus/knowledge/hook-files-round59.md:54-57` at data commit `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, against independently fetched S085 and S087 bytes. Also opened the served plugin page to test the strongest version counterexample. This is a scoped semantic attack report, not an admission decision or native-judge verdict.

Primary impacted axis: **depth** (correct event names with actionable API scope). Secondary risks: **calibration** (not implying cross-version compatibility or exhaustive absence), **operability** (using the correct registration API). Freshness evidence is the fetch record below; no runtime behavior was tested.

The round-59 snapshots directory contains S096-S101, not S085/S087; I therefore fetched their pinned URLs. Both fetched digests and byte counts match `corpus/SOURCES.md:98,100`. Page aliases below are files under `/fast/scratch/hyaku/kotoba-r59/Cellsopencode/`. Quotes retain their original bytes, including indentation and Markdown where present; no markup was stripped or line breaks folded. Each source excerpt is at most 25 words.

## 1. Every Events-cell backticked span

The complete backticked-span inventory of `SKILL.md:133`'s Events cell is **two** spans. The parenthetical source/line references are not backticked.

| Span | Required ruling | Exact source evidence | Interpretation |
|---|---|---|---|
| `execute.before` | **event** | S085.page:1738: `await ctx.tool.hook("execute.before", (event) => {` | Registration through the tool domain's hook API, not an unrelated identifier. S085.page:1735 says: `Inspect or replace tool input before execution.` |
| `execute.after` | **event** | S085.page:1746: `await ctx.tool.hook("execute.after", (event) => {` | Registration through the same hook API. S085.page:1743 says: `Inspect successful results or failures after execution.` It is not limited to successful calls. |

Both registration lines begin at column zero in the fetched page. Further independent context on that same page:

S085.page:1755-1758:
```ts
interface ToolHooks {
  "execute.before": ToolExecuteBefore
  "execute.after": ToolExecuteCompleted | ToolExecuteFailed
}
```

S085.page:1761-1764:
```ts
  hook<Name extends keyof ToolHooks>(
    name: Name,
    callback: (event: ToolHooks[Name]) => Promise<void> | void,
  ): Promise<Registration>
```

These are named lifecycle interception points used as such, not merely strings found somewhere on the page. **No span is ruled `not an event`; no event replacement is required by the freeze addendum at `plans/round-59.md:93-98`.** The version-scope finding below is separate.

## 2. All cell claims and parenthetical references

| Attacked claim/reference | Classification | Exact page text / evidence |
|---|---|---|
| Hook config: hook code is a plugin module | **supported** | S085.page:10 names `.opencode/plugins/example/index.ts` as the local example module in its fence. Its default export and `setup(ctx)` are at :13-18; its hook registration APIs are at :1335-1342 and :1738-1764. The served page states the mechanism explicitly at :64-65; see quote below. |
| Hook config: no hook file | **supported as a routing distinction** between a separate hook-definition file and plugin module code | The cited pages teach programmatic registration, not a standalone hook-definition schema. This does **not** mean opencode has no hooks, or that plugin selection never uses configuration. S085.page:21-22 and S087.page:5,33-34 explicitly describe configuration selecting plugins. A 404 alone would not establish the broader negative. |
| Hook config parenthetical: § Plugin manifests by client; S085, S087 | **supported** | The heading exists at SKILL.md:93 and the opencode module/discovery row is :105. S085 supplies module/API behavior; S087 supplies global discovery. They are complementary references, not two interchangeable event pages. |
| Events parenthetical: S085 index.mdx :1738 | **supported, exact line** | The fetched :1738 is the `ctx.tool.hook("execute.before", ...)` registration quoted above. |
| Events parenthetical: S085 index.mdx :1746 | **supported, exact line** | The fetched :1746 is the `ctx.tool.hook("execute.after", ...)` registration quoted above. Neither reference has drifted. |
| Action: read the plugin module | **supported** | S085's module example and hook registrations place the behavior in code. Served-plugins.page:64-65 explicitly describes a module returning a hooks object. |
| Action: do not look for a hook config file | **supported in that same dedicated hook-definition sense** | Inspect the module for event registration; do not invent a settings-like hooks file. Do not interpret this as permission to ignore the configuration selecting a non-default plugin. S087.page:33-34 states that configured paths load a module. |
| Unqualified opencode applicability of the printed Events | **overstated across V1/V2** | S085.page:1796-1825 explicitly separates the APIs and says sharing an export does not translate hooks. Finding OC-VERSION below gives the concrete counterexample and smallest correction. |

Exact mechanism text, served-plugins.page:64-65 (24 words):
```text
A plugin is a **JavaScript/TypeScript module** that exports one or more plugin
functions. Each function receives a context object and returns a hooks object.
```

Exact module-loading text, S087.page:33-34 (25 words):
```text
Configured local paths must be directories. OpenCode loads the directory's `server` or `index` module, such as
`index.ts`. A path to a single file is skipped.
```

I found no concrete counterexample to the module-routing distinction on these pages. I did not independently repeat the entire changelog/current-source-tree/corpus Q30 sweep from `build/SrcOpencodeNegative.md:45-53`; therefore this report does not assert exhaustive documentation silence. The client positively documents hooks.

## 3. Every claim in the entry's opencode note

Target: `corpus/knowledge/hook-files-round59.md:54-57`.

| Note claim / reference | Classification | Evidence |
|---|---|---|
| Hook code is a plugin module; no separate hook-file route | **supported**, with the same bounded meaning as above | S085.page:10-18,1335-1342,1733-1764; served-plugins.page:64-65. |
| Default discovery in `.opencode/plugins/` | **supported** | S085.page:21 explicitly says automatic loading. S087.page:46-47 states what is discovered; exact quote below. |
| Default global discovery in `~/.config/opencode/plugins/` | **supported** | S087.page:57 says global plugins use the same layout under the config directory, followed by the exact path at :60. This global fact is correctly sourced to S087, not invented from S085's local example. |
| Parenthetical: configured plugin paths also load | **supported** | S085.page:21-22; S087.page:5 and :33-34. The latter states module selection from configured directories, not arbitrary single-file imports. |
| Parenthetical: npm packages also load | **supported** | S087.page:105: `Package installation accepts npm names with versions, tags, or ranges, plus npm-compatible Git package specifications.` |
| Parenthetical: § Plugin manifests by client; S085, S087; build/CriticCensus.md OC-1 | **supported** | SKILL.md:93,105 provide the route. `build/CriticCensus.md:46-60` identifies and corrects the exclusive-two-default-roots rationale. The landed note says **by default** and retains configured/package alternatives, so that correction is present here. |
| `opencode.ai/docs/hooks.md` is HTTP 404 | **supported at this access time** | Independent fetch returned HTTP 404, 97 bytes; hooks-route.page:1 is quoted below. This is a route-status fact, not a proof that hooks do not exist. |
| Parenthetical report references at :57 | **supported as pointers** | `w0/Censusopencode.md:15-23` records that route's earlier 404; `build/SrcOpencodeNegative.md:45-53` records its broader sweep and the two failed hooks routes. My independent 404 receipt agrees. |

S087.page:46-47:
```text
OpenCode also loads direct `.ts` and `.js` files and immediate plugin package directories from every discovered
`.opencode/plugins/` directory.
```

S087.page:57 (15 words):
```text
Global plugins use the same discovery layout under the OpenCode config directory.
```

S087.page:60:
```text
~/.config/opencode/plugins/
```

hooks-route.page:1:
```json
{"status":404,"message":"Cannot find any route matching [GET] https://opencode.ai/docs/hooks.md"}
```

## 4. OC-VERSION — the strongest counterexample

**Result: MIXED.** The two names survive the exact semantic test on S085. Their applicability is V2, not an unqualified contract for both opencode APIs.

The same cited page documents both sides. S085.page:1798:
```text
A plugin can support V1 and V2 from the same package entrypoint. Default export
```

Within that one example, the V2 `setup()` branch registers at S085.page:1808:
```ts
      await ctx.tool.hook("execute.before", () => {
```

The V1 `server()` branch instead returns this key at S085.page:1815:
```ts
      "tool.execute.before": async () => {
```

The decisive contract is S085.page:1825:
```text
- Keep each implementation on its own API; sharing an export does not translate V1 hooks into V2 hooks.
```

The live served plugin page independently names the V1 pair under its `#### Tool Events` heading at served-plugins.page:190-193:
```text
#### Tool Events

- `tool.execute.after`
- `tool.execute.before`
```

It also uses `tool.execute.before` as an actual returned hook key at :88 and :241, so these are not stray names either. S085 itself supplies the version distinction; the live page is corroboration, not a replacement source for the frozen Events spans. The lane already distinguishes V1/V2 in SKILL.md:91,225, and records an opencode-ai 1.19.3 evidence lineage at :531-534. I did not run that client or independently verify the installed version.

**Smallest safe correction:** keep the client label, the two Events spans, both exact line numbers, the module route and the counter unchanged. In SKILL.md:133 change only the Events parenthetical from `(S085 index.mdx :1738, :1746)` to `(V2 API; S085 index.mdx :1738, :1746)`. Add a short sentence to the opencode entry note: `The SKILL event names use the V2 plugin API; V1 uses a separate hook-key namespace (S085 index.mdx:1796-1825).`

This is a fixable source-scope defect, not evidence that either span is `not an event`. It requires no new source row, token, alias, fallback, runtime implementation, counter rule or target. It does not justify changing the frozen counter or its predicate. Whether the remaining measurement establishes the round claim belongs to the canonical judge, not this seat.

## 5. Access receipts and commands

Sandbox setup, exit 0, no stdout:
```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; timeout 120s git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/Cellsopencode && timeout 30s git -C /fast/scratch/hyaku/kotoba-r59/Cellsopencode checkout -q c63ccc6823e1f6a8577acbb43d19551eadbbee9a
```

No sandbox commit was made.

Each command below exited 0. Curl intentionally did not use `--fail`, so the hooks-route command's shell success does not disguise its HTTP 404.

### S085

```sh
timeout 5s date -u && timeout 60s curl -sSL --max-time 45 -A 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S085.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' 'https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx' && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S085.page && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S085.page && timeout 5s date -u
```

Observed output:
```text
Fri 23 Oct 2026 09:53:24 AM UTC
url=https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx
http=200
bytes=60780
60780 /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S085.page
e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5  /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S085.page
Fri 23 Oct 2026 09:53:24 AM UTC
```

### S087

```sh
timeout 5s date -u && timeout 60s curl -sSL --max-time 45 -A 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S087.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' 'https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx' && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S087.page && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S087.page && timeout 5s date -u
```

Observed output:
```text
Fri 23 Oct 2026 09:53:24 AM UTC
url=https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/plugins.mdx
http=200
bytes=4371
4371 /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S087.page
39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3  /fast/scratch/hyaku/kotoba-r59/Cellsopencode/S087.page
Fri 23 Oct 2026 09:53:24 AM UTC
```

### Claimed absent hooks route

```sh
timeout 5s date -u && timeout 60s curl -sSL --max-time 45 -A 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/Cellsopencode/hooks-route.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' 'https://opencode.ai/docs/hooks.md' && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r59/Cellsopencode/hooks-route.page && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r59/Cellsopencode/hooks-route.page && timeout 5s date -u
```

Observed output:
```text
Fri 23 Oct 2026 09:53:24 AM UTC
url=https://opencode.ai/docs/hooks.md
http=404
bytes=97
97 /fast/scratch/hyaku/kotoba-r59/Cellsopencode/hooks-route.page
92a89398eab4dc82babfb28e2cfb91bdc69fea5ca769a418db5c5f6ddd2c932a  /fast/scratch/hyaku/kotoba-r59/Cellsopencode/hooks-route.page
Fri 23 Oct 2026 09:53:24 AM UTC
```

### Served plugin page, version counterexample

```sh
timeout 5s date -u && timeout 60s curl -sSL --max-time 45 -A 'Mozilla/5.0' --output /fast/scratch/hyaku/kotoba-r59/Cellsopencode/served-plugins.page --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' 'https://opencode.ai/docs/plugins.md' && timeout 5s wc -c /fast/scratch/hyaku/kotoba-r59/Cellsopencode/served-plugins.page && timeout 5s sha256sum /fast/scratch/hyaku/kotoba-r59/Cellsopencode/served-plugins.page && timeout 5s date -u
```

Observed output:
```text
Fri 23 Oct 2026 09:54:38 AM UTC
url=https://opencode.ai/docs/plugins.md
http=200
bytes=9357
9357 /fast/scratch/hyaku/kotoba-r59/Cellsopencode/served-plugins.page
c76613823185b6bf7f6a164211bcdc7bba3bc738aba1cc927b51189f8da8681e  /fast/scratch/hyaku/kotoba-r59/Cellsopencode/served-plugins.page
Fri 23 Oct 2026 09:54:38 AM UTC
```

## 6. Counter and no-harm bounds

Static source reading only: `verifiers/check_hook_files.py:253-254` fixes TARGET=4 and NEW_TARGET=5. At :892-900 a Hook config cell without a backticked token never enters K; the opencode row has no such token. At :912-914 the Action check counts words, not meaning. Thus the successful C1 receipt cannot itself establish this row's event, module-routing or version semantics.

No counter run, mutation, self-test, hook execution, CLI model call, build, native judge or alternate agent runtime was invoked by this seat. No passing status is claimed for any unrun check. The proposed qualifier leaves both event spans, all tokens and the predicate untouched; it does not promote opencode into the six eligible rows. Only this report was written in the lane; fetched bytes and the read-only review clone are confined to this seat's scratch directory. No tool was installed or updated.

Report: .ufo/waves/round-59/falsify/Cellsopencode.md
