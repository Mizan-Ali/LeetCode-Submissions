from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = {}
        ans = 0
        for i in count.keys():
            diff = i + k
            if diff in count:
                # print(i, diff)
                if k != 0:
                    ans += 1
                else:
                    if count[i] >= 2:
                        ans += 1
        return ans