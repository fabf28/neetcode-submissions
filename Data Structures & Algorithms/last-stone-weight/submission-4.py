import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = self.heapify(stones)
        print(stones)

        x = 0

        while len(stones) > 1:
            n = len(stones)
            if 2 < n and stones[1] > stones[2] or 2 == n:
                y = 1
            else:
                y = 2

            if stones[x] == stones[y]:
                stones.pop(y)
                stones.pop(0)
            elif stones[x] < stones[y]:
                stones[y] = stones[y] - stones[x]
                stones.pop(x)
            elif stones[y] < stones[x]:
                stones[x] = stones[x] - stones[y]
                stones.pop(y)
            print(stones)
            stones = self.heapify(stones)
        
        print(stones)
        if len(stones) == 1:
            return stones[0]
        return 0
    
    def heapify(self, arr):
        neg = [-x for x in arr]
        heapq.heapify(neg)
        new = [-x for x in neg]
        return new
        