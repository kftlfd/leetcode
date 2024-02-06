"""
Leetcode
49. Group Anagrams
Medium
2024-02-06

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

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime: 95 ms, faster than 47.74% of Python3 online submissions for Group Anagrams.
    Memory Usage: 21.5 MB, less than 32.83% of Python3 online submissions for Group Anagrams.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def to_hash(word: str):
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            return tuple(arr)

        ht = defaultdict(list)
        for word in strs:
            ht[to_hash(word)].append(word)

        return list(ht.values())
