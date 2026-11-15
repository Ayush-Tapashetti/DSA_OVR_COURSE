"""
Number of Provinces (LeetCode 547)
There are $n$ cities, and you are given an n X n adjacency matrix M where M[i][j] = 1 if city i and city j are directly connected, and 0 otherwise. 
Return the total number of provinces (groups of directly or indirectly connected cities). 
"""
class DSU:
    def __init__(s, n): s.p = list(range(n)); s.r = [0]*n
    def find(s, x):
        while s.p[x] != x: s.p[x] = s.p[s.p[x]]; x = s.p[x]
        return x
    def union(s, a, b):
        a, b = s.find(a), s.find(b)
        if a == b: return False
        if s.r[a] < s.r[b]: a, b = b, a
        s.p[b] = a
        if s.r[a] == s.r[b]: s.r[a] += 1
        return True

def find_circle_num(M):
    n = len(M); d = DSU(n); comps = n
    for i in range(n):
        for j in range(i+1, n):
            if M[i][j] and d.union(i, j): comps -= 1
    return comps