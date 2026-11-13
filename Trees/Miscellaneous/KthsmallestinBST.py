# Kth smallest in a BST  (LC 230)
# Problem: Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed).
# Idea: in-order of a BST is sorted -> stop at the kth visit (iterative, early exit).
# O(h + k) time

import random
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build(level):
    if not level or level[0] is None:
        return None
    
    root = TreeNode(level[0])
    q, i = deque([root]), 1
    
    while q and i < len(level):
        n = q.popleft()
        if i < len(level) and level[i] is not None:
            n.left = TreeNode(level[i]); q.append(n.left)
        i += 1
    
        if i < len(level) and level[i] is not None:
            n.right = TreeNode(level[i]); q.append(n.right)
        i += 1
    
    return root


def kth_smallest(root, k):
    stack, cur = [], root
    
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
    
        if k == 0:
            return cur.val
        cur = cur.right

if __name__ == "__main__":
    
    t = build([5, 3, 6, 2, 4, None, None, 1])
    assert [kth_smallest(t, k) for k in range(1, 7)] == [1, 2, 3, 4, 5, 6]

    # Randomised tests
    random.seed(3)
    
    for _ in range(300):
        vals = random.sample(range(100), random.randint(1, 30))
        root = None
    
        def ins(n, v):
            if not n: return TreeNode(v)
    
            if v < n.val: n.left = ins(n.left, v)
    
            else: n.right = ins(n.right, v)
            return n
    
        for v in vals:
            root = ins(root, v)
        s = sorted(vals)
        assert all(kth_smallest(root, i + 1) == s[i] for i in range(len(s)))
    
    print("Kth Smallest tests passed!! ")