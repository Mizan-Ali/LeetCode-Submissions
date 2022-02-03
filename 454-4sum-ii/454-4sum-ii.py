from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hmap = defaultdict(int)
        for i in nums1:
            for j in nums2:
                hmap[i+j] += 1
        ans = 0
        for i in nums3:
            for j in nums4:
                add = -(i+j)
                ans += hmap[add]
        return ans