class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        # Find the element common among all the dices
        a, b = tops[0], bottoms[0]
        for i in range(1, n):
            if a not in (tops[i], bottoms[i]):
                a = -1
            if b not in (tops[i], bottoms[i]):
                b = -1
        if a == -1 and b == -1:
            return -1
        
        ans1, ans2 = float('inf'), float('inf')
        if a != -1:
            # We count the top occurences of a and bottom occurences of a
            topCount = 0
            for i in tops:
                if i == a:
                    topCount += 1
            bottomCount = 0
            for i in bottoms:
                if i == a:
                    bottomCount += 1
            ans1 = n - max(topCount, bottomCount)                        
        if b != -1:
            topCount = 0
            for i in tops:
                if i == b:
                    topCount += 1
            bottomCount = 0
            for i in bottoms:
                if i == b:
                    bottomCount += 1
            ans2 = n - max(topCount, bottomCount)
        return min(ans1, ans2)