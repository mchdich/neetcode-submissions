class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = float('-inf')
        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return res if res > 0 else 0