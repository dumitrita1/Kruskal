from typing import List, Tuple, Set

Edge = Tuple[str, str, int]


def nodes_from_edges(edges: List[Edge]) -> Set[str]:
	nodes: Set[str] = set()
	for u, v, _ in edges:
		nodes.add(u)
		nodes.add(v)
	return nodes


def total_weight(edges: List[Edge]) -> int:
	return sum(w for _, _, w in edges)


def kruskal(edges: List[Edge]) -> List[Edge]:
	nodes = nodes_from_edges(edges)

	parent = {n: n for n in nodes}

	def find(x: str) -> str:
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	def union(a: str, b: str) -> bool:
		ra = find(a)
		rb = find(b)
		if ra == rb:
			return False
		parent[rb] = ra
		return True

	mst: List[Edge] = []
	for u, v, w in sorted(edges, key=lambda e: e[2]):
		if union(u, v):
			mst.append((u, v, w))
			if len(mst) == len(nodes) - 1:
				break
	return mst


def is_spanning_tree(graph_edges: List[Edge], tree_edges: List[Edge]) -> bool:
	nodes = nodes_from_edges(graph_edges)
	if len(tree_edges) != len(nodes) - 1:
		return False

	graph_set = {(min(u, v), max(u, v), w) for u, v, w in graph_edges}
	for u, v, w in tree_edges:
		if (min(u, v), max(u, v), w) not in graph_set:
			return False

	parent = {n: n for n in nodes}

	def find2(x: str) -> str:
		if parent[x] != x:
			parent[x] = find2(parent[x])
		return parent[x]

	for u, v, _ in tree_edges:
		ru = find2(u)
		rv = find2(v)
		if ru != rv:
			parent[rv] = ru

	roots = {find2(n) for n in nodes}
	return len(roots) == 1


if __name__ == "__main__":
	g: List[Edge] = [
		("A", "B", 1),
		("A", "C", 2),
		("A", "D", 3),
		("B", "C", 4),
		("B", "D", 5),
		("C", "D", 6),
	]
	print("Graph edges:", g)
	mst = kruskal(g)
	print("MST:", mst)
	print("Total weight:", total_weight(mst))


