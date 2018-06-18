import unittest
import cProfile
from c3 import Score, data


class PearsonCorrelationScoreTestCase(unittest.TestCase):
    def test_pcs(self):
        row_names, col_names, vals = data.load_data()
        print(vals[0])
        print(vals[1])

        result = Score.pcs(vals[0], vals[2])
        print("\nScore.pcs(vals[0], vals[2])  Result:", result)
        self.assertEqual(result >= 0, True)


if __name__ == '__main__':
    unittest.main()
