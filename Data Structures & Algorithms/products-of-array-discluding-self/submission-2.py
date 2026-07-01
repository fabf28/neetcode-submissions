class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #2n complexity
        import math
        list2 = [x for x in nums if x != 0]
        total = math.prod(list2)
        zero_count = nums.count(0)
        print(zero_count)
        products = []
        length = len(nums)
        list3 = [0] * length 

        for i in range(length):
            if zero_count > 1:
                return list3
            elif zero_count == 1:
                if nums[i] == 0:
                    list3[i] = total
                    return list3
            else:
                products.append(int(total/nums[i]))

        return products
                

                

        return products