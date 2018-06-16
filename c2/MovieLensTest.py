import unittest

from c2 import MovieLens, RecommendingItems


class MovieLensTestCase(unittest.TestCase):
    def test_load_movie_lens(self):
        data = MovieLens.load_movie_lens()

        # print(data)
        result = RecommendingItems.get_recommending_items(data, "100")
        print("\nMovieLens RecommendingItems.get_recommending_items(data, '100')  Result:", result)

        self.assertEqual(len(result) > 0, True)


if __name__ == '__main__':
    unittest.main()
