class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        hmap = [[(a-b),[a,b]] for a, b in costs]
        hmap = sorted(hmap, key= lambda x: x[0], reverse=True)
        print(hmap)
        ans = 0
        n = 1
    
        for val in hmap:
            if n > len(costs)//2:
                ans += val[1][0]
                print(val[1][0])
            else:
                ans += val[1][1]
                print(val[1][1])
            n += 1
        return ans
        