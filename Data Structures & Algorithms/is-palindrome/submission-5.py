class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for c in s:
            lower = c.lower()
            if self.alphanum(lower):
                cleaned.append(lower)
        ''.join(cleaned)
        return cleaned == cleaned[::-1]
            
    def alphanum(self, c):
        if "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9":
            return True
        return False