"""
Leetcode
792. Number of Matching Subsequences (medium)
2022-07-20

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""

from typing import List


# TLE
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        num = 0
        for word in words:
            if self.isSubseq(word, s):
                num += 1
        return num

    def isSubseq(self, word: str, s: str) -> bool:
        l = len(s)
        i = 0
        for c in word:
            while i < l and s[i] != c:
                i += 1
            if i == l:
                return False
            else:
                i += 1
        return True


# TLE
class Solution1:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ht = {}
        for i, c in enumerate(s):
            ht[c] = ht.get(c, []) + [i]

        num = 0
        for word in words:
            if self.isSubseq(word, ht):
                num += 1
        return num

    def isSubseq(self, word: str, ht: dict) -> bool:
        i = -1
        for c in word:
            if c in ht:
                for j in range(len(ht[c]) + 1):
                    if j >= len(ht[c]):
                        return False
                    elif ht[c][j] > i:
                        i = ht[c][j]
                        break
                    else:
                        j += 1
            else:
                return False
        return True


# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
# Runtime: 609 ms, faster than 69.81% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.6 MB, less than 75.71% of Python3 online submissions for Number of Matching Subsequences.
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


s = Solution1()
tests = [
    ("abcde", ["a", "bb", "acd", "ace"]),
    ("btovxbkumc", ["btovxbku", "to", "zueoxxxjme", "yjkclbkbtl"]),
    ("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]),
]
for t in tests:
    print(t)
    print(s.numMatchingSubseq(t[0], t[1]))
    print()
