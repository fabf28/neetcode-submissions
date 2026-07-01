class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = int((l + r)/ 2)

        while l < r:
            if nums[m] > nums[r]:
                l = m + 1
                m = int((l + r)/ 2)
            elif nums[l] > nums[m]:
                r = m
                m = int((l + r)/ 2)
            else:
                return nums[l]
        
        return nums[m]