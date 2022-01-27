from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = {}
        ans = 0
        for i in nums:
            if i < k:
                diff = k+i
            else:
                diff = i-k
            if diff in count:
                temp = []
                if diff != i:
                    if count[i] > 0 and count[diff] > 0:
                        temp = (max(i, diff), min(i, diff))
                        
                else:
                    if count[i] >= 2:
                        temp = (max(i, diff), min(i, diff))
                if len(temp) == 2:
                    if temp not in res:
                        res[temp] = 1
                        ans += 1
                        
        return ans