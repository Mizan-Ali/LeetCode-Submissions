class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def bfs(i, j):
            queue = [(i, j)]
            component = 0
            while queue:
                x, y = queue.pop(0)
                if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                    component += 1
                    grid[x][y] = 0
                    dx = [-1, +1, 0, 0]
                    dy = [0, 0, -1, +1]
                    for a, b in zip(dx, dy):
                        queue.append((x+a, y+b))
            return component
                        
        
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    componentSize = bfs(i, j)
                    maxArea = max(maxArea, componentSize)
        return maxArea