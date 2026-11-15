import sys

def a_star_matrix(graph, source, goal, h):
    n = len(graph)

    g = [sys.maxsize] * n                                     # Step 1: actual cost from source
    f = [sys.maxsize] * n                                     #         total estimated cost f = g + h
    visited = [False] * n                                     #         finalised nodes
    parent = [-1] * n                                         #         to reconstruct the path

    g[source] = 0                                             # Step 2 & 3
    f[source] = g[source] + h[source]

    for _ in range(n):
        min_f = sys.maxsize                                   # Step 4: unvisited node with smallest f
        u = -1
        for i in range(n):
            if not visited[i] and f[i] < min_f:
                min_f = f[i]
                u = i

        if u == -1:                                           # no reachable node left
            break

        if u == goal:                                         # early termination: target reached!
            visited[u] = True
            break

        visited[u] = True

        for v in range(n):                                    # relax neighbours
            if graph[u][v] != 0 and not visited[v]:
                new_g = g[u] + graph[u][v]
                if new_g < g[v]:
                    g[v] = new_g
                    f[v] = g[v] + h[v]
                    parent[v] = u

    return g, parent


def reconstruct_path(parent, source, goal):
    if parent[goal] == -1 and source != goal:
        return "No Path"
    path = []
    curr = goal
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def a_star_trace(graph, source, goal, h, names):
    """Same algorithm with a print for every expansion (shows the order A* picks nodes)."""
    n = len(graph)
    g = [sys.maxsize] * n
    f = [sys.maxsize] * n
    visited = [False] * n
    g[source], f[source] = 0, h[source]
    order = []
    for _ in range(n):
        u = min((i for i in range(n) if not visited[i] and f[i] < sys.maxsize), key=lambda i: f[i], default=-1)
        if u == -1:
            break
        order.append(names[u])
        print(f"  expand {names[u]}: g={g[u]} h={h[u]} f={f[u]}")
        if u == goal:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not visited[v] and g[u] + graph[u][v] < g[v]:
                g[v] = g[u] + graph[u][v]
                f[v] = g[v] + h[v]
    return order


def Astar():
    node_names = ["A", "B", "C", "D", "E"]                    # 0..4, go from A (0) to E (4)
    graph = [                                                 # 0 = no direct edge
        # A  B  C  D  E
        [0, 4, 2, 0, 0],    # A
        [0, 0, 1, 5, 0],    # B
        [0, 0, 0, 8, 10],   # C
        [0, 0, 0, 0, 2],    # D
        [0, 0, 0, 0, 0],    # E
    ]
    h_values = [7, 6, 5, 2, 0]                                # h(E) must be 0
    src, dest = 0, 4

    g_costs, parent_ptrs = a_star_matrix(graph, src, dest, h_values)
    path_indices = reconstruct_path(parent_ptrs, src, dest)
    named_path = " -> ".join([node_names[i] for i in path_indices])
    print(f"--- A* Matrix Search from {node_names[src]} to {node_names[dest]} ---")
    print(f"Optimal Total Cost: {g_costs[dest]}")
    print(f"Shortest Path: {named_path}")
    print("expected: cost 11, path A -> B -> D -> E")

    print("\nExpansion order (A* always expands the smallest f = g + h):")
    order = a_star_trace(graph, src, dest, h_values, node_names)
    print("  order:", order)

    zero_h = [0] * 5
    gz, pz = a_star_matrix(graph, src, dest, zero_h)
    print(f"With h = 0 everywhere A* behaves like Dijkstra: cost {gz[dest]}, path "
          + " -> ".join(node_names[i] for i in reconstruct_path(pz, src, dest)))
    _, p_back = a_star_matrix(graph, 4, 0, h_values)           # E -> A has no path
    print("A* with an unreachable goal (E → A):", reconstruct_path(p_back, 4, 0))


if __name__ == "__main__":
    Astar()
    