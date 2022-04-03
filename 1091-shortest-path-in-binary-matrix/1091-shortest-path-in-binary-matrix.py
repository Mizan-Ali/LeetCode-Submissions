class Solution:
    def isValid(self, i, j, grid):
        row, col = len(grid), len(grid[0])
        if 0<=i<row and 0<=j<col and grid[i][j] == 0:
            return True
        return False
    
    def getNeighbors(self, i, j, visited, grid):
        x = [-1, -1, -1, 0, +1, +1, +1, 0]
        y = [-1, 0, +1, +1, +1, 0, -1, -1]
        neighbors = []
        for a, b in zip(x, y):
            if self.isValid(i+a, j+b, grid):
                if (i+a, j+b) not in visited:
                    neighbors.append((i+a, j+b))
        return neighbors
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        # apply bfs
        n = len(grid)
        queue = [(0, 0, 0)]
        dist = 0
        visited = {(0,0): True}
        while queue:
            i, j, dist = queue.pop(0)
            if i == n-1 and j == n-1:
                return dist+1
            neighbors = self.getNeighbors(i, j, visited, grid)
            
            for a, b in neighbors:
                queue.append((a, b, dist+1))
                visited[(a, b)] = True
                
        return -1