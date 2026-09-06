#CRUD for STACKS using Arrays[PUSH, POP, PEEK, Traverse]

#Push Function
def push(arr, top, max_size, val):
    if top == max_size - 1:
        print("Stack Overflow")
        return top
    top += 1
    arr[top] = val
    return top

#Pop Function
def pop(arr, top):
    if top == -1:
        print("Stack Underflow")
        return None, top
    val = arr[top]
    top -= 1
    return val, top

#Peek Function
def peek(arr, top):
    if top == -1:
        print("Stack is Empty")
        return None
    return top

#Traversal/Display Function
def display(arr, top):
    if top == -1:
        print("Array is Empty")
        return
    print("Stack elemetns top to bottom:")
    i = top

    while i >= 0:
        print(arr[i])
        i -= 1

max_size = 3
arr = [None] * max_size
top = -1

#Pushing
print("Push Operations")
top = push(arr, top, max_size, 10)
top = push(arr, top, max_size, 20)
top = push(arr, top, max_size, 30)
display(arr, top)

print("Overflow Case")
top = push(arr, top, max_size, 10)

#Peeking
print("Peek Operation")
print("Top ELements:", peek(arr, top))

#Popping
print("Pop Operation")
val, top = pop(arr, top)
print("Popped:", val)
val, top = pop(arr, top)
print("Popped:", val)
val, top = pop(arr, top)
print("Popped:", val)

print("Underflow COndition")
val = pop(arr, top)
