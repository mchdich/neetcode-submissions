class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # l == r is where min is
        while l < r:
            mid = (l + r)//2
            # resets on right, search right
            if nums[mid] > nums[r]:
                l = mid + 1
            # resets on left, search left
            elif nums[l] > nums[mid]:
                r = mid
            elif nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
        return nums[l]