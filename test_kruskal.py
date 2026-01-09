import unittest

from kruskal import kruskal, total_weight, is_spanning_tree


class TestKruskalSimple(unittest.TestCase):
    def setUp(self):
        self.graph = [
            ("A", "B", 1),
            ("A", "C", 2),
            ("A", "D", 3),
            ("B", "C", 4),
            ("B", "D", 5),
            ("C", "D", 6),
        ]

    def test_mst_weight(self):
        mst = kruskal(self.graph)
        self.assertEqual(total_weight(mst), 6)

    def test_is_spanning_tree(self):
        mst = kruskal(self.graph)
        self.assertTrue(is_spanning_tree(self.graph, mst))


if __name__ == "__main__":
    unittest.main()
