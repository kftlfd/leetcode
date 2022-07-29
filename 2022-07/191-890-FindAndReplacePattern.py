"""
Leetcode
890. Find and Replace Pattern (medium)
2022-07-29

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
"""

from typing import List


# Runtime: 42 ms, faster than 73.01% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 13.9 MB, less than 28.72% of Python3 online submissions for Find and Replace Pattern.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def hash(word: str) -> List[int]:
            ht = {"length": 0, "seq": []}
            for c in word:
                if c not in ht:
                    ht[c] = ht["length"]
                    ht["length"] += 1
                ht["seq"].append(ht[c])
            return ht["seq"]

        pattern_hash = hash(pattern)

        return [w for w in words if hash(w) == pattern_hash]


# leetcode solution 1
# https://leetcode.com/problems/find-and-replace-pattern/solution/
# Runtime: 27 ms, faster than 99.31% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 13.9 MB, less than 76.64% of Python3 online submissions for Find and Replace Pattern.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)


# leetcode solution 2
# https://leetcode.com/problems/find-and-replace-pattern/solution/
# Runtime: 67 ms, faster than 15.40% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14 MB, less than 28.72% of Python3 online submissions for Find and Replace Pattern.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)


s = Solution()
tests = [
    (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"),
    (["a", "b", "c"], "a"),
]
for words, pattern in tests:
    print(words, pattern)
    print(s.findAndReplacePattern(words, pattern))
    print()
