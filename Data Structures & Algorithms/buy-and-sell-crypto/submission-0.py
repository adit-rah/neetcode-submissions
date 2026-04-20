class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for b in range(len(prices) - 1):
            s = len(prices) - 1

            while b < s:
                p = prices[s] - prices[b]
                if res < p:
                    res = p
                s -= 1

        return res

        