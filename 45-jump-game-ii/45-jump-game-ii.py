class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, steps = len(nums), 0, 0, 0
        while end < n-1:
            steps += 1
            maxend = end+1
            
            for i in range(start, maxend):
                if i + nums[i] >= n-1:
                    return steps
                maxend = max(maxend, i+nums[i])
            start = end+1
            end = maxend
        return steps
        