class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, ptr = m-1, n-1, len(nums1)-1
        
        while j >= 0:
            if nums1[i] >= nums2[j] and i >= 0:
                nums1[ptr] = nums1[i]
                i -= 1
            else:
                nums1[ptr] = nums2[j]
                j -= 1
            ptr -= 1
        
      