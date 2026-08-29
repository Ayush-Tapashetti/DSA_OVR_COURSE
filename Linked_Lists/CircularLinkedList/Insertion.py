def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(start):
    if start is None:
        print("List is empty")
        return
    ptr = start
    while True:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
        if ptr == start:        # completed the full circle
            break
    print("(HEAD)")

def insert_at_beginning(start, val):
    new_node = Node(val)
    if start is None:
        new_node.next = new_node       # points to itself
        return new_node
    ptr = start
    while ptr.next != start:            # find last node
        ptr = ptr.next
    new_node.next = start
    ptr.next = new_node                 # last node now points to new head
    start = new_node
    return start


def insert_at_end(start, val):
    new_node = Node(val)
    if start is None:
        new_node.next = new_node
        return new_node
    ptr = start
    while ptr.next != start:
        ptr = ptr.next
    ptr.next = new_node
    new_node.next = start               # close the circle again
    return start


def insert_after_node(start, target_val, val):
    if start is None:
        print("List is empty")
        return start
    new_node = Node(val)
    ptr, found = start, False
    while True:
        if ptr.data == target_val:
            found = True
            break
        ptr = ptr.next
        if ptr == start:
            break
    if not found:
        print("Target node not found")
        return start
    new_node.next = ptr.next
    ptr.next = new_node
    return start


def insertions():
    section("3.2 CLL Insertion — 3 cases")

    start = None
    start = insert_at_beginning(start, 10)   # first node, list was empty
    print("After first insert (10):        ", end="")
    traverse(start)

    start = insert_at_beginning(start, 5)
    print("After insert_at_beginning(5):", end="")
    traverse(start)

    start = insert_at_end(start, 20)
    print("After insert_at_end(20):    ", end="")
    traverse(start)

    start = insert_after_node(start, 10, 15)
    print("After insert_after_node(10,15):", end="")
    traverse(start)

if __name__ == "__main__":
    insertions()
