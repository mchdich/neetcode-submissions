class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                res = max(res, profit)
        return res if res > 0 else 0