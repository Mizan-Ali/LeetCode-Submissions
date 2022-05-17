from collections import defaultdict

class Solution:
    def createGraph(self, wordList, visited):
        graph = defaultdict(list)
        for word in wordList:
            for a in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(word)):
                    newWord = word[:i] + a + word[i+1:]
                    if newWord in visited and word != newWord:
                        graph[word].append(newWord)
                        
        return graph
    
    def dfs(self, partial, endWord, curr_depth, min_depth):
        global min_paths, adj_list
        if curr_depth == min_depth:
            if partial[-1] != endWord:
                return
            else:
                if partial not in min_paths:
                    min_paths.append(partial)
                return
        
        for child in adj_list[partial[-1]]:
                self.dfs(partial+[child], endWord, curr_depth+1, min_depth)
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList.append(beginWord)
        
        # visited to store the level of each word
        visited = {word: 0 for word in wordList}
        graph = self.createGraph(wordList, visited)
        
        queue = [(beginWord, 1)]
        visited[beginWord] = 1
        while queue:
            word, level = queue.pop(0)
            
            for child in graph[word]:
                if visited[child] == 0:
                    visited[child] = level+1
                    queue.append((child, level+1))
        
        # create special adjecency list 
        global adj_list
        adj_list = defaultdict(list)
        
        for word in graph:
            for child in graph[word]:
                if visited[child] <= visited[word]:
                    continue
                else:
                    adj_list[word].append(child)
        # print(dict(adj_list))
        # print("-------------------------------")
        # print(dict(graph))
        # print("-------------------------------")
        # print(visited)
        
        
        # apply dfs
        global min_paths
        min_paths = []
        min_depth = visited[endWord]
        curr_depth = 1
        self.dfs([beginWord], endWord, curr_depth, min_depth)
        
        return min_paths