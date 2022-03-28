class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)-1//2
        l, r = 0, len(nums)-1
        '''
        Either left is sorted or right is sorted at all times
        '''
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            # check if left half is sorted
            if(nums[l] <= nums[mid]): # left is sorted
                if target >= nums[l] and target <= nums[mid]: # this means element is on left
                    r = mid-1
                else:
                    l = mid+1 
            else: # right is sorted
                if target >= nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
                
                
                    