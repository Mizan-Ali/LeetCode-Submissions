class Solution:
    def removeCoveredIntervals(self, arr: List[List[int]]) -> int:
        c, n = 0, len(arr)
        arr.sort()
        print(arr)
        visited = {i: False for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if not visited[j]:
                    if arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]:
                        c += 1
                        visited[j] = True
        return n-c if c != 0 else n