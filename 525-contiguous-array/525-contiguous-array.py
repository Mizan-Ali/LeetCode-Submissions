from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if (1 not in nums) or (0 not in nums):
            return 0
        temp = [0]
        for i in nums:
            if i == 1:
                temp.append(temp[-1] + 1)
            else:
                temp.append(temp[-1] - 1)
        hmap = defaultdict(list)
        for idx, val in enumerate(temp):
            hmap[val].append(idx)
        
        ans = 0
        for i in hmap:
            ans = max(ans, hmap[i][-1] - hmap[i][0] - 1)
        return ans + 1