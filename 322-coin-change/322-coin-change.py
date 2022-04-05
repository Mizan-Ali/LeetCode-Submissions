class Solution:    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(idx, amt):
            if idx < 0 and amt != 0:
                return float('inf')
            if amt == 0:
                return 0
            
            if (idx, amt) not in dp:
                f1 = float('inf')
                if coins[idx] <= amt:
                    f1 = 1 + solve(idx, amt-coins[idx])                
                f2 = solve(idx-1, amt)
                
                dp[(idx, amt)] = min(f1, f2)
                
            return dp[(idx, amt)] 
            
        ans = solve(len(coins)-1, amount)
        return ans if ans != float('inf') else -1