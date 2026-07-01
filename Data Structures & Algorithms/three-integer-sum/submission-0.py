class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        list1 = []
        list2 = []
        size = len(nums)
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if i == j or i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        indexes = sorted([i,j,k])
                        values = sorted([nums[i], nums[j], nums[k]])
                        if indexes not in list1 and values not in list2:
                            list2.append(values)
                        else:
                            list1.append(indexes)
        return list2

                        