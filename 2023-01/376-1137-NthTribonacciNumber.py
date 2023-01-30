"""
Leetcode
1137. N-th Tribonacci Number (easy)
2023-01-30

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
"""

from typing import List, Optional


# Runtime: 29 ms, faster than 83.30% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 10.24% of Python3 online submissions for N-th Tribonacci Number.
class Solution:
    vals = {
        0: 0,
        1: 1,
        2: 1
    }

    def tribonacci(self, n: int) -> int:
        if n in self.vals:
            return self.vals[n]

        val = self.tribonacci(n-1) + \
            self.tribonacci(n-2) + \
            self.tribonacci(n-3)

        self.vals[n] = val

        return val


# Runtime: 19 ms, faster than 99.65% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.8 MB, less than 54.01% of Python3 online submissions for N-th Tribonacci Number.
class Solution1:
    vals = {}

    def tribonacci(self, n: int) -> int:
        if not self.vals:
            self.vals[0] = 0
            self.vals[1] = 1
            self.vals[2] = 1
            for i in range(3, 38):
                self.vals[i] = \
                    self.vals[i - 1] + \
                    self.vals[i - 2] + \
                    self.vals[i - 3]

        return self.vals[n]


s = Solution1()
tests = [
    (4,
     4),

    (25,
     1389537)
]
for inp, exp in tests:
    res = s.tribonacci(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
