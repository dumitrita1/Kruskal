from typing import List, Tuple

Edge = Tuple[str, str, int]


def kruskal(edges: List[Edge]) -> List[Edge]:
	nodes = set()
	for u, v, _ in edges:
		nodes.add(u); nodes.add(v)

	parent = {n: n for n in nodes}

	def find(x: str) -> str:
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	def union(a: str, b: str) -> bool:
		ra = find(a); rb = find(b)
		if ra == rb: return False
		parent[rb] = ra
		return True

	mst: List[Edge] = []
	for u, v, w in sorted(edges, key=lambda e: e[2]):
		if union(u, v):
			mst.append((u, v, w))
			if len(mst) == len(nodes) - 1: break
	return mst


def nodes_from_edges(edges: List[Edge]) -> set:
	#die Menge der Knoten zurück
	nodes = set()
	for u, v, _ in edges:
		nodes.add(u); nodes.add(v)
	return nodes


def total_weight(edges: List[Edge]) -> int:
	# summiert die Gewichte
	return sum(w for _, _, w in edges)


def is_spanning_tree(graph_edges: List[Edge], tree_edges: List[Edge]) -> bool:
	nodes = nodes_from_edges(graph_edges)
	if len(tree_edges) != len(nodes) - 1:
		return False

	# prüfen Verbindung mit Union-Find
	parent = {n: n for n in nodes}

	def find(x: str) -> str:
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]
	# prüfen Baumkanten im Graph sind
	graph_set = {(min(u, v), max(u, v), w) for u, v, w in graph_edges}
	for u, v, w in tree_edges:
		if (min(u, v), max(u, v), w) not in graph_set:
			return False
		ru = find(u); rv = find(v)
		if ru != rv:
			parent[rv] = ru

	roots = {find(n) for n in nodes}
	return len(roots) == 1


def main() -> None:
	g = [("A","B",1),("A","C",2),("A","D",3),("B","C",4),("B","D",5),("C","D",6)]
	print("Graph:", g)
	print("MST:", kruskal(g))


if __name__ == "__main__":
	main()


