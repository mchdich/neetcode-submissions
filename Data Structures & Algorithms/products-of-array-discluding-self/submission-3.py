# if 2 elements, return it reversed

# Brute force: O(n^2)
# Prefix and suffix array
# [1,2,4,6]
# [1,1,2,8] [48,24,6,1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        product = 1
        for i in range(n):
            prefix[i] = product
            product *= nums[i]
        product = 1
        for j in range(n-1, -1, -1):
            suffix[j] = product
            product *= nums[j]
        res = [0] * n
        for k in range(n):
            res[k] = prefix[k] * suffix[k]
        return res