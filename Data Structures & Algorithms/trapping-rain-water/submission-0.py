class Solution:
    def trap(self, height: List[int]) -> int:
        cur = 0
        leftMax, rightMax = [0] * len(height), [0] * len(height)
        minLR = [0] * len(height)
        for i in range(len(height)):
            leftMax[i] = cur
            cur = max(cur, height[i])
        cur = 0
        for i in range(len(height)-1, -1, -1):
            rightMax[i] = cur
            cur = max(cur, height[i])
        for i in range(len(height)):
            minLR[i] = min(leftMax[i], rightMax[i])

        total = 0
        for i in range(len(height)):
            add = minLR[i] - height[i]
            total += add if add > 0 else 0
        return total