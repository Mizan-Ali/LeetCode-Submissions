class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        def memo(idx, positive):
            if idx == n-1:
                return 1
            
            if (idx, positive) in dp:
                return dp[(idx, positive)]
            
            diff = nums[idx+1] - nums[idx]
            if(positive):
                if(diff > 0):
                    dp[(idx, positive)] = 1 + memo(idx+1, 0)
                else:
                    dp[(idx, positive)] = memo(idx+1, 1)
            else:
                if(diff < 0):
                    dp[(idx, positive)] = 1 + memo(idx+1, 1)
                else:
                    dp[(idx, positive)] = memo(idx+1, 0)
            return dp[(idx, positive)] 
        
        return max(memo(0, 0), memo(0, 1))