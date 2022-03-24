class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people)-1
        c = 0
        while i<=j:
            if(people[i]+people[j] <= limit):
                c += 1
                i += 1
                j -= 1
                
            else:
                c += 1
                j -= 1
        return c