"""
Leetcode
1048. Longest String Chain (medium)
2022-06-15

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

 - For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""

from typing import List
from collections import defaultdict



# Runtime: 290 ms, faster than 40.18% of Python3 online submissions for Longest String Chain.
# Memory Usage: 14.3 MB, less than 71.69% of Python3 online submissions for Longest String Chain.
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # separate words by length
        lengths = defaultdict(list)
        lengths[0] = []
        for w in words:
            lengths[len(w)].append(w)
        
        # go through words ordered by lengths from longest to shortest
        chains = defaultdict(int)
        for arr in sorted(lengths.keys(), reverse=True):
            for w in lengths[arr]:

                # start a chain with word if not already a part of a chain
                if w not in chains:
                    chains[w] = 1

                # for every letter in word, if word with this letter removed is
                # in the words array, 
                for c in range(len(w)):
                    tmp = w[:c] + w[c+1:]
                    if tmp in lengths[arr - 1]:
                        chains[tmp] = max(chains[w] + 1, chains[tmp])
        
        return max(chains.values())



# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC++Python-DP-Solution
# Runtime: 244 ms, faster than 52.26% of Python3 online submissions for Longest String Chain.
# Memory Usage: 14.3 MB, less than 71.69% of Python3 online submissions for Longest String Chain.
class Solution1:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())



s = Solution()
tests = [
    ["a","ab","ac","bd","abc","abd","abdd"],
    ["a","b","ba","bca","bda","bdca"],
    ["xbc","pcxbcf","xb","cxbc","pcxbc"],
    ["abcd","dbqca"],
]
for t in tests:
    print(t)
    print(s.longestStrChain(t))
    print()
