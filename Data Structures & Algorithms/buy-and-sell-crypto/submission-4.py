class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
        return res