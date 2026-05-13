class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = []
        for index, value in enumerate(nums):
            arr.append([value, index])
        arr.sort()
        l, r = 0, len(arr) - 1
        while l < r:
            sum = arr[l][0] + arr[r][0]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [min(arr[l][1], arr[r][1]), max(arr[l][1], arr[r][1])]
        return []