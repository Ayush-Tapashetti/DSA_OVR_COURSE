"""
Pacific Atlantic Water Flow (LeetCode 417) -> Reverse BFS from each ocean
There is an m X n rectangular island bordering the Pacific Ocean (top and left edges) and the Atlantic Ocean (bottom and right edges), represented by a matrix h of cell heights. 
Rainwater can flow from a cell to a 4-directionally adjacent cell with a height less than or equal to its own. 
Return a sorted list of [r, c] coordinates from which rainwater can flow to both the Pacific and Atlantic oceans. 
"""

from collections import deque

def pacific_atlantic(h):
    R, C = len(h), len(h[0])
    def reach(starts):
        seen = set(starts); q = deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = r+dr, c+dc
                if 0 <= a < R and 0 <= b < C and (a, b) not in seen and h[a][b] >= h[r][c]:
                    seen.add((a, b)); q.append((a, b))
        return seen
    pac = reach([(0, c) for c in range(C)] + [(r, 0) for r in range(1, R)])
    atl = reach([(R-1, c) for c in range(C)] + [(r, C-1) for r in range(R-1)])
    return sorted(map(list, pac & atl))

