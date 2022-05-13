class Solution:
    def backtrack(self, partial, to_pick, visited):
        if len(partial) == self.n:
            self.allsoln.append(partial[:])
            return
        
        for idx, val in enumerate(to_pick):
            if visited[val] == True:
                continue
            partial.append(val)
            visited[val] = True
            self.backtrack(partial, to_pick, visited)
            visited[val] = False
            partial.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.allsoln = []
        self.n = len(nums)
        self.backtrack([], nums, {i: False for i in nums})
        return self.allsoln