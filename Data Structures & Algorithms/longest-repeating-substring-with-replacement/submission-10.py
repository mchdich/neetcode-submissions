class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxFreq = 0
        freq = defaultdict(int)
        #AABABBA
        # l  r
        #A:3,B:2,m=3,r=4
        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res