class MinStack:

    def __init__(self):
        self.stack = []
        self.getMinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.getMinStack[-1]) if self.getMinStack else val
        self.getMinStack.append(minimum)

    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack.pop()
        self.getMinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.getMinStack[-1]
