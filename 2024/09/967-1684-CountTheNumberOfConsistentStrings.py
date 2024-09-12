"""
Leetcode
2024-09-12
1684. Count the Number of Consistent Strings
Easy

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

 

Constraints:

    1 <= words.length <= 10^4
    1 <= allowed.length <= 26
    1 <= words[i].length <= 10
    The characters in allowed are distinct.
    words[i] and allowed contain only lowercase English letters.
"""

from typing import List


class Solution01:
    """
    Runtime: 201 ms, faster than 80.88% of Python3 online submissions for Count the Number of Consistent Strings.
    Memory Usage: 18.4 MB, less than 83.05% of Python3 online submissions for Count the Number of Consistent Strings.
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)
        ans = 0

        for word in words:
            is_ok = 1
            for c in word:
                if c not in chars:
                    is_ok = 0
                    break
            ans += is_ok

        return ans


class Solution02:
    """
    Runtime: 204 ms, faster than 74.31% of Python3 online submissions for Count the Number of Consistent Strings.
    Memory Usage: 18.6 MB, less than 40.73% of Python3 online submissions for Count the Number of Consistent Strings.
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = ord("a")
        chars = [False] * 26
        for c in allowed:
            chars[ord(c) - a] = True

        ans = 0
        for word in words:
            is_ok = 1
            for c in word:
                if not chars[ord(c) - a]:
                    is_ok = 0
                    break
            ans += is_ok

        return ans


class Solution1:
    """
    https://leetcode.com/problems/count-the-number-of-consistent-strings/solution/2621063
    Runtime: 233 ms, faster than 25.37% of Python3 online submissions for Count the Number of Consistent Strings.
    Memory Usage: 18.4 MB, less than 83.05% of Python3 online submissions for Count the Number of Consistent Strings.
    """

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum((all((c in allowed) for c in word) for word in words))
