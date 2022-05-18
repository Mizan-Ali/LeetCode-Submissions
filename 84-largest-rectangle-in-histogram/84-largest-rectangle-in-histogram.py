class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0 for _ in heights]
        stack = [0]
        
        for i in range(1, n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        
        right = [0 for _ in heights]
        right[n-1] = n-1
        stack = [n-1]
        for i in range(n-2, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                right[i] = n-1
            else:
                right[i] = stack[-1] - 1
            stack.append(i)
        maxArea = 0
        
        for i in range(n):
            maxArea = max(maxArea, (right[i]-left[i]+1)*heights[i])
        return maxArea