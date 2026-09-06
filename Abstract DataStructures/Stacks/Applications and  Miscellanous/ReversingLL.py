

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None 

    def is_empty(self):
        return self.top is None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
            
        val = self.top.data
        self.top = self.top.next 
        return val

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return
            
        print("Stack elements from top to bottom:")
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next


print("Stack Operations ")
my_stack = LinkedListStack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()

print("\nPeek Operation, Top Element:", my_stack.peek())

print("\nPop Operations:")
print("Popped:", my_stack.pop())
print("Popped:", my_stack.pop())
my_stack.display()

print("Popped:", my_stack.pop())
print("Popped:", my_stack.pop()) # Underflow test


#Reversing an Array using our New Stack
def reverse_list_with_stack(arr):
    stack = LinkedListStack()
    
    # 1. Push all array elements onto the stack
    for item in arr:
        stack.push(item)
        
    # 2. Pop them off (they will come out in reverse order)
    for i in range(len(arr)):
        arr[i] = stack.pop()

print("\n Array Reversal ")
arr = [10, 20, 30, 40, 50]
print("Original List:", arr)
reverse_list_with_stack(arr)
print("Reversed List:", arr)