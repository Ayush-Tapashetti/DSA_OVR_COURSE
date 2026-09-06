

def postfixtoinfix(exp):
    stack = []
    
    for ch in exp:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop() 
            op1 = stack.pop()
            new_expr = f"({op1}{ch}{op2})"
            stack.append(new_expr)
    return stack.pop()

print("ABc*-  -->", postfixtoinfix("ABc*-"))
print("Ab-c*  -->", postfixtoinfix("Ab-c*"))
print("ABc^-  -->", postfixtoinfix("ABc^-"))
