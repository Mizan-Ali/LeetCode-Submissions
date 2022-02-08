class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        temp = num
        while temp % 10 != temp:
            while temp != 0:
                n = temp%10
                res += n
                temp = temp//10
            temp = res
            res = 0
        return temp