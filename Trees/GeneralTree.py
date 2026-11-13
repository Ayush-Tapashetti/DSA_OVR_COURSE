#GeneralTree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []           # a general tree (not binary)

    def add_child(self, child_node):
        self.children.append(child_node)


def print_tree(node, level=0):       # DFS display, indent = 2 spaces per level
    print(" " * level * 2 + str(node.value))
    for i in node.children:
        print_tree(i, level + 1)


def GeneralTree():
    root = TreeNode("A")
    b, c, d, e, f, g = (TreeNode(x) for x in "BCDEFG")
    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)
    c.add_child(g)
    print_tree(root)

if __name__ == "__main__":
    GeneralTree()
