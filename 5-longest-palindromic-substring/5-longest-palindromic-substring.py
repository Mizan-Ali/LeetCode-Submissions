class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        startIdx, maxLen = 0, 1
        
        for i in range(n):
            dp[i+1][i+1] = 1
            
            if i+1 < n:
                if s[i] == s[i+1]:
                    startIdx = i
                    maxLen = 2
                    dp[i+1][i+2] = 1
        
        gap = 3
        row = 1
        while gap < n+1:
            for row in range(1, len(dp)-gap+1):
                i = row
                j = row + gap - 1
                if s[i-1] == s[j-1]:
                    if dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        
                        if(j-i)+1 > maxLen:
                            startIdx = i-1
                            maxLen = (j-i)+1
            gap += 1
        
        return s[startIdx: startIdx+maxLen]