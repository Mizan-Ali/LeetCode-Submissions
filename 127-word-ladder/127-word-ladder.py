from collections import defaultdict, Counter
class Solution:
    def createGraph(self, wordList):
        check = set(wordList)
        graph = defaultdict(list)
        visited = set()
        for word in wordList:
            for idx in range(len(word)):
                newWords = []
                for a in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:idx] + a + word[idx+1:]
                    newWords.append(newWord)
                for new in newWords:
                    if new in check:
                        graph[word].append(new)
                        graph[new].append(word)
        return graph
            
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a graph and apply bfs from source to destination
        if (endWord not in wordList) or (not wordList):
            return 0
        
        wordList.append(beginWord)
        graph = self.createGraph(wordList)
        
        
        queue = [(beginWord, 1)]
        visited = {i: False for i in wordList}
        visited[beginWord] = True
        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for nextWord in graph[word]:
                if not visited[nextWord]:
                    visited[nextWord] = True
                    queue.append((nextWord, dist+1))
                    
        return 0