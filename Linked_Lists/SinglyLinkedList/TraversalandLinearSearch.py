#Build a list Manuallyand complete traversal
def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_and_traverse():
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


def search(start, val):
    ptr = start
    while ptr is not None:
        if val == ptr.data:
            return ptr          
        ptr = ptr.next
    return None                  


def search2():
    section("2.2 Searching an SLL (Linear Search — O(n))")

    start = Node(10)
    start.next = Node(20)
    start.next.next = Node(30)

    result = search(start, 20)
    print("Search for 20:", result.data if result else "Not found")

    result = search(start, 99)
    print("Search for 99:", result.data if result else "Not found")

if __name__ == "__main__":
    search2()
    build_and_traverse()