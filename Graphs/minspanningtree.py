import sys

def prims(graph):
    """PDF code. graph = adjacency MATRIX (0 = no edge). Starts at vertex 0. O(V^2)."""
    n = len(graph)

    selected = [False] * n                                    # MST set
    key = [sys.maxsize] * n                                   # shortest edge weight to the tree
    parent = [-1] * n                                         # to store MST edges

    key[0] = 0                                                # start from vertex 0

    for i in range(n - 1):
        min_value = sys.maxsize                               # select the min-key vertex not in MST
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_value:
                min_value = key[v]
                u = v

        selected[u] = True

        for v in range(n):                                    # update keys of its neighbours
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge  : Weight")                                   # print the MST edges
    for i in range(1, n):
        print(parent[i], "-", i, ":", graph[i][parent[i]])
    return parent, sum(graph[i][parent[i]] for i in range(1, n))


def prim_trace(adj, start):
    """Reproduces the 'Tree vertices | Remaining vertices' table of the PDF (p.18).
    adj = {v: {neighbour: weight}}. Each remaining vertex shows (nearest tree vertex, weight)."""
    INF = float("inf")
    key = {v: (None, INF) for v in adj}
    key[start] = (None, 0)
    in_tree, total, edges = set(), 0, []
    while len(in_tree) < len(adj):
        u = min((v for v in adj if v not in in_tree), key=lambda v: key[v][1])
        in_tree.add(u)
        if key[u][0] is not None:
            edges.append((key[u][0], u, key[u][1]))
            total += key[u][1]
        shown = ", ".join(f"{v}({key[v][0] or '-'},{key[v][1] if key[v][1] != INF else '∞'})"
                          for v in adj if v not in in_tree)
        label = f"{u}({key[u][0] or '-'},{key[u][1] if key[u][1] else '-'})"
        print(f"  tree += {label:8s} | remaining: {shown}")
        for v, w in adj[u].items():
            if v not in in_tree and w < key[v][1]:
                key[v] = (u, w)
    return edges, total


# ---- Kruskal: Union-Find exactly as in the PDF (union by rank, no path compression) ----
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])                            # no path compression (simple version)


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def kruskal(vertices, edges):
    """vertices = number of vertices ; edges = list of [u, v, weight]"""
    parent = [i for i in range(vertices)]                     # Step 1: forest
    rank = [0] * vertices
    edges.sort(key=lambda x: x[2])                            # Step 2: sort by weight (stable)
    mst = []
    for u, v, w in edges:                                     # Step 3: process edges one by one
        if find(parent, u) != find(parent, v):                # Step 5: connects two different trees?
            mst.append([u, v, w])
            union(parent, rank, u, v)
        if len(mst) == vertices - 1:                          # stop at V-1 edges
            break
    return mst


def kruskal_trace(names, edges):
    """Verbose Kruskal showing ACCEPT / REJECT, like the PDF's sorted-edge-list illustration."""
    idx = {nm: i for i, nm in enumerate(names)}
    parent = list(range(len(names)))
    rank = [0] * len(names)
    es = sorted(edges, key=lambda e: e[2])
    print("  sorted:", " ".join(f"{u}{v}={w}" for u, v, w in es))
    total, count = 0, 0
    for u, v, w in es:
        if find(parent, idx[u]) != find(parent, idx[v]):
            union(parent, rank, idx[u], idx[v])
            total += w
            count += 1
            print(f"  {u}{v} ({w}) → ACCEPT   (total {total})")
            if count == len(names) - 1:
                break
        else:
            print(f"  {u}{v} ({w}) → reject  (would form a cycle)")
    return total


def minspantree():
    graph = [                                                 # PDF example (adjacency matrix)
        [0, 6, 0, 4, 0, 0, 0],   # A
        [6, 0, 7, 8, 6, 0, 0],   # B
        [0, 7, 0, 0, 4, 0, 0],   # C
        [4, 8, 0, 0, 14, 5, 0],  # D
        [0, 6, 4, 14, 0, 7, 8],  # E
        [0, 0, 0, 5, 7, 0, 10],  # F
        [0, 0, 0, 0, 8, 10, 0],  # G
    ]
    print("--- Prim (matrix) ---")
    parent, total = prims(graph)
    print("MST weight =", total, "  (expected edges 0-1:6 4-2:4 0-3:4 1-4:6 3-5:5 4-6:8 → 33)")

    print("\n--- Prim trace, PDF Example 1 (vertices a-f) ---")
    adj = {
        "a": {"b": 3, "f": 5, "e": 6},
        "b": {"a": 3, "c": 1, "f": 4},
        "c": {"b": 1, "f": 4, "d": 6},
        "d": {"c": 6, "f": 5, "e": 8},
        "e": {"a": 6, "d": 8, "f": 2},
        "f": {"a": 5, "b": 4, "c": 4, "d": 5, "e": 2},
    }
    edges, total = prim_trace(adj, "a")
    print("  MST edges:", edges, " total =", total, "(expected 15: ab3 bc1 bf4 fe2 fd5)")

    print("\n--- Prim, PDF Example 3 (vertices A-E) ---")
    adj3 = {"A": {"B": 7, "C": 3}, "B": {"A": 7, "C": 4, "D": 9, "E": 11}, "C": {"A": 3, "B": 4, "D": 10},
            "D": {"B": 9, "C": 10}, "E": {"B": 11}}
    edges, total = prim_trace(adj3, "A")
    print("  MST total =", total, "(expected 27: AC3 CB4 BD9 BE11)")

    print("\n--- Kruskal (PDF code) ---")
    edges = [
        [0, 1, 7],   # A - B
        [0, 2, 6],   # A - C
        [0, 3, 1],   # A - D
        [1, 2, 8],   # B - C
        [2, 3, 5],   # C - D
        [2, 4, 3],   # C - E
        [3, 4, 4],   # D - E
        [3, 5, 5],   # D - F
        [4, 5, 2],   # E - F
    ]
    mst = kruskal(6, edges)
    print("MST edges (u - v : weight):")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("expected: 0-3:1  4-5:2  2-4:3  3-4:4  0-1:7   → total", sum(w for _, _, w in mst), "(17)")

    print("\n--- Kruskal trace, PDF example (vertices a-f) ---")
    ex = [("b", "c", 1), ("e", "f", 2), ("a", "b", 3), ("b", "f", 4), ("c", "f", 4), ("a", "f", 5),
          ("d", "f", 5), ("a", "e", 6), ("c", "d", 6), ("d", "e", 8)]
    t = kruskal_trace(list("abcdef"), ex)
    print("  MST total =", t, "(expected 15 — same as Prim ✔)")

    print("\n--- Spanning trees of the PDF's 4-vertex weighted graph ---")
    from itertools import combinations
    K4 = {("A", "B"): 3, ("A", "C"): 4, ("A", "D"): 7, ("B", "C"): 5, ("B", "D"): 6, ("C", "D"): 2}
    trees = []
    for combo in combinations(K4, 3):
        p = {x: x for x in "ABCD"}
        def f(x):
            while p[x] != x:
                x = p[x]
            return x
        ok = True
        for a, b in combo:
            if f(a) == f(b):
                ok = False
                break
            p[f(a)] = f(b)
        if ok:
            trees.append((sum(K4[e] for e in combo), combo))
    trees.sort()
    print(f"  K4 has {len(trees)} spanning trees (Cayley: 4^2 = 16). Cheapest three:")
    for cost, combo in trees[:3]:
        print("   cost", cost, combo)
    print("  All 16 costs:", [c for c, _ in trees], "  (PDF figure shows 9, 10, 11, 12, 14, 15 ...)")

if __name__ == "__main__":
    minspantree()
    