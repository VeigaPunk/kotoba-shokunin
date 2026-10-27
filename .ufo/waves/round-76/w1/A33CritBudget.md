# A33CritBudget — budget arithmetic review

Axes: operability, consistency, calibration.

## Counterexample / evidence

The draft predicts 595 lines (590 base + 5 additions), within `trigger.line_budget` ≤600, but it is conditional on exact application of the two-line-to-three-line preamble replacement and additions; independently counted draft deltas are +1 preamble line, +1 body row, +2 registry rows = +4, not +5. The draft explicitly labels +5 as two preamble wrap lines + rule row + two registry rows, yet its replacement is 2 lines to 3 lines: net +1. Thus projected line count is **594**, not 595, if the described replacement is applied literally. Either result stays under cap.

Registry row shape is eight fields, verified by splitting the two draft rows on `|`: nine pipe delimiters each, hence eight cells. The body rule has three fields (four pipes). No malformed-row risk found.

Evidence: `.ufo/waves/round-76/build/skill-patch.md` lines 6–7, 14–24, 48–58; `.ufo/waves/round-76/w1/B13SkillPatch.md` lines 17–23, 31–34. Base is documented as 590 lines and trigger threshold 600. The row draft itself specifies the registry's eight-column order.

## Smallest safe correction

Correct the draft/report projected count and margin to **594 / 6 lines**, or clarify the second added preamble line if one is intended. Keep the existing 3-cell and 8-cell rows unchanged. The trigger budget predicate remains satisfied either way; do not change the checklist box.
