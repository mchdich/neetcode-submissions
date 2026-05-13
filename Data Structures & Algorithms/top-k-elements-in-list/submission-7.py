class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        pairs = []
        for num, freq in freq.items():
            pairs.append([freq, num])
        pairs.sort()
        top = []
        while len(top) < k:
            top.append(pairs.pop()[1])
        return top