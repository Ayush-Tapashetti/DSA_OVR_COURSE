# Build a tree from preorder + inorder  (LC 105)
# Problem: Given preorder and inorder traversals of a tree, construct and return the binary tree.
# Idea: preorder's first item is the root; its position in inorder splits left/right.
# A value->index map makes the split O(1). O(n) time.


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Helper to validate output
def level_order(root):
    out = []
    if not root:
        return out
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
    return out

def build_tree(preorder, inorder):
    pos = {v: i for i, v in enumerate(inorder)}
    it = iter(preorder)

    def go(lo, hi):                       # inorder window [lo, hi]
        if lo > hi:
            return None
        root = TreeNode(next(it))
        m = pos[root.val]
        root.left = go(lo, m - 1)         # left BEFORE right (preorder order!)
        root.right = go(m + 1, hi)
        return root
    return go(0, len(inorder) - 1)

if __name__ == "__main__":
    t = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert level_order(t) == [[3], [9, 20], [15, 7]]
    t = build_tree([1, 2, 4, 5, 3], [4, 2, 5, 1, 3])
    assert level_order(t) == [[1], [2, 3], [4, 5]]
    print("Build Tree tests passed!!")