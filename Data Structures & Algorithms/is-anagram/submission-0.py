class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
	        return False
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        return freq_s == freq_t