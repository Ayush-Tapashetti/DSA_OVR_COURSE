"""
Course Schedule I and II (LEETCODE 207 and 210)
There are n courses labeled from 0 to n - 1, and you are given an array of prerequisite pairs [a, b] indicating that you must take course b before course a.
    Course Schedule I (can_finish): Return True if you can finish all courses (i.e., there are no cyclic dependencies), or False otherwise.   
    Course Schedule II (find_order): Return a valid ordering of courses you should take to finish all courses, or an empty list [] if it is impossible.  
"""

from collections import deque, defaultdict

def find_order(n, prereqs):
    adj = defaultdict(list); indeg = [0]*n
    for a, b in prereqs: adj[b].append(a); indeg[a] += 1
    q = deque(i for i in range(n) if indeg[i] == 0); order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
    return order if len(order) == n else []
def can_finish(n, prereqs): return len(find_order(n, prereqs)) == n