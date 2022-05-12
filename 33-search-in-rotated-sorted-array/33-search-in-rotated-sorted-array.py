class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]:
                # Left is sorted
                if nums[l] <= target <= nums[mid]:
                    h = mid-1
                else:
                    l = mid+1

            else:
                if nums[mid] <= target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
            
        return -1
                
                