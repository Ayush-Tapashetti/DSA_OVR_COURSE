import sys
import heapq

def dijkstra_matrix(graph, source):
    """PDF version 1 — adjacency MATRIX (0 = no edge), O(V^2)."""
    n = len(graph)

    dist = [sys.maxsize] * n                                  # Step 1: distances = infinity
    visited = [False] * n                                     # tracks nodes inserted into N (finalised)

    dist[source] = 0                                          # Step 3: label source with 0

    for _ in range(n):
        min_dist = sys.maxsize                                # Step 7: pick node not in N with smallest label
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:                                           # no more reachable nodes
            break

        visited[u] = True                                     # insert u into N

        for v in range(n):                                    # Step 5 & 6: update neighbours
            if graph[u][v] != 0 and not visited[v]:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    return dist


# ---- hand-written binary min-heap on (key, value) tuples, exactly as on PDF p.28-29 ----
def heap_push(heap, item):
    heap.append(item)
    idx = len(heap) - 1
    while idx > 0:
        parent_idx = (idx - 1) // 2
        if heap[idx][0] < heap[parent_idx][0]:
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]    # swap
            idx = parent_idx
        else:
            break


def heap_pop(heap):
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop()

    root_val = heap[0]
    heap[0] = heap.pop()

    idx = 0
    n = len(heap)
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < n and heap[left][0] < heap[smallest][0]:
            smallest = left
        if right < n and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break

    return root_val


def dijkstra_heap(vertices, graph, source):
    """PDF version 2 — adjacency LIST {u: [(v, w), ...]} + min-heap, O((V+E) log V)."""
    dist = {}                                                 # Step 1 & 2: initialise
    parent = {}
    visited = {}                                              # the finalised set 'N'

    for v in vertices:
        dist[v] = float("inf")
        parent[v] = None
        visited[v] = False

    dist[source] = 0                                          # Step 3: label source 0, push to heap
    min_heap = []
    heap_push(min_heap, (0, source))

    while len(min_heap) > 0:                                  # Step 4
        current_dist, u = heap_pop(min_heap)

        if visited[u]:                                        # already finalised -> skip (lazy deletion)
            continue

        visited[u] = True                                     # Step 7: finalise u into N

        for neighbor, weight in graph.get(u, []):             # Step 5 & 6: relax outgoing edges
            if not visited[neighbor]:
                new_distance = dist[u] + weight
                if new_distance < dist[neighbor]:             # relaxation step
                    dist[neighbor] = new_distance
                    parent[neighbor] = u
                    heap_push(min_heap, (new_distance, neighbor))

    return dist, parent


def get_path(parent, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def Dijkshtra():
    graph = [                                                 # PDF matrix (directed)  A B C D E F G
        [0, 0, 2, 0, 0, 0, 0],      # A -> C 2
        [4, 0, 0, 0, 0, 0, 0],      # B -> A 4
        [0, 0, 0, 0, 0, 0, 0],      # C
        [0, 15, 0, 0, 0, 5, 23],    # D -> B 15, F 5, G 23
        [0, 17, 0, 0, 0, 0, 11],    # E -> B 17, G 11   (row partly cut off in the PDF screenshot)
        [0, 0, 9, 0, 0, 0, 13],     # F -> C 9, G 13
        [0, 0, 0, 0, 0, 0, 0],      # G
    ]
    distances = dijkstra_matrix(graph, 3)                     # source = D (index 3)
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    print("Shortest distances from D (matrix version):\n")
    for i in range(len(distances)):
        value = distances[i]
        if value == sys.maxsize:
            value = "No_Distance"
        print(f"Distance from D to {vertices[i]} = {value}")
    print("expected: A=19 B=15 C=14 D=0 E=No_Distance F=5 G=18")

    print("\n--- Min-heap version (PDF) ---")
    nodes = ["A", "B", "C", "D", "E"]
    adj_list = {
        "D": [("A", 4), ("B", 2)],
        "A": [("B", 1), ("C", 5)],
        "B": [("C", 8), ("D", 3)],
        "C": [],
        "E": [("C", 2)],
    }
    dists, parents = dijkstra_heap(nodes, adj_list, "D")
    print("--- Dijkstra's Shortest Paths from Source: D ---")
    for node in nodes:
        d = dists[node]
        if d == float("inf"):
            print(f"To Node {node}: UNREACHABLE (no path exists)")
        else:
            path = " -> ".join(get_path(parents, node))
            print(f"To Node {node}: Cost = {d:2d} | Route: {path}")
    print("expected: A=4 (D->A)  B=2 (D->B)  C=9 (D->A->C)  D=0  E unreachable")

    # sanity check of the hand-written heap against Python's heapq
    h, ref = [], []
    for x in [5, 3, 8, 1, 9, 2, 7, 3]:
        heap_push(h, (x, "n"))
        heapq.heappush(ref, x)
    assert [heap_pop(h)[0] for _ in range(8)] == [heapq.heappop(ref) for _ in range(8)]
    print("hand-written heap_push / heap_pop agree with heapq ✔")

if __name__ == "__main__":
    Dijkshtra()
    