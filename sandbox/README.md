# Can you fool the force-trace detector?

This is a fictional, synthetic data challenge. The numbers are arbitrary and do
not describe an engine, instrument, physical experiment, or measured thrust.

Run `python challenge.py challenge.csv` using Python 3. The script prints each
run's average apparent signal and the average after subtracting a deliberately
imperfect artifact proxy. It does **not** decide whether a residual is thrust.

For runs A through D, tell us:

1. Which looks explained by the measured proxy?
2. Which might contain an injected reference, and what else could explain it?
3. Which cannot be judged because a channel is missing?
4. Can you construct a fifth synthetic run that fools this simple subtraction?
5. What control or independent measurement would resolve your counterexample?

Open a GitHub issue with your reasoning, modified fictional CSV, and a
reproducible command. Please do not submit hardware instructions, confidential
designs, or personal data. Criticism and null results are welcome. The organizer
will publish the answer key and corrections after the first review round.

**Interpretation rule:** A residual in synthetic data is never evidence of
physical propulsion. No physical experiment has been performed by this challenge.
