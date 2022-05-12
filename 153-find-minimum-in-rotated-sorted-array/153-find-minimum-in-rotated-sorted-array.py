class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        res = nums[0]        
        while l <= h:
            mid = (l+h)//2
            res = min(res, nums[mid])
            if nums[l] <= nums[h]:
                # Already sorted
                res = min(res, nums[l])
                return res
            
            if nums[mid] >= nums[l]:
                # search right
                l = mid+1
            else:
                h = mid-1
        
        return res