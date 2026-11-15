"""
Clone Graph (LEETCODE 133)
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a value (val) and a list of its neighboring nodes (neighbors).
"""

from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None): self.val = val; self.neighbors = neighbors or []
def clone_graph(node):
    if not node: return None
    copy = {node: Node(node.val)}; q = deque([node])
    while q:
        u = q.popleft()
        for v in u.neighbors:
            if v not in copy: copy[v] = Node(v.val); q.append(v)
            copy[u].neighbors.append(copy[v])
    return copy[node]
