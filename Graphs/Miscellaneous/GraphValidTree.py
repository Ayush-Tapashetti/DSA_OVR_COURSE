"""
Graph Valid Tree (LeetCode 261)
You have a graph of n nodes labeled from 0 to n - 1 and a list of undirected edges. 
Return True if these edges make up a valid tree (i.e., the graph is fully connected and contains no cycles), and False otherwise.   
"""

from Provinces import DSU

def valid_tree(n, edges):
    if len(edges) != n-1: return False
    d = DSU(n)
    return all(d.union(a, b) for a, b in edges)