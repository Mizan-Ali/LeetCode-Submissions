class Solution:
    def backtrack(self, idx, partial, partialSum):
        global allNum, ans
        
        if partialSum == self.n and len(partial) == self.k:
            ans.append(partial[:])
            return 
        
        if idx == len(allNum):
            return 
        if len(partial) >= self.k or partialSum > self.n:
            return 
        
        
        # Pick
        partial.append(allNum[idx])
        self.backtrack(idx+1, partial, partialSum + allNum[idx])
        partial.pop()
        
        # Skip
        self.backtrack(idx+1, partial, partialSum)
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k*(k+1)//2 > n:
            return []
        
        self.n = n
        self.k = k
        global allNum, ans
        allNum = [i for i in range(1, 10)]
        ans = []
        self.backtrack(0, [], 0)
        
        return (ans)