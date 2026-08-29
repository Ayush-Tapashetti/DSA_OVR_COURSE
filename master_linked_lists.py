"""
MASTER CODE — Linked Lists
==========================
Every code example from Linked_Lists_Summary.md, expanded into a fully
self-contained, runnable version — each with its own Node class (where
needed), sample data, and printed output so you can run this file directly
and see every concept work.

Run:  python master_linked_lists.py
"""

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# =====================================================================
# 1. OOP RECAP — Node anatomy
# =====================================================================
def demo_oop_recap():
    section("1. OOP Recap — Node anatomy")

    class Node:
        def __init__(self, data):          # constructor: runs automatically on creation
            self.data = data                # stores the value
            self.next = None                # "pointer" (reference) to the next Node

    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2                      # node1 now "points to" node2

    print("node1.data:", node1.data)
    print("node1.next.data:", node1.next.data)   # 20 — reached via the pointer


# =====================================================================
# 2. SINGLY LINKED LIST (SLL)
# =====================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(start, end_label="None"):
    """Utility used by every demo below to display a list's contents."""
    ptr = start
    out = []
    while ptr is not None:
        out.append(str(ptr.data))
        ptr = ptr.next
    print(" -> ".join(out) + " -> " + end_label if out else end_label)


def demo_sll_build_and_traverse():
    section("2.1 Building an SLL manually + traversal")

    # Step 1: create nodes
    first = Node(10)
    second = Node(20)
    third = Node(30)

    # Step 2: link them
    first.next = second
    second.next = third

    # Step 3: define head
    head = first

    # Step 4: traverse and print
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def search_linked_list(start, val):
    ptr = start
    while ptr is not None:
        if val == ptr.data:
            return ptr          # found — return the node
        ptr = ptr.next
    return None                  # not found


def demo_sll_search():
    section("2.2 Searching an SLL (Linear Search — O(n))")

    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)

    result = search_linked_list(start, 20)
    print("Search for 20:", result.data if result else "Not found")

    result = search_linked_list(start, 99)
    print("Search for 99:", result.data if result else "Not found")


def insert_at_beginning(start, val):
    new_node = Node(val)
    new_node.next = start   # point to old head
    start = new_node        # new node becomes head
    return start


def insert_at_end(start, val):
    new_node = Node(val)
    if start is None:
        return new_node
    ptr = start
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = new_node
    return start


def insert_after_node(start, target_val, val):
    new_node = Node(val)
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None:
        print("Target node not found")
        return start
    new_node.next = ptr.next   # new node points to what used to come after target
    ptr.next = new_node        # target now points to new node
    return start


def insert_before_node(start, target_val, val):
    if start is None:
        return start
    new_node = Node(val)
    if start.data == target_val:            # target is the very first node
        new_node.next = start
        return new_node
    ptr, prevptr = start, None
    while ptr is not None and ptr.data != target_val:
        prevptr = ptr
        ptr = ptr.next
    if ptr is None:
        print("Target node not found")
        return start
    new_node.next = ptr
    prevptr.next = new_node
    return start


def demo_sll_insertions():
    section("2.3 SLL Insertion — 4 cases")

    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    print("Original list:      ", end="")
    print_list(start)

    start = insert_at_beginning(start, 5)
    print("After insert_at_beginning(5):    ", end="")
    print_list(start)

    start = insert_at_end(start, 40)
    print("After insert_at_end(40):         ", end="")
    print_list(start)

    start = insert_after_node(start, 20, 25)
    print("After insert_after_node(20, 25): ", end="")
    print_list(start)

    start = insert_before_node(start, 30, 27)
    print("After insert_before_node(30, 27):", end="")
    print_list(start)


def delete_first(start):
    if start is None:
        print("Underflow")
        return None
    return start.next     # simply move head forward; old node is discarded


def delete_last(start):
    if start is None:
        print("Underflow")
        return None
    if start.next is None:       # only one node
        return None
    ptr, prevptr = start, None
    while ptr.next is not None:
        prevptr = ptr
        ptr = ptr.next
    prevptr.next = None
    return start


def delete_after_node(start, target_val):
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None or ptr.next is None:
        print("Node cannot be deleted")
        return start
    ptr.next = ptr.next.next     # skip over the node being removed
    return start


def delete_val(start, target_val):
    if start is None:
        print("Underflow")
        return None
    if start.data == target_val:            # deleting the head itself
        return start.next
    ptr, prevptr = start, None
    while ptr is not None and ptr.data != target_val:
        prevptr = ptr
        ptr = ptr.next
    if ptr is None:
        print("Target value not found")
        return start
    prevptr.next = ptr.next
    return start


def demo_sll_deletions():
    section("2.4 SLL Deletion — 4 cases")

    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    start.next.next.next = Node(40)
    print("Original list:                 ", end="")
    print_list(start)

    start = delete_first(start)
    print("After delete_first():          ", end="")
    print_list(start)

    start = delete_last(start)
    print("After delete_last():           ", end="")
    print_list(start)

    # rebuild for the remaining demos
    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    start.next.next.next = Node(40)

    start = delete_after_node(start, 20)
    print("After delete_after_node(20):   ", end="")
    print_list(start)

    start = delete_val(start, 40)
    print("After delete_val(40):          ", end="")
    print_list(start)


# =====================================================================
# 3. CIRCULAR LINKED LIST (CLL)
# =====================================================================
def traverse_cll(start):
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


def demo_cll_traverse():
    section("3.1 Circular Linked List — build + traverse")

    start = Node(10)
    second = Node(20)
    third = Node(30)
    start.next = second
    second.next = third
    third.next = start          # close the circle

    traverse_cll(start)


def insert_at_beginning_cll(start, val):
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


def insert_at_end_cll(start, val):
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


def insert_after_node_cll(start, target_val, val):
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


def demo_cll_insertions():
    section("3.2 CLL Insertion — 3 cases")

    start = None
    start = insert_at_beginning_cll(start, 10)   # first node, list was empty
    print("After first insert (10):        ", end="")
    traverse_cll(start)

    start = insert_at_beginning_cll(start, 5)
    print("After insert_at_beginning_cll(5):", end="")
    traverse_cll(start)

    start = insert_at_end_cll(start, 20)
    print("After insert_at_end_cll(20):    ", end="")
    traverse_cll(start)

    start = insert_after_node_cll(start, 10, 15)
    print("After insert_after_node_cll(10,15):", end="")
    traverse_cll(start)


def delete_first_cll(start):
    if start is None:
        print("Underflow")
        return None
    if start.next == start:             # only one node
        return None
    ptr = start
    while ptr.next != start:
        ptr = ptr.next
    start = start.next
    ptr.next = start                    # last node -> new head
    return start


def delete_last_cll(start):
    if start is None:
        print("Underflow")
        return None
    if start.next == start:
        return None
    ptr, prevptr = start, None
    while ptr.next != start:
        prevptr = ptr
        ptr = ptr.next
    prevptr.next = start                # second-to-last now points to head
    return start


def delete_val_cll(start, target_val):
    if start is None:
        print("Underflow")
        return None
    if start.data == target_val:
        return delete_first_cll(start)
    ptr, prevptr, found = start, None, False
    while True:
        if ptr.data == target_val:
            found = True
            break
        prevptr = ptr
        ptr = ptr.next
        if ptr == start:
            break
    if not found:
        print("Target node not found")
        return start
    prevptr.next = ptr.next
    return start


def demo_cll_deletions():
    section("3.3 CLL Deletion — 3 cases")

    # build 5 -> 10 -> 15 -> 20 -> (back to 5)
    start = Node(5)
    n2 = Node(10)
    n3 = Node(15)
    n4 = Node(20)
    start.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = start

    print("Original list:                  ", end="")
    traverse_cll(start)

    start = delete_first_cll(start)
    print("After delete_first_cll():       ", end="")
    traverse_cll(start)

    start = delete_last_cll(start)
    print("After delete_last_cll():        ", end="")
    traverse_cll(start)

    start = delete_val_cll(start, 15)
    print("After delete_val_cll(15):       ", end="")
    traverse_cll(start)


# =====================================================================
# 4. DOUBLY LINKED LIST (DLL)
# =====================================================================
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


def traverse_backward(start):
    if start is None:
        return
    ptr = start
    while ptr.next is not None:      # first walk to the tail
        ptr = ptr.next
    while ptr is not None:            # then walk back using .prev
        print(ptr.data, end=" <-> ")
        ptr = ptr.prev
    print("None")


def demo_dll_traverse():
    section("4.1 DLL — build + forward/backward traversal")

    first = DNode(10)
    second = DNode(20)
    third = DNode(30)
    first.next = second
    second.prev = first
    second.next = third
    third.prev = second

    start = first
    print("Forward: ", end="")
    traverse_forward(start)
    print("Backward:", end="")
    traverse_backward(start)


def insert_at_beginning_dll(start, val):
    new_node = DNode(val)
    new_node.next = start
    if start is not None:
        start.prev = new_node
    start = new_node
    return start


def insert_at_end_dll(start, val):
    new_node = DNode(val)
    if start is None:
        return new_node
    ptr = start
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = new_node
    new_node.prev = ptr
    return start


def insert_after_node_dll(start, target_val, val):
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


def insert_before_node_dll(start, target_val, val):
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


def demo_dll_insertions():
    section("4.2 DLL Insertion — 4 cases")

    start = DNode(20)
    start.next = DNode(30)
    start.next.prev = start
    print("Original list:                    ", end="")
    traverse_forward(start)

    start = insert_at_beginning_dll(start, 10)
    print("After insert_at_beginning_dll(10):", end="")
    traverse_forward(start)

    start = insert_at_end_dll(start, 40)
    print("After insert_at_end_dll(40):      ", end="")
    traverse_forward(start)

    start = insert_after_node_dll(start, 20, 25)
    print("After insert_after_node_dll(20,25):", end="")
    traverse_forward(start)

    start = insert_before_node_dll(start, 30, 27)
    print("After insert_before_node_dll(30,27):", end="")
    traverse_forward(start)


def delete_first_dll(start):
    if start is None:
        print("Underflow")
        return None
    if start.next is None:
        return None
    start = start.next
    start.prev = None
    return start


def delete_last_dll(start):
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


def delete_val_dll(start, target_val):
    if start is None:
        print("Underflow")
        return None
    if start.data == target_val:
        return delete_first_dll(start)
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

    start = DNode(10)
    n2 = DNode(20)
    n3 = DNode(30)
    n4 = DNode(40)
    start.next = n2
    n2.prev = start
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3

    print("Original list:              ", end="")
    traverse_forward(start)

    start = delete_first_dll(start)
    print("After delete_first_dll():   ", end="")
    traverse_forward(start)

    start = delete_last_dll(start)
    print("After delete_last_dll():    ", end="")
    traverse_forward(start)

    # rebuild for delete_val demo
    start = DNode(10)
    n2 = DNode(20)
    n3 = DNode(30)
    start.next = n2
    n2.prev = start
    n2.next = n3
    n3.prev = n2

    start = delete_val_dll(start, 20)
    print("After delete_val_dll(20):   ", end="")
    traverse_forward(start)


# =====================================================================
# RUN EVERYTHING
# =====================================================================
if __name__ == "__main__":
    demo_oop_recap()
    demo_sll_build_and_traverse()
    demo_sll_search()
    demo_sll_insertions()
    demo_sll_deletions()
    demo_cll_traverse()
    demo_cll_insertions()
    demo_cll_deletions()
    demo_dll_traverse()
    demo_dll_insertions()
    demo_dll_deletions()
    print("\n" + "=" * 70)
    print("ALL LINKED LIST DEMOS COMPLETE")
    print("=" * 70)
