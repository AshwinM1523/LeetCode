class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        node = [value, value]
        if len(self.stack) > 0 and self.stack[-1][1] < value:
            node[1] = self.stack[-1][1]
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()