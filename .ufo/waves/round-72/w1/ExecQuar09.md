# ExecQuar09 — Quarantine hand-check, register slice row 9 of 13 (round 72, wave 1)

## Verdict: `unverifiable-class` (prose class cell — NOT fabrication)

The register row contains no quoted span to verify; the cell in the quote column is prose:
"the cited source could not be fetched, so no quote was checked". Per the seat assignment, a
prose class cell such as this makes the row `unverifiable`, which is not fabrication.
The cited source is nonetheless fetchable today (see §3), so the plan's claim that it "could not
be fetched" is stale/unobserved as of this check.

---

## 1. Register row (verbatim, line 9 of quarantine-slice-full.txt)

```
| `kotoba` | round10 | S237` | the cited source could not be fetched, so no quote was checked | https://skills.sh/audits |
```

- Campaign id: `S237` (round10, lane kotoba).
- Quoted span: none — the cell between the S237 badge and the URL is prose, not a backticked quote.
- Fetch URL: `https://skills.sh/audits`.

## 2. Staged row lookup (SOURCES.append.md, by host+path `skills.sh/audits`)

Staged id: **S317** — `grep -n "skills\.sh" SOURCES.append.md` → line 121:

```
121:| S317 | skills.sh — Security Audits — https://skills.sh/audits | docs | B | ... | the introductory line above the per-skill table | the registry publishes per-skill audit verdicts from three named third-party auditors, so the audit layer of this ecosystem is public rather than implied | mined | 2026-10-24 | 90d — re-fetch the audits page and confirm the auditor list is unchanged | corpus/knowledge/installer-security-guidance-round10.md |
```

(Staged anchor for S317: "the introductory line above the per-skill table".)

## 3. Fetch record (independent, not accepting plan's claim)

Command: `curl -sSL -A 'Mozilla/5.0' -o /tmp/k72q9-audits.html -w '...' 'https://skills.sh/audits'`

- HTTP status: **308** on `https://skills.sh/audits` (redirect), then **200** at final URL `https://www.skills.sh/audits`.
- Final URL: `https://www.skills.sh/audits` (host `skills.sh` → `www.skills.sh`).
- Byte size: 484,518; content-type `text/html; charset=utf-8`.
- sha256 of fetched bytes: `5ec72d107324b308b4b3ccb2172d29b5256d8c0a56972b9628d12ef028cb9ee9`.
- Access date: 2026-10-25T21:37Z (UTC).
- `.md` export attempt: `https://skills.sh/audits.md` → **404**, final `https://www.skills.sh/audits.md`, 21,096 bytes (404 page). No web.archive redirect involved, so no archive form was needed.

Page content confirms the audits page exists and carries the per-skill audit table
(text extraction of the fetched HTML, first lines):
`Security Audits ... Combined security audit results from Gen Agent Trust Hub, Socket, and Snyk. # Skill Gen Socket Snyk 1 find-skills vercel-labs/skills Safe 0 alerts Med Risk ...`
This matches staged S317's anchor location ("introductory line above the per-skill table"),
but no quote in this register row is pinned to it.

## 4. Findings

1. Row 9 is `unverifiable-class`: no quote was ever captured; the cell is prose
   ("could not be fetched, so no quote was checked"). Not fabrication.
2. The cited source is reachable now (HTTP 200, 484,518 bytes, sha256
   `5ec72d10...`), so the plan's "could not be fetched" statement is not the current
   observed state. If the lane wants S237 converted to a verified quote row, the
   fetch in §3 and the S317 anchor are available as ground truth.
3. The URL is not a web.archive redirect; the `.md` export 404s. No quote can be
   located because none exists in the register row.

## 5. Scratch cleanup

Fetched scratch files removed on completion: `/tmp/k72q9-audits.html`,
`/tmp/k72q9-audits.md`, `/tmp/k72q9-audits.txt`.

---

Report: .ufo/waves/round-72/w1/ExecQuar09.md
