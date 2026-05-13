class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for index, value in enumerate(nums):
            map[value] = index
        for index, value in enumerate(nums):
            if value in map and map[value] != index:
                return True
        return False