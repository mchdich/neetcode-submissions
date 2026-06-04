class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resW, resL = [-1, -1], float('inf')
        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1
        for i in range(len(s)):
            freq_s = defaultdict(int)
            for j in range(i, len(s)):
                freq_s[s[j]] += 1
                contains = True
                for c in t:
                    if freq_s[c] < freq_t[c]:
                        contains = False
                        break
                if contains and (j - i + 1) < resL:
                    resW = [i, j]
                    resL = (j - i + 1)
        return s[resW[0] : resW[1] + 1] if resL < float('inf') else ""