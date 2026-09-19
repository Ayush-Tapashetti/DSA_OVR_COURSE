# 2.4 CIRCULAR QUEUE — LINKED LIST-BASED

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def circular_queue_LL():

    state = {"FRONT": None, "REAR": None}

    def enqueue(value):
        newnode = Node(value)
        if state["FRONT"] is None:
            state["FRONT"] = state["REAR"] = newnode
            state["REAR"].next = state["FRONT"]     # circular: rear -> front
            return
        state["REAR"].next = newnode
        state["REAR"] = newnode
        state["REAR"].next = state["FRONT"]          # keep the circle closed

    def dequeue():
        if state["FRONT"] is None:
            print("UNDERFLOW")
            return None
        temp = state["FRONT"]
        if state["FRONT"] == state["REAR"]:           # single element
            state["FRONT"] = state["REAR"] = None
            return temp.data
        state["FRONT"] = state["FRONT"].next
        state["REAR"].next = state["FRONT"]           # keep the circle closed
        return temp.data

    def is_empty():
        if state["FRONT"] is None:
            print("QUEUE IS EMPTY")
            return True
        print("QUEUE IS NOT EMPTY")
        return False

    def display():
        if state["FRONT"] is None:
            print("Queue is empty")
            return
        temp = state["FRONT"]
        while temp.next != state["FRONT"]:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)               # print the last node too

    enqueue(10); enqueue(20); enqueue(30)
    display()                          # 10 20 30
    is_empty()                         # QUEUE IS NOT EMPTY
    print("Dequeue:", dequeue())       # 10
    display()                          # 20 30
    print("Dequeue:", dequeue())
    print("Dequeue:", dequeue())
    display()                          # Queue is empty
    is_empty()                         # QUEUE IS EMPTY
    print("Dequeue:", dequeue())       # UNDERFLOW -> None


circular_queue_LL()