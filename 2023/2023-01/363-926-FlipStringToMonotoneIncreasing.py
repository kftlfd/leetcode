"""
Leetcode
926. Flip String to Monotone Increasing (medium)
2023-01-18

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
"""

from typing import List, Optional


# leetcode solution 1 - Dynamic Windows
# Runtime: 165 ms, faster than 86.60% of Python3 online submissions for Flip String to Monotone Increasing.
# Memory Usage: 14.8 MB, less than 93.79% of Python3 online submissions for Flip String to Monotone Increasing.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == '0':
                m += 1
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans


# leetcode solution 2 - Dynamic Programming
# Runtime: 136 ms, faster than 93.14% of Python3 online submissions for Flip String to Monotone Increasing.
# Memory Usage: 15 MB, less than 53.59% of Python3 online submissions for Flip String to Monotone Increasing.
class Solution1:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0
        for c in s:
            if c == '0':
                ans = min(num, ans + 1)
            else:
                num += 1
        return ans


s = Solution()
tests = [
    ("00110",
     1),

    ("010110",
     2),

    ("00011000",
     2)
]
for inp, exp in tests:
    res = s.minFlipsMonoIncr(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
