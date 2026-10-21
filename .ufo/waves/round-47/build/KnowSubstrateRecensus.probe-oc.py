import re, json, sys
from pathlib import Path
OC = Path('/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings').read_text(errors='replace')
OM = Path('/fast/scratch/kotoba-r47/shared/omp-18.12.5.strings').read_text(errors='replace')
r14 = {
 'OC-1 array': re.compile(r'\["AGENTS\.md"[^\]]{0,200}?"CONTEXT\.md"\]'),
 'OC-1 gate CLAUDE': re.compile(r'disableClaudeCodePrompt\?\["CLAUDE\.md"\]'),
 'OC-2 config join': re.compile(r'[\w$]+\.join\([\w$]+\.config,"AGENTS\.md"\)'),
 'OC-2 home join': re.compile(r'[\w$]+\.join\([\w$]+\.home,"\.claude","CLAUDE\.md"\)'),
 'OC-3a for-of instructions': re.compile(r'for\(let [\w$]+ of [\w$]+\.instructions\)'),
 'OC-3b remote https': re.compile(r'\.instructions[^;]{0,400}startsWith\("https://"\)'),
 'OC-3b Instructions from': re.compile(r'`Instructions from: '),
 'OC-4 Instruction.resolve': re.compile(r'fn\("Instruction\.resolve"\)'),
 'OC-4 system-reminder': re.compile(r'<system-reminder>'),
 'OC-5 env': re.compile(r'OPENCODE_DISABLE_PROJECT_CONFIG'),
 'OC-5 globUp pair': re.compile(r'globUp\([\w$]+\.directory,[\w$]+\.worktree\)'),
 'OC-6 observe': re.compile(r'InstructionContext\.observe'),
 'OC-6 core/instructions': re.compile(r'Key\.make\("core/instructions"\)'),
 'OC-6 targets AGENTS': re.compile(r'targets:\["AGENTS\.md"\]'),
 'OC-6 system-context-builtins': re.compile(r'system-context-builtins'),
 'R18 ConfigInstructionPlugin.projectSource': re.compile(r'ConfigInstructionPlugin\.projectSource'),
 'R18 projectSource(any)': re.compile(r'projectSource'),
 'R18 ReadTool.Plugin': re.compile(r'ReadTool\.Plugin'),
 'R18 SessionInstructions.load': re.compile(r'SessionInstructions\.load'),
 'R18 /instructions/entries': re.compile(r'/instructions/entries'),
 'R18 session.instructions.entry.put': re.compile(r'session\.instructions\.entry\.put'),
}
out = {}
for k, rx in r14.items():
    ms = list(rx.finditer(OC))
    out[k] = len(ms)
for k, v in out.items(): print(f'{k:42s} {v}')
# version strings
print('version-ish 1.19.3 hits:', len(re.findall(r'1\.19\.3', OC)), ' 2.0.26 hits:', len(re.findall(r'2\.0\.26', OC)))
# show the OC-1 array context
m = r14['OC-1 array'].search(OC)
print('OC-1 array ctx:', OC[m.start()-160:m.end()+20] if m else None)
