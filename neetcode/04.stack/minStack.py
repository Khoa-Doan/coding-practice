class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minStack:
            self.minStack.append(val)
            return
        
        lastVal = self.minStack[-1]
        if lastVal > val:
            self.minStack.append(val)
        else:
            self.minStack.append(lastVal)
            

    def pop(self) -> None:
            self.stack.pop()
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()