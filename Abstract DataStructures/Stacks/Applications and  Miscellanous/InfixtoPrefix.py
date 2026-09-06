

def oper(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infixtoprefix(exp):
    reversed_exp = ""
    for ch in exp[::-1]:
        if ch == '(':
            reversed_exp += ')'
        elif ch == ')':
            reversed_exp += '('
        else:
            reversed_exp += ch

    output = []
    stack = []
    
    for ch in reversed_exp:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(':
                prec_stack = oper(stack[-1])
                prec_ch = oper(ch)
                if prec_stack > prec_ch or (prec_stack == prec_ch and ch == '^'):
                    output.append(stack.pop())
                else:
                    break
            stack.append(ch)
            
    while stack:
        output.append(stack.pop())
    return "".join(output)[::-1]

print("Infix to Prefix:")
print("A-B*c    -->", infixtoprefix("A-B*c"))
print("(A-b)*c  -->", infixtoprefix("(A-b)*c"))
print("A-B^c    -->", infixtoprefix("A-B^c"))



