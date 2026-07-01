class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stones.reverse()
        print(stones)

        x = 0
        y = 1

        while len(stones) > 1:
            if stones[x] == stones[y]:
                stones.pop(0)
                stones.pop(0)
            elif stones[x] < stones[y]:
                stones[y] = stones[y] - stones[x]
                stones.pop(x)
            elif stones[y] < stones[x]:
                stones[x] = stones[x] - stones[y]
                stones.pop(y)
            stones.sort()
            stones.reverse()
        
        if len(stones) == 1:
            return stones[0]
        return 0
        