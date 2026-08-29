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


def traverse():
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

if __name__ == "__main__":
    traverse()
