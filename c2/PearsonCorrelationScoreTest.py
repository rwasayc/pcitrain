import unittest
import cProfile
from c2 import PearsonCorrelationScore, data


class PearsonCorrelationScoreTestCase(unittest.TestCase):
    def test_pcs(self):
        result = PearsonCorrelationScore.pcs(data.book_critics, 'Lisa Rose', 'Jack Matthews')
        print("\nPearsonCorrelationScore.pcs(data.book_critics, 'Lisa Rose', 'Jack Matthews')  Result:", result)
        self.assertEqual(result > 0, True)

    def test_pcs_benchmark(self):
        cProfile.run(
            'from c2 import data, PearsonCorrelationScore, MovieLens\ndata = MovieLens.load_movie_lens()\nPearsonCorrelationScore.pcs(data, "100", "500")')


if __name__ == '__main__':
    unittest.main()
