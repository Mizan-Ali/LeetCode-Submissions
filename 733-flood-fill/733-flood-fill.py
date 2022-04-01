class Solution:
    def isValid(self, visited, image, color, i, j):
        row, col = len(image), len(image[0])
        if 0 <= i < row and 0 <= j < col:
            if(image[i][j] == color and (i, j) not in visited):
                return True
        return False
    def getNeighbors(self, visited, image, i, j):
        neighbors = []
        row, col = len(image), len(image[0])
        color = image[i][j]
        if self.isValid(visited, image, color, i+1, j):
            neighbors.append([i+1, j])
        if self.isValid(visited, image, color, i-1, j):
            neighbors.append([i-1, j])
        if self.isValid(visited, image, color, i, j+1):
            neighbors.append([i, j+1])
        if self.isValid(visited, image, color, i, j-1):
            neighbors.append([i, j-1])
        return neighbors
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Breadth first search
        queue = [[sr, sc]]
        visited = {}
        while queue:
            i, j = queue.pop(0)
            visited[(i, j)] = True
            neighbors = self.getNeighbors(visited, image, i, j)
            image[i][j] = newColor
            queue.extend(neighbors)
            # print(queue)
        return image
            
            