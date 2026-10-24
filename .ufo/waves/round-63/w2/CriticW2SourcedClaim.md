# CriticW2SourcedClaim

role: UFO-FSD critic (read-only production review)
item: Attack the round-63 sourced-claim requirement, S119 provenance, located quotes, used-by targets, and teaching scope.
revision: `cbbee56e9a3589b0b46736ad36f1b77701def80e`
axes: **freshness** (assigned); calibration is implicated by any claim that the provenance trio is complete. No round/admission judgment is made here.

## Counterexample and verdict on the committed bytes

**One fixable provenance defect.** `corpus/knowledge/compound-clause-citation-round63.md:1` cites S119, but the entry does **not** have the required opening provenance trio: `verified-at:` and `recheck:` are absent from the entire committed blob. Its `source:` line also omits S119's external URL and anchor. The second line is blank and the third is `## What it is`, not the missing fields. The assignment's provenance-trio requirement is therefore not met. This is also the explicit rule at canonical `/home/vgpnk/Projects/kimi-shokunin/skills/shokunin/protocol/CORPUS.md:18-20,162-165`; the adjacent r62 entry already uses all three fields (`corpus/knowledge/erratum-absorption-round62.md:1-3`). Provenance buried later in the prose does not make the entry visible to a field-based freshness sweep.

**The other scoped attacks found no defect:**

- Lesson Gate quotes are **16 and 7 words**, independently counted by Python split and actual `wc -w`. They are exact raw-byte substrings of committed `S119.page` at **170 and 172**, respectively. The first quote correctly preserves the two spaces after `notice`.
- S119 is `mined`; both used-by paths are committed blobs at the pinned revision and both cite S119.
- The snapshot is 22,722 bytes, SHA-256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2`, matching the lesson and source row.
- Strongest semantic counterexample: snapshot **171** explicitly recommends posting a **new article version**. Thus the source would not justify a literal append-only-files mandate. The committed S119 teaches cell already says **“the page does not mandate literal append-only files”**, and the entry's correction-practice paragraph expressly separates the source's direction from the lane's stricter LOG discipline. That bound survives the counterexample; do not remove it or attribute the G9 mechanism to S119.
- **No supporting citation tested here fails to resolve.** The ICMJE URL returns HTTP 200 on this fresh reopening. The two used-by files, full snapshot path, source-fetch/reviewer receipts, and all four named verifier paths in the entry resolve at the committed revision. The entry's `S119.page:170,172` shorthand resolves through S119's explicit full snapshot path. The COPE/NISO failures in Gate are expressly rejected candidates, not supporting citations; their reported failures were not rerun.

This is metadata repair, not an unavoidable axis trade or grounds for this critic to pronounce a round verdict. Census rendering/search-log issues are outside this item and were left to `CriticW2Census`.

## Attack commands and verbatim output

All blob inspection used `git show <pinned-rev>:<path>` / `git cat-file`, not mutable lane copies. The executed probe was:

```sh
python3 -B /tmp/kotoba-r63-CriticW2SourcedClaim-probe.py
```

Verbatim stdout (exit 0; this probe reports findings rather than acting as an admission gate):

```text
revision=cbbee56e9a3589b0b46736ad36f1b77701def80e
read_surface=git show <revision>:<path>; no working-tree reads
entry=corpus/knowledge/compound-clause-citation-round63.md
entry.source_cites_S119=True
entry.source_has_URL=False
entry.source_has_snapshot_anchor=False
entry.source: lines=1
entry.verified-at: lines=ABSENT
entry.recheck: lines=ABSENT
entry.opening_trio=False
S119.row_line=131; cells=11; status=mined; tier=A
S119.URL=https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
S119.teaches=A journal publishes a correction notice "as soon as possible detailing changes from and citing the original publication" and "archive all prior versions of the article" — transparent correction with preserved history, not a silent rewrite of the record; the page does not mandate literal append-only files
S119.explicit_append_only_bound=True
S119.used_by=corpus/knowledge/compound-clause-citation-round63.md; object_type=blob; cites_S119=True
S119.used_by=corpus/lessons/round-63.md; object_type=blob; cites_S119=True
Gate.quote:170; split_words=16; wc_words=16; le25=True; raw_literal_at_line=True
Gate.exact_quote="publish a correction notice  as soon as possible detailing changes from and citing the original publication"
Gate.quote:172; split_words=7; wc_words=7; le25=True; raw_literal_at_line=True
Gate.exact_quote="archive all prior versions of the article"
Gate.located_quote_count=2
snapshot.bytes=22722; sha256=d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2
snapshot.digest_in_Gate=True; digest_in_S119_row=True
snapshot:171=The journal also should post a new article version with details of the changes from the original version and the date(s) on which the changes were made.
entry.citation=verifiers/check_erratum_absorption.py; object_type=blob
entry.citation=verifiers/check_r63_routed_repairs.py; object_type=blob
entry.citation=verifiers/check_scoped_rules_v31.py; object_type=blob
entry.citation=verifiers/check_scoped_rules_v32.py; object_type=blob
source_chain.citation=.ufo/waves/round-63/w1/ExecSourceS119.md; object_type=blob
source_chain.citation=.ufo/waves/round-63/w1/RevSourceQuote.md; object_type=blob
source_chain.citation=.ufo/waves/round-63/snapshots/S119.page; object_type=blob
finding=FIXABLE: provenance opening lacks verified-at/recheck and source URL/anchor
finding=NO scoped missing target: S119 row, used-by, snapshot, source receipts and named verifier paths resolve
```

The exact executed probe is embedded here so its temporary filename is not a required evidence dependency:

```python
import hashlib
import json
import re
import subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
REV = "cbbee56e9a3589b0b46736ad36f1b77701def80e"
ENTRY = "corpus/knowledge/compound-clause-citation-round63.md"
LESSON = "corpus/lessons/round-63.md"
SOURCES = "corpus/SOURCES.md"
SNAPSHOT = ".ufo/waves/round-63/snapshots/S119.page"


def git(*args):
    return subprocess.run(
        ["git", "-C", LANE, *args], capture_output=True, check=True
    ).stdout


def text(path):
    return git("show", f"{REV}:{path}").decode("utf-8")


entry = text(ENTRY)
lesson = text(LESSON)
sources = text(SOURCES)
snapshot = git("show", f"{REV}:{SNAPSHOT}")
print(f"revision={REV}")
print("read_surface=git show <revision>:<path>; no working-tree reads")
print(f"entry={ENTRY}")
source_line = entry.splitlines()[0]
print("entry.source_cites_S119=" + str(bool(re.match(r"^source:.*\bS119\b", source_line))))
print("entry.source_has_URL=" + str("https://www.icmje.org/" in source_line))
print("entry.source_has_snapshot_anchor=" + str(SNAPSHOT + ":170" in source_line))
for key in ("source:", "verified-at:", "recheck:"):
    locations = [str(n) for n, line in enumerate(entry.splitlines(), 1) if line.startswith(key)]
    print(f"entry.{key} lines=" + (",".join(locations) or "ABSENT"))
print("entry.opening_trio=" + str(
    all(line.startswith(key) for line, key in zip(entry.splitlines()[:3],
        ("source:", "verified-at:", "recheck:")))
))
row_number, row = next((n, line) for n, line in enumerate(sources.splitlines(), 1)
    if re.match(r"^\|\s*S119\s*\|", line))
header = next(line for line in sources.splitlines() if line.startswith("| id |"))
field_names = [cell.strip() for cell in header.split("|")[1:-1]]
row_values = [cell.strip() for cell in row.split("|")[1:-1]]
source = dict(zip(field_names, row_values))
print(f"S119.row_line={row_number}; cells={len(row_values)}; status={source['status']}; tier={source['tier']}")
url = re.search(r"https://[^ ]+", source["source"])[0]
print("S119.URL=" + url)
print("S119.teaches=" + source["teaches"])
print("S119.explicit_append_only_bound=" + str("the page does not mandate literal append-only files" in source["teaches"]))
for path in (p.strip() for p in source["used-by"].split(",")):
    kind = git("cat-file", "-t", f"{REV}:{path}").decode().strip()
    cited = bool(re.search(r"\bS119\b", text(path)))
    print(f"S119.used_by={path}; object_type={kind}; cites_S119={cited}")

lines = snapshot.splitlines()
gate = lesson.split("## Gate\n", 1)[1].split("\n## ", 1)[0]
quotes = []
for lesson_line in gate.splitlines():
    match = re.match(r"^\s*- `:(\d+)` — “([^”]+)”", lesson_line)
    if match:
        location, quote = int(match[1]), match[2]
        words = len(quote.split())
        wc = subprocess.run(["wc", "-w"], input=quote.encode(), capture_output=True, check=True)
        literal = quote.encode() in lines[location - 1]
        quotes.append((location, words, literal))
        print(f"Gate.quote:{location}; split_words={words}; wc_words={wc.stdout.decode().strip()}; le25={words <= 25}; raw_literal_at_line={literal}")
        print("Gate.exact_quote=" + json.dumps(quote, ensure_ascii=False))
print(f"Gate.located_quote_count={len(quotes)}")
digest = hashlib.sha256(snapshot).hexdigest()
print(f"snapshot.bytes={len(snapshot)}; sha256={digest}")
print(f"snapshot.digest_in_Gate={digest in gate}; digest_in_S119_row={digest in row}")
print("snapshot:171=" + re.sub(r"<[^>]+>", "", lines[170].decode()).strip())
for path in sorted(set(re.findall(r"`(verifiers/[^`]+\.py)`", entry))):
    print(f"entry.citation={path}; object_type=" + git("cat-file", "-t", f"{REV}:{path}").decode().strip())
for path in (".ufo/waves/round-63/w1/ExecSourceS119.md",
             ".ufo/waves/round-63/w1/RevSourceQuote.md", SNAPSHOT):
    print(f"source_chain.citation={path}; object_type=" + git("cat-file", "-t", f"{REV}:{path}").decode().strip())
print("finding=FIXABLE: provenance opening lacks verified-at/recheck and source URL/anchor")
print("finding=NO scoped missing target: S119 row, used-by, snapshot, source receipts and named verifier paths resolve")
```

Independent live reopening (exit 0):

```sh
curl --silent --show-error --location --output /tmp/kotoba-r63-CriticW2SourcedClaim-live.page --write-out 'url_effective=%{url_effective}\nhttp_code=%{http_code}\ncontent_type=%{content_type}\nsize_download=%{size_download}\n' https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
```

```text
url_effective=https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
http_code=200
content_type=text/html
size_download=22722
```

```sh
sha256sum /tmp/kotoba-r63-CriticW2SourcedClaim-live.page
```

```text
f600c500da83a933a8539f3a3e600c0efd0bbd19344df244d92c2eedfcb737ce  /tmp/kotoba-r63-CriticW2SourcedClaim-live.page
```

The different live digest is **not** a snapshot failure: the row explicitly disclaims cross-fetch byte identity. I also reopened the fresh HTML at lines 168–174 and the primary URL with the static reader; the correction/version/archive statements remain present. Raw literal assertions above are against the **committed** bytes, as required, not normalized reader output.

## Smallest safe correction — exact proposed text

L1 should replace only the entry's first line with the following three opening lines, leaving the body and S119 scope bound unchanged:

```text
source: S119 (correction practice; https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html; § A. Corrections and Version Control, snapshot `.ufo/waves/round-63/snapshots/S119.page:170-174`); the depth half rests on `verifiers/check_erratum_absorption.py` (r62 frozen catalogue), `verifiers/check_scoped_rules_v31.py` (r62 successor) and `verifiers/check_scoped_rules_v32.py` (r63 successor) — not on S119
verified-at: 2026-10-23 — S119's located quotes rechecked against the committed snapshot at `cbbee56e9a3589b0b46736ad36f1b77701def80e`
recheck: Re-open S119's URL and compare its correction/version-preservation statements with `.ufo/waves/round-63/snapshots/S119.page:170-174`; run `python3 -B verifiers/check_scoped_rules_v32.py --self-test` and `python3 -B verifiers/check_r63_routed_repairs.py --rev <reviewed-rev>` for the separate local mechanisms.
```

No S119 row rewrite is needed for the semantic attack. This correction restores discoverable freshness metadata without changing the cited source's authority, the G9 claim, or the round counters. L1 owns any integration and post-integration checks; this seat did not execute the production verifiers or an admission runtime.

## Scope and tooling

Only this report was written in the lane; probes and the fresh download were confined to `/tmp`. No production file, fleet/sibling file, lane Git index, or jj state was changed. No tools were installed or updated; the host-wide pacman pause was respected. Checked items and outcomes above are observations, not projected post-correction results.

Report: .ufo/waves/round-63/w2/CriticW2SourcedClaim.md
