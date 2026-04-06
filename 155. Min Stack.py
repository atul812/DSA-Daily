class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self) -> None:
        if self.is_empty():
            return "Stack is empty"
        self.items.pop()

    def top(self) -> int:
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def getMin(self) -> int:
        mini = self.items[0]
        for i in range(1, len(self.items)):
            mini = min(mini, self.items[i])

        return mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
