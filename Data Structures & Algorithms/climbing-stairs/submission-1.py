class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [-1] * n
        return self.dfs(n, 0)
    def dfs(self, n, c):
        if c == n:
            return 1
        if c > n:
            return 0
        if self.dp[c] != -1:
            return self.dp[c]
        self.dp[c] = self.dfs(n, c + 1) + self.dfs(n, c + 2)
        return self.dp[c]