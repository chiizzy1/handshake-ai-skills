"""Regression checks for actual observations and partial package counters."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location("manifest", Path(__file__).with_name("mark_manifest.py"))
manifest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(manifest)


class ManifestChecks(unittest.TestCase):
    def test_styled_distant_row_does_not_count_as_data(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "table.xlsx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("xl/worksheets/sheet1.xml", '''<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
                <dimension ref="A1:A20000"/><sheetData>
                <row r="1"><c r="A1" t="inlineStr"><is><t>Header</t></is></c></row>
                <row r="2"><c r="A2"><v>42</v></c></row>
                <row r="20000"><c r="A20000" s="1"/></row>
                </sheetData></worksheet>''')
            self.assertEqual(manifest._xlsx_rows(path), 1)

    def test_tab_blank_lines_and_unsupported_stata(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "table.tab"
            path.write_text("id\tvalue\n1\t2\n\n\t\n2\t3\n")
            self.assertEqual(manifest.count_rows(str(path), ".tab"), 2)
            self.assertIsNone(manifest.count_rows(str(path), ".dta"))

    def test_size_limits_and_manual_requirements(self):
        row = {"file": "a.csv", "format": ".csv", "family": "data",
               "bytes": 10_000_000, "rows": 10_000, "necessary": True,
               "role": "observations", "source": "source", "pulled": "2026-09-08",
               "licence": "CC0", "sha256": "a" * 64}
        checks, _ = manifest.check([row])
        statuses = {name: passed for name, _, _, passed in checks}
        self.assertIsNone(statuses["2+ substantial files (content review)"])
        self.assertIsNone(statuses["Shipping ZIP strictly under 50 MB (bytes)"])
        self.assertFalse(statuses["Each file strictly under 10 MB (largest bytes)"])
        checks, _ = manifest.check([dict(row, bytes=9_999_999)], zip_bytes=50_000_000)
        statuses = {name: passed for name, _, _, passed in checks}
        self.assertTrue(statuses["Each file strictly under 10 MB (largest bytes)"])
        self.assertFalse(statuses["Shipping ZIP strictly under 50 MB (bytes)"])


if __name__ == "__main__":
    unittest.main()
