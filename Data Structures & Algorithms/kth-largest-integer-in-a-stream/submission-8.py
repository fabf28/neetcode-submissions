from collections import deque

class KthLargest:
    #priority queue method
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = nums

    def add(self, val: int) -> int:
        self.queue.append(val)
        self.queue.sort()
        return self.queue[-self.k]
        
