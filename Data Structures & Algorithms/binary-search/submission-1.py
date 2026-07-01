class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursive_fun(r, l, target):
            if l < r:
                return -1
            
            m = (r + l) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                return recursive_fun(r, m - 1, target)
            elif target > nums[m]:
                return recursive_fun(m + 1, l, target)
            
        return recursive_fun(0, len(nums) - 1, target)
