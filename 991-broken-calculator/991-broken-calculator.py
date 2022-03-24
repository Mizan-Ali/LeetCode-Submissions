class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue - target
        
        if(target % 2 == 0):
            return 1 + self.brokenCalc(startValue, target//2)
        else:
            return 1 + self.brokenCalc(startValue, target+1)
        