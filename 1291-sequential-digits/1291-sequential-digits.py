import math
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nl = math.floor(math.log10(low)+1)
        nh = math.floor(math.log10(high)+1)
        arr = [str(i) for i in range(1, 10)]
        ans = []
        for i in range(nl, nh+1):
            for j in range(10-i):
                num = int(''.join(arr[j:j+i]))
                if num >= low and num <= high:
                    ans.append(num)
        return ans