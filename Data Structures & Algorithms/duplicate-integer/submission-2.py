class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = []
        for i in nums:
            if i in list1:
                return True
            else:
                list1.append(i)
        return False