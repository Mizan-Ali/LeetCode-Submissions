from collections import defaultdict
class Solution:
    # Refer: https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        runningSum, count = 0, 0
        for i in nums:
            runningSum += i
            if runningSum == k:
                count += 1
            if (runningSum-k) in hmap:
                count += hmap[runningSum-k]
            hmap[runningSum] += 1
        return count