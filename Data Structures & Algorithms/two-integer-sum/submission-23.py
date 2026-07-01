class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #brute force

        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if target == nums[i] + nums[j]:
                    return sorted([i, j])
                    
 