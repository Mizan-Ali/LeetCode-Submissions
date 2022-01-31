class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i]
        product = 1
        ans[-1] = ans[-2]
        for i in range(n-1, -1, -1):
            if i == 0:
                ans[i] = product
                break
            ans[i] = ans[i-1] * product
            product *= nums[i]
        return ans
        