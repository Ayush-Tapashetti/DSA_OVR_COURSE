"""
Compilers use stacks to verify that every opening bracket `(`, `{`, `[` has a
correctly matching, correctly ordered closing bracket `)`, `}`, `]`.
"""

def matchingPair(open, close):
    if open == '(' and close == ')':
        return True
    if open == '{' and close == '}':
            return True
    if open == '[' and close == ']':
            return True
    return False

def checbrackets(exp):
    stack = []
    for ch in exp:
        if ch in '({[':    
            stack.append(ch)
        elif ch in ')}]':
            if not stack:
                return False
            popped_char = stack.pop()
            if not matchingPair(popped_char, ch):
                 return False
    return len(stack) == 0

test_1 = "{[(())]}"
test_2 = "[(()]"
test_3 = "](())]}"             

for i in [test_1,  test_2, test_3]:
     print(i, "-->", "Balanced" if checbrackets(i) else "UnBalanced")