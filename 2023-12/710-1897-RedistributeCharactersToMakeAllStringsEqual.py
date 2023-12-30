"""
Leetcode
1897. Redistribute Characters to Make All Strings Equal
Easy
2023-12-30

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

 

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 77 ms, faster than 17.14% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
    Memory Usage: 17.4 MB, less than 9.52% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
    """

    def makeEqual(self, words: List[str]) -> bool:
        count = Counter()

        for word in words:
            count += Counter(word)

        n = len(words)

        for char_count in count.values():
            if char_count % n != 0:
                return False

        return True
