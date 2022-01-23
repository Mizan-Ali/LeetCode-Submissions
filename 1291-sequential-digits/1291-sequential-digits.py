class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if low > 123456789:
            return []
        num = [str(i) for i in range(1, 10)]
        startidx = int(str(low)[0])-1
        Range = len(str(low))
        if startidx + Range <= 9:
            startnum = int(''.join(num[startidx : startidx + Range]))
            print(startnum)
        else:
            startidx = 0
            Range += 1
            startnum = int(''.join(num[startidx : startidx + Range]))
            print(startnum)
        addtn = int('1' * Range)
        ans = []
        while True:
            if startnum < low:
                if startnum%10 != 9:
                    startnum += addtn
                else:
                    Range += 1
                    startidx = 0
                    addtn = int('1' * Range)
                    startnum = int(''.join(num[startidx : startidx + Range]))
            elif startnum > high:
                break
            elif startnum == 123456789:
                ans.append(startnum)
                break
            else:
                if startnum%10 != 9:
                    ans.append(startnum)
                    startnum += addtn
                else:
                    ans.append(startnum)
                    Range += 1
                    startidx = 0
                    addtn = int('1' * Range)
                    startnum = int(''.join(num[startidx : startidx + Range]))
                    
        return ans
        
        