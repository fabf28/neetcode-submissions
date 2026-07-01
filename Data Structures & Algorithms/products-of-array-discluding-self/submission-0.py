class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            product = 1
            for i in (nums[:i] + nums[i + 1:]):
                product *= i
            products.append(product)
        return products