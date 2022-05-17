class Solution:
    def memo(self, idx1, idx2, w1, w2):
        if idx1 == len(w1):
            return len(w2)-idx2
        
        if idx2 == len(w2):
            return len(w1)-idx1
        
        if (idx1, idx2) in self.dp:
            return self.dp[(idx1, idx2)]
            
        if w1[idx1] == w2[idx2]:
            self.dp[(idx1, idx2)] = self.memo(idx1+1, idx2+1, w1, w2)
            return self.dp[(idx1, idx2)]
        
        else:
            self.dp[(idx1, idx2)] = 1 + min(self.memo(idx1+1, idx2, w1, w2), self.memo(idx1+1, idx2+1, w1, w2), self.memo(idx1, idx2+1, w1, w2))
            return self.dp[(idx1, idx2)]
            
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        self.dp = {}
        
        return self.memo(0, 0, word1, word2)
        