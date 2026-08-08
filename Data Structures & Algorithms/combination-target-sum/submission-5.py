class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.bt(nums, [], target, 0, 0)
        return self.res
    def bt(self, nums, curr, t, i, s):
        if s == t:
            self.res.append(curr[:])
            return
        for j in range(i, len(nums)):
            if s + nums[j] <= t: #safe
                curr.append(nums[j])
                self.bt(nums, curr, t, j, s + nums[j])
                curr.pop()
            #don't return, explore other options