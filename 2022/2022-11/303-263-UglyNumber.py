"""
Leetcode
263. Ugly Number (easy)
2022-11-18

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

from typing import List, Optional


# leetcode solution
# Runtime: 71 ms, faster than 17.49% of Python3 online submissions for Ugly Number.
# Memory Usage: 13.9 MB, less than 12.22% of Python3 online submissions for Ugly Number.
class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        def factorOut(num, f):
            while num % f == 0:
                num //= f
            return num

        for f in [2, 3, 5]:
            n = factorOut(n, f)

        return n == 1


# https://leetcode.com/problems/ugly-number/solution/1688020
# Runtime: 72 ms, faster than 15.52% of Python3 online submissions for Ugly Number.
# Memory Usage: 13.9 MB, less than 60.08% of Python3 online submissions for Ugly Number.
class Solution2:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        while not n % 3:
            n //= 3

        while not n % 5:
            n //= 5

        # check if power of 2
        return (n & (n-1)) == 0


s = Solution()
tests = [
    (6,
     True),

    (1,
     True),

    (14,
     False),
]
for inp, exp in tests:
    res = s.isUgly(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
