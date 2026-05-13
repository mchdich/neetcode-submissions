class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            sortedString = ''.join(sorted(string))
            map[sortedString].append(string)
        return list(map.values())