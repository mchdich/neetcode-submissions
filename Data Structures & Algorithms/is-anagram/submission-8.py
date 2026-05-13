class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        sorted_s, sorted_t = sorted(s), sorted(t)
        if sorted_s != sorted_t:
            return False
        return True