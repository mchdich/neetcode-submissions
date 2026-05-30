class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        res = 0
        c = set()  
        for i in range(len(s)):
          c.add(s[i])
          for j in range(i+1, len(s)):
            if s[j] in c:
              res = max(res, len(c))
              c.clear()
              break
            c.add(s[j])
        res = max(res, len(c))
        return res