class FreqStack:

    def __init__(self):
        self.stackHmap = {}
        self.freqHmap = {}
        self.maxFreq = -1

    def push(self, val: int) -> None:
        if val in self.freqHmap:
            self.freqHmap[val] += 1
            pos = self.freqHmap[val]
        else:
            self.freqHmap[val] = 1
            pos = self.freqHmap[val]
        if pos in self.stackHmap:
            self.stackHmap[pos].append(val)
        else:
            self.stackHmap[pos] = [val]
        
        self.maxFreq = max(self.maxFreq, pos)

    def pop(self) -> int:
        ans = self.stackHmap[self.maxFreq].pop()
        if len(self.stackHmap[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.freqHmap[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()