from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left != right:
            hours = 0
            mid = (left+right)//2
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                right = mid
            else:
                left = mid+1
        return left