"""Check truthful metadata handling and incomplete inspection reporting."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import openpyxl

spec = importlib.util.spec_from_file_location("realism", Path(__file__).with_name("mark_realism_check.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class RealismChecks(unittest.TestCase):
    def test_simple_workbook_needs_no_invented_author(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "decision.xlsx"
            workbook = openpyxl.Workbook()
            workbook.properties.creator = None
            workbook.active.append(["Option", "Value"])
            workbook.active.append(["A", 42])
            workbook.save(path)
            workbook.close()
            self.assertEqual(checker.xlsx_report(path), [])

    def test_broken_reference_is_located(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "decision.xlsx"
            workbook = openpyxl.Workbook()
            workbook.active["B2"] = "=#REF!+1"
            workbook.save(path)
            workbook.close()
            self.assertTrue(any("B2" in note for note in checker.xlsx_report(path)))

    def test_missing_file_or_dependency_is_not_a_clean_inspection(self):
        with tempfile.TemporaryDirectory() as folder, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(checker.main([folder, "--authored", "absent.xlsx"]), 2)
            Path(folder, "decision.xlsx").touch()
            with patch.object(checker, "xlsx_report", side_effect=ImportError("openpyxl")):
                self.assertEqual(checker.main([folder]), 2)


if __name__ == "__main__":
    unittest.main()
