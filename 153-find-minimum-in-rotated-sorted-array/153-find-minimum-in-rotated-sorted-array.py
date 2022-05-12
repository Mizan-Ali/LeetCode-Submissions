class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        
        while l < h:
            mid = l + (h-l)//2
            if(mid > 0 and nums[mid-1] > nums[mid]):
                return nums[mid]
            if(nums[l] <= nums[mid] and nums[mid] > nums[h]):
                l = mid+1
            else:
                h = mid-1
            
        return nums[l]