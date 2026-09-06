#CRUD for STACKS using LinkedList[PUSH, POP, PEEK, Traverse]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Push Function
def push(start, val):
    new_node = Node(val)
    new_node.next = start
    start = new_node
    return start

#Pop Function
def pop(start):
    if start is None:
        print("Stack Underflow")
        return None, None
    val = start.data
    b = start
    start = start.next
    b.next = None
    return val, start

#Peek Function
def peek(start):
    if start is None:
        print("Stack is Empty")
        return None
    return start.data

#Display Function
def display(start):
    if start is None:
        print("Stack is Empty")
        return None
    print("Stack elements from top to bottom:")
    ptr = start
    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next

top = None

print("Push Operations")
top = push(top, 10)
top = push(top, 20)
top = push(top, 30)
display(top)

#OVERFLOW is not possible in Stcks built using LINKED LISTS

print("Peek Operation")
print("Top Element:", peek(top))

print("Pop Operation")
val, top = pop(top)
print("Popped:", val)
val, top = pop(top)
print("Popped:", val)
display(top)

val, top = pop(top)
print("Popped:", val)

# Underflow
val, top = pop(top)
