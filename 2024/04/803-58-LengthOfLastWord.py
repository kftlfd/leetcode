"""
Leetcode
58. Length of Last Word
Easy
2024-04-01

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""


class Solution:
    """
    Runtime: 32 ms, faster than 75.14% of Python3 online submissions for Length of Last Word.
    Memory Usage: 16.7 MB, less than 27.38% of Python3 online submissions for Length of Last Word.
    """

    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            elif length > 0:
                break

        return length
