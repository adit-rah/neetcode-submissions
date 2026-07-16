class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        l = 0

        for r in range(1,n):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
        
        return res 


