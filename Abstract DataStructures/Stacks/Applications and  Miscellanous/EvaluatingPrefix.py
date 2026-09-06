
def evaluate_prefix(exp):
    stack = []
    
    for ele in reversed(exp.split()):
        if ele.lstrip('-').isdigit():
            stack.append(int(ele))
        else:
            a = stack.pop()
            b = stack.pop()
            
            if ele == '+':
                stack.append(a + b)
            elif ele == '-':
                stack.append(a - b)
            elif ele == '*':
                stack.append(a * b)
            elif ele == '/':
                stack.append(a / b)
                
    return stack.pop()
print(evaluate_prefix("- + 2 * 3 1 9"))