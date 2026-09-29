import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from challenge import summarize
from contribution_board import eligible


class ChallengeTest(unittest.TestCase):
    def test_examples_keep_missing_channel_inconclusive(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            summarize("challenge.csv")
        result = out.getvalue()
        self.assertIn("A: mean signal=+0.588", result)
        self.assertIn("C: mean signal=+0.592; proxy missing; INCONCLUSIVE", result)
        self.assertIn("No physical force or propulsion verified", result)

    def test_nonfinite_value_cannot_be_scored(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.csv"
            path.write_text("run,step,signal,artifact_proxy\nX,1,nan,0\n")
            with self.assertRaisesRegex(ValueError, "Non-finite"):
                summarize(path)

    def test_unreviewed_issue_never_appears_on_board(self):
        issue = {
            "title": "[Challenge] Example",
            "body": "**Public credit:** yes",
            "labels": [],
        }
        self.assertFalse(eligible(issue))
        issue["labels"] = [{"name": "reviewed-entry"}]
        self.assertTrue(eligible(issue))
        issue["body"] = "**Public credit:** no"
        self.assertFalse(eligible(issue))


if __name__ == "__main__":
    unittest.main()
