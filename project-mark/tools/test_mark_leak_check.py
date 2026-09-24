"""Regression checks for current-vs-legacy prompt contracts."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("mark_leak_check", Path(__file__).with_name("mark_leak_check.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

class PromptContracts(unittest.TestCase):
    def test_natural_prose_outputs_and_repeated_reference(self):
        text = "Send decision.xlsx and briefing.pdf. The chart belongs in decision.xlsx."
        files, problems = checker.check_contract(text)
        self.assertEqual(list(files), ["decision.xlsx", "briefing.pdf"])
        self.assertEqual(problems, [])

    def test_current_boundary_and_legacy_distinction(self):
        self.assertFalse(checker.check_contract("Send decision.xlsx.")[1])
        self.assertTrue(checker.check_contract("Send a.csv, b.pdf, c.py and d.png.")[1])
        self.assertTrue(checker.check_contract("Send decision.xlsx.", "legacy")[1])
        legacy = "\n".join(f"{i}. {name}\n- first\n- second\n- third" for i, name in enumerate(["a.csv", "b.pdf", "c.py"], 1))
        self.assertFalse(checker.check_contract(legacy, "legacy")[1])

    def test_input_references_can_be_disambiguated(self):
        text = "Use a.csv, b.csv and c.csv to prepare decision.xlsx."
        self.assertTrue(checker.check_contract(text)[1])
        self.assertFalse(checker.check_contract(text, deliverables=["decision.xlsx"])[1])
        self.assertTrue(checker.check_contract(text, deliverables=["missing.xlsx"])[1])

if __name__ == "__main__":
    unittest.main()
