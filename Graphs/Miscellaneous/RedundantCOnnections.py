"""
Redundant Connection (LeetCode 684)
Given an undirected graph that started as a tree with n nodes (labeled 1 to n) and had one additional edge added,
find and return the edge [a, b] that can be removed so that the resulting graph is a tree of n nodes.   
"""

from Provinces import DSU

def find_redundant(edges):
    d = DSU(len(edges)+1)
    for a, b in edges:
        if not d.union(a, b): return [a, b]