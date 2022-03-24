class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        c = 0
        cnum = startValue
        if startValue > target:
            return startValue - target
        while startValue != target:
            if target % 2 == 1:
                target += 1
                c += 1
            elif target % 2 == 0:
                target //= 2
                c += 1
            if startValue > target:
                c += startValue - target
                break
        return c