class Solution:
    def backtrack(self, partial, to_pick):
        if len(partial) == self.n:
            self.allsoln.append(partial[:])
            return
        
        for idx, val in enumerate(to_pick):
            if val in partial:
                continue
            partial.append(val)
            self.backtrack(partial, to_pick)
            partial.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.allsoln = []
        self.n = len(nums)
        self.backtrack([], nums)
        return self.allsoln