import unittest

from c2 import data, TopMatches


class TopMatchesTestCase(unittest.TestCase):
    def test_top_matches(self):
        result = TopMatches.top_matches(data.book_critics, 'Lisa Rose', 2)
        print("\nTopMatches.top_matches(data.book_critics, 'Lisa Rose', 2)  Result:", result)

        self.assertEqual(len(result), 2)

        result = TopMatches.top_matches(data.book_critics, 'Lisa Rose', 3)
        print("\nTopMatches.top_matches(data.book_critics, 'Lisa Rose', 3)  Result:", result)

        self.assertEqual(len(result), 3)

        tdata = data.transform_data(data.book_critics)
        result = TopMatches.top_matches(tdata, 'Lady in the Water', 3)
        print("\nTopMatches.top_matches(tdata, 'Lady in the Water', 3)  Result:", result)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
