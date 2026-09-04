import unittest

from pydataset import filter_rows, select_columns, summarize


class DatasetTests(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"name": "medu", "score": 10},
            {"name": "dev", "score": 7},
            {"name": "guest", "score": None},
        ]

    def test_select(self):
        self.assertEqual(select_columns(self.rows, ["name"]), [{"name": "medu"}, {"name": "dev"}, {"name": "guest"}])

    def test_filter(self):
        self.assertEqual(len(filter_rows(self.rows, lambda row: (row["score"] or 0) >= 8)), 1)

    def test_summary(self):
        self.assertEqual(summarize(self.rows), {"rows": 3, "columns": {"name": 3, "score": 2}})


if __name__ == "__main__":
    unittest.main()
