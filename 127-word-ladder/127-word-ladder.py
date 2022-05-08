from collections import defaultdict
class Solution:
    def createGraph(self, wordList):
        graph = defaultdict(list)
        check = {word: 0 for word in wordList}
        for word in wordList:
            for idx in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:idx] + char + word[idx+1:]
                    if newWord in check:
                        graph[newWord].append(word)
                        graph[word].append(newWord)
        return graph
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        graph = self.createGraph(wordList)
        
        
        if endWord not in graph or len(wordList) == 1:
            return 0
        
        queue = [(beginWord, 1)]
        visited = {word: False for word in wordList}
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for child in graph[word]:
                if not visited[child]:
                    visited[child] = True
                    queue.append((child, dist+1))
        return 0