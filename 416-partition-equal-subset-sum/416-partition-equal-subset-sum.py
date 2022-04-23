class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Find a subset whose sum Is equal to sum of nums divided by two.
        dp = {}
        def subsetSum(idx, partSum):
            if idx == len(nums):
                return False
            if partSum == 0:
                return True
            
            if(idx, partSum) not in dp:
                dp[(idx, partSum)] = subsetSum(idx+1, partSum-nums[idx]) or subsetSum(idx+1, partSum) 
            return dp[(idx, partSum)]
        
        arrSum = sum(nums)
        if arrSum % 2 == 1:
            return False
        else:
            return subsetSum(0, arrSum//2)