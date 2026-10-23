# Fixture — a stated word count that carries its counting command.

The same shape as the mined line, with the command the rule asks for.

- **Gemini CLI hooks-overview quote** — reject: 29 words, above the 25-word cap; the counting command is pasted on the next line.
  `sed -n 94,97p` cut at the token | `wc -w` -> 25

- **best-practices quote** — admit: a 10-word quote, counted by `printf %s '<quote>' | wc -w` -> 10.
