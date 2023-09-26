"""
Leetcode
316. Remove Duplicate Letters (medium)
2023-09-26

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.
"""


class Solution:
    """
    https://leetcode.com/problems/remove-duplicate-letters/discuss/1859515/Python-oror-O(n)-Beats-98-oror-Stack-oror-Detailed-Explanation-oror-Simple
    Runtime: 39 ms, faster than 78.86% of Python3 online submissions for Remove Duplicate Letters.
    Memory Usage: 16.3 MB, less than 52.05% of Python3 online submissions for Remove Duplicate Letters.
    """

    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        stack = []
        visited = set()

        for i in range(len(s)):
            last_occ[s[i]] = i

        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])

        return ''.join(stack)
