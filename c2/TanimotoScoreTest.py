import unittest
import cProfile
from c2 import data, TanimotoScore


class TanimotoScoreTestCase(unittest.TestCase):
    def test_ts(self):
        result = TanimotoScore.ts(data.book_critics, 'Lisa Rose', 'Toby')
        print("\nTanimotoScore.ts(data.book_critics, 'Lisa Rose', 'Toby')  Result:", result,"\n")
        self.assertEqual(result > 0, True)

    def test_ts_benchmark(self):
        cProfile.run(
            'from c2 import data, TanimotoScore, MovieLens\ndata = MovieLens.load_movie_lens()\nTanimotoScore.ts(data, "100", "500")')


if __name__ == '__main__':
    unittest.main()
