class MinStack:
    #Time: O(1) Since all operations take O(1) time and space
    #Space: O(1)
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        minSoFar = self.minStack[-1] if len(self.minStack) else val
        self.minStack.append(min(val, minSoFar))
        self.stack.append(val)

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