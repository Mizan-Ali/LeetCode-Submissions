class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastidx = {val:idx for idx, val in enumerate(s)}
        visited = {i: False for i in lastidx.keys()}
        stack = []
        for i in range(len(s)):
            if visited[s[i]] == True:
                continue
            while len(stack) > 0 and stack[-1] > s[i] and lastidx[stack[-1]] > i:
                visited[stack.pop()] = False
            stack.append(s[i])
            visited[s[i]] = True
        return ''.join(stack)