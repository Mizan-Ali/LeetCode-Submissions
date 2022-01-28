class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = float('inf')
        maxsofar = 0
        
        for i, val in enumerate(prices):
            if val < minsofar:
                minsofar = val
            elif maxsofar < prices[i] - minsofar:
                maxsofar = prices[i] - minsofar
        return maxsofar
        