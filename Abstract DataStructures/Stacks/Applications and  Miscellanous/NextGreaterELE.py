

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n 
    stack = []        
    
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
            
        stack.append(arr[i])
        
    return result

if __name__ == "__main__":
    test_cases = [
        [4, 5, 2, 25],
        [13, 7, 6, 12],
        [5, 4, 3, 2, 1]  
    ]
    
    for arr in test_cases:
        print(f"Array:  {arr}")
        print(f"Result: {next_greater_element(arr)}\n")