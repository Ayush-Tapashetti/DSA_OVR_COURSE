"""
Rotting Oranges (LeetCode 994)
You are given an m X n grid where each cell can have one of three values: 0 (empty cell), 1 (fresh orange), or 2 (rotten orange). 
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. 
Return the minimum number of minutes that must elapse until no cell has a fresh orange, or -1 if this is impossible.   
"""

from collections import deque

def oranges_rotting(grid):
    R, C = len(grid), len(grid[0]); q = deque(); fresh = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: q.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    t = 0; g = [row[:] for row in grid]
    while q:
        r, c, t = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            a, b = r+dr, c+dc
            if 0 <= a < R and 0 <= b < C and g[a][b] == 1:
                g[a][b] = 2; fresh -= 1; q.append((a, b, t+1))
    return t if fresh == 0 else -1