#AVL TREE

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if not node:
        return 0
    return node.height


def right_rotate(y):                 # fixes LL
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x                         # new root


def left_rotate(x):                  # fixes RR
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y                         # new root


def get_balance(node):               # BF = height(left) - height(right)
    if not node:
        return 0
    return height(node.left) - height(node.right)


def avl_insert(node, key):
    # 1. normal BST insertion
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = avl_insert(node.left, key)
    elif key > node.key:
        node.right = avl_insert(node.right, key)
    else:
        return node                  # equal keys not allowed

    # 2. update height
    node.height = 1 + max(height(node.left), height(node.right))
    # 3. balance factor
    balance = get_balance(node)

    # 4. four cases
    if balance > 1 and key < node.left.key:       # Left Left
        return right_rotate(node)
    
    if balance < -1 and key > node.right.key:     # Right Right
        return left_rotate(node)
    
    if balance > 1 and key > node.left.key:       # Left Right
        node.left = left_rotate(node.left)
        return right_rotate(node)
    
    if balance < -1 and key < node.right.key:     # Right Left
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node


def pre_order(root):
    if root:
        print(root.key, end=" ")
        pre_order(root.left)
        pre_order(root.right)


def avl_show(root, level=0, side="root"):      # sideways text picture with balance factors
    if root:
        avl_show(root.right, level + 1, "R")
        print("      " * level + f"{root.key}(bf={get_balance(root):+d})" + ("" if side == "root" else f" <{side}"))
        avl_show(root.left, level + 1, "L")


def avl_is_valid(node):
    """True if every node is a BST node and |BF| <= 1 and stored heights are right."""
    def check(n, lo, hi):
        if not n:
            return True, 0
        if not (lo < n.key < hi):
            return False, 0
        okl, hl = check(n.left, lo, n.key)
        okr, hr = check(n.right, n.key, hi)
        ok = okl and okr and abs(hl - hr) <= 1 and n.height == 1 + max(hl, hr)
        return ok, 1 + max(hl, hr)
    return check(node, float("-inf"), float("inf"))[0]


def AVLTREE():
    root = None
    for k in (10, 20, 30, 40, 50, 25):
        root = avl_insert(root, k)
    print("Preorder (PDF driver) :", end=" "); pre_order(root)
    print("   (expected 30 20 10 25 40 50)")

    # --- the 4 rotation cases on 3 nodes ---
    cases = {
        "LL (30,20,10)": [30, 20, 10],
        "RR (10,20,30)": [10, 20, 30],
        "LR (30,10,20)": [30, 10, 20],
        "RL (10,30,20)": [10, 30, 20],
    }
    for name, seq in cases.items():
        r = None
        for k in seq:
            r = avl_insert(r, k)
        print(f"{name:14s} -> root={r.key}, left={r.left.key}, right={r.right.key}   (all become 10-20-30 with 20 at root)")

    # --- Example 10.6 ---
    seq = [63, 9, 19, 27, 18, 108, 99, 81]
    print("\nExample 10.6 — insert", seq)
    r = None
    for k in seq:
        r = avl_insert(r, k)
        print(f"  after {k:3d}: preorder = ", end=""); pre_order(r); print(f"   valid={avl_is_valid(r)}")
    print("Final tree (sideways, right at top):")
    avl_show(r)
    print("Expected final: root 19; left 9 (left-child of 9 is none, right 18); right 63 -> 27 and 99(81,108)")

    # --- sorted input stays balanced (this is the whole point) ---
    r = None
    for k in range(1, 128):
        r = avl_insert(r, k)
    print(f"\nInsert 1..127 in sorted order -> height = {height(r)} (a plain BST would be 127), valid={avl_is_valid(r)}")

if __name__ == "__main__":
    AVLTREE()