

def evaluate_postfix(exp):
    stack = []
    for ele in exp.split():
        if ele.lstrip('-').isdigit():
            stack.append(int(ele))
        else:
            b = stack.pop()
            a = stack.pop()
            if ele == '+':
                stack.append(a + b)
            elif ele == '-':
                stack.append(a - b)
            elif ele == '*':
                stack.append(a * b)
            elif ele == '/':
                stack.append(a / b)
    return stack.pop()

print(evaluate_postfix("2 3 1 * + 9 -"))