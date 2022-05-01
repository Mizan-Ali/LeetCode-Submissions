class Solution:
    def createString(self, s):
        newStr = []
        for i in s:
            if i != '#':
                newStr.append(i)
            else:
                if len(newStr) != 0:
                    newStr.pop()
        return newStr
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.createString(s) == self.createString(t)