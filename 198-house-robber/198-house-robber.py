class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def solve(idx):
            if idx >= n:
                return 0
            if idx not in dp:
                dp[idx] = max(nums[idx] + solve(idx+2), solve(idx+1))
            return dp[idx]
        return solve(0)
            