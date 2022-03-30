class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        
        for i in range(n):
            if len(stack) == 0:
                left[i] = 0
                stack.append(i)
            else:
                while(len(stack)!=0 and heights[stack[-1]] >= heights[i]):
                    stack.pop()
                if len(stack) == 0:
                    left[i] = 0
                else:
                    left[i] = stack[-1] + 1
                stack.append(i)
        stack = []
        for i in range(n-1, -1, -1):
            if len(stack) == 0:
                right[i] = n-1
                stack.append(i)
            else:
                while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if len(stack) == 0:
                    right[i] = n-1
                else:
                    right[i] = stack[-1]-1
                stack.append(i)
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, (right[i]-left[i]+1)*heights[i])
        return maxArea