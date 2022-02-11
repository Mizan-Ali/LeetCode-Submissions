class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap1 = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in s1:
            hmap1[i] += 1
        hmap2 = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for j in range(len(s1)):
            hmap2[s2[j]] += 1
        
        i, j = 0, len(s1)-1
        while j < len(s2):
            if hmap1 == hmap2:
                return True
            hmap2[s2[i]] -= 1
            i += 1
            j += 1
            if j < len(s2):
                hmap2[s2[j]] += 1
        return False