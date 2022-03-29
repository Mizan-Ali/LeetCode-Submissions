class Solution:
    global dp
    dp = {}
    def climbStairs(self, n: int) -> int:
        global dp
        if n == 1 or n == 2:
            return n
        if n not in dp:
            dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return dp[n]