"""
Leetcode
1137. N-th Tribonacci Number
Easy
2024-04-24

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

 

Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    """
    Runtime: 30 ms, faster than 82.85% of Python3 online submissions for N-th Tribonacci Number.
    Memory Usage: 16.5 MB, less than 31.32% of Python3 online submissions for N-th Tribonacci Number.
    """

    def __init__(self):
        self.memo = {
            0: 0,
            1: 1,
            2: 1,
        }

    def tribonacci(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = (
                self.tribonacci(n-1) +
                self.tribonacci(n-2) +
                self.tribonacci(n-3)
            )
        return self.memo[n]
