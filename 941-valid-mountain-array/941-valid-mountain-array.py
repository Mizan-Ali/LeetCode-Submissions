class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        increasing = True
        incC, decC = 0, 0
        for i in range(len(arr)-1):
            if increasing:
                if arr[i] < arr[i+1]:
                    incC += 1
                    continue
                elif arr[i] == arr[i+1]:
                    return False
                else:
                    decC += 1
                    increasing = False
            else:
                if incC == 0:
                    return False
                if arr[i] > arr[i+1]:
                    decC += 1
                    continue
                elif arr[i] == arr[i+1]:
                    return False
                else:
                    return False
        if incC == 0 or decC == 0:
            return False
        return True