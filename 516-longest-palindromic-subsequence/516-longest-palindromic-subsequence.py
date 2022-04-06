class Solution:
    def lcs(self, i, j, s, dp):
        if i == j:
            return 1
        if i > j:
            return 0
        if (i, j) not in dp:
            if s[i] == s[j]:
                dp[(i, j)] = 2 + self.lcs(i+1, j-1, s, dp)
            else:
                dp[(i, j)] = max(self.lcs(i+1, j, s, dp), self.lcs(i, j-1, s, dp))
        return dp[(i, j)] 
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        return self.lcs(0, len(s)-1, s, dp)