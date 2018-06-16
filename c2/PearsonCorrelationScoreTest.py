import unittest

from c2 import PearsonCorrelationScore
from c2 import data


class PearsonCorrelationScoreTestCase(unittest.TestCase):
    def test_pcs(self):
        result = PearsonCorrelationScore.pcs(data.book_critics, 'Lisa Rose', 'Jack Matthews')
        print("\nPearsonCorrelationScore.pcs(data.book_critics, 'Lisa Rose', 'Jack Matthews')  Result:", result)
        self.assertEqual(result > 0, True)


if __name__ == '__main__':
    unittest.main()
