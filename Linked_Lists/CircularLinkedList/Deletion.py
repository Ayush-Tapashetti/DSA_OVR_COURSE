def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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


def cll_deletions():
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

if __name__ == "__main__":
    cll_deletions()