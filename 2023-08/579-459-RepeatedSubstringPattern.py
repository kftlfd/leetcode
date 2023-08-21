"""
Leetcode
459. Repeated Substring Pattern (easy)
2023-08-21

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.
"""

import re


class Solution:
    """
    brute-force: Time Limit Exceeded
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        for end in range(1, len(s) // 2 + 1):
            pattern = s[:end]
            matches = re.findall(pattern, s)
            if len(matches) * len(pattern) == len(s):
                return True
        return False


class Solution1:
    """
    brute-force + skip non-divisors
    Runtime: 901 ms, faster than 6.35% of Python3 online submissions for Repeated Substring Pattern.
    Memory Usage: 22.3 MB, less than 7.19% of Python3 online submissions for Repeated Substring Pattern.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for end in range(1, len(s) // 2 + 1):
            if n % end != 0:
                continue

            pattern = s[:end]
            matches = re.findall(pattern, s)

            if len(matches) * len(pattern) == n:
                return True

        return False


class Solution2:
    """
    leetcode solution 1: Using Divisors
    Runtime: 39 ms, faster than 94.52% of Python3 online submissions for Repeated Substring Pattern.
    Memory Usage: 16.2 MB, less than 94.58% of Python3 online submissions for Repeated Substring Pattern.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False


class Solution3:
    """
    leetcode solution 2: String Concatenation
    Runtime: 41 ms, faster than 91.38% of Python3 online submissions for Repeated Substring Pattern.
    Memory Usage: 16.4 MB, less than 75.82% of Python3 online submissions for Repeated Substring Pattern.
    """

    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        if s in t[1:-1]:
            return True
        return False


sol = Solution()
tests = [
    ('abab',
     True),

    ('aba',
     False),

    ('abcabcabcabc',
     True),
]
for inp, exp in tests:
    res = sol.repeatedSubstringPattern(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
