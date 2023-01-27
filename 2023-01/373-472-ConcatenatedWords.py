"""
Leetcode
472. Concatenated Words (hard)
2023-01-27

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
"""

from typing import List, Optional


# https://leetcode.com/problems/concatenated-words/discuss/95639/Python3-Solution-beats-100
# Runtime: 342 ms, faster than 93.09% of Python3 online submissions for Concatenated Words.
# Memory Usage: 27.7 MB, less than 37.94% of Python3 online submissions for Concatenated Words.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        res = []
        words_set = set(words)

        def check(word):
            if word in words_set:
                return True
            for i in range(len(word)):
                if word[i:] in words_set and check(word[:i]):
                    return True
            return False

        for word in words:
            words_set.remove(word)
            if check(word):
                res.append(word)
            words_set.add(word)

        return res


s = Solution()
tests = [
    (["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
     ["catsdogcats", "dogcatsdog", "ratcatdogcat"]),

    (["cat", "dog", "catdog"],
     ["catdog"])
]
for inp, exp in tests:
    res = s.findAllConcatenatedWordsInADict(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
