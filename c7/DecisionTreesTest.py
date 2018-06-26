import unittest, cProfile
from c7 import data, DecisionTrees


class DecisionTreesTestCase(unittest.TestCase):
    def test_divide_set(self):
        (set1, set2) = DecisionTrees.divide_set(data.example_data, 2, 'yes')
        print(
            "\nDecisionTrees.divide_set(data.example_data, 2, 'yes')  \nSet1:", set1, "\nSet2:", set2)

    def test_divide_set_benchmark(self):
        cProfile.run(
            'from c7 import data, DecisionTrees\nDecisionTrees.divide_set(data.example_data, 2, "yes")')

    def test_gini_impurity(self):
        result = DecisionTrees.gini_impurity(data.example_data)
        print(
            "\nDecisionTrees.gini_impurity(data.example_data)  \nResult:", result)

    def test_gini_impurity_benchmark(self):
        cProfile.run(
            'from c7 import data, DecisionTrees\nDecisionTrees.gini_impurity(data.example_data)')

    def test_entropy(self):
        result = DecisionTrees.entropy(data.example_data)
        print(
            "\nDecisionTrees.entropy(data.example_data)  \nResult:", result)

    def test_entropy_benchmark(self):
        cProfile.run(
            'from c7 import data, DecisionTrees\nDecisionTrees.entropy(data.example_data)')

    def test_build_trees(self):
        result = DecisionTrees.build_trees(data.example_data)
        DecisionTrees.print_tree(result)

    def test_build_trees_benchmark(self):
        cProfile.run(
            'from c7 import data, DecisionTrees\nDecisionTrees.build_trees(data.example_data)')

    def test_classify(self):
        tree = DecisionTrees.build_trees(data.example_data)
        DecisionTrees.print_tree(tree)
        result = DecisionTrees.classify(['(direct)', 'USA', 'yes', 5], tree)
        print(
            "\nDecisionTrees.classify(['(direct)', 'USA', 'yes', 5], tree) \nResult:", result)

    def test_classify_benchmark(self):
        cProfile.run(
            'from c7 import data, DecisionTrees\nDecisionTrees.build_trees(data.example_data)\nDecisionTrees.classify(["(direct)", "USA", "yes", 5], tree)')


if __name__ == '__main__':
    unittest.main()
