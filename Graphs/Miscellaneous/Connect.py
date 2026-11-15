"""
Min Cost to Connect All Points (LeetCode 1584)
You are given an array points representing integer coordinates [x, y] of points on a 2D plane. 
The cost of connecting two points is the Manhattan distance |x_1 - x_2| + |y_1 - y_2|. 
Return the minimum total cost to make all points connected such that there is exactly one simple path between any two points.
"""

def min_cost_connect(points):
    n = len(points); INF = float('inf'); key = [INF]*n; key[0] = 0; used = [False]*n; tot = 0
    for _ in range(n):
        u = min((i for i in range(n) if not used[i]), key=lambda i: key[i])
        used[u] = True; tot += key[u]
        for v in range(n):
            if not used[v]:
                d = abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
                if d < key[v]: key[v] = d
    return tot