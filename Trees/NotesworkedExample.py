#Worked Examples
from BinaryTreeandTraversal import Node, preorder, inorder, postorder, levelOrder, bst_insert

def Examples():
    
    
    # ---- Figure (a): traversals ----
    #            A
    #          /   \
    #         B     C
    #        / \     \
    #       D   E     F
    #      / \       / \
    #     G   H     I   J
    #          \         /
    #           L       K
    
    n = {c: Node(c) for c in "ABCDEFGHIJKL"}
    n["A"].left, n["A"].right = n["B"], n["C"]
    n["B"].left, n["B"].right = n["D"], n["E"]
    n["C"].right = n["F"]
    n["D"].left, n["D"].right = n["G"], n["H"]
    n["H"].right = n["L"]
    n["F"].left, n["F"].right = n["I"], n["J"]
    n["J"].left = n["K"]          # K is J's LEFT child (matches PDF in-order ... I F K J)
    
    a = n["A"]
    
    print("Figure (a)")
    print(" Pre  :", end=" ")
    preorder(a)
    print("  (PDF: A B D G H L E C F I J K)")
    
    print(" In   :", end=" ")
    inorder(a)
    print("  (PDF: G D H L B E A C I F K J)")
    
    print(" Post :", end=" ")
    postorder(a)
    print("  (PDF: G L H D E B I K J F C A)")
    
    print(" Level:", end=" ")
    levelOrder(a)
    print("  (PDF: A B C D E F G H I J L K)")

   
   
    # ---- Figure (b) ----
    #        A
    #       / \
    #      B   C
    #     /   /
    #    D   E
    #         \
    #          F
    #         /
    #        G
    #       / \
    #      H   I
    
    m = {c: Node(c) for c in "ABCDEFGHI"}
    
    m["A"].left, m["A"].right = m["B"], m["C"]
    m["B"].left = m["D"]             # in-order starts D B A ... so D is B's left child
    m["C"].left = m["E"]
    m["E"].right = m["F"]
    m["F"].left = m["G"]
    m["G"].left, m["G"].right = m["H"], m["I"]
    
    b = m["A"]
    print("Figure (b)")
    
    print(" Pre  :", end=" ")
    preorder(b)
    print("  (PDF: A B D C E F G H I)")
    
    print(" In   :", end=" ")
    inorder(b)
    print("  (PDF: D B A E H G I F C)")
    
    print(" Post :", end=" ")
    postorder(b)
    print("  (PDF: D B H I G F E C A)")
    
    print(" Level:", end=" ")
    levelOrder(b)
    print("  (PDF: A B C D E F G H I)")

    # ---- BST construction example: insert one by one ----
    seq = [45, 39, 56, 12, 34, 78, 32, 10, 89, 54, 67, 81]
    ROOT = None
    print("BST construction from", seq)
    for i, v in enumerate(seq, 1):
        ROOT = bst_insert(ROOT, v)
        print(f"  Step {i:2d}: insert {v:2d}  level-order = ", end="")
        levelOrder(ROOT)
        print()
    
    print("  Final inorder (sorted):", end=" ")
    inorder(ROOT)
    print()

if __name__ == "__main__":
    Examples()