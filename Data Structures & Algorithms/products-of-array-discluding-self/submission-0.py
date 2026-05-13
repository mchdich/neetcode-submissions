class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            if len(nums) == 2:
                return [nums[i+1], nums[i]]
            product = 1
            for j in range(0, len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            res[i] = product
        return res