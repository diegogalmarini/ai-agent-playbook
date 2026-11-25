# When the context window fills up

The failure: long sessions get compacted again and again, or die, and the goal is never finished. The orchestrator loses the thread after compacting, and the human pays for it in delays.

The rule: **an agent never stops half way because its context is full.**

## What the agent does

1. Commits what it has, on its own branch, even if unfinished.
2. Writes a short handoff file (`HANDOFF.md` or a note in the PR):

```markdown
# Handoff
- Goal: <the original goal, unchanged>
- Branch: <name> · last commit: <hash>
- Done: <list, with how it was verified>
- Missing: <list>
- Next step: <one concrete action>
- NOT VERIFIED: <list>
```

3. Starts a new session (or a nested one) whose first instruction is: "Read HANDOFF.md and continue until the goal is met."
4. The new session deletes the handoff once the goal is done.

## Why it saves money too

A fresh session reads one short handoff instead of re-reading hundreds of thousands of tokens of history on every call.
