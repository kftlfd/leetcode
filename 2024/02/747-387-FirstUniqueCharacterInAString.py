"""
Leetcode
387. First Unique Character in a String
Easy
2024-02-05

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""


class Solution:
    """
    Runtime: 67 ms, faster than 95.48% of Python3 online submissions for First Unique Character in a String.
    Memory Usage: 16.7 MB, less than 78.97% of Python3 online submissions for First Unique Character in a String.
    """

    def firstUniqChar(self, s: str) -> int:
        places = {}  # {c: [first, last]}

        for i, c in enumerate(s):
            if c not in places:
                places[c] = [i, i]
            else:
                places[c][1] = i

        for first, last in places.values():
            if first == last:
                return first

        return -1
