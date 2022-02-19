class MaxStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        
        current_max = self.stack[-1][1]
        self.stack.append((x, max(current_max, x)))
        

    def pop(self) -> int:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def peekMax(self) -> int:
        return self.stack[-1][1]
        

    def popMax(self) -> int:
        
        max_val = self.peekMax()
        temp_stack = []
        
        while self.top() != max_val:
            temp_stack.append(self.pop())
            
        r = self.pop()
        
        while temp_stack:
            self.push(temp_stack.pop())
            
        return r
                    


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
