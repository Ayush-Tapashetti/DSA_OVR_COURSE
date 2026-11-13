# Lowest common ancestor in a binary tree  (LC 236)
# Problem: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Idea: post-order. A node returns itself if it is p or q; if both sides return
# something non-null, THIS node is the split point = LCA.
# O(n) time, O(h) space


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

def find(root, v):
    if not root: return None
    if root.val == v: return root
    return find(root.left, v) or find(root.right, v)

def lowest_common_ancestor(root, p, q):
    if root is None or root is p or root is q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right

if __name__ == "__main__":
    t = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(t, find(t, 5), find(t, 1)).val == 3
    assert lowest_common_ancestor(t, find(t, 5), find(t, 4)).val == 5
    assert lowest_common_ancestor(t, find(t, 6), find(t, 4)).val == 5
    print(" Lowest Common Ancestor tests passed !!")