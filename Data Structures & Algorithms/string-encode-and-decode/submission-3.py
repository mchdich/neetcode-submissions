# ["hi", "100", "meow meow meow"] -> "2#hi3#10014#meow meow meow"
class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        print(parts)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1:j + length + 1])
            i = j + length + 1
        return decoded