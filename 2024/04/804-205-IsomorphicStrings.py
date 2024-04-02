"""
Leetcode
205. Isomorphic Strings
Easy
2024-04-02

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

 

Constraints:

    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    """
    Runtime: 48 ms, faster than 27.49% of Python3 online submissions for Isomorphic Strings.
    Memory Usage: 16.8 MB, less than 32.93% of Python3 online submissions for Isomorphic Strings.
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()

        for c1, c2 in zip(s, t):
            if c1 not in mapping:
                if c2 in mapped:
                    return False
                mapping[c1] = c2
                mapped.add(c2)
            elif mapping[c1] != c2:
                return False

        return True


class Solution1:
    """
    sample 29 ms submission
    Runtime: 43 ms, faster than 55.52% of Python3 online submissions for Isomorphic Strings.
    Memory Usage: 16.8 MB, less than 32.93% of Python3 online submissions for Isomorphic Strings.
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                # Init
                d[s[i]] = t[i]
        return True
