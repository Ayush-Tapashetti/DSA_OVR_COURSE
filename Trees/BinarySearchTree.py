#BinarySearchTree

from BinaryTreeandTraversal import bst_insert, inorder

def bst_search(ROOT, item):
    if ROOT is None:
        return False
    if item == ROOT.data:
        return True
    elif item < ROOT.data:
        return bst_search(ROOT.left, item)
    else:
        return bst_search(ROOT.right, item)


def findMin(node):
    while node.left:
        node = node.left
    return node


def bst_delete(ROOT, item):
    if ROOT is None:
        return ROOT
    if item < ROOT.data:
        ROOT.left = bst_delete(ROOT.left, item)
    elif item > ROOT.data:
        ROOT.right = bst_delete(ROOT.right, item)
    else:                            # node found
        # Case A: no child
        if ROOT.left is None and ROOT.right is None:
            return None
        # Case B: one child
        if ROOT.left is None:
            return ROOT.right
        if ROOT.right is None:
            return ROOT.left
        # Case C: two children -> inorder successor
        minNode = findMin(ROOT.right)
        ROOT.data = minNode.data
        ROOT.right = bst_delete(ROOT.right, minNode.data)
    return ROOT


def countNodes(TREE):
    if TREE is None:
        return 0
    return countNodes(TREE.left) + countNodes(TREE.right) + 1


def build_bst(values):
    ROOT = None
    for v in values:
        ROOT = bst_insert(ROOT, v)
    return ROOT


def BinarySearchTree():
    values = [50, 30, 20, 40, 70, 60, 80]
    ROOT = build_bst(values)

    print("Inorder Traversal (Sorted):", end=" ")
    inorder(ROOT)
    print("   (expected 20 30 40 50 60 70 80)")

    print("search(40) ->", bst_search(ROOT, 40), "  (expected True)")
    print("search(90) ->", bst_search(ROOT, 90), "  (expected False)")

    print("Total Nodes in BST =", countNodes(ROOT), "  (expected 7)")

    print("Original Inorder :", end=" ")
    inorder(ROOT)
    print()
    
    ROOT = bst_delete(ROOT, 20)      # leaf
    ROOT = bst_delete(ROOT, 30)      # one child (40 after 20 removed)
    ROOT = bst_delete(ROOT, 50)      # two children (root)
    
    print("After Deletions  :", end=" ");
    inorder(ROOT)
    print("   (expected 40 60 70 80)")
    
    print("Root after deleting 50 (successor 60):", ROOT.data)

if __name__ == "__main__":
    BinarySearchTree()