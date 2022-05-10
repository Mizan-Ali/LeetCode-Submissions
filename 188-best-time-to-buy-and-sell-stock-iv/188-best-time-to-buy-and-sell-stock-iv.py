class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}
        def memo(idx, buy, count):
            if idx == len(prices):
                return 0 
            if count == k:
                return 0
            
            if (idx, buy, count) in dp:
                return dp[(idx, buy, count)]
            
            if buy == 1 and count < k:
                dp[(idx, buy, count)] = max(-prices[idx] + memo(idx+1, 0, count+1),
                             0 + memo(idx+1, 1, count))
            elif buy == 0 and count <= k:
                dp[(idx, buy, count)] = max(prices[idx] + memo(idx+1, 1, count+1),
                            0 + memo(idx+1, 0, count))
            return dp[(idx, buy, count)]
        
        k = 2 * k
        return memo(0, 1, 0)
                             