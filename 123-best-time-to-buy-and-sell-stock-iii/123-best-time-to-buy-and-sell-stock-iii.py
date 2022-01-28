class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def solve(day, count):
            if (day, count) not in dp:
                if day == len(prices):
                    return 0
                if count == 4:
                    return 0
                # skip
                a = solve(day+1, count)

                # Buy or sell
                buy = count % 2 == 0
                if buy:
                    b = solve(day+1, count+1) - prices[day]
                else:
                    b = solve(day+1, count+1) + prices[day]
                dp[(day, count)] = max(a, b)
            return dp[(day, count)]
        
        idx = day = 0
        return solve(idx, day)