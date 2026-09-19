
# 2.1 SIMPLE (LINEAR) QUEUE — ARRAY-BASED
def simple_queue_array():
    MAX = 5
    QUEUE = [None] * MAX
    state = {"FRONT": -1, "REAR": -1}

    def enqueue(value):
        if state["REAR"] == MAX - 1:
            print("OVERFLOW")
            return
        if state["FRONT"] == -1:
            state["FRONT"] = 0
        state["REAR"] += 1
        QUEUE[state["REAR"]] = value

    def dequeue():
        if state["FRONT"] == -1 or state["FRONT"] > state["REAR"]:
            print("UNDERFLOW")
            return None
        value = QUEUE[state["FRONT"]]
        state["FRONT"] += 1
        return value

    def peek():
        if state["FRONT"] == -1 or state["FRONT"] > state["REAR"]:
            print("QUEUE IS EMPTY")
            return None
        return QUEUE[state["FRONT"]]

    def is_empty():
        if state["FRONT"] == -1 or state["FRONT"] > state["REAR"]:
            print("QUEUE IS EMPTY")
            return True
        print("QUEUE IS NOT EMPTY")
        return False

    def is_full():
        if state["REAR"] == MAX - 1:
            print("QUEUE IS FULL")
            return True
        print("QUEUE IS NOT FULL")
        return False

    def display():
        if state["FRONT"] == -1 or state["FRONT"] > state["REAR"]:
            print("Queue empty")
            return
        for i in range(state["FRONT"], state["REAR"] + 1):
            print(QUEUE[i], end=" ")
        print()

    enqueue(10); enqueue(20); enqueue(30)
    display()                              # 10 20 30
    print("Peek:", peek())                 # 10
    is_full()                              # QUEUE IS NOT FULL

    enqueue(40); enqueue(50); enqueue(60)  # OVERFLOW on the 6th item
    display()                              # 10 20 30 40 50

    print("Dequeue:", dequeue())           # 10
    print("Dequeue:", dequeue())           # 20
    display()                              # 30 40 50

    is_empty()                             # QUEUE IS NOT EMPTY
    dequeue(); dequeue(); dequeue()
    print("Dequeue:", dequeue())           # UNDERFLOW -> None

if __name__ == "__main__":
    simple_queue_array()
