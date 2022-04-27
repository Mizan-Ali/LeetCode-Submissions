from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # create a graph and find components
        graph = defaultdict(list)
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        
        components = []
        visited = set()
        for i in range(len(s)):
            if i not in visited:
                visited.add(i)
                queue = [i]
                comp = []
                while queue:
                    idx = queue.pop(0)
                    comp.append(idx)
                    for neigh in graph[idx]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
                components.append(comp)
        
        charComp = []
        for comp in components:
            c = []
            for idx in comp:
                c.append(s[idx])
            c.sort()
            charComp.append(c)
            comp.sort()
        ans = ['x' for _ in range(len(s))]
        
        for comp in range(len(charComp)):
            for c in range(len(charComp[comp])):
                ans[components[comp][c]] = charComp[comp][c]
        return ''.join(ans)
            
        
                
                