def BFS(graph, start):
    status = {v: 1 for v in graph}                            # Step 1: 1 = ready
    queue = []
    queue.append(start)                                       # Step 2: enqueue start
    status[start] = 2                                         #         2 = waiting
    order = []
    while queue:                                              # Step 3
        N = queue.pop(0)                                      # Step 4: dequeue and process
        print(N, end=" ")
        order.append(N)
        status[N] = 3                                         #         3 = processed
        for v in graph[N]:                                    # Step 5: enqueue ready neighbours
            if status[v] == 1:
                queue.append(v)
                status[v] = 2
    return order                                              # Step 6: exit


def BFS_shortest_path(graph, start, dest):
    status = {v: 1 for v in graph}                            # Step 1: STATUS and ORIG
    orig = {v: None for v in graph}                           #         predecessor
    queue = []
    queue.append(start)                                       # Step 2
    status[start] = 2
    while queue:                                              # Step 3
        N = queue.pop(0)                                      # Step 4
        status[N] = 3
        if N == dest:                                         #         destination found -> Step 6
            break
        for M in graph[N]:                                    # Step 5
            if status[M] == 1:
                status[M] = 2
                orig[M] = N                                   #         record predecessor
                queue.append(M)
    path = []                                                 # Step 6: backtrack
    node = dest
    if orig[node] is None and node != start:                  # no path exists
        return None
    while node is not None:
        path.append(node)
        node = orig[node]
    path.reverse()
    return path


def bfs_trace(graph, start, dest):
    """Reproduces the FRONT / REAR / QUEUE / ORIG tables of the PDF illustration (p.8-9)."""
    status = {v: 1 for v in graph}
    queue, orig = [start], [None]                             # QUEUE and ORIG are parallel arrays
    status[start] = 2
    front, rear = 0, 0
    show = lambda: ['NULL'] + orig[1:]
    print(f"(a) FRONT={front} REAR={rear} QUEUE={queue} ORIG={show()}")
    while front <= rear:
        N = queue[front]
        status[N] = 3
        front += 1
        for M in graph[N]:
            if status[M] == 1:
                status[M] = 2
                queue.append(M)
                orig.append(N)
                rear += 1
        print(f"    dequeued {N}: FRONT={front} REAR={rear} QUEUE={queue} ORIG={show()}")
        if dest in queue:          # PDF figure (g): stop as soon as the destination is ENQUEUED
            break
    return queue, orig


def BFSfunc():
    graph = {                                                 # PDF example (undirected)
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print("BFS order from A:", end=" ")
    BFS(graph, "A")
    print("   (expected A B C D E F)")

    path = BFS_shortest_path(graph, "A", "F")
    print("Shortest Path:", path, "  (expected ['A', 'C', 'F'])")

    # ---- the 9-node directed illustration (adjacency lists on PDF p.8) ----
    g9 = {"A": ["B", "C", "D"], "B": ["E"], "C": ["B", "G"], "D": ["C", "G"], "E": ["C", "F"],
          "F": ["C", "H"], "G": ["F", "H", "I"], "H": ["E", "I"], "I": ["F"]}
    print("\nPDF illustration — minimum path A → I (QUEUE / ORIG trace):")
    bfs_trace(g9, "A", "I")
    print("Path:", " -> ".join(BFS_shortest_path(g9, "A", "I")), "  (expected A -> C -> G -> I)")
    print("No-path case, A → Z:", BFS_shortest_path({"A": [], "Z": []}, "A", "Z"), "  (expected None)")

if __name__ == "__main__":
    BFSfunc()
    