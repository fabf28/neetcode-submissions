class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for list1 in matrix:
            nums += list1
        
        def binary_search(l, r, target):
            m = (l + r) // 2

            if l > r:
                return False
            
            if nums[m] == target:
                return True
            elif target < nums[m]:
                return binary_search(l, m - 1, target)
            elif target > nums[m]:
                return binary_search(m + 1, r, target)
        
        return binary_search(0, len(nums) - 1, target)