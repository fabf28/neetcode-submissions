class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers - brute force
        l = 0
        r = 1
        maxx = 0
        n = len(prices)

        while r < n:
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[r] - prices[l] > maxx:
                maxx = prices[r] - prices[l]
                r += 1
            else:
                r += 1
  
        return maxx
            



        