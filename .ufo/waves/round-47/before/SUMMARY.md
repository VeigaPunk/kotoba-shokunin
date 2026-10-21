# round-47 before — BASE c61a973b2e02e1ded169703ddcb06466f4edd8bd — 2026-10-21T12:11:26-03:00
census: kotoba ok exit=0 (sources-census.sh validate)
surfaces default: exit=2 (opencode binary not found: /home/vgpnk/.opencode/bin/opencode)
surfaces --opencode-binary <npx 1.19.3>: 4 PASS / 3 FAIL (literal_present, no_uncovered_class vacuity 0/8, opencode_extract OC-1/OC-4/OC-6)
pins: exit=2 DRIFT 3/3
checklist --json: exit=1 9 PASS/1 FAIL governance.citation_resolves LOG.md:2111
corpus integrity: exit=1 DRIFT tracked_files 59!=58, unindexed 1
corpus independent: exit=1 DRIFT unindexed
harness claims: exit=1 21/28
frontmatter <skills> count: 1
omp: omp/18.12.5 sha256 fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e mtime 2026-10-21 03:30:38.135013187 -0300
opencode: 1.19.3 npx-cache ELF /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode sha256 179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9
