import unittest
import subprocess
from csv_combiner import CSV_Combiner


# UNIT TESTS
class TestCSV_Combiner(unittest.TestCase):
    # Tests combine method with no input
    def test_emptyInput(self):
        self.assertEqual(CSV_Combiner([]).combine([]), 0)

    # Tests combine method with non csv file
    def test_nonCSVFile(self):
        with self.assertRaises(SystemExit) as cm:
            CSV_Combiner(["csv_combiner.py"]).combine(["csv_combiner.py"])
        self.assertEqual(cm.exception.code, 1)

    # Tests combine method with non existent csv file
    def test_nonExistantCSVFile(self):
        self.assertTrue(CSV_Combiner(["nonexistant.csv"]).combine(["nonexistant.csv"]), 1)

    # Tests that combine works
    def test_combine(self):
        self.assertTrue(
            subprocess.run(["python", "csv_combiner.py", "./fixtures/clothing.csv", "./fixtures/accessories.csv"]), 0)
