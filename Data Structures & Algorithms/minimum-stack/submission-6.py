class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minimum == None or val <= self.minimum:
            self.minimums.append(self.minimum)
            self.minimum = val

    def pop(self) -> None:
        item = self.stack.pop()

        if item == self.minimum:
            self.minimum = self.minimums[-1]
            self.minimums.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum

        