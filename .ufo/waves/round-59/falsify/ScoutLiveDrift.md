Result: HOLDS — counter-header live bodies match all six committed snapshots; code.claude.com is UA-sensitive and cursor.com is Accept-sensitive, and the other four hosts are not.

Attacked: live drift of S096–S101 against `.ufo/waves/round-59/snapshots/`, and which of those hosts are still in the round-58 R3 class (plan `plans/round-59.md:15`: live fetch UA-sensitive). Snapshot blobs are identical at data `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`, measure receipt `d64d945b3435e2532203c505ad64ecf5d91b780e`, and the HEAD observed while fetching, `3f15f84436c43c2e8e64859fa7612972db6f35ba` (one later commit: LOG/SCORECARD/falsify spec). Working-tree hashes equal those blobs. No lane file was edited except this report. No tool was installed.

## Clients

Each URL once, inside `Fri 23 Oct 2026 09:53:02 AM UTC` … `Fri 23 Oct 2026 09:53:06 AM UTC` (`date -u` before and after; script `START`/`END` the same instants). Exit 0.

- **plain:** `curl -sSL --max-time 30` with no `-A` and no `Accept` override. Trace shows the request sent `user-agent: curl/8.23.0` and `accept: */*`. curl 8.23.0 (`curl --version`, same minute).
- **counter:** same curl plus `-A` and `-H` taken from `verifiers/check_hook_files.py:316-318`. Trace shows that UA and `accept: text/markdown, text/plain;q=0.9, */*;q=0.8`.
- **urllib:** `urllib.request.build_opener().open(url, timeout=30)` on Python 3.14.8. Logged request headers are only `Host` and `User-agent: Python-urllib/3.14` (no `Accept`). `urllib.request.__version__` is `3.14`.

`--max-time`, `-D`, `-o`, `-w`, and `--trace-ascii` do not add request headers. Bodies hashed are the response bodies only. Every final URL equals the requested URL; curl `num_redirects=0`; every curl exit 0; stderr empty. Scratch: `/fast/scratch/hyaku/kotoba-r59/ScoutLiveDrift/` (`results.json`, bodies, traces).

Counter UA string: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.

## Eighteen fetches

Snapshot sha256 is the SOURCES figure (`corpus/SOURCES.md:108-113`) and the file on disk.

| id | host / URL | variant | status | bytes | sha256 | vs snapshot |
|---|---|---|---:|---:|---|---|
| S096 | code.claude.com `/docs/en/hooks.md` | plain | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | match |
| S096 | | counter | 200 | 274129 | `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8` | match |
| S096 | | urllib | 403 | 17 | `2938e9f1284180959e33ab1718d0793a72ff6e4cdb8108c34dcd14e69446de5c` | differ |
| S097 | learn.chatgpt.com `/docs/hooks.md` | plain | 200 | 47133 | `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92` | match |
| S097 | | counter | 200 | 47133 | same | match |
| S097 | | urllib | 200 | 47133 | same | match |
| S098 | code.visualstudio.com `/docs/agent-customization/hooks.md` | plain | 200 | 15152 | `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08` | match |
| S098 | | counter | 200 | 15152 | same | match |
| S098 | | urllib | 200 | 15152 | same | match |
| S099 | docs.github.com `/en/copilot/concepts/customizations/hooks.md` | plain | 200 | 8428 | `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4` | match |
| S099 | | counter | 200 | 8428 | same | match |
| S099 | | urllib | 200 | 8428 | same | match |
| S100 | geminicli.com `/docs/hooks/best-practices.md` | plain | 200 | 17650 | `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc` | match |
| S100 | | counter | 200 | 17650 | same | match |
| S100 | | urllib | 200 | 17650 | same | match |
| S101 | cursor.com `/docs/hooks` | plain | 200 | 1307361 | `380c5a72c14ca5d72cfbc91f90bf7d285c2d2f1652588c4aa7dfcfe5dcdc8bd3` | differ |
| S101 | | counter | 200 | 69145 | `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d` | match |
| S101 | | urllib | 200 | 1307361 | `380c5a72c14ca5d72cfbc91f90bf7d285c2d2f1652588c4aa7dfcfe5dcdc8bd3` | differ |

Content-Type: markdown `text/markdown` on every match. S096 urllib: `text/plain`, body the 17 bytes `error code: 1010\n`, `Server: cloudflare` (response `Date: Fri, 23 Oct 2026 09:53:03 GMT`). S101 plain and urllib: `text/html; charset=utf-8`. S101 counter: `text/markdown; charset=utf-8`, `vary: Accept`.

## Which hosts are sensitive

The three required variants confound UA with Accept, so four labelled extra curls were sent at `Fri 23 Oct 2026 09:54:01 AM UTC` (`date -u` 09:54:01 and 09:54:02; each curl exit 0, 0 redirects).

**UA-sensitive: code.claude.com only.**

- `curl -sSL --max-time 30 -A 'Python-urllib/3.14'` (curl's HTTP/2 stack, default `Accept: */*`) → 403, 17 bytes, sha256 `2938e9f1…de5c`, same body, `server: cloudflare`, `date: Fri, 23 Oct 2026 09:54:01 GMT`. The UA string is sufficient. This is not Python's TLS fingerprint.
- `curl -sSL --max-time 30 -H 'Accept:'` (curl UA, Accept removed) → 200, 274129 bytes, snapshot sha. Missing Accept is not the 403.
- plain vs counter already differed in both UA and Accept and returned identical snapshot bytes. Accept does not change this page.

**Accept-sensitive, not UA-sensitive: cursor.com only.**

- `curl -sSL --max-time 30 -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8'` (curl UA, no browser UA) → 200, 69145 bytes, snapshot sha, `text/markdown`.
- `curl -sSL --max-time 30 -A '<counter UA>'` (browser UA, default `Accept: */*`) → 200, 1307361 bytes, sha256 `380c5a72…8bd3`, `text/html`, same body as plain and as urllib.
- Python-urllib/3.14 was HTTP 200 here, not 403.

**Not sensitive across the three variants:** learn.chatgpt.com, code.visualstudio.com, docs.github.com, geminicli.com. All three bodies match each other and the snapshot. learn.chatgpt.com sends `vary: Accept` and still returned one body for `Accept: */*`, the counter Accept, and a missing Accept. Other Accept values were not sent.

## Does any live page differ from its snapshot?

No, for the representation the counter fetches. All six counter-header bodies are byte-identical to the committed snapshots. There is no content drift of the measured pages between the 09:34–09:35Z SOURCES fetches and this 09:53Z pass.

Yes, for the other two clients, and only on the sensitive hosts:

- code.claude.com under Python-urllib is a 17-byte Cloudflare 403, not the snapshot.
- cursor.com under plain curl and under urllib is the HTML document (1,307,361 B), not the markdown snapshot (69,145 B). The HTML contains the snapshot's opening sentence and does not contain the snapshot bytes, the mid line `**Available matchers by hook:**`, or the snapshot's last line. It is a different serialization of the same URL, not a byte-level copy. Prose equality after stripping HTML was not checked.

## Round-58 R3

The class named in `plans/round-59.md:15` is still real, and it is split across two hosts today. A client that omits the counter headers does not see the snapshot on code.claude.com (UA) or cursor.com (Accept). The round-58 example was cursor.com returning 403 to urllib with UA `kotoba-shokunin-counter/58` while curl got the page (`.ufo/waves/round-58/falsify/ReopenS094.md:46`). That exact UA was not resent. Today's `Python-urllib/3.14` is not 403'd by cursor.com; it gets the HTML. The counter's browser UA plus markdown Accept is what still selects the snapshotted markdown there.

## Limits

- One fetch per required variant, plus the four cross-tests. No retry, no second sample later.
- HTML-stripped equality of the cursor page to the markdown snapshot was not measured.
- `kotoba-shokunin-counter/58` was not sent.
- `check_hook_files.py` was not run.
- Cookie values from the 403 responses are omitted.

## Report path

```
ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/falsify/ScoutLiveDrift.md
-rw-r--r-- 1 vgpnk vgpnk 7640 Oct 23 06:55 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/falsify/ScoutLiveDrift.md
```

That `ls` is of the file before this section was appended.
