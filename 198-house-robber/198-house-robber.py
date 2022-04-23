class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        global ans
        dp = {}
        ans = 0
        def solve(idx, amt, dp):
            global ans
            if idx >= n:
                ans = max(ans, amt)
                return ans
            
            if(idx, amt) not in dp:
                # Rob
                a = solve(idx+2, amt+nums[idx], dp)

                # Skip
                b = solve(idx+1, amt, dp)
            
                dp[(idx, amt)] = max(a, b)
            return dp[(idx, amt)]
            
        return solve(0, 0, dp)
            