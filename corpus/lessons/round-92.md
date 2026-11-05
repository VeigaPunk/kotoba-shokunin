# Round 92 — kotoba (Linux host, omp 18.15.0): lesson

Author: **ScribeCorpusR92** (scribe seat). This file is the round-92 **scaffold**: the Gate record,
the Mistakes row and the Considerthese entry below are written; **the L1 completes the settlement**
(the seat record, the claim verdicts, the wave disposition and the final numbers).
Round: 92, plan `plans/round-92.md` (frozen at `e073723ae667b64e534f8621bddb83ad12ad0e71`), base
`e073723ae667b64e534f8621bddb83ad12ad0e71`.
Pre-data controls: `plans/round-92-controls.md`, executed before any candidate score — receipt
`.ufo/waves/round-92/receipts/freeze-gate-r92.txt` (`freeze gate: 6 control(s) held — freeze may
proceed`, exit 0).

## Gate

Candidates considered, with the decision and the reason:

- **S265** — Python documentation, `subprocess`
  (`https://docs.python.org/3/library/subprocess.html`). **Admitted** as tier A, as a
  *correction row* that supersedes S263: the page is unchanged in substance, and the only defect
  the round-91 spot-check routed (its defect 4) is an anchor line in the S263 row, not a wrong
  claim. Access date 2026-11-05; HTTP 200; 208648 B — byte-identical to the round-91 reading, with
  the same page footer "Last updated on Nov 05, 2026 (12:47 UTC)." at HTML line 2037. Located
  quote (§ `subprocess.run`, HTML lines 289-291, 25 words): "If the timeout expires, the child
  process will be killed and waited for. The TimeoutExpired exception will be re-raised after the
  child process has terminated." Contrast quote (§ `subprocess.Popen.communicate`, HTML line 1071
  continuing to 1072, 10 words): "The child process is not killed if the timeout expires".
  - **Why a new row and not an edit to S263** — the SOURCES contract is append-only: a correction
    lands as a new row whose `teaches` cell opens `supersedes S263 — `, naming the corrected
    anchor; the superseded row keeps its own bytes. The corrected anchors are the `Popen.communicate`
    entry dt at **HTML line 1051** (signature line 1052) and the contrast quote at **HTML line
    1071**; S263's cited line 1042 is a `versionchanged` note belonging to the preceding
    `Popen.wait` entry, not the contrast quote. The `subprocess.run` entry dt (270) and its timeout
    paragraph (288-294, quoted sentence at 289-291) are unchanged. The kill-and-wait contract the
    cap calibration rests on is therefore unaffected — only the anchor line was wrong.
- **S266** — Python documentation, built-in exceptions
  (`https://docs.python.org/3/library/exceptions.html`, requested; the path answers **301** and
  lands on `https://docs.python.org/3/builtins/exceptions.html`). **Admitted** as tier A, scoped to
  *which exception the Python runtime raises when a path component is not a directory* — the
  grounding for the freeze gate's fail-closed work-root rung. Access date 2026-11-05; final HTTP
  200; 145885 B; page title "Built-in Exceptions — Python 3.15.2 documentation". The
  `NotADirectoryError` definition-list entry is at HTML line 1118 (signature line 1119, body
  1120-1124). Located quote (HTML lines 1120-1121, 17 words): "Raised when a directory operation
  (such as os.listdir()) is requested on something which is not a directory." The POSIX
  path-component clause is quotable in the same budget (HTML lines 1122-1123, 22 words): "it may
  also be raised if an operation attempts to open or traverse a non-directory file as if it were a
  directory." The errno correspondence is `ENOTDIR` (line 1124); the exception-hierarchy tree places
  the entry under `OSError` (HTML line 1440) at HTML line 1452, inside the tree block that opens at
  line 1416.
  - **Why the exception class and not a general filesystem row** — the round's C2(b) rung 1 is the
    `--work` argument resolving under a regular file. What the gate must translate is one named
    environment exception, `NotADirectoryError` (an `OSError` subclass), so the row is scoped to
    that class and to the path-component case the POSIX clause states, not to path handling in
    general. The page names exactly one `os` function for this exception — `os.listdir()` (line
    1120); the adjacent `os.remove()` mention at line 1112 belongs to `IsADirectoryError` and is
    **not** attributed here.

**No candidate was rejected this round.** Both candidates are tier-A official documentation whose
located quotes were re-verified against the bytes the scout fetched; no row carries a `rejected`
status, and no flip condition is open.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **190** before this round (receipt `.ufo/waves/round-92/census-before.txt`,
validate rc 0 with the 33 pre-existing W04 duplicate-URL warnings) and **192** after — the two
rows appended above (S265, S266), no row dropped, consistent with the plan's § Frontier
expectation of 190 → 192. Validation:
`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
--today 2026-11-05` → exit 0, the same 33 pre-existing W04 warnings and no E-code.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `vacuous` (**the L1-confirmed row**) — a frozen pre-data control reads MET on the shortcut it names: `ctl-c2-capline-only` (cap raised to 360, no `INSTRUMENT_PINS` admission) prints `C2-PREDICATE-MET`, exit 0; the control reads only the working-tree cap, so it never refuses the shortcut world it declares | `.ufo/waves/round-91/w1/CriticClaims.md` § Controls (the shortcut-check table names the same control as a **control defect**: it reports MET for the shortcut it is declared to refuse) and `verifiers/fixtures/round-91/ctl-c2-capline-only.sh`; the round-92 red-before receipt `.ufo/waves/round-92/receipts/redbefore-ctl-c2.txt` re-observes the defect at this round's base bytes | Q37's gap: a control need not refuse its own shortcut — Q37 requires the cheapest real-input shortcut to be built and run under the frozen predicate, but not that the control *refuses* the failing conjunct of that shortcut, so the control was satisfied in form while reading MET on the shortcut it names | `plans/round-92.md` C1 — the shortcut world is committed and the public gates read it, so the control refuses its own shortcut instead of restating a threshold; the row is confirmed by the L1 in the round-92 plan (the same routed defect the plan carries as C1's red-before) |

## Status changes

- **S263 — corrected by S265** (new row, `mined`, opened 2026-11-05, recheck `180d`). The
  correction is the anchor line only: S263 cites the `Popen.communicate` contrast quote at HTML
  line 1042; on today's byte-identical page (HTTP 200, 208648 B, same footer timestamp at line
  2037) that line is a `versionchanged` note of the preceding `Popen.wait` entry, while the
  `Popen.communicate` entry dt is at line 1051 and the contrast quote at line 1071. The quote text,
  its section, and the teach are unchanged, so the kill-and-wait contract the cap calibration
  rests on stands; only the anchor line was wrong (the round-91 spot-check's routed defect 4).
  S263's own row bytes are **not** rewritten — the correction lands as the appended row, per the
  SOURCES contract's append-only rule for a cited token.
- **S266 — new row**, `mined` at opening (2026-11-05), tier A, kind `docs`, recheck `180d`, used-by
  `corpus/lessons/round-92.md`. No other row's `status`, `recheck` or `used-by` cell changed.

## Sources

- **S265** — Python documentation, `subprocess`; URL
  `https://docs.python.org/3/library/subprocess.html`; access 2026-11-05; HTTP 200; 208648 B
  (byte-identical to the round-91 reading); page footer "Last updated on Nov 05, 2026 (12:47 UTC)."
  at HTML line 2037; located quote at HTML lines 289-291 (25 words) and the contrast quote at HTML
  line 1071 (10 words), the `Popen.communicate` entry dt at HTML line 1051, the `subprocess.run`
  entry dt at HTML line 270 and its timeout paragraph at HTML lines 288-294. Tier A scoped; a
  correction row superseding S263 (anchor repair only). Status `mined`; used-by
  `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md`.
- **S266** — Python documentation, built-in exceptions; URL requested
  `https://docs.python.org/3/library/exceptions.html` (HTTP 301), effective
  `https://docs.python.org/3/builtins/exceptions.html`; access 2026-11-05; final HTTP 200; 145885 B;
  page title "Built-in Exceptions — Python 3.15.2 documentation"; located quote at HTML lines
  1120-1121 (17 words) and the POSIX path-component clause at HTML lines 1122-1123 (22 words), the
  `NotADirectoryError` entry dt at HTML line 1118, the exception-hierarchy tree at HTML lines 1440
  and 1452, and the `errno.ENOTDIR` correspondence at HTML line 1124. Tier A scoped to the
  non-directory path-component exception class. Status `mined`; used-by
  `corpus/lessons/round-92.md`.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **No proposal implemented this round.** Both claims are instrument-deepening with frozen
  predicates, so no proposal of this file is inside either claim's scope, and no proposal is
  implemented outside them.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried: it needs a SKILL.md description rewrite, and the 600-line budget cannot absorb one —
  `SKILL.md` is already 600 lines / 92 672 B at the freeze (receipt
  `.ufo/waves/round-92/receipts/base-skill-size.txt`), so a rewrite of the frontmatter description
  has to be paid for by lines saved elsewhere, which is a claim-adjacent edit this round's frozen
  predicates do not admit.
- **Proposals 1, 4 and 5** (a byte/line ceiling; "do not close a round before its falsify wave
  runs"; a per-round evidence budget) are carried unchanged from the previous rounds; proposals 1
  and 5 are already mined as criteria Q78 and Q82 and are not re-mined here.

## Settlement (L1 — placeholder)

**Placeholder — the L1 completes this section at settlement.** The seat record for wave `r92-w1`,
the claim verdicts for C1 and C2 (which this seat does **not** write: no claim verdict is recorded
anywhere in this file), the wave disposition, the landing revision and the final numbers are the
L1's to settle and land.
