def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
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

def delete_first(start):
    if start is None:
        print("Underflow")
        return None
    if start.next is None:
        return None
    start = start.next
    start.prev = None
    return start


def delete_last(start):
    if start is None:
        print("Underflow")
        return None
    if start.next is None:
        return None
    ptr = start
    while ptr.next is not None:
        ptr = ptr.next
    ptr.prev.next = None
    return start


def delete_val(start, target_val):
    if start is None:
        print("Underflow")
        return None
    if start.data == target_val:
        return delete_first(start)
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None:
        print("Target value not found")
        return start
    ptr.prev.next = ptr.next
    if ptr.next is not None:
        ptr.next.prev = ptr.prev
    return start


def demo_dll_deletions():
    section("4.3 DLL Deletion — 3 cases")

    start = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    start.next = n2
    n2.prev = start
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3

    print("Original list:              ", end="")
    traverse_forward(start)

    start = delete_first(start)
    print("After delete_first():   ", end="")
    traverse_forward(start)

    start = delete_last(start)
    print("After delete_last():    ", end="")
    traverse_forward(start)

    start = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    start.next = n2
    n2.prev = start
    n2.next = n3
    n3.prev = n2

    start = delete_val(start, 20)
    print("After delete_val(20):   ", end="")
    traverse_forward(start)

if __name__ == "__main__":
    demo_dll_deletions()

