class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            def solve(idx, partial, psum):
                global allsoln
                if psum == target:
                    allsoln.append(partial[:])
                    return
                if idx == len(candidates):
                    return
                if psum > target:
                    return

                # With
                solve(idx, partial+[candidates[idx]], psum+candidates[idx])

                # Without
                solve(idx+1, partial, psum)

            
            global allsoln
            allsoln = []
            solve(0, [], 0)
            
            return allsoln