class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        # For 8 directional movement
        x = [-1, -1, -1, 0, +1, +1, +1, 0]
        y = [-1, 0, +1, +1, +1, 0, -1, -1]
        
        # apply bfs
        n = len(grid)
        queue = [(0, 0, 1)]
        
        while queue:
            i, j, dist = queue.pop(0)
            
            if i == n-1 and j == n-1:
                return dist
            
            for a, b in zip(x, y):
                a = i+a
                b = j+b
                if(0<=a<n and 0<=b<n and grid[a][b] == 0):
                    grid[a][b] = 1
                    queue.append((a, b, dist+1))
        return -1