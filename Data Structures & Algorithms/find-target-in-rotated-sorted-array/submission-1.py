class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin1, end1, begin2, end2 = 0,0,0,len(nums)-1
        isSorted = True
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                end1 = i
                begin2 = i+1
                isSorted = False
        if isSorted == False:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        sub1 = nums[begin1:end1+1]
        l, r = 0, len(sub1) - 1
        while l <= r:
            mid = (l+r)//2
            if sub1[mid] < target:
                l = mid + 1
            elif sub1[mid] > target:
                r = mid - 1
            else:
                return mid
        sub2 = nums[begin2:end2+1]
        l, r = 0, len(sub2) - 1
        while l <= r:
            mid = (l+r)//2
            if sub2[mid] < target:
                l = mid + 1
            elif sub2[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1