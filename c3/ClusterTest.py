import unittest
import cProfile
from c3 import data, Cluster


class ClusterTestCase(unittest.TestCase):
    def test_hcluster(self):
        row_names, col_names, vals = data.load_data()
        result = Cluster.hcluster(vals)
        print("\nCluster.hcluster(vals)  Result:%s" % result)

    def test_pcs_benchmark(self):
        cProfile.run(
            'from c3 import data, Cluster\nrow_names, col_names, vals = data.load_data()\nCluster.hcluster(vals)')


if __name__ == '__main__':
    unittest.main()
