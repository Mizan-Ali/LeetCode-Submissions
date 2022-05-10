class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def memo(idx, buy):
            if idx == len(prices):
                return 0
            if (idx, buy) in dp:
                return dp[(idx, buy)]
            if buy == 1 :
                dp[(idx, buy)] = max(-prices[idx] + memo(idx+1, 0),
                            0 + memo(idx+1, 1))
            else:
                dp[(idx, buy)] = max(prices[idx] + memo(idx+1, 1),
                            0 + memo(idx+1, 0))
            return dp[(idx, buy)]
            
        return memo(0, 1) # 1 means buy || 0 means sell