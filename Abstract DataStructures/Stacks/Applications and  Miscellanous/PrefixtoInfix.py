

def prefixtoinfix(exp):
    stack = []
    
    for ch in reversed(exp):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{ch}{op2})"
            stack.append(new_expr)
    return stack.pop()

print("\nPrefix to Infix:")
print("-A*Bc    -->", prefixtoinfix("-A*Bc"))
print("*-Abc    -->", prefixtoinfix("*-Abc"))
print("-A^Bc    -->", prefixtoinfix("-A^Bc"))