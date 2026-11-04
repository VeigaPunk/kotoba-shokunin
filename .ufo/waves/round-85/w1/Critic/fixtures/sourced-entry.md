# Description trigger discipline — round 85 (S213)

source: S213
verified-at: 2026-11-04
recheck: re-run verifiers/check_description_render.py after every SKILL.md description edit
locator: S213, Optimizing skill descriptions, Testing whether a description triggers / Running multiple times; registry corpus/SOURCES.md:153
quote: A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default).

## Why

The router renders a fixed-width cut of the frontmatter description; the first
sentence must carry the domain inside that cut. Trigger terms belong behind an
imperative invocation and an explicit `Triggers:` clause so the full
description stays machine-auditable.
