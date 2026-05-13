class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep counts for all frequencies
        # can't make array because of negative nums
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        print(freq)
        res = []
        for i in range(k):
            keyVal = [0] * 2
            for key, value in freq.items():
                if value > keyVal[1]:
                    keyVal[0] = key
                    keyVal[1] = value
            print(keyVal)
            res.append(keyVal[0])
            freq.pop(keyVal[0])
        return res