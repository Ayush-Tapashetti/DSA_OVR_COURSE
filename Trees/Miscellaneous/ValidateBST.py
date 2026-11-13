# Validate BST  (LC 98)
# Problem: Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Idea: every node must lie inside an (low, high) window that tightens as we go down.
# Why not just compare with children? A grandchild can violate an ancestor.
# O(n) time, O(h) space


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


def is_valid_bst(root, low=float("-inf"), high=float("inf")):
    if root is None:
        return True
    
    if not (low < root.val < high):
        return False
    
    return is_valid_bst(root.left, low, root.val) and is_valid_bst(root.right, root.val, high)

if __name__ == "__main__":
    
    assert is_valid_bst(build([5, 3, 8, 2, 4, 7, 9]))
    assert not is_valid_bst(build([5, 1, 4, None, None, 3, 6]))
    assert not is_valid_bst(build([10, 5, 15, None, None, 6, 20]))      # 6 is in the right of 10
    assert is_valid_bst(None)

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
        assert is_valid_bst(root)
    
    print("Validate BST tests passed!! ")
