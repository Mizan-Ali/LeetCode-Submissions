class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        
        for idx, val in enumerate(nums):
            if val in hmap:
                return [hmap[val], idx]
            else:
                hmap[target-val] = idx
        