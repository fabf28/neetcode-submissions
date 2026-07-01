class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()
        n = len(nums)

        #create dict
        for i, num in enumerate(nums):
            prev[num] = i

        
        for i in range(n):
            diff = target - nums[i]
            if diff in nums:
                j = prev[diff]
                if i != j:
                    return sorted([i, j])
            