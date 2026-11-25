# Subagent brief — the template I use to delegate a long job

Why it exists: in five days of agent work I spent $1,150, and 87% went on re-reading context, not on thinking.
Handing each long job to a helper with a complete brief and a clean context cost $118 where the main agent would have spent about $392 (70% less; 72% with the same large model).
The saving comes from the brief, not from a cheaper model.

A good brief lets the helper start cold: it never needs the conversation that produced it.

---

```markdown
# Brief: <one-line goal>

## Goal
<What "done" looks like, in one or two sentences. Measurable if possible.>

## Context the helper needs (and nothing more)
- Repository / folder: <path>
- Files to read first: <path>, <path>
- Decisions already taken (do not reopen them): <decision>, <decision>
- Constraints: <budget, deadline, things that must not change>

## Do
1. <step>
2. <step>
3. <step>

## Do NOT
- Do not touch production, delete data or spend money.
- Do not <specific thing that would be tempting and wrong>.
- Do not stop to ask what is already written above: decide and note the decision.

## Verify before reporting
- <command or check that proves it works, e.g. tests, build, a request>
- Report anything unchecked as NOT VERIFIED.

## Report back
- What changed (files, commits) and the real output of the checks.
- NOT VERIFIED: <list>.
- Open questions for the human: at most one.
```

---

## Habits that go with it

1. A new session when the task changes.
2. Do not switch models halfway through a session: the new model re-reads everything.
3. Long jobs go to a helper, with everything it needs in writing.
4. Do not come back to a huge session after a long pause: start a new one from a short handoff.
