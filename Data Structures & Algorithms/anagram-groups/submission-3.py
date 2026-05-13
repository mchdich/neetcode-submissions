class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            sortedKey = ''.join(sorted(string))
            if sortedKey not in map:
                map[sortedKey] = []
            map[sortedKey].append(string)
        return list(map.values())