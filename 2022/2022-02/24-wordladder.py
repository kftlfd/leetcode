'''
Leetcode
127. Word Ladder (hard)
2022-02-12

A transformation sequence from word beginWord to word endWord using a 
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> 
... -> sk such that:
 - Every adjacent pair of words differs by a single letter.
 - Every si for 1 <= i <= k is in wordList. Note that beginWord does 
   not need to be in wordList.
 - sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from 
beginWord to endWord, or 0 if no such sequence exists.
'''



# taken from 
# https://leetcode.com/problems/word-ladder/discuss/1764371/A-very-highly-detailed-EXPLANATION
# Time limit exceeded
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList: return 0
        
        queue = []
        visited = set()
        depth = 0
        l = len(beginWord)
        letters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        
        queue.append(beginWord)
        
        while len(queue) > 0:
            
            depth += 1
            
            ql = len(queue)
            
            # look at every word in queue
            for word in range(ql):
                
                curr = queue.pop(0)
                
                if curr == endWord: return depth
                
                # change letters in word
                for i in range(l):
                    
                    for c in letters:
                                                
                        temp = curr[:i] + c + curr[i+1:]
                        
                        if temp in wordList and temp not in visited:
                            queue.append(temp)
                            visited.add(temp)
        
        return 0



# taken from
# https://leetcode.com/problems/word-ladder/discuss/1765042/Python-3-Breadth-First-Search-Solution-and-Explanation
# Runtime: 151 ms, faster than 79.17% of Python3 online submissions for Word Ladder.
# Memory Usage: 18.2 MB, less than 19.24% of Python3 online submissions for Word Ladder.
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        l = len(beginWord)
        
        wordHash = defaultdict(list)
        for word in wordList:
            # Put * in every possible index and add up its prefix and suffix
            for i in range(l):
                wordHash[word[:i] + '*' + word[i + 1:]].append(word)
                
        visited = {}
        queue = deque([[beginWord, 1]]) # every element store [word, level]
        while queue:
            popWord, level = queue.popleft()
            visited[popWord] = True
            
            for i in range(len(popWord)):
                prefix = popWord[:i]
                suffix = popWord[i + 1:]
                key = prefix + '*' + suffix # key value
                # Traverse through and find next word to be append in queue
                for nextWord in wordHash[key]:
                    # End point
                    if nextWord == endWord:
                        return level + 1 
                    # Append next word in queue
                    if nextWord not in visited:
                        queue.append([nextWord, level + 1])
                # To prevent trverse same key again and find all visited
                wordHash[key] = [] 
        return 0