class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        max_profit = 0
        
        for i in prices:
            min_so_far = min(min_so_far, i)
            max_profit = max(max_profit, i - min_so_far)
            
        return max_profit