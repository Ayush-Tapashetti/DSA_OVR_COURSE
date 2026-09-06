

def sort_stack(stack):
    tmp_stack = []
    
    while stack:
        temp = stack.pop()
        while tmp_stack and tmp_stack[-1] > temp:
            stack.append(tmp_stack.pop())
        tmp_stack.append(temp)
    while tmp_stack:
        stack.append(tmp_stack.pop())
        
    return stack

if __name__ == "__main__":
    my_stack = [34, 3, 31, 98, 92, 23]
    
    print("Original Stack (top is last):", my_stack)
    sorted_stack = sort_stack(my_stack)
    print("Sorted Stack (top is last):  ", sorted_stack)