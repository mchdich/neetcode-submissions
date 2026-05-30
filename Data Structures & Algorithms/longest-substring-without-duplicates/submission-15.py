class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        # lr
        # {z:0, x:1, y:2}
        # r=3
        # mp[s[z]] = 0 + 1 = 1

        res = 0
        l, r = 0, 0
        c = set()
        while r < len(s):
            if s[r] not in c:
                c.add(s[r])
                r += 1
                continue
            res = max(res, len(c))
            while s[r] in c:
                c.remove(s[l])
                l += 1
        res = max(res, len(c))
        return res