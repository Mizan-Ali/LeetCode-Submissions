class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        dp = {}
        def memo(idx, prevColor, totalNeigh):
            if totalNeigh > target:
                return INF
            
            if idx == m:
                if totalNeigh == target:
                    return 0
                else:
                    return INF
            else:
                key = (idx, prevColor, totalNeigh)
                if key in dp:
                    return dp[key]
                ans = INF
                if houses[idx] == 0:
                    for j in range(n):
                        ans = min(ans, cost[idx][j] + memo(idx+1, j+1, totalNeigh if (prevColor == j+1) else (totalNeigh + 1)))
                else:
                    ans = min(ans, memo(idx+1, houses[idx], totalNeigh if (houses[idx] == prevColor) else (totalNeigh + 1)))
                dp[key] = ans
                    
            return dp[key]
        
        res = memo(0, 0, 0)
        return -1 if res == INF else res