

def oper(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3

def infixtopostfix(exp):
    output  = []
    stack = []
    for ch in exp:
        if ch.isalnum():
            output.append(ch)
        elif ch =='(':
            stack.append(ch)
        elif ch ==')':
            while stack and stack[-1] !='(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] !='(' and oper(stack[-1]) >= oper(ch):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return "".join(output)

print(infixtopostfix("A-B*c"))
print(infixtopostfix("(A-b)*c"))
print(infixtopostfix("A-B^c"))




