class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        visited = {}
        nums.sort()
        def solve(idx, partial):
            if idx == n:
                if tuple(partial) not in visited:
                    visited[tuple(partial)] = 1
                    ans.append(partial)
                return
            # Pick
            solve(idx+1, partial + [nums[idx]])
            
            # Skip
            solve(idx+1, partial)
        
        solve(0, [])
        return ans