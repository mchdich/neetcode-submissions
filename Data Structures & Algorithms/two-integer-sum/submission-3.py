class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = []
        for i in range(len(nums)):
            sorted.append([nums[i], i])
        sorted.sort()
        l, r = 0, len(sorted) - 1
        while l < r:
            sum = sorted[l][0] + sorted[r][0]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [min(sorted[l][1], sorted[r][1]), max(sorted[l][1], sorted[r][1])]
            print(f"{l}, {r}")
        return []