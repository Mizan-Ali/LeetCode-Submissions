class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        # Fill the one size substr
        maxlen = 1
        for i in range(n):
            dp[i][i] = 1
            
        start = 0
        # Fill two sized substr
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                maxlen = 2
                start = i
            else:
                dp[i][i+1] = 0
        
        gap = 3
        while gap <= n:
            i = 0
            while i < (n-gap+1):
                j = i+gap-1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    
                    if gap > maxlen:
                        maxlen = gap
                        start = i
                i += 1
            gap += 1
            
        return s[start: start+maxlen]