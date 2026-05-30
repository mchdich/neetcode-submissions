class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        #  l  r
        res = 0
        l, r = 0, 0
        c = set()
        while r < len(s):
            if s[r] not in c:
                c.add(s[r])
                r += 1
                continue
            res = max(res, len(c))
            while s[l] != s[r]:
                c.remove(s[l])
                l += 1
            c.remove(s[l])
            l += 1
        res = max(res, len(c))
        return res