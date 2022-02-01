class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        prefix = [-1 for _ in range(len(nums))]
        suffix = [-1 for _ in range(len(nums))]
        msf = -1 # Max so far
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = max(nums[i-1], prefix[i-1])
        
        msf = -1 # Max so far reinitialized
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = min(nums[i+1], suffix[i+1])
        
        # print(prefix)
        # print(suffix)
        flag = 0
        ans = 0
        for i in range(1, len(nums)-1):
            if prefix[i] < nums[i] < suffix[i]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans
        
        