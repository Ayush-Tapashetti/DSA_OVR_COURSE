def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# To print the elements in list
def print_list(start, end_label="None"):
    ptr = start
    out = []
    while ptr is not None:
        out.append(str(ptr.data))
        ptr = ptr.next
    print(" -> ".join(out) + " -> " + end_label if out else end_label)

#Insertion at the beginning
def insert_at_beginning(start, val):
    new_node = Node(val)
    new_node.next = start   # point to old head
    start = new_node        # new node becomes head
    return start

#Insertion at end
def insert_at_end(start, val):
    new_node = Node(val)
    if start is None:
        return new_node
    ptr = start
    while ptr.next is not None:
        ptr = ptr.next
    ptr.next = new_node
    return start

#Insertion after Node
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

#Insertion before a node
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

#Calling all other functions 
def insertions():
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

if __name__ == "__main__":
    insertions()