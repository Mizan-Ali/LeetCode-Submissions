class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in visited:
                return [visited[remaining], i]
            else:
                visited[nums[i]] = i
            