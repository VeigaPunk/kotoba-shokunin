# SimplifyC2 — YAGNI review of the C1 and C2 counters (round 70, wave 1)

**Verdict: 10 deletions/dedups found and applied in a /tmp copy; every verdict, finding line and
self-test line is byte-identical before and after (14 output pairs: self-test, `--rev` tip, `--rev`
base, `--fetch`, and 5 rebuilt control/discriminator worlds). Net −4 lines (757 → 753). The lane was
never edited.** Seat: read-only simplifier; scratch `/tmp/k70w1-SimplifyC2.JVm5` (deleted on return).

## Semantic-reference method (stated limitation)

No LSP server is reachable from this seat's toolset, so there is no semantic `references` proof.
Fallbacks used and labelled as such: `vulture 2.16` (per file — run jointly, it pools names across
both files and hides C2's unused `BASE` because C1 uses a `BASE` of its own), `pyflakes 4.0.3`, and
literal `rg`, plus the observed outputs below as the behavioural proof. Neither file is imported by
any other lane file: `rg -n "check_skill_evals|check_r69_routed_repairs" --glob '!*.md' --glob '!*.txt' .`
→ only each file's own docstring (lines 2 and 6).

## Deletions applied — `verifiers/check_skill_evals.py` (C2), 353 → 354 lines

| # | Line (tip) | Change | Proof it is dead or duplicated |
|---|---|---|---|
| D1 | 41 | delete `BASE = "7d51…"` | `vulture --min-confidence 0 orig/check_skill_evals.py` → `orig/check_skill_evals.py:41: unused variable 'BASE' (60% confidence)`; `rg -n BASE` → line 41 only. The base sha stays in the docstring contract (line 10). |
| D2 | 125 | `check(repo, fetch=None)` → `check(repo)` | `rg -n '\bcheck\(' ` → callers at 257, 262, 336; none passes `fetch`; the body never reads it. `--fetch` is handled in `main` through `live_fetch`. |
| D3 | 243–244 | `_source_row(sid, status="mined", used=ENTRY)` → `_source_row(sid)` with the literals inlined | the only caller is line 249, `_source_row(s)`; the self-test's "row not mined" and "used-by" mutations edit the rendered text, not these parameters. |
| D4 | 256–263 | the honest-world branch ran `check()` twice (once for `n`, again to print findings on failure) → one call, `n, findings, _ = check(FakeRepo(**_honest()))`; `run()` uses `FakeRepo(**world)` | `_honest()` returns exactly the keys `files` and `snaps` (line 250), the `FakeRepo.__init__` parameter names. |
| D5 | 84–97 | `show` and `snapshot` built the same `git -C <repo> show <rev>:<path>` command twice → one `raw()` byte reader; `show` decodes it, `snapshot` hashes the raw bytes and then decodes | sha256 is still taken over the undecoded bytes, so the tamper check is unchanged. **Tradeoff: +3 lines** (one new method) in exchange for a single git-show path. It can be dropped on its own if line count is the priority. |

## Deletions applied — `verifiers/check_r69_routed_repairs.py` (C1), 404 → 399 lines

| # | Line (tip) | Change | Proof it is dead or duplicated |
|---|---|---|---|
| D6 | 273 | delete `FakeRepo.rev = "f" * 40` | `rg -n '\.rev\b'` → the only readers of `.rev` are `Repo.show/blob/checklist` (lines 94, 98, 109, 112) on the real `Repo`. `FakeRepo.checklist` never reads it, and no `k*_` check reads `repo.rev`. |
| D7 | 195 | K69-6: drop the `f"**{l}**" not in low` disjunct | `**l**` contains `l**` as a substring, so whenever the bold disjunct matches, the kept `f"{l}**"` disjunct matches too; `(¬a ∧ ¬b ∧ ¬c) ≡ (¬a ∧ ¬c)`. Exercised by world `k6-bold-labels` (below). |
| D8 | 72–74, 221 | `re.search(verdict, b)` → `verdict in b`; drop the `r""` prefixes | none of the three verdict strings contains a regex metacharacter (`python3 -c … set(v) & set('.^$*+?{}[]\\|()')` → `[]` for all three), so `re.search` is a substring test. Exercised by world `k8-wrong-verdict`. |
| D9 | 301 | `v.replace(chr(92), '')` → `v` | `[chr(92) in v for v in R69_COUNTERS.values()]` → `[False, False, False]`: a no-op left over from the regex form. |
| D10 | 161–204 | K69-2, K69-3 and K69-7 had identical bodies (read the entry → "no appended" finding → token-miss finding) → one helper `_entry_tokens(repo, kid, tokens)` | finding strings are formatted the same way (`f"{kid}: …"`); the base and skip worlds print the "no appended" and "lacks […]" variants byte-identically. K69-6 keeps its own body (lowercasing plus label forms). |

`re` remains used in C1 (k1, k8 `exit=0`, k8 split); `pyflakes new/*.py` → exit 0; per-file
`vulture --min-confidence 0 new/*.py` → no output.

## Evidence — outputs before vs after

Setup: `git clone -q --shared <lane> /tmp/k70w1-SimplifyC2.JVm5/lane && git checkout -q 16b212a…`;
`orig/` = tip bytes, `new/` = edited copies; each run writes stdout+stderr+`exit=N` and is compared
with `cmp`.

```
IDENTICAL check_skill_evals selftest (exit=0; e51f32d05e42)          self-test: 0 failure(s) over 13 assertions
IDENTICAL check_skill_evals rev      (exit=0; 903b2a4f5bf5)          skill eval facts backed 8 of 8
IDENTICAL check_skill_evals base     (exit=1; e04702f9a2dc)          skill eval facts backed 0 of 8
IDENTICAL check_skill_evals fetch    (exit=0; 30af0de97ac3)          skill eval facts backed 8 of 8 / live quotes found 8 of 8
IDENTICAL check_r69_routed_repairs selftest (exit=0; 65a99ea614b6)   self-test: 0 failure(s) over 17 assertions
IDENTICAL check_r69_routed_repairs rev      (exit=1; b5a8a8125b07)   r69 routed defects closed 9 of 10 / K69-11: governance.citation_resolves FAIL
IDENTICAL check_r69_routed_repairs base     (exit=1; f4fb0786e0d0)   r69 routed defects closed 0 of 10
```

(sha256 prefixes are of the full captured output files. `rev` = `--repo <lane> --rev 16b212a…`;
`base` = `--rev 7d51253…`, the plan's kill-rule control; `fetch` = `--rev 16b212a… --fetch`.)

**Controls rebuilt.** The committed controls' sandbox commits are gone from the lane object store
(`git cat-file -e` → absent for `f1ae741…`, `20a6e59…`, `4e088af…`), so this seat rebuilt them in its
own clone (`build_worlds.py`, scratch), plus two worlds that target D7 and D8:

```
IDENTICAL check_r69_routed_repairs world=skip            (2db07f65bf73)  closed 0 of 10, exit=1  (53de0ac + bare LOG heading + bare SCORECARD line)
IDENTICAL check_skill_evals        world=junk            (a40eabec15ec)  backed 0 of 8, exit=1   (on-snapshot 6-word windows lacking key terms)
IDENTICAL check_skill_evals        world=forged          (6866f46c16d6)  backed 0 of 8, exit=1   (each quote + " always")
IDENTICAL check_r69_routed_repairs world=k6-bold-labels  (abcc13cca9c0)  closed 9 of 10, exit=1  (r69 entry labels `**Trigger:**` → `**Trigger**`; no `label:` form left, so only the bold disjuncts can pass K69-6 — and it passes in both)
IDENTICAL check_r69_routed_repairs world=k8-wrong-verdict(41ff1ac9c11e)  closed 8 of 10, exit=1  (receipt `5 of 5` → `4 of 5`; "K69-8: check_skill_precedence.py block lacks its verdict line" in both)
```

The skip, junk and forged finding lines match the committed `controls/C1-skip-control.txt`,
`C2-junk-control.txt` and `C2-forged-control.txt` line for line, except for the `measured-rev` sha.

**Lane untouched:** `git hash-object` equals `git rev-parse HEAD:<f>` for both verifiers
(`d432387d…` C2, `d4240112…` C1). At seat start and at the diff step, `git status --short` listed only
the four untracked `.ufo/waves/round-70/` paths. After scratch deletion it also shows ` M`
`corpus/README.md`, `corpus/knowledge/skill-eval-artefacts-round70.md`, `corpus/lessons/round-70.md`
and `verifiers/verify_skill_checklist.py`. This seat wrote none of them: its only lane write is this
report, and every other edit was under `/tmp`. They are concurrent peer work. Every measurement here
reads committed bytes at `16b212a`/`7d51253` or sandbox commits, so those working-tree edits do not
affect it.

## Candidates found, not applied (with reason)

- **Cross-file duplication**: `EnvError`, the `main()` rev resolution (`rev-parse --verify --quiet
  <rev>^{commit}`), `--repo` default, `Repo.show`. The lane has no shared helper module (no
  `verifiers/_*.py`, no `*common*/*util*` module), and every counter is standalone, so extracting one
  would create a second convention. Rejected.
- **C1 `_r69_log_entry` runs 4× per check** (K69-2/3/6/7 → 8 `git show` subprocesses). Caching would
  add state for about 10 ms. Not applied.
- **C1 `_r69_log_entry` manual loops → `next(...)`**: restyling, not a deletion. Not applied.
- **C1 self-test `blob()` helper used once, `n, f = _run(w)` with `f` unused in the loop**: trivial,
  left alone.

## Tooling

- `vulture 2.16` — `uv tool install --force vulture` (the existing `~/.local/bin/vulture` symlink was
  dangling: `uv tool install` said it was installed, but the shell reported `command not found`).
  Reason: dead-code scan. No other installs; `pyflakes 4.0.3` was already present.
- Tool anomaly: the seat's file-read tool refused both 15–17 KB verifier files ("exceeds maximum
  allowed characters (100000)") even with `offset`/`limit`, so they were read with `cat -n` in the
  scratch clone.

## Checks for the main agent

If the diff is adopted: `python3 -B verifiers/check_skill_evals.py --self-test`,
`python3 -B verifiers/check_r69_routed_repairs.py --self-test`, both counters at `--rev <new tip>`,
and the no-harm battery from `plans/round-70.md`. Note that the frozen predicate sentences in the
docstrings are unchanged by this diff.

## Diff (unified, `orig` = tip `16b212a`)

```diff
--- orig/check_skill_evals.py
+++ new/check_skill_evals.py
@@ -38,7 +38,6 @@
 from pathlib import Path
 
 TOTAL = 8
-BASE = "7d51253f99906b8551b6a0a108761eedac00de74"
 ENTRY = "corpus/knowledge/skill-eval-artefacts-round70.md"
 SOURCES = "corpus/SOURCES.md"
 SKILL = "SKILL.md"
@@ -81,20 +80,23 @@
     def __init__(self, path: Path, rev: str):
         self.path, self.rev = path, rev
 
-    def show(self, path: str) -> str | None:
+    def raw(self, path: str) -> bytes | None:
         proc = subprocess.run(["git", "-C", str(self.path), "show", f"{self.rev}:{path}"],
                               capture_output=True)
-        return proc.stdout.decode("utf-8", "replace") if proc.returncode == 0 else None
+        return proc.stdout if proc.returncode == 0 else None
+
+    def show(self, path: str) -> str | None:
+        data = self.raw(path)
+        return None if data is None else data.decode("utf-8", "replace")
 
     def snapshot(self, sid: str) -> str:
         name, sha, _ = SNAPSHOTS[sid]
-        proc = subprocess.run(["git", "-C", str(self.path), "show", f"{self.rev}:{SNAPDIR}/{name}"],
-                              capture_output=True)
-        if proc.returncode != 0:
+        data = self.raw(f"{SNAPDIR}/{name}")
+        if data is None:
             raise EnvError(f"snapshot {name} not committed at {self.rev}")
-        if hashlib.sha256(proc.stdout).hexdigest() != sha:
+        if hashlib.sha256(data).hexdigest() != sha:
             raise EnvError(f"snapshot_tampered: {name}")
-        return proc.stdout.decode("utf-8", "replace")
+        return data.decode("utf-8", "replace")
 
 
 def _cells(line: str) -> list[str]:
@@ -122,7 +124,7 @@
     return out
 
 
-def check(repo, fetch=None) -> tuple[int, list[str], list[tuple[str, str, str]]]:
+def check(repo) -> tuple[int, list[str], list[tuple[str, str, str]]]:
     entry = repo.show(ENTRY)
     if entry is None:
         return 0, [f"entry {ENTRY} absent"], []
@@ -240,8 +242,8 @@
     return f"source: S209 S210 S211\nverified-at: x\nrecheck: 90d\n\n| id | fact | row | quote |\n|---|---|---|---|\n{rows}\n"
 
 
-def _source_row(sid: str, status: str = "mined", used: str = ENTRY) -> str:
-    return f"| {sid} | t | docs | A | s | a | t | {status} | 2026-10-25 | 90d | {used} |"
+def _source_row(sid: str) -> str:
+    return f"| {sid} | t | docs | A | s | a | t | mined | 2026-10-25 | 90d | {ENTRY} |"
 
 
 def _honest() -> dict:
@@ -254,13 +256,12 @@
     failures = 0
 
     def run(world):
-        return check(FakeRepo(world["files"], world["snaps"]))[0]
+        return check(FakeRepo(**world))[0]
 
-    n = run(_honest())
+    n, findings, _ = check(FakeRepo(**_honest()))
     if n != TOTAL:
         failures += 1
-        print(f"FAIL honest world: backed {n} of {TOTAL}; {check(FakeRepo(**_honest()))[1]}",
-              file=sys.stderr)
+        print(f"FAIL honest world: backed {n} of {TOTAL}; {findings}", file=sys.stderr)
     else:
         print(f"PASS honest world: backed {TOTAL} of {TOTAL}")
 
--- orig/check_r69_routed_repairs.py
+++ new/check_r69_routed_repairs.py
@@ -69,9 +69,9 @@
     f"{W69}/ScoutStaleLane.md": "6f4c23bad11a5aee7aa7ab255dc4e11d44bddd94",
 }
 R69_COUNTERS = {
-    "check_skill_precedence.py": r"skill precedence backed 5 of 5",
-    "check_r68_routed_repairs.py": r"r68 routed defects closed 8 of 8",
-    "check_province_core.py": r"province core rows 2 of 2",
+    "check_skill_precedence.py": "skill precedence backed 5 of 5",
+    "check_r68_routed_repairs.py": "r68 routed defects closed 8 of 8",
+    "check_province_core.py": "province core rows 2 of 2",
 }
 LABELS = ("trigger", "action", "outcome", "pointer")
 
@@ -158,20 +158,20 @@
     return [f"K69-1: annotation block lacks {miss}"] if miss else []
 
 
-def k2_offbranch(repo: Repo) -> list[str]:
+def _entry_tokens(repo: Repo, kid: str, tokens: tuple[str, ...]) -> list[str]:
     entry = _r69_log_entry(repo)
     if entry is None:
-        return ["K69-2: no appended `## Round 69` LOG.md entry"]
-    miss = [t for t in ("fast-forward", "orchestrator", *R69_COMMITS) if t not in entry]
-    return [f"K69-2: round-69 entry lacks {miss}"] if miss else []
+        return [f"{kid}: no appended `## Round 69` LOG.md entry"]
+    miss = [t for t in tokens if t not in entry]
+    return [f"{kid}: round-69 entry lacks {miss}"] if miss else []
 
 
+def k2_offbranch(repo: Repo) -> list[str]:
+    return _entry_tokens(repo, "K69-2", ("fast-forward", "orchestrator", *R69_COMMITS))
+
+
 def k3_attribution(repo: Repo) -> list[str]:
-    entry = _r69_log_entry(repo)
-    if entry is None:
-        return ["K69-3: no appended `## Round 69` LOG.md entry"]
-    miss = [t for t in ("4844216b", "9d9f181e", "probe", "0a1199a0") if t not in entry]
-    return [f"K69-3: round-69 entry lacks {miss}"] if miss else []
+    return _entry_tokens(repo, "K69-3", ("4844216b", "9d9f181e", "probe", "0a1199a0"))
 
 
 def k5_inherited(repo: Repo) -> list[str]:
@@ -192,16 +192,12 @@
     if entry is None:
         return ["K69-6: no appended `## Round 69` LOG.md entry"]
     low = entry.lower()
-    miss = [l for l in LABELS if f"{l}:" not in low and f"**{l}**" not in low and f"{l}**" not in low]
+    miss = [l for l in LABELS if f"{l}:" not in low and f"{l}**" not in low]
     return [f"K69-6: round-69 entry lacks labels {miss}"] if miss else []
 
 
 def k7_numeric(repo: Repo) -> list[str]:
-    entry = _r69_log_entry(repo)
-    if entry is None:
-        return ["K69-7: no appended `## Round 69` LOG.md entry"]
-    miss = [t for t in ("10 receipts", "23 landed", "1 dispositioned") if t not in entry]
-    return [f"K69-7: round-69 entry lacks {miss}"] if miss else []
+    return _entry_tokens(repo, "K69-7", ("10 receipts", "23 landed", "1 dispositioned"))
 
 
 def k8_receipt(repo: Repo) -> list[str]:
@@ -218,7 +214,7 @@
             out.append(f"K69-8: no `command:` line for {counter}")
             continue
         b = hit[0]
-        if not re.search(verdict, b):
+        if verdict not in b:
             out.append(f"K69-8: {counter} block lacks its verdict line")
         if not re.search(r"^exit=0\s*$", b, re.M):
             out.append(f"K69-8: {counter} block lacks exit=0")
@@ -270,7 +266,6 @@
     def __init__(self, files: dict[str, str], base: dict[str, str], blobs: dict[str, str],
                  gate_status: str | None):
         self.files, self.base, self.blobs, self.gate_status = files, base, blobs, gate_status
-        self.rev = "f" * 40
 
     def show(self, path, rev=None):
         return (self.base if rev == BASE else self.files).get(path)
@@ -298,7 +293,7 @@
     sc = base[SCORECARD] + ("**Round 69 axis annotations (append-only).** check_skill_precedence.py "
                             f"check_r68_routed_repairs.py check_province_core.py {R69_TIP} {R69_BASE}\n")
     receipt = f"measured-rev: {R69_TIP}\n" + "".join(
-        f"command: python3 -B verifiers/{c} --rev {R69_TIP}\n{v.replace(chr(92), '')}\nexit=0\n"
+        f"command: python3 -B verifiers/{c} --rev {R69_TIP}\n{v}\nexit=0\n"
         for c, v in R69_COUNTERS.items())
     lesson70 = ("# r70\n" + "\n".join(INHERITED) +
                 "\n- S201 anchor cell: `(13 words)` -> `(14 words)` (old -> new)\n")
```
