class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if self.isAlphanum(s[r]) and self.isAlphanum(s[l]):
                charL, charR = s[l].lower(), s[r].lower()
                if charL != charR:
                    return False
                else:
                    l = l+1
                    r = r-1
            elif not self.isAlphanum(s[r]):
                r = r-1
            else:
                l = l+1
        return True
    
    def isAlphanum(self, c: char) -> bool:
        if "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9":
            return True
        else:
            return False