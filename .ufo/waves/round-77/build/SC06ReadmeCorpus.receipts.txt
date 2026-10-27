SC06ReadmeCorpus — receipts (kotoba round 77, w1). All commands run from a scratch clone of
lane HEAD 6523aced1ee0ebe07dca996213bdc645a6acbd1e under
/fast/scratch/hyaku/kotoba-r77/SC06ReadmeCorpus/ (scratch, removed before yield).
Every exit status below is the gate's/program's own: `cmd > out 2>&1; echo "exit=$?"` — no pipeline status.

S = /fast/scratch/hyaku/kotoba-r77/SC06ReadmeCorpus
L = /home/vgpnk/Projects/shokunin/kotoba-shokunin

[1] base measurement, lane tree at HEAD (read-only)
$ python3 -B verifiers/verify_corpus_integrity.py --json
 exit=1  (DRIFT on corpus.index.tracked_files 146 vs 144, corpus.index.unindexed 2,
          corpus.pointers.report_total 102 vs 99, corpus.pointers.commit_total 44 vs 43)
 observed: tracked_files=146 index_patterns=162 unindexed=2 stale_patterns=0 missing_paths=0
           report_total=102 report_dead=0 commit_total=44 commit_unresolvable=0 commit_nonhash=0
 unindexed_detail:
   corpus/lessons/round-75-verifier-spotcheck.md
   corpus/lessons/round-76-verifier-spotcheck.md

[2] patch generation and apply-ability at lane HEAD
$ git clone --shared $L $S/final && git -C $S/final rev-parse --show-toplevel   # = $S/final
$ git -C $S/clone diff --src-prefix=a/ --dst-prefix=b/ 6523aced1ee0ebe07dca996213bdc645a6acbd1e \
    -- corpus/README.md > $L/.ufo/waves/round-77/build/SC06ReadmeCorpus.patch
 exit=0 ; sha256 9f7fe56dd11aafe8be8a6cbe5d0af8f4bfc5a01aa73f32d0491bbfc981c4781a
 patch touches exactly one path: corpus/README.md (5 coverage rows inserted after the
 Round-74 spot-check row; 1 Frontier note appended after the Round-74 note).

$ git -C $S/final apply --check $L/.ufo/waves/round-77/build/SC06ReadmeCorpus.patch
 exit=0
$ git -C $S/final apply $L/.ufo/waves/round-77/build/SC06ReadmeCorpus.patch
 exit=0

[3] red-before: patch applied, the three indexed data files absent (sequencing constraint)
$ python3 -B $S/applytest/verifiers/verify_corpus_integrity.py --no-baseline --json --repo $S/applytest
 exit=1  (missing_paths=3)
 observed: tracked_files=146 index_patterns=167 unindexed=0 stale_patterns=0 missing_paths=3
           report_total=102 commit_total=44
 missing_paths_detail:
   corpus/README.md:150: knowledge/description-craft-round76.md -> knowledge/description-craft-round76.md
   corpus/README.md:151: lessons/round-76.md -> lessons/round-76.md
   corpus/README.md:154: lessons/round-77.md -> lessons/round-77.md
$ python3 -B $S/applytest/verifiers/verify_corpus_independent.py --json --repo $S/applytest
 exit=1  (index: unindexed=0 stale_tokens=3 missing_paths=3; tracked_files=146 index_tokens=167)
 => the two spot-check rows alone repair the base `unindexed 2`; the other three rows require the
    files to land in the same commit (or after).

[4] form test with the data files present (delivered patch bytes; fresh clone)
 files added for the fixture: corpus/knowledge/description-craft-round76.md (copy of
 .ufo/waves/round-76/build/entry-draft.md), corpus/lessons/round-76.md (copy of
 .ufo/waves/round-76/build/lesson-draft.md with the one fixture change named in [6]),
 corpus/lessons/round-77.md (placeholder line: `# round-77 lesson placeholder (index-form test only)`
 — NOT the landed lesson; the index gate tests existence, and no row content is claimed from it).
$ python3 -B $S/final/verifiers/verify_corpus_integrity.py --no-baseline --json --repo $S/final
 exit=0
 observed: tracked_files=149 index_patterns=167 unindexed=0 stale_patterns=0 missing_paths=0
           report_total=102 report_dead=0 commit_total=44 commit_unresolvable=0 commit_nonhash=0
$ python3 -B $S/final/verifiers/verify_corpus_independent.py --json --repo $S/final
 exit=0
 observed: index tracked_files=149 index_tokens=167 unindexed=0 stale_tokens=0 missing_paths=0;
           pointers report_total=102 report_dead=0; commits commit_total=44 commit_unresolvable=0
           commit_nonhash=0
 => both corpus instruments green on the delivered README rows.

[5] baseline refresh the L1 must pin (the README patch changes no baseline file; README alone
    cannot be green in baseline mode without this, because three `equal` checks move)
$ python3 -B $S/final/verifiers/verify_corpus_integrity.py --json --repo $S/final   # unmodified baseline
 exit=1
 DRIFT: corpus.index.tracked_files 149 (expect 144)
        corpus.pointers.report_total 102 (expect 99)
        corpus.pointers.commit_total 44 (expect 43)
$ # after setting those three expect values to 149 / 102 / 44 in the scratch clone's
$ # verifiers/corpus-baseline.json (scratch only; not written to the lane):
$ python3 -B $S/applytest2/verifiers/verify_corpus_integrity.py --json --repo $S/applytest2
 exit=0 ; all nine checks PASS
 [corpus.index.tracked_files PASS, corpus.index.unindexed PASS, corpus.index.stale_patterns PASS,
  corpus.index.missing_paths PASS, corpus.pointers.report_total PASS, corpus.pointers.report_dead PASS,
  corpus.pointers.commit_total PASS, corpus.pointers.commit_unresolvable PASS,
  corpus.pointers.commit_nonhash PASS]
 Deltas this patch implies for that refresh: tracked_files 144 -> 149 (+3 data files over the base
 146); report_total 99 -> 102 (the r74-closure pointers already at base; this patch adds 0);
 commit_total 43 -> 44 (44 at base; this patch adds 0). index_patterns is observed only: 162 -> 167 (+5 rows).

[6] cross-seat finding, measured in scratch (not a README defect)
 with the round-76 lesson draft landed verbatim, corpus/lessons/round-76.md:183 reads
 `commit `69ef37e`` (the upstream agentskills commit):
$ python3 -B $S/final/verifiers/verify_corpus_integrity.py --no-baseline ...
 commit_total=45 commit_unresolvable=1  (detail: corpus/lessons/round-76.md:183: 69ef37e), exit=1
 the independent gate likewise exits 1 (commit_unresolvable=1).
 fixture-only change `commit ` -> `revision ` (sha unchanged: 69ef37e) in the scratch copy:
 both gates exit=0, commit_total=44 commit_unresolvable=0.
 => the lesson scribe / L1 must not land the `commit `<foreign hex>`` shape; the README rows carry
    no commit tokens of their own (proved: commit_total stays 44 in [3] and [4]).

[7] no tool installs, no pacman, no git/jj writes in the lane; the only lane writes are
 .ufo/waves/round-77/build/SC06ReadmeCorpus.patch, .ufo/waves/round-77/build/SC06ReadmeCorpus.receipts.txt,
 .ufo/waves/round-77/w1/SC06ReadmeCorpus.md.
