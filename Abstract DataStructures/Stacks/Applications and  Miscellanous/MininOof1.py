

class MinStackOptimized:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
            return

        if val >= self.min_val:
            self.stack.append(val)
        else:
            encoded_val = (2 * val) - self.min_val
            self.stack.append(encoded_val)
            self.min_val = val

    def pop(self):
        if not self.stack:
            return None
            
        popped = self.stack.pop()
        
        if popped >= self.min_val:
            return popped
        else:
            actual_val = self.min_val
            self.min_val = (2 * self.min_val) - popped
            if not self.stack:
                self.min_val = None
                
            return actual_val

    def top(self):
        if not self.stack:
            return None
        top_val = self.stack[-1]
        if top_val < self.min_val:
            return self.min_val
        return top_val

    def get_min(self):
        return self.min_val


if __name__ == "__main__":
    ms = MinStackOptimized()
    
    for v in [5, 3, 7, 2, 8]:
        ms.push(v)
        
    print("get_min after pushes:", ms.get_min())   

    ms.pop()
    print("after popping 8, get_min:", ms.get_min())   

    ms.pop()
    print("after popping 2, get_min:", ms.get_min())   