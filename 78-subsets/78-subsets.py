class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        allsoln = []
        def solve(idx, partial):
            if idx == n:
                allsoln.append(partial)
                return
            
            # Pick
            solve(idx+1, partial + [nums[idx]])
            
            # Skip
            solve(idx+1, partial)
        
        solve(0, [])
        return allsoln