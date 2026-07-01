class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i != j:
                    return sorted([i, j])
            