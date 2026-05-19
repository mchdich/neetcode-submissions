# Brute force O(n^2)
# double for loop, j-i, break when warmer found, 0 otherwise
# Two pointers O(n^2)
# Stack
# push temps to stack until warmer day

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result