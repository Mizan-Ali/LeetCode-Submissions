class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(n, amt):
            if n == 0 and amt != 0:
                return float('inf')
            if amt == 0:
                return 0
            if (n, amt) not in dp:
                if coins[n-1] <= amt:
                    dp[(n, amt)] = min(1 + solve(n, amt-coins[n-1]), solve(n-1, amt))
                else:
                    dp[(n, amt)] = solve(n-1, amt)
            return dp[(n, amt)] 
        n = len(coins)
        ans = solve(n, amount)
        if ans == float('inf'):
            return -1
        return ans