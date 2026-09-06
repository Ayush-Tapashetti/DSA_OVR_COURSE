

def factorial(n, depth=0):
    indent = "  " * depth
    if n == 1:
        print(f"{indent}Reached base case for n=1. Popping off stack and returning 1")
        return 1
    print(f"{indent}Pushing factorial({n}) to stack. Waiting for factorial({n-1})...")
    result_from_next = factorial(n - 1, depth + 1)
    current_result = n * result_from_next
    print(f"{indent}Popping factorial({n}) off stack. ({n} * {result_from_next} = {current_result})")
    
    return current_result


if __name__ == "__main__":
    print(" Starting Recursive Call Stack ")
    final_answer = factorial(4)
    print("\nFinal Answer:", final_answer)