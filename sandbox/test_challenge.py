import contextlib
import io
import unittest

from challenge import summarize


class ChallengeTest(unittest.TestCase):
    def test_examples_keep_missing_channel_inconclusive(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            summarize("challenge.csv")
        result = out.getvalue()
        self.assertIn("A: mean signal=+0.588", result)
        self.assertIn("C: mean signal=+0.592; proxy missing; INCONCLUSIVE", result)
        self.assertIn("No physical force or propulsion verified", result)


if __name__ == "__main__":
    unittest.main()
