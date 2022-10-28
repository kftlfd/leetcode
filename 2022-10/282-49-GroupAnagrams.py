"""
Leetcode
49. Group Anagrams (medium)
2022-10-28

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

from typing import List, Optional
from collections import defaultdict


# Runtime: 371 ms, faster than 5.17% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.5 MB, less than 39.60% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hash_str(s: str) -> str:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            return ".".join([str(c) for c in letters])

        hm = defaultdict(list)

        for s in strs:
            hm[hash_str(s)].append(s)

        return hm.values()


# Runtime: 197 ms, faster than 62.48% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 58.95% of Python3 online submissions for Group Anagrams.
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)

        for s in strs:
            hm["".join(sorted(s))].append(s)

        return hm.values()


s = Solution()
tests = [
    (["bdddddddddd", "bbbbbbbbbbc"],
     [["bbbbbbbbbbc"], ["bdddddddddd"]]),

    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),

    ([""],
     [[""]]),

    (["a"],
     [["a"]])
]
for inp, exp in tests:
    res = s.groupAnagrams(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
