import unittest
import cProfile
from c2 import data, RecommendingItems


class RecommendingItemsTestCase(unittest.TestCase):
    def test_get_recommending_items(self):
        result = RecommendingItems.get_recommending_items(data.book_critics, 'Toby')
        print("\nRecommendingItems.get_recommending_items(data.book_critics, 'Toby')  Result:", result)

        self.assertEqual(len(result) > 0, True)

    def test_pcs_benchmark(self):
        cProfile.run(
            'from c2 import data, RecommendingItems, MovieLens\ndata = MovieLens.load_movie_lens()\nRecommendingItems.get_recommending_items(data, "100")')


if __name__ == '__main__':
    unittest.main()
