# 6. RED-BLACK TREE

RED, BLACK = "R", "B"


class RBNode:
    def __init__(self, key, color=RED, nil=None):
        self.key = key
        self.color = color
        self.left = nil
        self.right = nil
        self.parent = nil


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, BLACK)           # Property 3: NIL leaves are BLACK
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root = self.NIL

    # ---- rotations (same pointer logic as AVL) ----
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        # Step 1: normal BST insert, new node RED
        z = RBNode(key, RED, self.NIL)
        parent, cur = self.NIL, self.root
        while cur != self.NIL:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return                           # duplicate ignored
        z.parent = parent
        if parent == self.NIL:
            self.root = z
        elif key < parent.key:
            parent.left = z
        else:
            parent.right = z
        self._fix_insert(z)

    def _fix_insert(self, z):
        # Case 2: parent is RED -> Red-Red violation
        while z.parent.color == RED:
            P = z.parent
            G = P.parent
            if P == G.left:
                U = G.right
                if U.color == RED:               # Case 2.1: uncle RED -> recolor, move up
                    P.color = BLACK
                    U.color = BLACK
                    G.color = RED
                    z = G
                else:                            # Case 2.2: uncle BLACK/NIL
                    if z == P.right:             # triangle (inner) -> rotate P to make a line
                        z = P
                        self._left_rotate(z)
                        P = z.parent
                    P.color = BLACK              # line (outer): rotate G, recolor
                    G.color = RED
                    self._right_rotate(G)
            else:                                # mirror image
                U = G.left
                if U.color == RED:
                    P.color = BLACK
                    U.color = BLACK
                    G.color = RED
                    z = G
                else:
                    if z == P.left:
                        z = P
                        self._right_rotate(z)
                        P = z.parent
                    P.color = BLACK
                    G.color = RED
                    self._left_rotate(G)
        self.root.color = BLACK                  # Case 1 / Property 2: root always BLACK

    # ---- helpers ----
    def inorder(self):
        out = []
        def go(n):
            if n != self.NIL:
                go(n.left); out.append(n.key); go(n.right)
        go(self.root)
        return out

    def show(self):
        def go(n, lvl=0, side="root"):
            if n != self.NIL:
                go(n.right, lvl + 1, "R")
                print("      " * lvl + f"{n.key}({n.color})" + ("" if side == "root" else f" <{side}"))
                go(n.left, lvl + 1, "L")
        go(self.root)

    def height(self):
        def h(n):
            return 0 if n == self.NIL else 1 + max(h(n.left), h(n.right))
        return h(self.root)

    def validate(self):
        """Check all 5 properties. Returns (ok, black_height)."""
        if self.root.color != BLACK:                       # P2
            return False
        def walk(n):
            if n == self.NIL:                              # P3
                return True, 1
            if n.color not in (RED, BLACK):                # P1
                return False, 0
            if n.color == RED and (n.left.color == RED or n.right.color == RED):   # P4
                return False, 0
            okl, bl = walk(n.left)
            okr, br = walk(n.right)
            if not (okl and okr) or bl != br:              # P5
                return False, 0
            return True, bl + (1 if n.color == BLACK else 0)
        return walk(self.root)[0]


def RedblackTree():
    t = RedBlackTree()
    for k in [10, 20, 30, 40, 50, 25]:
        t.insert(k)
    print("Inserted 10,20,30,40,50,25 ; inorder =", t.inorder())
    t.show()
    print("All 5 RB properties hold:", t.validate())

    t2 = RedBlackTree()
    for k in range(1, 1024):
        t2.insert(k)
    print(f"Sorted insert 1..1023 -> height {t2.height()} (<= 2*log2(n+1) = 20), valid={t2.validate()}")


if __name__ == "__main__":
    RedblackTree()