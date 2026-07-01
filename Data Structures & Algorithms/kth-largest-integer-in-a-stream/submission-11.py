from collections import deque

class KthLargest:
    #priority queue method
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]
        
        for x in nums:
            self.push(x)

        while len(self.heap) > k + 1:
            self.pop()

    def add(self, val: int) -> int:

        self.push(val)
        if len(self.heap) > self.k + 1:
            self.pop()
        return self.heap[1]
    
    def push(self, val):
        self.heap.append(val)
        n = len(self.heap)
        i = n - 1
        change = False

        if n > 2:
            #perculate up
            while i // 2 != 0 and self.heap[i // 2] > self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
                i = i // 2 

    def pop(self):
        last = self.heap[-1]
        first = self.heap[1]
        self.heap[1] = last
        self.heap[-1] = first

        self.heap.pop()

        n = len(self.heap)

        #perculate down
        i = 1
        while i * 2 < n:
            if i * 2 + 1 < n and self.heap[i * 2 + 1] < self.heap[i * 2] and self.heap[i] > self.heap[i * 2 + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
        


        