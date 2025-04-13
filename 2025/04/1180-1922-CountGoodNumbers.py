"""
Leetcode
2025-04-13
1922. Count Good Numbers
Medium

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

    For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.

Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example 2:

Input: n = 4
Output: 400

Example 3:

Input: n = 50
Output: 564908303

 

Constraints:

    1 <= n <= 10^15


Hint 1
Is there a formula we can use to find the count of all the good numbers?
Hint 2
Exponentiation can be done very fast if we looked at the binary bits of n.
"""


class Solution:
    """
    Time Limit Exceeded
    """

    def countGoodNumbers(self, n: int) -> int:
        even, rem = divmod(n, 2)
        odd = even

        if rem > 0:
            even += 1

        return ((5 ** even) * (4 ** odd)) % (10**9 + 7)


class Solution1:
    """
    leetcode solution 1: Fast Exponentiation
    Runtime 0ms Beats 100.00%
    Memory 17.72MB Beats 71.93%
    """

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        # use fast exponentiation to calculate x^y % mod
        def quickmul(x: int, y: int) -> int:
            ret, mul = 1, x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2
            return ret

        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod
