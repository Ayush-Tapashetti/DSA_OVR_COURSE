def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)
    
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def traverse_forward(start):
    ptr = start
    while ptr is not None:
        print(ptr.data, end=" <-> ")
        ptr = ptr.next
    print("None")

def insert_at_beginning(start, val):
    new_node = DNode(val)
    new_node.next = start
    if start is not None:
        start.prev = new_node
    start = new_node
    return start


def insert_at_end(start, val):
    new_node = DNode(val)
    if start is None:
        return new_node
    ptr = start
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = new_node
    new_node.prev = ptr
    return start


def insert_after_node(start, target_val, val):
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None:
        print("Target node not found")
        return start
    new_node = DNode(val)
    new_node.next = ptr.next
    new_node.prev = ptr
    if ptr.next is not None:
        ptr.next.prev = new_node
    ptr.next = new_node
    return start


def insert_before_node(start, target_val, val):
    if start is None:
        return start
    if start.data == target_val:            # inserting before the head
        new_node = DNode(val)
        new_node.next = start
        start.prev = new_node
        return new_node
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None:
        print("Target node not found")
        return start
    new_node = DNode(val)
    new_node.next = ptr
    new_node.prev = ptr.prev
    ptr.prev.next = new_node
    ptr.prev = new_node
    return start


def insertions():
    section("4.2 DLL Insertion — 4 cases")

    start = DNode(20)
    start.next = DNode(30)
    start.next.prev = start
    print("Original list:                    ", end="")
    traverse_forward(start)

    start = insert_at_beginning(start, 10)
    print("After insert_at_beginning_dll(10):", end="")
    traverse_forward(start)

    start = insert_at_end(start, 40)
    print("After insert_at_end_dll(40):      ", end="")
    traverse_forward(start)

    start = insert_after_node(start, 20, 25)
    print("After insert_after_node_dll(20,25):", end="")
    traverse_forward(start)

    start = insert_before_node(start, 30, 27)
    print("After insert_before_node_dll(30,27):", end="")
    traverse_forward(start)

if __name__ == "__main__":
    insertions()
