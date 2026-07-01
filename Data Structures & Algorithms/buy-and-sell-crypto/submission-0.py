class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers - brute force

        a = 0
        n = len(prices)
        profits = []

        while a < n - 1:
            #find dip
            while a < n - 1 and prices[a] > prices[a + 1]:
                a += 1
                b = a + 1
            #from dip to end record profits
            for b in range(a, n):
                if prices[a] < prices[b]:
                    profits.append(prices[b] - prices[a])
            a += 1
        
        if not profits:
            return 0
        return max(profits)
            



        