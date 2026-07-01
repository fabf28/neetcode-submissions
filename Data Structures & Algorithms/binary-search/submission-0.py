class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = 0
        l = len(nums) - 1

        while l >= r:
            m = int((l + r)/2)
            print(r, m, l)
            if nums[m] == target:
                return m
            elif target < nums[m]:
                l = m - 1
            elif target > nums[m]:
                r = m + 1
        
        return -1
