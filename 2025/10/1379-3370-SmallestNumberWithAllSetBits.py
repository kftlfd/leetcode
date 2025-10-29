"""
Leetcode
2025-10-29
3370. Smallest Number With All Set Bits
Easy

You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

    1 <= n <= 1000

"""


class Solution01:
    """
    Runtime 3ms Beats 16.30%
    Memory 17.74MB Beats 47.25%
    """

    def smallestNumber(self, n: int) -> int:
        ans = 1
        while ans < n:
            ans = (ans << 1) + 1
        return ans


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.81MB Beats 26.92%
    """

    def smallestNumber(self, n: int) -> int:
        exp = len(bin(n)) - 2
        return (1 << exp) - 1


class Solution03:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.76MB Beats 47.25%
    """

    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1
