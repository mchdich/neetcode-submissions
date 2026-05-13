# Only ASCII characters
# Delimiter: " "

# ["Hello", "There", "World"] -> "Hello There World " add each word to master s
# "Hello There World " -> ["Hello", "There", "World"] add each character to temporary s
# O(mn) O(mn)

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "."
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        temp = ""
        for c in s:
            if c != ".":
                temp += c
            else:
                decoded.append(temp)
                temp = ""
        return decoded