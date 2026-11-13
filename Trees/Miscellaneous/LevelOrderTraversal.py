# Level-order, grouped by level  (LC 102)
# Problem: Given the root of a binary tree, return the level order traversal of its nodes' values.
# Idea: BFS; freeze len(queue) at the start of each round = one level.
# O(n) time, O(w) space


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

if __name__ == "__main__":
    assert level_order(build([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(None) == []
    print("Level Order tests passed!!")