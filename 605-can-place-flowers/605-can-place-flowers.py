class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n == 1):
                return True
            else:
                return False
            
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                if count == n:
                    return True
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
            flowerbed[-1] = 1
        if count >= n:
            return True
        return False
                