class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for i in range(len(nums)):
            val_idx[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in val_idx and val_idx[target - nums[i]] != i:
                return [i, val_idx[target - nums[i]]]