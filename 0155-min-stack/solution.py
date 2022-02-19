# Approach 1 - Stack of Value/Minimum Pairs

# Time: O(1)
# Space: O(N)

class MinStack:

    def __init__(self):
        self.stack = [] # save elements as tuple (value, current_minimum)
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_min = self.stack[-1][1]
        self.stack.append((val, min(current_min, val)))
        

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
