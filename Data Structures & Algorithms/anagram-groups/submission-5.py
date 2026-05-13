class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            freqKey = tuple(count)
            if freqKey not in map:
                map[freqKey] = []
            map[freqKey].append(string)
        return list(map.values()) 