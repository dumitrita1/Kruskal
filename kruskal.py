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


def main() -> None:
	g = [("A","B",1),("A","C",2),("A","D",3),("B","C",4),("B","D",5),("C","D",6)]
	print("Graph:", g)
	print("MST:", kruskal(g))


if __name__ == "__main__":
	main()


