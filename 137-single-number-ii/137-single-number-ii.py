from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        for i in hmap:
            if hmap[i] == 1:
                return i