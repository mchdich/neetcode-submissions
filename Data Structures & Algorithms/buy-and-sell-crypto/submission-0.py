class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # subtract latter from former
        max = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max