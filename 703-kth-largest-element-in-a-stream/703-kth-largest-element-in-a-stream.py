from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heap = []
        for i in self.nums:
            if len(self.heap) < k:
                heappush(self.heap, i)
            else:
                heappush(self.heap, i)
                heappop(self.heap)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappush(self.heap, val)
            heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)