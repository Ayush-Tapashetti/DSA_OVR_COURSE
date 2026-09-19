
# 2.3 CIRCULAR QUEUE — ARRAY-BASED
def circular_queue_arr():
    MAX = 5
    QUEUE = [None] * MAX
    state = {"FRONT": -1, "REAR": -1}

    def enqueue(value):
        if (state["FRONT"] == 0 and state["REAR"] == MAX - 1) or \
           (state["FRONT"] == state["REAR"] + 1):
            print("OVERFLOW")
            return
        if state["FRONT"] == -1:
            state["FRONT"] = state["REAR"] = 0
            QUEUE[state["REAR"]] = value
            return
        if state["REAR"] == MAX - 1:
            state["REAR"] = 0
            QUEUE[state["REAR"]] = value
            return
        state["REAR"] += 1
        QUEUE[state["REAR"]] = value

    def dequeue():
        if state["FRONT"] == -1:
            print("UNDERFLOW")
            return None
        value = QUEUE[state["FRONT"]]
        if state["FRONT"] == state["REAR"]:
            state["FRONT"] = state["REAR"] = -1
            return value
        if state["FRONT"] == MAX - 1:
            state["FRONT"] = 0
            return value
        state["FRONT"] += 1
        return value

    def display():
        if state["FRONT"] == -1 and state["REAR"] == -1:
            print("QUEUE IS EMPTY")
            return
        if state["FRONT"] <= state["REAR"]:
            for i in range(state["FRONT"], state["REAR"] + 1):
                print(QUEUE[i], end=" ")
            print()
            return
        for i in range(state["FRONT"], MAX):
            print(QUEUE[i], end=" ")
        for i in range(0, state["REAR"] + 1):
            print(QUEUE[i], end=" ")
        print()

    enqueue(10); enqueue(20); enqueue(30); enqueue(40); enqueue(50)  # full
    display()                          # 10 20 30 40 50
    enqueue(60)                        # OVERFLOW

    print("Dequeue:", dequeue())       # 10
    print("Dequeue:", dequeue())       # 20
    display()                          # 30 40 50

    enqueue(60); enqueue(70)           # wrap into freed slots
    display()                          # 30 40 50 60 70

    enqueue(80)                        # OVERFLOW (full again)

circular_queue_arr()
