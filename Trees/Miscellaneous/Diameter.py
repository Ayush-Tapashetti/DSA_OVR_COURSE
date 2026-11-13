# Diameter of a binary tree  (LC 543)
# Problem: Given the root of a binary tree, return the length of the longest path between any two nodes.
# Idea: the longest path through a node = height(left) + height(right).
# Compute heights bottom-up and track the best. O(n)


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

def diameter(root):
    best = 0

    def h(n):
        nonlocal best
        if not n:
            return 0
        l, r = h(n.left), h(n.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    h(root)
    return best

if __name__ == "__main__":
    assert diameter(build([1, 2, 3, 4, 5])) == 3
    assert diameter(build([1, 2])) == 1
    assert diameter(None) == 0
    print("Diameter tests passed!!")