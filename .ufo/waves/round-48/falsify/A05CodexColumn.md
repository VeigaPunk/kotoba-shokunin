# A05CodexColumn: round-48 falsify of the Codex (S021) column, footnote (a), S021 row, and S013 supersession

Seat: KotobaR48.A05CodexColumn (leaf, no delegation). Lane: kotoba-shokunin, master 84b9c9ba89559b51a72c83c2b9605b184df4ae9e. Judged on: freshness.
Scratch copies: /fast/scratch/hyaku/kotoba-r48-a2/seats2/A05CodexColumn/. Lane writes: this file only.

## Verdict

1. Does S021 correctly supersede S013? CONFIRMED, with MINOR defects in S021's own cells (F1, F2).
   Contract rule 2 is met. S021's teaches open "supersedes S013 —". The S013 row is byte-unchanged (E5). Both rows name the same canonical URL. Every S013 fact is in S021, and the defects the seat recorded against S013 are fixed: anchor, revision token, "gates" wording, and units.
2. Footnote (a): CONFIRMED. The grep reproduces (no output, exit 1). DEFECT (MINOR): its search omits the terms behind 2 of 10 Codex cells (F3), and it leaves out the shipped parser's name-optional fallback (F4).
3. S021 quote md:37-39, override md:43-44, implicit-invocation md:98-99: CONFIRMED verbatim. DEFECT (MINOR, F2): "may omit skills" is cited at md:37-40 but sits on md:41.
4. Freshness of the S021 pin: CONFIRMED. Markdown sha256 ed6e324f… (11,035 B, 232 lines), re-observed at 08:51:53Z and 08:55:20Z. The HTML page has moved; the markdown has not (F8).

Totals: 0 CRITICAL, 0 MAJOR, 7 MINOR (F1-F7), 1 INFO (F8), 1 residual (R1), 1 record note (R2).

## Findings

F1 MINOR. S021 drops the per-skill implicit-invocation switch.
- SOURCES.md:34 (S021) cites "implicit-invocation bullet md:98-99" and says only "keys on the description". Its scope cell names implicit invocation.
- The page documents the switch at md:207 and md:218: "allow_implicit_invocation (default: true): When false, Codex won't implicitly invoke the skill based on user prompt; explicit $skill invocation still works." (20 words; accessed 2026-10-22T08:51:53Z.)
- The seat's corrected anchor (.ufo/waves/round-48/build/FrSourceDefects.md:78-80) included md:218. The landed row does not. Round-47's candidate (SrcNewCodexSkills.md:40) cited "§ Optional metadata policy.allow_implicit_invocation", and that anchor was lost at landing.
- Fix: add md:207-218 to the anchor and "per-skill agents/openai.yaml policy switch, default on" to teaches.

F2 MINOR. Off-by-one citation.
- `grep -n 'may omit' build-skills.md` gives `41:sets, Codex may omit some skills from the initial list and show a warning.` S021 cites md:37-40. The range is one line short. The error comes from FrSourceDefects.md:78.
- Fix: cite md:37-41.

F3 MINOR. A Q14 gap in the Codex column.
- The entry intro promises that every "not stated" cell names the search that found nothing (Q14; QUALITY.md:25 says "the search that produced the absence"). All 10 Codex cells cite "(a)".
- Footnote (a)'s pattern covers 8 of the 10 terms. It does not cover "name equals directory" (no director, folder or match term) or "unknown top-level fields" (no unknown, unexpected, field or metadata term).
- Substance holds on my sweep. `grep -niE 'director|folder|match|unknown|unexpected|unrecogni|field|metadata|extra|additional' build-skills.md` shows only a skill-folder description (md:48, md:121), "matches the skill description" (md:99, md:103), "context window is unknown" (md:39), and the Optional metadata section (md:193-195), which is not SKILL.md frontmatter. Directory absence is also covered by C2CodexOpencodeDocs.md:11-13 ("must match" 0, "directory name" 0). No recorded search covers unknown fields.
- Fix: widen footnote (a), or cite the sweep for each cell.

F4 MINOR. Footnote (a) omits the one place the shipped Codex parser departs from the docs on a name rule.
- Page md:48: "The SKILL.md file must include name and description."
- Tag-pinned parser, rust-v0.163.0, codex-rs/skills/src/parser.rs (7,250 B, sha256 f3532df1…, fetched 2026-10-22T08:56Z): lines 68-69 `.filter(|value| !value.is_empty()).unwrap_or_else(default_name)`, so name is optional. Line 82 applies MAX_NAME_LEN = 64. Lines 83-84 reject an empty description. The seat reports the fallback is the parent directory name (host.rs:396). I did not re-read host.rs.
- Footnote (a) says the Codex CLI parser "has its own limits (64-character name, catalog descriptions truncated at 1,024)" and that the page "documents only that name and description are required". It does not say the shipped parser never requires name.
- Fix: state the name-optional fallback as a documented-versus-shipped divergence.

F5 MINOR. No executable recheck covers the Codex authority.
- Entry header line 3 (`recheck:`) covers the spec only. C2RecheckCommand.md:69-73 lists five commands: spec, skills-ref, packager at dbd4588, packager at main, and best-practices. A grep for codex, chatgpt or build-skills on that file finds nothing. S021's only recheck is the "90d" cadence.
- The entry's Limits section says the recheck commands "fail closed … when the rule text moves". That holds for five sources, not for S021, the one source whose HTML changed inside this round.
- Suggested fail-closed checks: `curl -fsSL https://learn.chatgpt.com/docs/build-skills.md | sha256sum` expects ed6e324f…; footnote (a)'s grep expects no output and exit 1.

F6 MINOR. Footnote (a) cites a source that has no registry row.
- The Codex CLI tag source (rust-v0.163.0) appears only in footnote (a). The entry's source header lists S018, S017, S019, S012, S021 and S020. Footnote (a) says "not tabled here because no source row pins that code."
- The SOURCES.md header says "A row exists only for a source the row's author opened this round." The seat did open this source.
- The Limits section says the entry "maps stated and executed validation rules only". Codex CLI rules were read in source, so they are neither stated nor executed.
- Fix: register a row, or narrow the Limits sentence.

F7 MINOR. The Codex CLI identity is pinned by version string, not by bytes.
- C2CodexOpencodeDocs.md:17 says "tag rust-v0.163.0 = installed codex-cli 0.163.0". The entry's S015 row says "A substrate pin is the binary's sha256, not its version string or path."
- Bytes verified now (E8): the installed native binary at `.../@openai/codex/node_modules/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex` has sha256 399ff69c431c066e40de318fba45c2b07f45a76b19939d247ee4828fc70c4215. The npm tarball openai-codex-0.163.0-linux-x64.tgz member `package/vendor/x86_64-unknown-linux-musl/bin/codex` has the same hash.
- The tag-to-bytes link is still by name only.
- Fix: record the binary hash in footnote (a).

F8 INFO. The HTML changed, and S021 records none of it.
- HEAD 2026-10-22T08:52:20Z: last-modified Thu, 22 Oct 2026 04:05:41 GMT; etag "05515a538c5ed12b2b141913bbefb301". Round 47 recorded ETag W/"ffc66e554470ca914642d4df868b6dc7" (SrcNewCodexSkills.md:21).
- Decoded HTML is 417,112 B in both rounds, but its sha256 differs: d738d30986a5f6ccd52e6b8d4fae5c5a6cb1060a76719b2050197fad35fc009c today (08:54:07Z and 08:55:20Z, identical), against 78abf99589567f6d56bbd6eebcaf251f5de38eab23c4d26d68e40d598d919e81 in round 47. The HTML bytes changed, not just the headers. S021 says only "HTML Last-Modified moved". The pinned markdown is unaffected.

R1 residual (census and contract, not an S021 defect). The supersession link is not checked by any tool.
- scripts/sources-census.sh: W04 (lines 644-645) fires for S018, S019 and S021 (same URL, different scope text). E04 (lines 646-648) exempts a `supersedes` marker only on the same-scope path. No code checks that the named id exists or shares the URL. So S021 to S013 is verified only by reading.
- Status: the contract (lines 36-37) defines queued as "opened, worth mining" and mined as "cited by ≥1 path in used-by". The enum has no superseded value (E07). S013 and S010 both stay queued, and census counts status.queued 8 with them included. S013's 90d recheck comes due 2027-01-19, one day before S021's.
- Contract rule 2 (lines 49-51) allows in-place changes only to status, recheck and used-by, each logged old to new. The round-48 lesson chose no change (lesson line 26). That choice is defensible. Route the superseded-state question to the contract owner.

R2 record note. Round-47 records give the markdown as 3,970 B (SrcNewCodexSkills.json:41 and :73). 3,970 is the compressed transfer size. The decoded size is 11,035 B (W2S013Reopen.md:83-96). S021's 11,035 B is correct. Round-47 records are append-only, so no S021 change is needed.

## Evidence

E1 Footnote (a): `grep -niE 'reserved|third person|xml|angle|500 lines|1024|1,024|64 char|lowercase|hyphen|consecutive' build-skills.md` gives no output, then exit=1. `grep -cniE` gives 0, exit 1.
E2 Pin: `sha256sum build-skills.md` gives ed6e324f747d47ad…919d5; `wc -c -l` gives 11035 B and 232 lines (08:51:53Z). A second fetch at 08:55:20Z gives the same hash and size.
E3 Line pins (`grep -n`): 37-39 quote; 41 "may omit"; 43-44 override; 48 must-include sentence; 91 heading; 98-99 implicit bullet; 101 "depends on description"; 193 Optional metadata; 207 and 218 allow_implicit_invocation.
E4 Located quotes, all from 2026-10-22T08:51:53Z: md:37-39, "By default, this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown." (22 words). md:43-44, "Use skills.max_context_tokens to set a different budget, up to 10,000 tokens." (11 words). md:98-99, "Implicit invocation: ChatGPT or Codex can choose a skill when your task matches the skill description." (16 words).
E5 Registry: `git -C kotoba-shokunin diff 75f671b…84b9c9b -- corpus/SOURCES.md` gives 6 insertions and 0 deletions, exit 0. Read-only.
E6 Census (read-only, stdout only): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` gives W04 for S018, S019 and S021, then `ok`, exit 0. `census` gives rows 21, mined 12, queued 8, rejected 1, exit 0.
E7 Live HTML: HEAD gives HTTP/2 200 (08:52:20Z). developers.openai.com/codex/skills gives 308 to learn.chatgpt.com/docs/build-skills.
E8 Codex CLI: `codex --version` gives codex-cli 0.163.0, exit 0. `npm view @openai/codex version` gives 0.163.0 (latest), exit 0 (08:55Z). `npm pack @openai/codex@0.163.0-linux-x64` and the sha256 match described in F7.
E9 Tag source (raw.githubusercontent.com, rust-v0.163.0, 08:56Z): parser.rs sha256 f3532df1… (7,250 B); render.rs sha256 d8ed87dc… (36,536 B). render.rs:19 default character budget 8_000; :20 configured token ceiling 10_000, which matches the page's override cap; :22 percent 2; :23 catalog description cap 1_024; :24 suffix "...".
E10 Contract: .ufo/waves/kaika/SOURCES-CONTRACT-v1.md, lines 36-37 and 49-51, read via search.

## Verification gaps (not passes)
- The config reference linked at md:43 (the skills.max_context_tokens key name) was not opened.
- The fetch time 2026-10-22T08:13:33Z is seat-attested (FrSourceDefects.md:108-109). I could not re-observe it. Content identity is re-observed at two later times.
- host.rs:396 was not re-read. The fallback at parser.rs:68-69 was.
- The GitHub release date (2026-10-15) is seat-attested only.
- verify_skill_checklist.py and the lane fixture runs were not run (not assigned).

## Tooling and access
- Installed or upgraded: none. Used curl, sha256sum, tar, the existing npm (fnm node v24.21.0) for `npm view` and `npm pack` (downloads only, nothing executed), and the lane's read-only census script.
- One pack name was wrong (404 for @openai/codex-linux-x64@0.163.0). The alias @openai/codex@0.163.0-linux-x64 resolved.
- No pacman, no git writes, and no lane edits except this report. A fleet-wide find used to locate the contract was stopped; its output was not used.
- Access record (UTC): learn.chatgpt.com/docs/build-skills.md at 08:51:53Z and 08:55:20Z; learn.chatgpt.com/docs/build-skills HEAD at 08:52:20Z and GET at 08:54:07Z and 08:55:20Z; raw.githubusercontent.com openai/codex rust-v0.163.0 (parser.rs, render.rs) at 08:56Z.
