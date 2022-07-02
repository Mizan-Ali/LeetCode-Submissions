class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        MOD = 10**9 + 7
        hCuts.append(0)
        vCuts.append(0)
        
        hCuts.append(h)
        vCuts.append(w)
        
        hCuts.sort()
        vCuts.sort()
        
        hGap, vGap = 0, 0
        
        for i in range(len(hCuts)-1):
            hGap = max(hGap, hCuts[i+1] - hCuts[i])
            
        for i in range(len(vCuts)-1):
            vGap = max(vGap, vCuts[i+1] - vCuts[i])
        
        return (hGap * vGap) % MOD