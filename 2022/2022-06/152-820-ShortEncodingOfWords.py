"""
Leetcode
820. Short Encoding of Words (medium)
2022-06-20

A valid encoding of an array of words is any reference string s and array of indices indices such that:

 - words.length == indices.length
 - The reference string s ends with the '#' character.
 - For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].

Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
"""

from typing import List



# Runtime: 286 ms, faster than 46.98% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 15.9 MB, less than 59.53% of Python3 online submissions for Short Encoding of Words.
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        trie = {}
        count = 0
        
        for word in sorted(sorted(words), key=len, reverse=True):
            # write reversed words to trie.
            # if word in trie, skip,
            # if not, add to trie, increase count.
            curr = trie
            writing = False
            for c in word[::-1]:
                if writing:
                    curr[c] = {}
                    curr = curr[c]
                elif c in curr:
                    curr = curr[c]
                else:
                    writing = True
                    curr[c] = {}
                    curr = curr[c]
                    count += len(word) + 1
            
        return count



# leetcode solution 1
# https://leetcode.com/problems/short-encoding-of-words/solution/
# Runtime: 122 ms, faster than 96.74% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 14.5 MB, less than 76.28% of Python3 online submissions for Short Encoding of Words.
class Solution1:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)



# leetcode solution 2
# https://leetcode.com/problems/short-encoding-of-words/solution/
# Runtime: 386 ms, faster than 27.44% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 16.3 MB, less than 55.81% of Python3 online submissions for Short Encoding of Words.
import collections
class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)



s = Solution()
tests = [
    ["time","atime","btime"],
    ["time","time","time","time"],
    ["time","me","bell"],
    ["t"],
]
for t in tests:
    print(t)
    print(s.minimumLengthEncoding(t))
    print()
