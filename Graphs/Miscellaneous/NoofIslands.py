""" 
Number of Islands (LEETCODE 200)
Given an m X n 2D grid map of '1's (land) and '0's (water), count and return the total number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.  
"""

from collections import deque

def num_islands(grid):
    if not grid: return 0
    R, C = len(grid), len(grid[0]); seen = set(); cnt = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1' and (r, c) not in seen:
                cnt += 1; seen.add((r, c)); q = deque([(r, c)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        a, b = x+dx, y+dy
                        if 0 <= a < R and 0 <= b < C and grid[a][b] == '1' and (a, b) not in seen:
                            seen.add((a, b)); q.append((a, b))
    return cnt