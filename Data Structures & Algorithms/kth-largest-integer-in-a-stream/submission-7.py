from collections import deque

class KthLargest:
    #priority queue method
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [None]
        self.queue = deque()
        
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:

        self.heap.append(val)
        n = len(self.heap)
        i = n - 1
        change = False

        if n > 2:
            #perculate up
            while i // 2 != 0 and self.heap[i // 2] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = tmp
                i = i // 2
                if i in [1]:
                    change = True
        else:
            change = True
        self.queue.appendleft(val)
        print(self.heap)
        print(sorted(self.heap[1:])[::-1])

        kth = self.findK()
        
        return kth
    
    def findK(self):
        n = len(self.heap)
        sortedList = sorted(self.heap[1:])[::-1]
        print(sortedList)
        if self.k > n - 1:
            return self.heap[1]
        else:
            return sortedList[self.k - 1]
        
        return self.heap[i]

