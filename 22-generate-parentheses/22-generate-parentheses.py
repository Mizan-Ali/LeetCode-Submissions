class Solution:
    def solve(self, res, combination, left, right):
        if(left == 0 and right == 0):
            res.append(combination)
            return
        if(left > right):
            return
        if(left > 0):
            self.solve(res, combination+'(', left-1, right)
        if(right>0):
            self.solve(res, combination+')', left, right-1)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.solve(res, '(', n-1, n)
        return res