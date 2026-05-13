class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        freq_s, freq_t = defaultdict(int), defaultdict(int)
        for i in range(n):
            freq_s[s[i]] += 1
            freq_t[t[i]] += 1
        return freq_s == freq_t