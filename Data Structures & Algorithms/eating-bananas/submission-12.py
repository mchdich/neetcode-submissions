class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        currMin = r
        while l <= r:
            curr = 0
            k = (l + r) // 2
            for i in range(len(piles)):
                curr += math.ceil(piles[i]/k)
            if curr > h:
                l = k + 1
            elif curr <= h:
                currMin = k
                r = k - 1
        return currMin