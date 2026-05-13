class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr, arr2 = [], []
        map = {}
        for string in strs:
            map[string] = 0
        for i in range(len(strs)):
            if map[strs[i]] == 1:
                continue
            arr2.append(strs[i])
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    arr2.append(strs[j])
                    map[strs[j]] = 1
            arr.append(arr2)
            arr2 = []
        return arr