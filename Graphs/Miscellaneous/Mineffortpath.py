"""
Path With Minimum Effort (LeetCode 1631)
You are given a 2D grid h of heights.
Starting at the top-left cell (0, 0) and moving 4-directionally to reach the bottom-right cell (R - 1, C - 1),
a route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from top-left to bottom-right.
"""

import heapq

def min_effort(h):
    R, C = len(h), len(h[0]); best = [[float('inf')]*C for _ in range(R)]; best[0][0] = 0; pq = [(0, 0, 0)]
    while pq:
        e, r, c = heapq.heappop(pq)
        if (r, c) == (R-1, C-1): return e
        if e > best[r][c]: continue
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            a, b = r+dr, c+dc
            if 0 <= a < R and 0 <= b < C:
                ne = max(e, abs(h[a][b]-h[r][c]))
                if ne < best[a][b]: best[a][b] = ne; heapq.heappush(pq, (ne, a, b))