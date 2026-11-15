"""
Network Delay Time (LeetCode 743)
You are given a network of $n$ nodes labeled 1 to n and a list of directed travel times [u, v, w] where w is the time it takes for a signal to travel from u to v. 
Return the minimum time it takes for all $n$ nodes to receive a signal sent from node k, or -1 if it is impossible for all nodes to receive it.
"""

from collections import defaultdict
import heapq

def network_delay(times, n, k):
    adj = defaultdict(list)
    for u, v, w in times: adj[u].append((v, w))
    dist = {}; h = [(0, k)]
    while h:
        d, u = heapq.heappop(h)
        if u in dist: continue
        dist[u] = d
        for v, w in adj[u]:
            if v not in dist: heapq.heappush(h, (d+w, v))
    return max(dist.values()) if len(dist) == n else -1