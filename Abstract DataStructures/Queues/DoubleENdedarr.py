
# 2.5 DOUBLE-ENDED QUEUE (DEQUE) — ARRAY-BASED
def deque_array():
    MAX = 5
    DEQUE = [None] * MAX
    state = {"FRONT": -1, "REAR": -1}

    def insert_front(value):
        if (state["FRONT"] == 0 and state["REAR"] == MAX - 1) or \
           (state["FRONT"] == state["REAR"] + 1):
            print("OVERFLOW")
            return
        if state["FRONT"] == -1:
            state["FRONT"] = state["REAR"] = 0
            DEQUE[state["FRONT"]] = value
            return
        if state["FRONT"] == 0:
            state["FRONT"] = MAX - 1
            DEQUE[state["FRONT"]] = value
            return
        state["FRONT"] -= 1
        DEQUE[state["FRONT"]] = value

    def insert_rear(value):
        if (state["FRONT"] == 0 and state["REAR"] == MAX - 1) or \
           (state["FRONT"] == state["REAR"] + 1):
            print("OVERFLOW")
            return
        if state["FRONT"] == -1:
            state["FRONT"] = state["REAR"] = 0
            DEQUE[state["REAR"]] = value
            return
        if state["REAR"] == MAX - 1:
            state["REAR"] = 0
            DEQUE[state["REAR"]] = value
            return
        state["REAR"] += 1
        DEQUE[state["REAR"]] = value

    def delete_front():
        if state["FRONT"] == -1:
            print("UNDERFLOW")
            return None
        value = DEQUE[state["FRONT"]]
        if state["FRONT"] == state["REAR"]:
            state["FRONT"] = state["REAR"] = -1
            return value
        if state["FRONT"] == MAX - 1:
            state["FRONT"] = 0
            return value
        state["FRONT"] += 1
        return value

    def delete_rear():
        if state["FRONT"] == -1:
            print("UNDERFLOW")
            return None
        value = DEQUE[state["REAR"]]
        if state["FRONT"] == state["REAR"]:
            state["FRONT"] = state["REAR"] = -1
            return value
        if state["REAR"] == 0:
            state["REAR"] = MAX - 1
            return value
        state["REAR"] -= 1
        return value

    def display():
        if state["FRONT"] == -1:
            print("DEQUE is empty")
            return
        print("DEQUE:", end=" ")
        if state["FRONT"] <= state["REAR"]:
            for i in range(state["FRONT"], state["REAR"] + 1):
                print(DEQUE[i], end=" ")
        else:
            for i in range(state["FRONT"], MAX):
                print(DEQUE[i], end=" ")
            for i in range(0, state["REAR"] + 1):
                print(DEQUE[i], end=" ")
        print()

    insert_rear(10) 
    insert_rear(20) 
    insert_front(5)
    insert_front(2)
    display()                                  # DEQUE: 2 5 10 20

    print("Delete front:", delete_front())     # 2
    display()                                  # DEQUE: 5 10 20

    print("Delete rear:", delete_rear())       # 20
    display()                                  # DEQUE: 5 10

    insert_rear(30)
    insert_front(1)
    display()                                  # DEQUE: 1 5 10 30

deque_array()