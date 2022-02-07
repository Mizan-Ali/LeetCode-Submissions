from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap = Counter(s)
        for i in t:
            if i in hmap and hmap[i] > 0:
                hmap[i] -= 1
            else:
                return i