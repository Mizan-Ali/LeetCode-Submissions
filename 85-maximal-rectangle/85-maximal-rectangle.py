class Solution:
    def maxRectInHistogram(self, heights):
        n = len(heights)
        left = [0 for i in range(n)]
        stack = [0]
        for i in range(1, n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        right = [0 for i in range(n)]
        stack = [n-1]
        right[n-1] = n-1
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
        print(maxArea)
        print(left, "  - ", right)
        
        return maxArea

    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        rect = [[0 for i in range(col)] for j in range(row)]
        
        for i in range(col):
            for j in range(row):
                if j == 0:
                    rect[j][i] = int(matrix[j][i])
                else:
                    if matrix[j][i] == "1":
                        rect[j][i] = rect[j-1][i] + 1
        maxArea = 0
        for R in rect:
            print(R)
            maxArea = max(maxArea, self.maxRectInHistogram(R))
        return maxArea