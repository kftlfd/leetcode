"""
Leetcode
916. Word Subsets (medium)
2022-07-30

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

 - For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""

from typing import List


# Time Limit Exceeded
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def make_hash(word: str) -> dict:
            h = {}
            for c in word:
                h[c] = h.get(c, 0) + 1
            return h

        def is_subset(check: dict, word: dict) -> bool:
            for c in check.keys():
                if c not in word or word[c] < check[c]:
                    return False
            return True

        words1_h = {w: make_hash(w) for w in words1}
        words2_h = [make_hash(w) for w in words2]

        ans = []
        for w1 in words1_h.keys():
            if all([is_subset(w2, words1_h[w1]) for w2 in words2_h]):
                ans.append(w1)
        return ans


# leetcode solution
# https://leetcode.com/problems/word-subsets/solution/
# Runtime: 1994 ms, faster than 12.34% of Python3 online submissions for Word Subsets.
# Memory Usage: 18.5 MB, less than 73.00% of Python3 online submissions for Word Subsets.
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in words2:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in words1:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans


s = Solution()
tests = [
    (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]),
    (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]),
]
for words1, words2 in tests:
    print(words1, words2)
    print(s.wordSubsets(words1, words2))
    print()
