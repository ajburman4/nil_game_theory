"""Synthetic validation fixtures only; never research observations."""
import sys
import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from spendgame.eada import numeric_status, require_unique, strict_sum, read_archive


class EvidenceTests(unittest.TestCase):
    def test_zero_and_missing_remain_distinct(self):
        self.assertEqual(numeric_status(None), "unknown")
        self.assertEqual(numeric_status(float("nan")), "unknown")
        self.assertEqual(numeric_status(0), "observed_zero")
        self.assertEqual(numeric_status(5), "observed_positive")

    def test_negative_or_infinite_disclosures_rejected(self):
        for value in [-1, float("inf"), float("-inf")]:
            with self.assertRaises(ValueError):
                numeric_status(value)

    def test_missing_components_cannot_create_reconciliation(self):
        self.assertTrue(pd.isna(strict_sum(pd.Series([12, None, 8]))))
        self.assertEqual(strict_sum(pd.Series([12, 0, 8])), 20)

    def test_duplicate_join_grain_rejected(self):
        frame = pd.DataFrame({"unitid": [1, 1], "year": [2020, 2020]})
        with self.assertRaises(ValueError):
            require_unique(frame, ["unitid", "year"], "synthetic")

    def test_null_join_key_rejected(self):
        with self.assertRaises(ValueError):
            require_unique(pd.DataFrame({"id": [None]}), ["id"], "synthetic")

    def test_year_is_part_of_grain(self):
        require_unique(pd.DataFrame({"unitid": [1, 1], "year": [2020, 2021]}),
                       ["unitid", "year"], "synthetic")

    def test_modified_snapshot_rejected_before_parsing(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.zip"
            path.write_bytes(b"synthetic changed input; not research data")
            path.with_suffix(".receipt.json").write_text(json.dumps({"sha256": "old_checksum"}))
            with self.assertRaisesRegex(ValueError, "differs from acquisition checksum"):
                read_archive(path, 2025)

    def test_unprovenanced_cached_input_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.zip"
            path.write_bytes(b"synthetic fixture")
            with self.assertRaisesRegex(ValueError, "missing acquisition receipt"):
                read_archive(path, 2025)


if __name__ == "__main__":
    unittest.main()
