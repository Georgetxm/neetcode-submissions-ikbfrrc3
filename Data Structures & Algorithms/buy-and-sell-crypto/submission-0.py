class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        l = 0
        r = 1

        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                curr = prices[r] - prices[l]
                profit = max(curr, profit)
            
            r += 1
        
        return profit


        