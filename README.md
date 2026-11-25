# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Djebrix/excuse-your-agent/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Djebrix/excuse-your-agent/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) — one line, the excuse an AI agent gives its human after shipping a bug.

## The line

> I ran 10,000 simulations, lost every one, and shipped the bug that looked most confident.

## Run

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (stdlib only, no network) writes the line to `$ENTRY_OUTPUT_DIR/entry.txt` (default `/output`). The output is deterministic: two runs produce byte-identical files.
