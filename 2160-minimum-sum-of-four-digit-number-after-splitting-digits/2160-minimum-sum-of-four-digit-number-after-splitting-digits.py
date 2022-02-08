class Solution:
    def minimumSum(self, num: int) -> int:
        digit = [int(i) for i in str(num)]
        digit.sort()
        num1 = (digit[0] * 10) + digit[3]
        num2 = (digit[1] * 10) + digit[2]
        return num1 + num2