class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = dict()
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        nums = []
        for i in range(k):
            listv = list(dict1.values())
            maxx = max(listv)
            maxi = list(dict1.values()).index(maxx)
            num = list(dict1.keys())[maxi]
            nums.append(num)
            dict1.pop(num)
        
        return nums
        