class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.minimum = None
        self.counts = dict()
        self.minimums = [ ]

    def push(self, val: int) -> None:
        #add item to stack
        self.stack.append(val)
        self.length += 1

        #check minimum
        if self.minimum == None or val <= self.minimum:
            self.minimums.append(self.minimum)
            self.minimum = val
            

        return 
        if val in self.counts.keys():
            self.counts[val] += 1
        else:
            self.counts[val] = 0

    def pop(self) -> None:
        item = self.stack.pop()
        self.length -= 1

        if item == self.minimum:
            self.minimum = self.minimums[-1]
            self.minimums.pop()

        return
        self.counts[item] -= 1
        if item == self.minimum:
            if self.counts[item] == 0:
                self.minimum = self.minimums[-1]
                self.minimums.pop()
        elif item in self.minimums:
            if self.counts[item] == 0:
                self.minimums.pop()
        

    def top(self) -> int:
        return self.stack[self.length - 1]
        

    def getMin(self) -> int:
        return self.minimum

        