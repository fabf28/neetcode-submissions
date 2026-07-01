class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        final = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            final = max(area, final)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return final