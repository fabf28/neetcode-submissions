class KthLargest:
    #simple queue method
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = sorted(nums)

    def add(self, val: int) -> int:
        n = len(self.queue)
        done = False
        for i in range(n - 1):
            if self.queue[i] <= val and val <= self.queue[i + 1]:
                self.queue.insert(i + 1, val)
                done = True
                break
        if not done:
            if not self.queue or val < self.queue[0]:
                self.queue.insert(0, val)
            else:
                self.queue.append(val)
        return self.queue[-self.k]