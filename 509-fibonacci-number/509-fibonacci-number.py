class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        prev1, prev2 = 1, 1
        num = 0
        for i in range(3, n+1):
            num = prev1 + prev2
            prev1 = prev2
            prev2 = num
        return num