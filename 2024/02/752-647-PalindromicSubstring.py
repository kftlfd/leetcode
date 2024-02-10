"""
Leetcode
647. Palindromic Substrings
Medium
2024-02-10

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""


from collections import deque


class Solution:
    """
    Runtime: 375 ms, faster than 15.14% of Python3 online submissions for Palindromic Substrings.
    Memory Usage: 91.9 MB, less than 7.76% of Python3 online submissions for Palindromic Substrings.
    """

    def countSubstrings(self, s: str) -> int:

        memo = {}

        def is_palindromic(start: int, end: int) -> bool:
            if start < 0 or end >= len(s):
                return False

            if start == end or start > end:
                return True

            if (start, end) in memo:
                return memo[(start, end)]

            res = s[start] == s[end] and is_palindromic(start + 1, end - 1)

            memo[(start, end)] = res
            return res

        q = deque()

        for i in range(len(s)):
            q.append((i, i))
        for i in range(len(s) - 1):
            q.append((i, i + 1))

        ans = 0

        while q:
            start, end = q.popleft()
            if is_palindromic(start, end):
                ans += 1
                q.append((start - 1, end + 1))

        return ans
