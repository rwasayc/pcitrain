import unittest

from c2 import data, RecommendingItems


class MyTestCase(unittest.TestCase):
    def test_get_recommending_items(self):
        result = RecommendingItems.get_recommending_items(data.book_critics, 'Toby')
        print("\nRecommendingItems.get_recommending_items(data.book_critics, 'Toby')  Result:", result)

        self.assertEqual(len(result) > 0, True)


if __name__ == '__main__':
    unittest.main()
