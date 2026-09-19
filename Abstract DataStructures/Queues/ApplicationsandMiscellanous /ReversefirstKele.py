#PRACTICE PROBLEM Q01 — Reverse the First K Elements of a Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversee_first_k():

    class Queue:
        def __init__(self):
            self.front = None
            self.rear = None

        def enqueue(self, value):
            newnode = Node(value)
            if self.front is None:
                self.front = newnode
                self.rear = newnode
                return
            self.rear.next = newnode
            self.rear = newnode

        def dequeue(self):
            if self.front is None:
                print("UNDERFLOW")
                return None
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

        def size(self):
            count, ptr = 0, self.front
            while ptr is not None:
                count += 1
                ptr = ptr.next
            return count

        def display(self):
            if self.front is None:
                print("Queue is empty")
                return
            ptr = self.front
            while ptr is not None:
                print(ptr.data, end=" ")
                ptr = ptr.next
            print()

    def reverse_first_k(queue, k):
        # Step 1: dequeue the first k elements, push each onto a stack
        stack = []
        for _ in range(k):
            stack.append(queue.dequeue())
        # Step 2: pop the stack back into the queue -- this reverses those k
        while stack:
            queue.enqueue(stack.pop())
        """ Step 3: the reversed k elements are now at the BACK (since we just
         enqueued them) and the untouched (n-k) elements are at the FRONT.
         Rotate those untouched elements from front to back so the reversed
         k elements end up at the front again, in their original position."""
        remaining = queue.size() - k
        for _ in range(remaining):
            queue.enqueue(queue.dequeue())
        return queue

    q = Queue()
    for v in [1, 2, 3, 4, 5]:
        q.enqueue(v)
    print("Input:  ", end="")
    q.display()                        # 1 2 3 4 5
    reverse_first_k(q, 3)
    print("Output (k=3): ", end="")
    q.display()                        # 3 2 1 4 5

    q2 = Queue()
    for v in [10, 20, 30, 40, 50, 60, 70]:
        q2.enqueue(v)
    print("\nInput:  ", end="")
    q2.display()                       # 10 20 30 40 50 60 70
    reverse_first_k(q2, 4)
    print("Output (k=4): ", end="")
    q2.display()                       # 40 30 20 10 50 60 70

    # edge cases
    q3 = Queue()
    for v in [1, 2, 3, 4, 5]:
        q3.enqueue(v)
    reverse_first_k(q3, 5)             # k == full length
    print("\nk = full length: ", end="")
    q3.display()                       # 5 4 3 2 1

    q4 = Queue()
    for v in [1, 2, 3, 4, 5]:
        q4.enqueue(v)
    reverse_first_k(q4, 0)             # k == 0
    print("k = 0 (no change): ", end="")
    q4.display()                       # 1 2 3 4 5

reversee_first_k()
