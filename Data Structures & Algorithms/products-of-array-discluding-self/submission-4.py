# if 2 elements, return it reversed

# Brute force: O(n^2)
# Prefix and suffix array
# [1,2,4,6]
# [1,1,2,8] [48,24,6,1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if n == 2:
                return [nums[i+1], nums[i]]
            product = 1
            for j in range(n):
                if j == i:
                    continue
                product *= nums[j]
            res[i] = product
        return res