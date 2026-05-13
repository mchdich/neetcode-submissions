class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        top = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                top.append(freq[i][j])
                if len(top) == k:
                    return top