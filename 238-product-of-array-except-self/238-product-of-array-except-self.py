class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1 for _ in range(n)]
        left[0] = nums[0]
        right = [1 for _ in range(n)]
        right[-1] = nums[-1]
        for i in range(1, n):
            left[i] = nums[i] * left[i-1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i] * right[i+1]
        ans = [1 for _ in range(n)]
        ans[0] = right[1]
        ans[-1] = left[-2]
        for i in range(1, n-1):
            ans[i] = left[i-1] * right[i+1]
        return ans