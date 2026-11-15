"""
Cheapest Flights Within K Stops (LeetCode 787)
There are $n$ cities connected by flights given as [u, v, w] (from u to v with price w).
Given a starting city src, destination dst, and integer k, return the cheapest price from src to dst with at most k intermediate stops, or -1 if no such route exists.  
"""

def cheapest_flight(n, flights, src, dst, k):
    INF = float('inf'); dist = [INF]*n; dist[src] = 0
    for _ in range(k+1):
        nd = dist[:]
        for u, v, w in flights:
            if dist[u] + w < nd[v]: nd[v] = dist[u] + w
        dist = nd
    return -1 if dist[dst] == INF else dist[dst]