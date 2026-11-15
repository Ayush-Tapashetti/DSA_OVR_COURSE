import sys
import random
from Graphrep import build_adj_list
from DFS import DFS
from BFS import BFS
from BFS import BFS_shortest_path
from DFS import DFS_path
from Astar import a_star_matrix
from Dijkshtra import dijkstra_matrix
from Dijkshtra import dijkstra_heap
from Dijkshtra import get_path
from connectedComponents import connected_components
from minspanningtree import kruskal
from minspanningtree import prims


def _floyd(n, W):
    INF = float("inf")
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
        for j in range(n):
            if W[i][j]:
                d[i][j] = W[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def algotests():
    random.seed(7)
    import io
    import contextlib
    quiet = lambda: contextlib.redirect_stdout(io.StringIO())

    for trial in range(300):
        n = random.randint(2, 9)
        # ---------- random weighted directed graph (matrix, 0 = no edge)
        W = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and random.random() < 0.35:
                    W[i][j] = random.randint(1, 20)
        fw = _floyd(n, W)
        src = random.randrange(n)
        inf = float("inf")

        # Dijkstra matrix vs Floyd-Warshall
        dm = dijkstra_matrix(W, src)
        for v in range(n):
            exp = fw[src][v]
            got = dm[v] if dm[v] != sys.maxsize else inf
            assert exp == got, (trial, "dijkstra matrix", W, src, v)

        # Dijkstra heap vs Floyd-Warshall
        names = list(range(n))
        adj = {u: [(v, W[u][v]) for v in range(n) if W[u][v]] for u in range(n)}
        dh, par = dijkstra_heap(names, adj, src)
        for v in range(n):
            assert dh[v] == fw[src][v]
            if dh[v] != inf:
                p = get_path(par, v)
                assert p[0] == src and p[-1] == v
                assert sum(W[a][b] for a, b in zip(p, p[1:])) == dh[v]

        # A*: h = 0 and h = exact (perfect heuristic) both give the optimal cost
        goal = random.randrange(n)
        gz, pz = a_star_matrix(W, src, goal, [0] * n)
        exp = fw[src][goal]
        if exp == inf:
            assert gz[goal] == sys.maxsize
        else:
            assert gz[goal] == exp
            exact = [fw[v][goal] if fw[v][goal] != inf else 10 ** 6 for v in range(n)]
            ge, pe = a_star_matrix(W, src, goal, [min(x, 10 ** 6) for x in exact])
            assert ge[goal] == exp

        # BFS shortest path (unweighted) vs Floyd on unit weights
        U = [[1 if W[i][j] else 0 for j in range(n)] for i in range(n)]
        fu = _floyd(n, U)
        g_adj = {u: [v for v in range(n) if U[u][v]] for u in range(n)}
        with quiet():
            p = BFS_shortest_path(g_adj, src, goal)
        if fu[src][goal] == inf:
            assert p is None
        else:
            assert p is not None and len(p) - 1 == fu[src][goal]
        with quiet():
            order = BFS(g_adj, src)
        assert set(order) == {v for v in range(n) if fu[src][v] != inf}     # BFS reaches exactly the reachable set
        with quiet():
            order = DFS(g_adj, src)
        assert set(order) == {v for v in range(n) if fu[src][v] != inf}     # ... and so does DFS
        with quiet():
            p = DFS_path(g_adj, src, goal)
        if fu[src][goal] == inf:
            assert p is None
        else:
            assert p[0] == src and p[-1] == goal and all(U[a][b] for a, b in zip(p, p[1:]))

        # ---------- random connected undirected graph: Prim == Kruskal == brute-force MST weight
        m = random.randint(2, 7)
        M = [[0] * m for _ in range(m)]
        for v in range(1, m):                                 # random spanning tree guarantees connectivity
            u = random.randrange(v)
            w = random.randint(1, 15)
            M[u][v] = M[v][u] = w
        for i in range(m):
            for j in range(i + 1, m):
                if M[i][j] == 0 and random.random() < 0.4:
                    M[i][j] = M[j][i] = random.randint(1, 15)
        with quiet():
            _, wp = prims(M)
        es = [[i, j, M[i][j]] for i in range(m) for j in range(i + 1, m) if M[i][j]]
        wk = sum(e[2] for e in kruskal(m, list(es)))
        assert wp == wk, (trial, "prim != kruskal", M)
        if m <= 6:                                            # brute force over all (m-1)-edge subsets
            from itertools import combinations
            best = inf
            for combo in combinations(es, m - 1):
                par = list(range(m))
                def fnd(x):
                    while par[x] != x:
                        x = par[x]
                    return x
                ok = True
                for u, v, w in combo:
                    a, b = fnd(u), fnd(v)
                    if a == b:
                        ok = False
                        break
                    par[a] = b
                if ok:
                    best = min(best, sum(e[2] for e in combo))
            assert best == wp, (trial, "mst != brute force")

    # ---------- connected components
    adj = build_adj_list(list(range(8)), [(0, 1), (1, 2), (3, 4), (6, 7)])
    assert sorted(map(sorted, connected_components(adj))) == [[0, 1, 2], [3, 4], [5], [6, 7]]
    print("300 random graphs: Dijkstra (matrix + heap) = Floyd-Warshall, A* optimal (h=0 and exact h),")
    print("BFS/DFS reach exactly the reachable set, BFS path = fewest edges, Prim = Kruskal = brute-force MST ✔")

if __name__ == "__main__":
    algotests()