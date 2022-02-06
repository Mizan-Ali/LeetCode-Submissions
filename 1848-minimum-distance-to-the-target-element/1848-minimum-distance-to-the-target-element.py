class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mindist = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                mindist = min(mindist, abs(i-start))
        return mindist