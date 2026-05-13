class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if self.isAlphanum(s[l]) and self.isAlphanum(s[r]):
                lLower, rLower = s[l].lower(), s[r].lower()
                if not lLower == rLower:
                    return False
                l += 1
                r -= 1
            else:
                if not self.isAlphanum(s[l]):
                    l += 1
                if not self.isAlphanum(s[r]):
                    r -= 1
        return True

    def isAlphanum(self, c):
        if "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9":
            return True
        return False