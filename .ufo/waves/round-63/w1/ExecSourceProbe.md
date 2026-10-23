# ExecSourceProbe

role: source-freshness probe executor
item: Probe r62 spot-check defect 3 for Cursor docs under three Accept-header conditions.

## Findings

1. For `https://cursor.com/docs/rules.md`, `Accept: text/markdown` returned HTTP 404 (389 bytes); `Accept: */*` and no explicit Accept header each returned HTTP 200 (17,252 bytes). Evidence commands and exact stdout are preserved in Artifacts 1–3. All 200 responses had `content-type: text/markdown; charset=utf-8`.
2. For `https://cursor.com/docs/reference/plugins.md`, `Accept: text/markdown` returned HTTP 404 (389 bytes); `Accept: */*` and no explicit Accept header each returned HTTP 200 (30,324 bytes). Evidence commands and exact stdout are preserved in Artifacts 4–6. All 200 responses had `content-type: text/markdown; charset=utf-8`.
3. Both endpoints exhibit Accept-dependent rejection: response headers include `vary: Accept`; the body SHA-256 is identical for both markdown-Accept 404s (`4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1`), while each endpoint's wildcard and default 200 bodies are identical to each other. This is freshness evidence from direct probes on 2026-10-23, not an inference from the earlier spot-check.

## Artifacts

1. Command: `curl -sS -D - -o /tmp/r63-cursor-rules-md -H 'Accept: text/markdown' https://cursor.com/docs/rules.md | head -20; wc -c /tmp/r63-cursor-rules-md; sha256sum /tmp/r63-cursor-rules-md; head -c 200 /tmp/r63-cursor-rules-md`

```text
HTTP/2 404 
age: 0
cache-control: public, max-age=0, must-revalidate
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 23:03:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-robots-tag: noindex
x-vercel-cache: MISS
x-vercel-id: gru1::iad1::q82fr-1792796581373-44a8eb6464f3

389 /tmp/r63-cursor-rules-md
4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1  /tmp/r63-cursor-rules-md
# Page not found

This page doesn't exist. Try one of these instead:

- [Documentation](https://cursor.com/docs)
- [Quickstart](https://cursor.com/docs/get-started/quickstart)
- [Agent overview](https
```

2. Command: `curl -sS -D - -o /tmp/r63-cursor-rules-any -H 'Accept: */*' https://cursor.com/docs/rules.md | head -20; wc -c /tmp/r63-cursor-rules-any; sha256sum /tmp/r63-cursor-rules-any; head -c 200 /tmp/r63-cursor-rules-any`

```text
HTTP/2 200 
age: 1800
cache-control: public, max-age=3600
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 22:33:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-vercel-cache: HIT
x-vercel-id: gru1::iad1::8hvdh-1792796581374-c8ad4da45fd5

17252 /tmp/r63-cursor-rules-any
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  /tmp/r63-cursor-rules-any
# Rules

Rules provide system-level instructions to Agent. They bundle prompts, scripts, and more together to manage and share workflows across your team.

Cursor supports four types o
```

3. Command: `curl -sS -D - -o /tmp/r63-cursor-rules-none https://cursor.com/docs/rules.md | head -20; wc -c /tmp/r63-cursor-rules-none; sha256sum /tmp/r63-cursor-rules-none; head -c 200 /tmp/r63-cursor-rules-none`

```text
HTTP/2 200 
age: 1800
cache-control: public, max-age=3600
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 22:33:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-vercel-cache: HIT
x-vercel-id: gru1::iad1::plbpj-1792796581372-705d91fafb8a

17252 /tmp/r63-cursor-rules-none
dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0  /tmp/r63-cursor-rules-none
# Rules

Rules provide system-level instructions to Agent. They bundle prompts, scripts, and more together to manage and share workflows across your team.

Cursor supports four types o
```

4. Command: `curl -sS -D - -o /tmp/r63-cursor-plugins-md -H 'Accept: text/markdown' https://cursor.com/docs/reference/plugins.md | head -20; wc -c /tmp/r63-cursor-plugins-md; sha256sum /tmp/r63-cursor-plugins-md; head -c 200 /tmp/r63-cursor-plugins-md`

```text
HTTP/2 404 
age: 0
cache-control: public, max-age=0, must-revalidate
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 23:03:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-robots-tag: noindex
x-vercel-cache: MISS
x-vercel-id: gru1::iad1::96gmj-1792796581379-2c4f8becbbf5

389 /tmp/r63-cursor-plugins-md
4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1  /tmp/r63-cursor-plugins-md
# Page not found

This page doesn't exist. Try one of these instead:

- [Documentation](https://cursor.com/docs)
- [Quickstart](https://cursor.com/docs/get-started/quickstart)
- [Agent overview](https
```

5. Command: `curl -sS -D - -o /tmp/r63-cursor-plugins-any -H 'Accept: */*' https://cursor.com/docs/reference/plugins.md | head -20; wc -c /tmp/r63-cursor-plugins-any; sha256sum /tmp/r63-cursor-plugins-any; head -c 200 /tmp/r63-cursor-plugins-any`

```text
HTTP/2 200 
age: 1799
cache-control: public, max-age=3600
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 22:33:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-vercel-cache: HIT
x-vercel-id: gru1::iad1::q82fr-1792796581380-3af815cd66c9

30324 /tmp/r63-cursor-plugins-any
3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204  /tmp/r63-cursor-plugins-any
# Plugins reference

Reference documentation for building, structuring, and submitting Cursor plugins. Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundle
```

6. Command: `curl -sS -D - -o /tmp/r63-cursor-plugins-none https://cursor.com/docs/reference/plugins.md | head -20; wc -c /tmp/r63-cursor-plugins-none; sha256sum /tmp/r63-cursor-plugins-none; head -c 200 /tmp/r63-cursor-plugins-none`

```text
HTTP/2 200 
age: 1799
cache-control: public, max-age=3600
content-type: text/markdown; charset=utf-8
date: Fri, 23 Oct 2026 22:33:01 GMT
link: </llms.txt>; rel="describedby"; type="text/plain"; title="llms.txt", </docs/sitemap.xml>; rel="sitemap"; type="application/xml"
server: Vercel
strict-transport-security: max-age=63072000
vary: Accept
x-content-type-options: nosniff
x-matched-path: /api/raw
x-vercel-cache: HIT
x-vercel-id: gru1::iad1::gg6h9-1792796581380-e0cf18d89d5a

30324 /tmp/r63-cursor-plugins-none
3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204  /tmp/r63-cursor-plugins-none
# Plugins reference

Reference documentation for building, structuring, and submitting Cursor plugins. Plugins package rules, skills, agents, commands, MCP servers, and hooks into distributable bundle
```

## Verdict

INFORMS — both `.md` URLs return 404 only for `Accept: text/markdown` in these probes and return 200 for wildcard/default Accept, confirming probe-dependent rejection. I would revise this finding only if a repeated direct probe under the same request conditions returned a different status or `Vary` behavior.
