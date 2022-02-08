class Solution:
    def countSetBits(self, n):
        count = 0
        while (n):
            n &= (n-1)
            count+= 1
        return count
     
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = [(i, self.countSetBits(i)) for i in arr]
        count = sorted(count, key = lambda x: x[0])
        count = sorted(count, key = lambda x: x[1])
        # print(count)
        ans = [i[0] for i in count]
        return ans