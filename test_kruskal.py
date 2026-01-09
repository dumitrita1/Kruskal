import unittest

from kruskal import kruskal, total_weight, is_spanning_tree, nodes_from_edges


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

    def norm(self, edge):
        u, v, w = edge
        if u > v:
            u, v = v, u
        return (u, v, w)

    def test_mst_edges(self):
        mst = kruskal(self.graph)
        expected = {self.norm(e) for e in [("A", "B", 1), ("A", "C", 2), ("A", "D", 3)]}
        actual = {self.norm(e) for e in mst}
        self.assertEqual(actual, expected)

    def test_other_spanning_tree(self):
        other = [("A", "B", 1), ("A", "D", 3), ("C", "D", 6)]
        self.assertTrue(is_spanning_tree(self.graph, other))
        self.assertGreater(total_weight(other), total_weight(kruskal(self.graph)))

    def test_nodes_from_edges(self):
        nodes = nodes_from_edges(self.graph)
        self.assertEqual(nodes, {"A", "B", "C", "D"})

    def test_is_spanning_tree(self):
        mst = kruskal(self.graph)
        self.assertTrue(is_spanning_tree(self.graph, mst))


if __name__ == "__main__":
    unittest.main()
