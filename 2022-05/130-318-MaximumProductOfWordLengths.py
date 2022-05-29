"""
Leetcode
318. Maximum Product of Word Lengths (medium)
2022-05-29

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
"""

from typing import List



# https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/76970/Python-solution-beats-99.67
# Runtime: 304 ms, faster than 93.04% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.5 MB, less than 42.09% of Python3 online submissions for Maximum Product of Word Lengths.
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        # hash table: {bit mask (occurence of letters): max length of word that consists of that letters}
        ht = {}
        for word in words:
            mask = 0
            for c in set(word):
                mask = mask | (1 << (ord(c) - ord('a')))
            ht[mask] = max(ht.get(mask, 0), len(word))
        
        # find max product of word length, if don't share letters (bit masks are opposites)
        mp = 0
        for x in ht:
            for y in ht:
                if x & y == 0:
                    mp = max(mp, ht[x] * ht[y])

        return mp



s = Solution()
tests = [
    ["abcw","baz","foo","bar","xtfn","abcdef"],
    ["a","ab","abc","d","cd","bcd","abcd"],
    ["a","aa","aaa","aaaa"],
]
for t in tests:
    print(t)
    print(s.maxProduct(t))
    print()
