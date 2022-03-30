class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        maxLen = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    maxLen = max(maxLen, dp[i][j])
        return maxLen**2