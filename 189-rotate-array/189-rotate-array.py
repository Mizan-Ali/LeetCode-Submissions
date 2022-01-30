class Solution:
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = k%n
        
        self.reverse(arr, 0, n-k-1)
        self.reverse(arr, n-k, n-1)
        self.reverse(arr, 0, n-1)
        
        
        