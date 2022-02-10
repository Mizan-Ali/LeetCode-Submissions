from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        ans = 0
        for i in hmap.keys():
            diff = i + k
            if diff in hmap:
                if k!= 0:
                    ans += 1
                elif hmap[diff] >= 2:
                    ans += 1
        return ans