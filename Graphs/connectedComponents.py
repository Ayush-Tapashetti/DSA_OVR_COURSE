from collections import deque
from Graphrep import build_adj_list

def connected_components(adj):
    """Undirected adjacency list {v: [neighbours]} -> list of components (BFS from each unseen vertex)."""
    seen, comps = set(), []
    for s in adj:
        if s in seen:
            continue
        comp, q = [], deque([s])
        seen.add(s)
        while q:
            u = q.popleft()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        comps.append(comp)
    return comps


def connectedComps():
    adj = build_adj_list(list("ABCDEFG"), [("A", "B"), ("B", "C"), ("D", "E"), ("F", "G")])
    adj["H"] = []                                             # an isolated node (degree 0)
    comps = connected_components(adj)
    print("Components:", comps, "  (expected 4 groups: [A,B,C] [D,E] [F,G] [H])")
    print("Isolated nodes (degree 0):", [v for v in adj if len(adj[v]) == 0])


if __name__ == "__main__":
    connectedComps()
    