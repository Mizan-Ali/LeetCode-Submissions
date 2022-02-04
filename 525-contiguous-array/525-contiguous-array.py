from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        onePresent, zeroPresent = False, False
        temp = [0]
        for i in nums:
            if i == 1:
                temp.append(temp[-1] + 1)
                onePresent = True
            else:
                temp.append(temp[-1] - 1)
                zeroPresent = True
        if (not onePresent) or (not zeroPresent):
            return 0
        hmap = defaultdict(list)
        for idx, val in enumerate(temp):
            hmap[val].append(idx)
        
        ans = 0
        for i in hmap:
            ans = max(ans, hmap[i][-1] - hmap[i][0] - 1)
        return ans + 1