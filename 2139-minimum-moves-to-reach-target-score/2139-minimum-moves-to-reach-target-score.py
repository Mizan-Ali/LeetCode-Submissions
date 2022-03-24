class Solution:
    def solve(self, mD, tgt):
        if tgt == 1:
            return 0
        if mD == 0:
            return tgt-1
        if tgt%2 == 0:
            return 1 + self.solve(mD-1, tgt//2)
        else:
            return 1 + self.solve(mD, tgt-1)
    
    def minMoves(self, target: int, maxDoubles: int) -> int:
        return self.solve(maxDoubles, target)