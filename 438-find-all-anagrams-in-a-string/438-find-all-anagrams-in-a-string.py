from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        main_map = {chr(i): 0 for i in range(97, 97+26)}
        temp_map = {chr(i): 0 for i in range(97, 97+26)}
        for k in p:
            main_map[k] += 1
        
        i = 0
        j = n-1
        ans = []
        
        substr = s[i: j+1]
        for k in substr:
            temp_map[k] += 1
        # print(temp_map)
        while j < len(s):
            # print(s[i:j+1])
            if temp_map == main_map:
                ans.append(i)
            temp_map[s[i]] -= 1
            i += 1
            j += 1
            if j < len(s):
                temp_map[s[j]] += 1
        return ans
            