#!/usr/bin/env bash
# fetch.sh — re-fetch the three A4 snapshots into FETCHED (default /tmp/k72w1-ExecAuthorControls.fetch).
# Each capture records its HTTP status beside the bytes; gen.py reads it if present.
set -euo pipefail
out=${FETCHED:-/tmp/k72w1-ExecAuthorControls.fetch}
mkdir -p "$out"
get() { # id url file
  local st
  st=$(timeout 40 curl -sSL -o "$out/$3" -w '%{http_code}' "$2")
  echo "$st" > "$out/$3.status"
  printf '%s  %s  %s bytes  status %s\n' "$1" "$2" "$(wc -c < "$out/$3")" "$st"
}
get S255 https://agentskills.io/skill.md S255-agent-skills-skill-md.md
get S262 https://docs.factory.ai/cli/configuration/skills.md S262-factory-droid-skills.md
get S263 https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/docs/skills.md S263-pi-skills.md
