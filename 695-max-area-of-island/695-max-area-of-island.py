class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if (0 <= i < len(grid)) and (0 <= j < len(grid[0])) and grid[i][j] == 1:
                grid[i][j] = 0    
                return (1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1))
            return 0
        
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
                
