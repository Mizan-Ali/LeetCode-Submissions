class Solution:
    def maxHistogram(self, arr):
        n = len(arr)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            if len(stack) == 0:
                left[i] = 0
                stack.append(i)
            else:
                while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
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
                while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    right[i] = n-1
                else:
                    right[i] = stack[-1]-1
                stack.append(i)
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, arr[i] * (right[i]-left[i]+1))
        return maxArea    
            
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        mat = [[0 for _ in range(col)] for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                if i == 0:
                    mat[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "1":
                        mat[i][j] = 1 + mat[i-1][j]
        maxArea = 0
        for i in range(row):
            maxArea = max(maxArea, self.maxHistogram(mat[i]))
        return maxArea
