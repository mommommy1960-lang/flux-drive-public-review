# Can you fool the force-trace detector?

This is a free, fictional, synthetic data challenge for adults. There is no prize or drawing. The numbers are arbitrary and do not describe an engine, instrument, physical experiment, or measured thrust.

Run `python3 challenge.py challenge.csv` using Python 3, or inspect the CSV by eye. The script prints each run's average apparent signal and the average after subtracting a deliberately imperfect artifact proxy. It does **not** decide whether a residual is thrust. It reads only your local CSV and has no network access. Do not run code from unknown commenters or open their files in a spreadsheet.

For runs A through D, tell us:

1. Which looks explained by the measured proxy?
2. Which might contain an injected reference, and what else could explain it?
3. Which cannot be judged because a channel is missing?
4. Can you construct a fifth fictional run that fools this simple subtraction?
5. What control or independent measurement would resolve your counterexample?

Open a GitHub issue with reasoning, a small modified fictional CSV, and a reproducible command. No hardware instructions, real data, confidential designs, personal data, links to executable content, or third-party material without permission. The organizer will publish the answer key and corrections after the first review round. Maintainers review submissions before the opt-in board lists them. The private Flux Drive sandbox never automatically executes or imports participant code.

Read [the participation terms](../CONTRIBUTING.md), [conduct rules](../CODE_OF_CONDUCT.md), [security guidance](../SECURITY.md), and [scope-limited reuse license](../LICENSE-SANDBOX.md) before posting.

**Interpretation rule:** A residual in synthetic data is never evidence of physical propulsion. No physical experiment has been performed by this challenge.
