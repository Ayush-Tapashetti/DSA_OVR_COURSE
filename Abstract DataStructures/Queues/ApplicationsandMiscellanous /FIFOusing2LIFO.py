# PRACTICE PROBLEM Q02 — Simulate a Queue (FIFO) Using Two Stacks (LIFO)

def queue_using_two_stacks():
    class QueueUsingStacks:
        """
        stack1 always receives new elements directly (enqueue = O(1)).
        stack2 holds elements in dequeue-ready order. It's only refilled
        from stack1 when it runs empty -- popping everything off stack1
        reverses it once, which is exactly what's needed to restore FIFO
        order (two reversals cancel out: LIFO -> LIFO -> FIFO).
        """
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def enqueue(self, value):
            self.stack1.append(value)

        def dequeue(self):
            if not self.stack2:
                if not self.stack1:
                    print("UNDERFLOW")
                    return None
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    q = QueueUsingStacks()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print("Enqueued: 1, 2, 3")
    print("Dequeue:", q.dequeue())   # 1
    q.enqueue(4)
    print("Enqueued: 4")
    print("Dequeue:", q.dequeue())   # 2
    print("Dequeue:", q.dequeue())   # 3
    print("Dequeue:", q.dequeue())   # 4
    print("Dequeue:", q.dequeue())   # UNDERFLOW -> None

queue_using_two_stacks()