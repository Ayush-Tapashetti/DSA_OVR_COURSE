"""
This codefile consists of 4 crazy scenarios in Linked List. They are as follows:
Reversing a Linked List
Finding the midddle using a 2 pointers
Floyd's Algorithm- Cycledetection
FInding Nth node from end

"""

def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(values):
    # To build a linked list from a Python list, return the head.
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head


def print_list(start):
    ptr = start
    out = []
    while ptr is not None:
        out.append(str(ptr.data))
        ptr = ptr.next
    print(" -> ".join(out) + " -> None")



# 1) Reversal of a Linked List
def reverse_list(start):
    prev, curr = None, start
    while curr is not None:
        nxt = curr.next     # save before overwriting
        curr.next = prev    # flip the link
        prev, curr = curr, nxt
    return prev              # new head


def call_reverse_list():
    section("1. Reversal of a Linked List")

    head = build_list([1, 2, 3, 4, 5])
    print("Original: ", end="")
    print_list(head)

    reversed_head = reverse_list(head)
    print("Reversed: ", end="")
    print_list(reversed_head)

    # edge cases
    single = build_list([42])
    print("\nSingle-node list reversed:  ", end="")
    print_list(reverse_list(single))

    empty_result = reverse_list(None)
    print("Empty list reversed:        ", "None" if empty_result is None else empty_result)


# 2) FInding the Middle(slow/fast  pointers)
def find_middle(start):
    slow = fast = start
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def call_find_middle():
    section("2. Slow/Fast Pointers — Finding the Middle")

    odd_list = build_list([1, 2, 3, 4, 5])
    print("Odd-length list:  ", end="")
    print_list(odd_list)
    print("Middle node data:", find_middle(odd_list).data)   # expected 3

    even_list = build_list([1, 2, 3, 4, 5, 6])
    print("\nEven-length list: ", end="")
    print_list(even_list)
    print("Middle node data:", find_middle(even_list).data)  # expected 4 (2nd middle)

    single = build_list([99])
    print("\nSingle-node list middle:", find_middle(single).data)  # expected 99


# 3) Floyd's ALgorithm-Cycle  Detection
def has_cycle(start):
    slow = fast = start
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    return False


def call_has_cycle():
    section("3. Cycle Detection — Floyd's Algorithm")

    # list WITHOUT a cycle
    no_cycle = build_list([1, 2, 3, 4, 5])
    print("List without a cycle:", end=" ")
    print_list(no_cycle)
    print("has_cycle() ->", has_cycle(no_cycle))   # expected False

    # list WITH a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> back to 3
    cyclic = build_list([1, 2, 3, 4, 5])
    # walk to node with data 3, and to the last node (5), then link 5 -> 3
    ptr = cyclic
    node3 = None
    while ptr is not None:
        if ptr.data == 3:
            node3 = ptr
        if ptr.next is None:
            last_node = ptr
        ptr = ptr.next
    last_node.next = node3   # introduce the cycle: 5 -> 3

    print("\nList with a cycle (5 -> back to 3):")
    print("has_cycle() ->", has_cycle(cyclic))   # expected True

# 4)Nth node from the end-2 pointer
def nth_from_end(start, n):
    first = second = start
    for _ in range(n):
        if first is None:
            return None      # list shorter than n
        first = first.next
    while first is not None:
        first, second = first.next, second.next
    return second


def call_nth_from_end():
    section("4. Two-Pointer — Nth Node From the End")

    head = build_list([1, 2, 3, 4, 5, 6, 7])
    print("List: ", end="")
    print_list(head)

    for n in [1, 3, 7]:
        result = nth_from_end(head, n)
        print(f"nth_from_end(n={n}) -> {result.data if result else None}")

    # edge case: n larger than the list length
    result = nth_from_end(head, 10)
    print(f"nth_from_end(n=10) -> {result}  (list shorter than n)")


if __name__ == "__main__":
    call_reverse_list()
    call_find_middle()
    call_has_cycle()
    call_nth_from_end()
