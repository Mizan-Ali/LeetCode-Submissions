class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        def dfs(i, j):
            if image[i][j] == color:
                image[i][j] = newColor
                
                if i >= 1:
                    dfs(i-1, j)
                if i+1 < row:
                    dfs(i+1, j)
                if j >= 1:
                    dfs(i, j-1)
                if j+1 < col:
                    dfs(i, j+1)
        dfs(sr, sc)
        return image