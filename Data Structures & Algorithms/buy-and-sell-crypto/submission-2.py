class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l = 0
        r = 1

        while r < len(prices):
            diff = prices[r] - prices[l]


            if diff < 0:
                l = r
                r = l + 1
                continue 
            
            mp = max(diff, mp)

            r += 1

        return mp
        