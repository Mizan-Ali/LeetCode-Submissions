class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        arr = [[0 for _ in range(k)] for k in range(1, 102)]
        arr[0][0] = poured
        
        for row in range(query_row+1):
            for col in range(row+1):
                if arr[row][col] > 1:
                    spill = arr[row][col]-1
                    arr[row+1][col] += spill/2.0
                    arr[row+1][col+1] = spill/2.0
        return min(1, arr[query_row][query_glass])