class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(size):
                print(i,j)
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i,j]
        