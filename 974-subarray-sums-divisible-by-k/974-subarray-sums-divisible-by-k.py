class Solution:
    
    # Refer: https://www.youtube.com/watch?v=kiHpKTfovRY
    
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modMap = {i: 0 for i in range(k)}
        runningSum = 0
        
        for i in nums:
            runningSum += i
            modMap[runningSum % k] += 1
    
        ans = 0
        for i in modMap:
            ans += (modMap[i] * (modMap[i]-1))/2
            if i == 0:
                 ans += modMap[i]
        return int(ans)