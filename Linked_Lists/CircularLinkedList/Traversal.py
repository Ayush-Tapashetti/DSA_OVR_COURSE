def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse1(start):
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


def traverse2():
    section("3.1 Circular Linked List — build + traverse")

    start = Node(10)
    second = Node(20)
    third = Node(30)
    start.next = second
    second.next = third
    third.next = start          # close the circle

    traverse1(start)

if __name__ == "__main__":
    traverse2()