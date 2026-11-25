# No silent failures

Two real cases that shaped this playbook:

- **Nine months of empty results.** On 14 January 2026 the embedding model behind a document search started answering 404. The code caught the error and returned an empty list. For the rest of the system there were simply "no results". Nobody saw an error and nobody got an alert until an audit on 10 October. The fix took a day: another model, re-embedding 52 chunks and one migration.
- **The watchdog that went blind.** A daily check watched the model provider's deprecation page. The provider moved that page on 4 November and the check started failing silently. The retirement of the model in use was found on 12 November, 19 days before shutdown.

## Rules

1. **Never turn a provider error into an empty value.** `catch { return [] }` is a bug. Return the error, or raise it.
2. **"No results" and "could not check" are different answers.** Make them different types, different UI states and different log lines.
3. **Every watchdog also alerts when it fails itself.** A monitor that cannot reach its source must raise an alert, not report "nothing new".
4. **An agent triages alerts first.** Error tracker, uptime monitors and automatic error emails go to a specialist agent. Only what needs a human decision reaches a person, with one action.
5. **Measure before you migrate.** When a model is retired, set a budget cap, run the real workload on test data, compare cost and quality, and keep tested fallbacks.

## Checklist for a model your product depends on

- [ ] Which models do we call, and from which files? (search the repo for model names)
- [ ] When does each one retire? (provider deprecation page, read by a check that alerts if the page itself cannot be read)
- [ ] What is the replacement, and was it measured on our own data?
- [ ] Which fallback model is configured, and was it tested?
- [ ] What does the user see if the model call fails? (it must never be "no results")

## Result of measuring first (real numbers)

Before switching the model that drafted documents, 132 drafts cost $20.21 under a $30 cap.
After the switch the drafting cost per document went from $0.150 to $0.071.
