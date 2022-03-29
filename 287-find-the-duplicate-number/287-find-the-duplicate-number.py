class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = nums[0]
        slow = start
        fast = start
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = start
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast