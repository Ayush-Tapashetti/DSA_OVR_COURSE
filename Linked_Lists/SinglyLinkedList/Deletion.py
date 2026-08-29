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

#To delete first element
def delete_first(start):
    if start is None:
        print("Underflow")
        return None
    return start.next     # simply move head forward; old node is discarded

#To delete last element
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

#To Delete after a specific Node
def delete_after_node(start, target_val):
    ptr = start
    while ptr is not None and ptr.data != target_val:
        ptr = ptr.next
    if ptr is None or ptr.next is None:
        print("Node cannot be deleted")
        return start
    ptr.next = ptr.next.next     # skip over the node being removed
    return start

#To Delete a specific valued Node
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


#Calling all other functions
def deletions():
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

    # rebuild list for the remaining
    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    start.next.next.next = Node(40)
    start = delete_last(start)

    print("After delete_last():           ", end="")
    print_list(start)

    # rebuild list for the remaining 
    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    start.next.next.next = Node(40)

    start = delete_after_node(start, 20)
    print("After delete_after_node(20):   ", end="")
    print_list(start)

    # rebuild list for the remaining
    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)
    start.next.next.next = Node(40)

    start = delete_val(start, 40)
    print("After delete_val(40):          ", end="")
    print_list(start)

if __name__ == "__main__":
    deletions()