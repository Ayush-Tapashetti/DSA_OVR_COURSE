# 2.2 SIMPLE QUEUE — LINKED LIST-BASED
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def simple_queue_LL():
    state = {"FRONT": None, "REAR": None}

    def enqueue(value):
        newnode = Node(value)
        if state["FRONT"] is None:
            state["FRONT"] = newnode
            state["REAR"] = newnode
            return
        state["REAR"].next = newnode
        state["REAR"] = newnode

    def dequeue():
        if state["FRONT"] is None:
            print("UNDERFLOW")
            return None
        temp = state["FRONT"]
        state["FRONT"] = state["FRONT"].next
        if state["FRONT"] is None:
            state["REAR"] = None
        return temp.data

    def peek():
        if state["FRONT"] is None:
            print("QUEUE IS EMPTY")
            return None
        return state["FRONT"].data

    def display():
        if state["FRONT"] is None:
            print("Queue is empty")
            return
        ptr = state["FRONT"]
        while ptr is not None:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

    enqueue(10); enqueue(20); enqueue(30)
    display()                          # 10 20 30
    print("Peek:", peek())             # 10
    print("Dequeue:", dequeue())       # 10
    display()                          # 20 30
    print("Dequeue:", dequeue())       # 20
    print("Dequeue:", dequeue())       # 30
    print("Dequeue:", dequeue())       # UNDERFLOW -> None

simple_queue_LL()