# ScoutPyDocs — round-92 source receipts (read-only scout)

Seat: ScoutPyDocs. Round 92, wave 1. Access date: 2026-11-05. Host: linux.
Fetch method: `curl -sS -L -w 'HTTP_STATUS=%{http_code} BYTES=%{size_download} URL=%{url_effective}\n'`.
Nothing was written outside this receipt directory and the seat's scratch
(`/fast/scratch/hyaku/kotoba-r92/ScoutPyDocs/`, deleted on exit). No corpus file was written.

---

## (1) S266 candidate — Python exception reference: `NotADirectoryError`

URL requested: `https://docs.python.org/3/library/exceptions.html`

| field | value |
|---|---|
| HTTP status (no follow) | `301` → `Location: https://docs.python.org/3/builtins/exceptions.html` |
| HTTP status (after redirect, final) | `200` |
| effective URL | `https://docs.python.org/3/builtins/exceptions.html` |
| byte size (downloaded body) | `145885` |
| lines in body | `1642` |
| md5 of body | `5fbeed2dd8f88e9b9d1454ba9ff97e46` |
| page title | `Built-in Exceptions — Python 3.15.2 documentation` |

**NOTE for the scribe:** the requested URL now answers `301` and lands on
`https://docs.python.org/3/builtins/exceptions.html` (the `library/` path was folded into
`builtins/` in the current docs build). Record the URL that was requested *and* the effective
final URL; a row that records only `https://docs.python.org/3/library/exceptions.html` is still
resolvable (it redirects), but its byte size and title are those of the **builtins** page, not of
a `library/exceptions.html` page. Title observed: `Built-in Exceptions`, not `Exception
hierarchy` / `exceptions —`.

### Entry heading line number

The `NotADirectoryError` definition-list entry (`<dt>`) is at **HTML line 1118**; its
signature line is 1119; the body (`<dd>`) runs 1120–1124.

```
=== L1118 ===
<dt class="sig sig-object py" id="NotADirectoryError">
=== L1119 ===
<span class="property"><span class="k"><span class="pre">exception</span></span><span class="w"> </span></span><span class="sig-name descname"><span class="pre">NotADirectoryError</span></span><a class="headerlink" href="#NotADirectoryError" title="Link to this definition">¶</a></dt>
```

### TWO located quotes (each ≤ 25 words)

**QUOTE A — what `NotADirectoryError` is raised for** — HTML lines **1120–1121** (17 words):

> "Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory."

Raw lines (verbatim, `sed -n '1120p'` / `sed -n '1121p'`):

```
=== L1120 ===
<dd><p>Raised when a directory operation (such as <a class="reference internal" href="../library/os.html#os.listdir" title="os.listdir"><code class="xref py py-func docutils literal notranslate"><span class="pre">os.listdir()</span></code></a>) is requested on
=== L1121 ===
something which is not a directory.  On most POSIX platforms, it may also be
```

The sentence continues on lines 1122–1123 and is also quotable at the same ≤25-word budget —
"it may also be raised if an operation attempts to open or traverse a non-directory file as if it
were a directory." (22 words), i.e. the POSIX **path-component-that-is-not-a-directory** case:

```
=== L1122 ===
raised if an operation attempts to open or traverse a non-directory file as if
=== L1123 ===
it were a directory.
=== L1124 ===
Corresponds to <code class="xref c c-data docutils literal notranslate"><span class="pre">errno</span></code> <a class="reference internal" href="../library/errno.html#errno.ENOTDIR" title="errno.ENOTDIR"><code class="xref py py-const docutils literal notranslate"><span class="pre">ENOTDIR</span></code></a>.</p>
```

**QUOTE B — its place in the `OSError` hierarchy** — the exception-hierarchy tree, **HTML line
1440** (`OSError`) and **HTML line 1452** (`NotADirectoryError`), inside the tree block that opens
at line 1416 (`BaseException`); the `OSError` branch runs lines 1440–1455 (closing with
`TimeoutError` at 1455). Located excerpt (the intermediate siblings elided; the two anchor lines
are given verbatim below):

> "├── OSError … │    ├── NotADirectoryError"

```
=== L1440 ===
      ├── OSError
=== L1452 ===
      │    ├── NotADirectoryError
```

Full contiguous tree span for the two anchors (L1440 → L1452), for the row's line reference:

```
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
```

Supporting (also ≤25 words, names the subclass relation in prose) — **HTML lines 1014–1015**,
the preamble of the `OS exceptions` section that contains the `NotADirectoryError` entry:

```
=== L1014 ===
<p>The following exceptions are subclasses of <a class="reference internal" href="#OSError" title="OSError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">OSError</span></code></a>, they get raised
=== L1015 ===
depending on the system error code.</p>
```

> "The following exceptions are subclasses of OSError, they get raised depending on the system error code." (16 words)

Supporting: the `OSError` entry itself is at **HTML line 594** (`<dt class="sig sig-object py" id="OSError">`),
the `OS exceptions` section opens at line 1012 (`<section id="os-exceptions">`) with its `<h3>` at 1013.

### Does the page name which `os` functions raise it?

**Yes, but only by one worked example.** The `NotADirectoryError` body names exactly one `os`
function — **`os.listdir()`** (HTML line 1120, hyperlinked to `../library/os.html#os.listdir`).
The page does **not** enumerate a fuller list of raising `os` functions for this exception; the
remaining description is generic ("a directory operation", "open or traverse a non-directory file
as if it were a directory"). The adjacent sibling entry `IsADirectoryError` names `os.remove()`
(line 1112) — that is `IsADirectoryError`, **not** `NotADirectoryError`; do not attribute it.

```
=== L1112 ===
<dd><p>Raised when a file operation (such as <a class="reference internal" href="../library/os.html#os.remove" title="os.remove"><code class="xref py py-func docutils literal notranslate"><span class="pre">os.remove()</span></code></a>) is requested
```

The errno correspondence is `ENOTDIR` (line 1124). Grep of the whole page for
`os.(listdir|open|scandir|stat|chdir|mkdir|remove)` returns only lines 1112 and 1120 — i.e. one
`os` call per sibling entry, none further for `NotADirectoryError`.

---

## (2) S263 anchor repair — Python `subprocess` documentation

URL: `https://docs.python.org/3/library/subprocess.html`

| field | value |
|---|---|
| HTTP status (no follow) | `200` (no redirect) |
| HTTP status (final) | `200` |
| effective URL | `https://docs.python.org/3/library/subprocess.html` |
| byte size (downloaded body) | `208648` — **byte-identical to the round-91 reading** (`208648 B`) |
| lines in body | `2047` |
| md5 of body | `f63cf7e1b7efaa24ea6bb341b536a03f` |
| page title | `subprocess — Subprocess management — Python 3.15.2 documentation` |
| page footer "Last updated on" | **HTML line 2037** — `Last updated on Nov 05, 2026 (12:47 UTC).` |

```
=== L2037 ===
      Last updated on Nov 05, 2026 (12:47 UTC).
```

The round-91 row's footer line (2037) and footer text still match exactly.

### `subprocess.run` — the timeout paragraph

- `subprocess.run` definition-list entry `<dt>`: **HTML line 270** (the row's cited "HTML line
  270" — still correct).
- The timeout paragraph itself begins at **HTML line 288** and runs through **line 294**:
  `A timeout may be specified in seconds, it is internally passed on to …` → `process creation takes.</p>`
- The round-91-cited **289–291** span is where the *quoted sentence* sits, and that is still exact:

```
=== L270 ===
<dt class="sig sig-object py" id="subprocess.run">
=== L288 ===
<p>A <em>timeout</em> may be specified in seconds, it is internally passed on to
=== L289 ===
<a class="reference internal" href="#subprocess.Popen.communicate" title="subprocess.Popen.communicate"><code class="xref py py-meth docutils literal notranslate"><span class="pre">Popen.communicate()</span></code></a>. If the timeout expires, the child process will be
=== L290 ===
killed and waited for. The <a class="reference internal" href="#subprocess.TimeoutExpired" title="subprocess.TimeoutExpired"><code class="xref py py-exc docutils literal notranslate"><span class="pre">TimeoutExpired</span></code></a> exception will be
=== L291 ===
re-raised after the child process has terminated. The initial process
=== L292 ===
creation itself cannot be interrupted on many platform APIs so you are not
=== L293 ===
guaranteed to see a timeout exception until at least after however long
=== L294 ===
process creation takes.</p>
```

> run() quote (25 words), HTML lines 289–291: "If the timeout expires, the child process will be killed and waited for. The TimeoutExpired exception will be re-raised after the child process has terminated."

### `Popen.communicate` — section start

- `<dl class="py method">` opens at **HTML line 1050**.
- The `Popen.communicate` entry `<dt id="subprocess.Popen.communicate">` is at **HTML line 1051**
  (signature line 1052).
- **This is the correct anchor for the row's "contrast entry subprocess.Popen.communicate".**

```
=== L1050 ===
<dl class="py method">
=== L1051 ===
<dt class="sig sig-object py" id="subprocess.Popen.communicate">
=== L1052 ===
<span class="sig-prename descclassname"><span class="pre">Popen.</span></span><span class="sig-name descname"><span class="pre">communicate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">input</span></em><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">timeout</span></em><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#subprocess.Popen.communicate" title="Link to this definition">¶</a></dt>
```

(L1052 above is the full untruncated line, 708 characters.)

### The contrast quote — exact line

**HTML line 1071.** The sentence begins there and continues onto 1072.

```
=== L1071 ===
<p>The child process is not killed if the timeout expires, so in order to
=== L1072 ===
cleanup properly a well-behaved application should kill the child process and
```

> contrast quote (10 words), HTML line **1071**: "The child process is not killed if the timeout expires"

### Anchor-repair verdict (for the S265 correction row)

The round-91 row S263 and lesson `corpus/lessons/round-91.md` cite the `Popen.communicate`
contrast at **HTML line 1042**. On today's byte-identical page (208648 B, same md5-class of
content, same footer timestamp), **line 1042 is not the contrast quote** — it is a
`versionchanged` note belonging to the *preceding* `Popen.wait` entry:

```
=== L1042 ===
<p><span class="versionmodified changed">Changed in version 3.3: </span><em>timeout</em> was added.</p>
```

The correct anchors are:

| what | wrong anchor (round 91) | correct anchor (today) |
|---|---|---|
| `Popen.communicate` contrast quote | 1042 | **1071** (continues 1072) |
| `Popen.communicate` entry `<dt>` | (not cited) | **1051** |
| `subprocess.run` entry `<dt>` | 270 | 270 — unchanged, still correct |
| `subprocess.run` timeout paragraph | 289–291 | 289–291 — unchanged, still correct (paragraph spans 288–294) |
| footer "Last updated on" | 2037 | 2037 — unchanged, still correct |
| byte size | 208648 | 208648 — unchanged |

This re-confirms round-91 spot-check routed defect 4 (the row and lesson cite 1042; the entry is
at 1051 and the quote at 1071). Quote text, section, and meaning are unchanged; only the anchor
line is wrong.

Additional anchors recorded for the same page (not required, but they pin the surrounding
structure the correction touches):

```
=== L1044 ===
<div class="versionchanged">
=== L1045 ===
<p><span class="versionmodified changed">Changed in version 3.15: </span>if <em>timeout</em> is not <code class="docutils literal notranslate"><span class="pre">None</span></code>, use efficient event-driven implementation
=== L1048 ===
</dd></dl>
=== L1809 ===
<section id="timeout-behavior">
=== L1810 ===
<span id="subprocess-timeout-behavior"></span><h3>Timeout Behavior<a class="headerlink" href="#timeout-behavior" title="Link to this heading">¶</a></h3>
```

The `Timeout Behavior` section (L1809–1810) is the page's own umbrella section for timeout
semantics; `subprocess.run`'s entry is at L270 and the `Popen.communicate` entry at L1051, both
inside the "Using the subprocess Module" section.

---

## Summary for the scribe (ScribeCorpusR92)

1. **S266 (new row)** — `https://docs.python.org/3/library/exceptions.html` → **301** →
   `https://docs.python.org/3/builtins/exceptions.html`; final **HTTP 200**, **145885 B**;
   title `Built-in Exceptions — Python 3.15.2 documentation`; entry `<dt>` at **line 1118**;
   quote A at **1120–1121**; quote B (hierarchy tree) at **1440** + **1452**; the page names
   `os.listdir()` (line 1120) as the one named `os` function, and `errno.ENOTDIR` (line 1124).
2. **S265 (correction row superseding S263)** — `https://docs.python.org/3/library/subprocess.html`;
   **HTTP 200**, **208648 B** (unchanged); title `subprocess — Subprocess management — Python
   3.15.2 documentation`; footer `Last updated on Nov 05, 2026 (12:47 UTC).` at **line 2037**;
   `subprocess.run` timeout paragraph **288–294** with the quoted sentence at **289–291**;
   `Popen.communicate` entry `<dt>` at **1051**; the contrast quote "The child process is not
   killed if the timeout expires" at **line 1071** — correcting the 1042 anchor in S263 and in
   `corpus/lessons/round-91.md`.
3. Both pages were reachable; no partial state. `SOURCE-READY` (full).
