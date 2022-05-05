class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        right = [1 for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        
        result = 0
        for i in range(n):
            result += max(left[i], right[i])
        
        return result