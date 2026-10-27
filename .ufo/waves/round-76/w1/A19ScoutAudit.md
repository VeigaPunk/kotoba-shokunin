# A19ScoutAudit — independent description measurement

**Finding: description-length disagreement.** At HEAD `4de12b61f75c73e3675ef0e422cc2be0f7da8960`, both independent render methods give **1,021**, not the claimed **1,022**. Both give first-sentence length **151**, matching the claim.

Evidence: read committed bytes with `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show HEAD:SKILL.md` (HEAD resolved to the revision above). The YAML folded description spans file lines 4–18. I manually unfolded its 15 content lines (strip the two-space indentation, fold each line break to a space, clip the final newline) and separately parsed the frontmatter with PyYAML 6.0.3 `safe_load`; the resulting strings were identical. Both lengths were 1,021 Unicode code points (UTF-8 byte length 1,025).

The first sentence through its terminating period is 151 code points. The two measurement methods agree on that value.

Exact measurement command: `python3 /fast/scratch/hyaku/kotoba-r76/A19ScoutAudit/measure_desc.py` (exit 0). Its output included `METHOD1 manual-fold rendered length = 1021`, `METHOD2 pyyaml rendered length      = 1021`, `methods agree on render: True`, `first-sentence length (def A, through '. ') = 151`, and `CLAIM render=1022  -> match A: False, pyyaml: False`. The temporary measurement script and scratch directory were removed after execution.

**Verdict: disagreement on rendered description length (1,021 measured vs 1,022 claimed); first-sentence length agrees (151).**