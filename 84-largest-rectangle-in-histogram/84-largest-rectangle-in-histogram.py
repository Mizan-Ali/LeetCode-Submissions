class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        left = [0 for _ in range(len(h))]
        right = [0 for _ in range(len(h))]
        s = []
        for i in range(len(h)):
            while len(s) > 0 and h[s[-1]] >= h[i]:
                s.pop()
            if len(s) == 0:
                left[i] = 0
            else:
                left[i] = s[-1] + 1
            s.append(i)
        print(left)
        s = []
        for i in range(len(h)-1, -1, -1):
            while len(s) > 0 and h[s[-1]] > h[i]:
                s.pop()
            if len(s) == 0:
                right[i] = len(h)-1
            else:
                right[i] = s[-1] - 1
            s.append(i)
        ans = 0
        for i in range(len(h)):
            ans = max(ans, h[i] * (right[i]-left[i]+1))
        return ans
        
            