class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(idx, partial):
            global allsoln
            if idx == len(nums):
                allsoln.append(partial[:])
                return
            # pick
            solve(idx+1, partial + [nums[idx]])
            
            #skip
            solve(idx+1, partial)
        global allsoln
        allsoln = []
        solve(0, [])
        return allsoln