#!/usr/bin/env bash
# Q45 census, round 73 C1: fetch six cited pages (+ two Kimi alternates), text-extract, count tokens with grep -c -F.
# usage: census-cn.sh [workdir]   (needs curl, python3, ext.py beside this script)
set -u
HERE=$(cd "$(dirname "$0")" && pwd); D=${1:-$(mktemp -d /tmp/k73census.XXXX)}; mkdir -p "$D"; cd "$D"
fetch() { curl -sL --max-time 60 -A 'Mozilla/5.0' -o "$1.html" -w "$1 %{http_code} %{size_download}\n" "$2"; }
fetch trae https://docs.trae.cn/ide_skills & fetch cbide https://www.codebuddy.ai/docs/zh/ide/Features/Skills &
fetch cbcli https://www.codebuddy.ai/docs/zh/cli/skills & fetch kimiraw https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md &
fetch kimiblob https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md & fetch kimicom https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html &
fetch zhipu https://docs.bigmodel.cn/cn/managed-agents/skills.md & wait
for n in trae cbide cbcli kimiblob kimicom; do python3 "$HERE/ext.py" $n.html > $n.txt; done; cp kimiraw.html kimiraw.txt; cp zhipu.html zhipu.txt
sha256sum *.txt
tok() { # vendor kind token pages...
  v=$1; k=$2; t=$3; shift 3; line="$v|$k|$t"
  for p in "$@"; do line="$line|$p=$(grep -c -F -- "$t" $p.txt)"; done; echo "$line"
}
tok TRAE root '.trae/skills/' trae
tok TRAE root '~/.trae-cn/skills/' trae
tok TRAE root '~/.trae/skills/' trae
tok TRAE root '.agents/skills/' trae
tok TRAE key 'name' trae
tok TRAE key 'description' trae
tok CodeBuddy root '.codebuddy/skills/' cbide cbcli
tok CodeBuddy root '~/.codebuddy/skills/' cbide cbcli
tok CodeBuddy key 'allowed-tools' cbide cbcli
tok CodeBuddy key 'disable-model-invocation' cbide cbcli
tok CodeBuddy key 'disable' cbide cbcli
tok CodeBuddy key 'name' cbide cbcli
tok CodeBuddy key 'description' cbide cbcli
tok Kimi root '.kimi-code/skills/' kimiraw kimiblob kimicom
tok Kimi root '.agents/skills/' kimiraw kimiblob kimicom
tok Kimi root '$KIMI_CODE_HOME/skills/' kimiraw kimiblob kimicom
tok Kimi root '~/.kimi-code/skills/' kimiraw kimiblob kimicom
tok Kimi root '~/.agents/skills/' kimiraw kimiblob kimicom
tok Kimi key 'whenToUse' kimiraw kimiblob kimicom
tok Kimi key 'when-to-use' kimiraw kimiblob kimicom
tok Kimi key 'when_to_use' kimiraw kimiblob kimicom
tok Kimi key 'disableModelInvocation' kimiraw kimiblob kimicom
tok Kimi key 'disable-model-invocation' kimiraw kimiblob kimicom
tok Kimi key 'disable_model_invocation' kimiraw kimiblob kimicom
tok Kimi key 'arguments' kimiraw kimiblob kimicom
tok Kimi key 'type' kimiraw kimiblob kimicom
tok Kimi key 'name' kimiraw kimiblob kimicom
tok Kimi key 'description' kimiraw kimiblob kimicom
tok Zhipu key 'type:zai' zhipu
tok Zhipu key 'type: zai' zhipu
tok Zhipu key 'type:custom' zhipu
tok Zhipu key 'type: custom' zhipu
tok Zhipu key 'name' zhipu
tok Zhipu key 'description' zhipu
tok Zhipu key 'zai' zhipu
tok Zhipu key 'custom' zhipu
