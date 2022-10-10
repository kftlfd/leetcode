"""
Leetcode
1328. Break a Palindrome (medium)
2022-10-10

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
"""

from typing import List, Optional


# https://leetcode.com/problems/break-a-palindrome/discuss/2687335/python-EASY-beats-92.92
# Runtime: 45 ms, faster than 68.88% of Python3 online submissions for Break a Palindrome.
# Memory Usage: 13.9 MB, less than 13.13% of Python3 online submissions for Break a Palindrome.
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""

        idx = -1
        for c in palindrome[:len(palindrome)//2 + 1]:
            idx += 1
            if c != 'a':
                break

        if idx == len(palindrome) // 2:
            return palindrome[:len(palindrome) - 1] + 'b'

        return palindrome[:idx] + 'a' + palindrome[idx + 1:]


s = Solution()
tests = [
    "aba",
    "abccba",
    "a",
    "aaaaaaa",
]
for t in tests:
    print(t)
    print(s.breakPalindrome(t))
    print()
