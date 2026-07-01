class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        n = len(nums)
        k = 0

        i = 0
        while i < n:
            if nums[i] in unique:
                nums.pop(i)
                i -= 1
                n -= 1
            else:
                unique.append(nums[i])
                k += 1
            
            i += 1
                
        return k