from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a heap
        # pop k times
        inverse = [-1*i for i in nums]
        heapify(inverse)
        num = 0
        while k != 0:
            num = heappop(inverse)
            k -= 1
        return -1 * num
        