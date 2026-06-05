class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resW, resL = [-1, -1], float('inf')
        freq_t, window = defaultdict(int), defaultdict(int)
        for c in t:
            freq_t[c] += 1
        have, need = 0, len(freq_t)
        l, r = 0, 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in freq_t and window[s[r]] == freq_t[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resL:
                    resL = r - l + 1
                    resW = [l, r]
                window[s[l]] -= 1
                if s[l] in freq_t and window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        return s[resW[0] : resW[1] + 1] if resL < float('inf') else ""