

def build_adj_matrix(n, edges, directed=False, weighted=False):
    """ edges = [u, v] or [u, v, w]. MAT[u][v] = 1 (or w)."""
    MAT = [[0 for _ in range(n)] for _ in range(n)]           # Step 1: n x n zeros
    for e in edges:                                           # Step 2
        u, v = e[0], e[1]
        val = e[2] if weighted else 1
        MAT[u][v] = val
        if not directed:
            MAT[v][u] = val
    return MAT                                                # Step 3


def build_adj_list(vertices, edges, directed=False, weighted=False):
    adj = {v: [] for v in vertices}                           # Step 2: empty list per vertex
    for e in edges:                                           # Step 3
        if weighted:
            u, v, w = e
            adj[u].append((v, w))
            if not directed:
                adj[v].append((u, w))
        else:
            u, v = e
            adj[u].append(v)
            if not directed:
                adj[v].append(u)
    return adj                                                # Step 4


def degrees(adj):
    """Return {v: (indeg, outdeg, deg)} for a DIRECTED adjacency list (unweighted)."""
    out = {v: len(adj[v]) for v in adj}
    ind = {v: 0 for v in adj}
    for u in adj:
        for v in adj[u]:
            ind[v] += 1
    return {v: (ind[v], out[v], ind[v] + out[v]) for v in adj}


def GraphicalRep():
    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
    matrix = [[0 for _ in range(n)] for _ in range(n)]        # Step 1
    for u, v in edges:                                        # Step 2
        matrix[u][v] = 1
        matrix[v][u] = 1                                      # undirected
    print("Adjacency matrix (PDF example):")
    for row in matrix:                                        # Step 3
        print(row)
    print("expected: [0,1,1,0,0] [1,0,0,1,1] [1,0,0,0,0] [0,1,0,0,0] [0,1,0,0,0]")

    # ---- the four matrices in the PDF figure, rebuilt from their edge lists ----
    A, B, C, D, E = range(5)
    print("\n(a) Directed graph  [A→B, A→D, B→D, C→B, D→E, E→B]:")
    for r in build_adj_matrix(5, [[A, B], [A, D], [B, D], [C, B], [D, E], [E, B]], directed=True):
        print("  ", r)
    print("(c) Undirected graph [A-B, A-D, B-C, B-D, C-E, D-E]  (symmetric matrix):")
    for r in build_adj_matrix(5, [[A, B], [A, D], [B, C], [B, D], [C, E], [D, E]]):
        print("  ", r)
    print("(d) Weighted directed graph [A→B 4, A→D 2, B→D 7, C→B 5, D→E 3, E→C 1]:")
    for r in build_adj_matrix(5, [[A, B, 4], [A, D, 2], [B, D, 7], [C, B, 5], [D, E, 3], [E, C, 1]],
                              directed=True, weighted=True):
        print("  ", r)

    # ---- PDF code: adjacency list, undirected ----
    vertices = ["A", "B", "C", "D", "E"]
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("D", "E")]
    adj = {v: [] for v in vertices}                           # Step 1: empty lists
    for u, v in edges:                                        # Step 2 (undirected)
        adj[u].append(v)
        adj[v].append(u)
    print("\nAdjacency list (PDF example):")
    for v in vertices:                                        # Step 3: textbook format
        print(v, "→", " | ".join(adj[v]))
    print("expected: A → B | C   B → A | D   C → A   D → B | E   E → D")

    # ---- PDF code: weighted adjacency list ----
    edges_w = [("A", "B", 4), ("A", "D", 3), ("B", "C", 2), ("D", "E", 5)]
    adjw = {v: [] for v in vertices}
    for u, v, w in edges_w:
        adjw[u].append((v, w))
        adjw[v].append((u, w))                                # remove this line for directed graph
    print("\nWeighted adjacency list (PDF example):")
    for v in vertices:
        print(v, "→", adjw[v])
    print("expected: A → [('B',4),('D',3)]  B → [('A',4),('C',2)]  C → [('B',2)]  D → [('A',3),('E',5)]  E → [('D',5)]")

    # ---- degrees ----
    d_adj = build_adj_list(vertices, [("A", "B"), ("A", "D"), ("B", "D"), ("C", "B"), ("D", "E"), ("E", "B")], directed=True)
    print("\nDegrees of the directed graph (indeg, outdeg, deg = indeg + outdeg):")
    for v, t in degrees(d_adj).items():
        print(f"  {v}: indeg={t[0]} outdeg={t[1]} deg={t[2]}")
    print("Sum of all degrees =", sum(t[2] for t in degrees(d_adj).values()), "= 2 × edges (6) →", 2 * 6)


if __name__ == "__main__":
    GraphicalRep()
    
