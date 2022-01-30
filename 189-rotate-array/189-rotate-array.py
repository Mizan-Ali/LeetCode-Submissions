class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = k%n
        
        def reverse(arr, l, r):
            while l < r:
                print(arr[l], arr[r])
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        reverse(arr, 0, n-k-1)
        reverse(arr, n-k, n-1)
        reverse(arr, 0, n-1)
        
        
        