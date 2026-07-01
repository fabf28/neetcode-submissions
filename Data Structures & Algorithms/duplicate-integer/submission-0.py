class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnums = []
        for i in nums:
            if i not in newnums:
                newnums.append(i)
            elif i in newnums:
                return True
        
        return False