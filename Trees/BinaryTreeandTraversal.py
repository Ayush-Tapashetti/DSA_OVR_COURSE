#BinaryTree and Traversal

from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def preorder(TREE):                  # Root -> Left -> Right
    if TREE is None:
        return
    print(TREE.data, end=" ")
    preorder(TREE.left)
    preorder(TREE.right)


def inorder(TREE):                   # Left -> Root -> Right  (sorted for a BST)
    if TREE is None:
        return
    inorder(TREE.left)
    print(TREE.data, end=" ")
    inorder(TREE.right)


def postorder(TREE):                 # Left -> Right -> Root
    if TREE is None:
        return
    postorder(TREE.left)
    postorder(TREE.right)
    print(TREE.data, end=" ")


def levelOrder(ROOT):                # BFS using a queue
    if ROOT is None:
        return
    queue = []                       # list as queue (as in the PDF)
    queue.append(ROOT)               # enqueue
    while len(queue) > 0:
        node = queue.pop(0)          # dequeue
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def levelOrder_deque(ROOT):          # same thing, O(1) dequeue (better practice)
    if ROOT is None:
        return
    q = deque([ROOT])
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def bst_insert(ROOT, item):
    if ROOT is None:
        return Node(item)
    if item < ROOT.data:
        ROOT.left = bst_insert(ROOT.left, item)
    elif item > ROOT.data:
        ROOT.right = bst_insert(ROOT.right, item)
    return ROOT                      # duplicates are ignored


def BinaryTreeTraversal():
    A, B, C, D, E = (Node(x) for x in "ABCDE")
    A.left, A.right = B, C
    B.left, B.right = D, E
    #        A
    #       / \
    #      B   C
    #     / \
    #    D   E
    
    
    print("Pre-order  :", end=" ")
    preorder(A)
    print("   (expected A B D E C)")
    
    print("In-order   :", end=" ")
    inorder(A)
    print("   (expected D B E A C)")
    
    print("Post-order :", end=" ")
    postorder(A)
    print("   (expected D E B C A)")
    
    print("Level-order:", end=" ")
    levelOrder(A)
    print("   (expected A B C D E)")

    # Level order on the BST from the PDF
    ROOT = None
    for v in [50, 30, 20, 40, 70, 60, 80]:
        ROOT = bst_insert(ROOT, v)
    print("Level Order Traversal:", end=" ")
    levelOrder(ROOT)
    print("   (expected 50 30 70 20 40 60 80)")
    
    print("Level Order (deque)  :", end=" ")
    levelOrder_deque(ROOT)
    print()

if __name__ == "__main__":
    BinaryTreeTraversal()