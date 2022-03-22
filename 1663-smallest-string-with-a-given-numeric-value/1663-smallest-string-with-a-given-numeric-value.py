class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a' for _ in range(n)]
        k -= n
        j = n-1
        while k > 0:
            ans[j] = chr(min(25, k) + ord('a'))
            k -= min(25, k)
            j -= 1
        return ''.join(ans)