from BFS import BFS_shortest_path

def DFS(graph, start):
    status = {v: 1 for v in graph}                            # Step 1
    stack = []
    stack.append(start)                                       # Step 2
    status[start] = 2
    order = []
    while stack:                                              # Step 3
        N = stack.pop()                                       # Step 4: pop and process
        print(N, end=" ")
        order.append(N)
        status[N] = 3
        for M in graph[N]:                                    # Step 5: push ready neighbours
            if status[M] == 1:
                stack.append(M)
                status[M] = 2
    return order                                              # Step 6


def DFS_path(graph, start, dest):
    status = {v: 1 for v in graph}                            # Step 1
    orig = {v: None for v in graph}
    stack = []
    stack.append(start)                                       # Step 2
    status[start] = 2
    while stack:                                              # Step 3
        N = stack.pop()                                       # Step 4
        status[N] = 3
        if N == dest:
            break
        for M in graph[N]:                                    # Step 5
            if status[M] == 1:
                status[M] = 2
                orig[M] = N
                stack.append(M)
    path = []                                                 # Step 6: backtrack
    node = dest
    if orig[node] is None and node != start:
        return None
    while node is not None:
        path.append(node)
        node = orig[node]
    path.reverse()
    return path


def DFS_recursive(graph, node, visited=None, order=None):
    """EXTRA (not in the PDF): the classic recursive DFS. Its visiting order can differ
    from the stack version above, because the stack version marks a node 'waiting' when it is PUSHED."""
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)
    for M in graph[node]:
        if M not in visited:
            DFS_recursive(graph, M, visited, order)
    return order


def DFSfunc():
    graph = {                                                 # PDF example (directed)
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print("DFS (stack) order from A:", end=" ")
    DFS(graph, "A")
    print("   (expected A C F B E D)")
    print("DFS (recursive) order   :", " ".join(DFS_recursive(graph, "A")), "  (A B D E F C — different order, still a valid DFS)")
    print("DFS_path A → F:", DFS_path(graph, "A", "F"), "  (expected ['A', 'C', 'F'])")

    # ---- why DFS does not guarantee the SHORTEST path (PDF p.15-16) ----
    g = {"A": ["B", "F"], "B": ["C"], "C": ["D"], "D": ["E"], "E": ["I"], "F": ["I"], "I": []}
    print("\nBFS vs DFS on a graph with Path1 A→B→C→D→E→I (5) and Path2 A→F→I (2):")
    print("  BFS_shortest_path:", BFS_shortest_path(g, "A", "I"))
    g_rev = dict(g)
    g_rev["A"] = ["F", "B"]       # neighbour order flipped: the stack pops B first -> long detour
    print("  DFS_path (neighbour order [B,F]):", DFS_path(g, "A", "I"), " (got lucky: F popped first)")
    print("  DFS_path (neighbour order [F,B]):", DFS_path(g_rev, "A", "I"), " (long detour — NOT shortest)")

if __name__ == "__main__":
    DFSfunc()
    