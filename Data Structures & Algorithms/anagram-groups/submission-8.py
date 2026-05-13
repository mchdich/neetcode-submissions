class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString not in map:
                map[sortedString] = []
            map[sortedString].append(string)
        return list(map.values())