import unittest

from c2 import EuclideanDistanceScore, data


class EuclideanDistanceScoreTestCase(unittest.TestCase):
    def test_eds(self):
        result = EuclideanDistanceScore.eds(data.book_critics, 'Lisa Rose', 'Jack Matthews')
        print("\nEuclideanDistanceScore.eds(data.book_critics, 'Lisa Rose', 'Jack Matthews')  Result:", result)
        self.assertEqual(result > 0, True)


if __name__ == '__main__':
    unittest.main()
