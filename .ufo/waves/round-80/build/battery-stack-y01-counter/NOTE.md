# NOTE — superseded by ../battery-stack-canonical-counter/

These receipts are the SAME stack world (rev 7b89d2107d14b4f15f936c6618faf8cf55210c6c)
measured with Y01's published counter bytes in verifiers/check_tip_battery.py instead of
E06's canonical E5-amended file (`check_tip_battery.amended.py`, sha256 15cc1761…).  Both
counters carry LINE_CAP 60 and the same two pins, so the frozen reading is identical:
`guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, in both argument forms (01, 02).

Receipt 05 in THIS directory carries a harness artifact, not a world defect: it was produced
by the FIRST version of run-battery.sh, which named the fleet-shaped world clone after the
scratch repo's directory (`clone`), so verify_skill_checklist.py's `trigger.name_directory`
check read "name 'kotoba-shokunin' != directory 'clone'" and exited 1 — while the tip
battery measured the same gate green inside its own sandbox (which always names its clone
`kotoba-shokunin`).  The runner was fixed (the world clone is now named after the lane's
SKILL.md `name:`) and every receipt in ../battery-stack-canonical-counter/ and
../battery-base/ was re-taken with the fixed runner; there, receipt 05 exits 0 with no
failing check.

Runner sha256 (fixed): cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601
