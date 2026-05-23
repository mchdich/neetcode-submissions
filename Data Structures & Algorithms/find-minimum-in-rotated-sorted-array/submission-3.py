class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin1, end1, begin2, end2 = 0,0,0,len(nums)-1
        isSorted = True
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                end1 = i
                begin2 = i+1
                isSorted = False
        if isSorted == False:
            return min(nums)
        return nums[begin2]
        # sub1 = nums[begin1:end1+1]
        # l, r = 0, len(sub1) - 1
        # currMin = float('inf')
        # while l <= r:
        #     mid = (l+r)//2
        #     if sub1[mid] < target:
        #         l = mid + 1
        #     elif sub1[mid] > target:
        #         r = mid - 1
        #     else:
        #         return sub1[mid]
        # sub2 = nums[begin2:end2+1]
        # l, r = 0, len(sub2) - 1
        # while l <= r:
        #     mid = (l+r)//2
        #     if sub2[mid] < target:
        #         l = mid + 1
        #     elif sub2[mid] > target:
        #         r = mid - 1
        #     else:
        #         return sub2[mid]
        # return -1