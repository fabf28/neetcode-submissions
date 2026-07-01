class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #optimized
        prev = dict()
        n = len(nums)

        for j in range(n):
            curr = nums[j]
            diff = target - curr
            if diff in prev.keys():
                return [prev[diff], j]
            prev[curr] = j
 