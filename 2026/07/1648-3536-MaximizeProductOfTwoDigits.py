"""
Leetcode
2026-07-25
3536. Maximum Product of Two Digits
Easy

You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

    The digits of n are [3, 1].
    The possible products of any two digits are: 3 * 1 = 3.
    The maximum product is 3.

Example 2:

Input: n = 22

Output: 4

Explanation:

    The digits of n are [2, 2].
    The possible products of any two digits are: 2 * 2 = 4.
    The maximum product is 4.

Example 3:

Input: n = 124

Output: 8

Explanation:

    The digits of n are [1, 2, 4].
    The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
    The maximum product is 8.

 

Constraints:

    10 <= n <= 10^9


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.26MB Beats 54.97%
    """

    def maxProduct(self, n: int) -> int:
        d = sorted(map(int, str(n)), reverse=True)
        return d[0] * d[1]


class Solution1:
    """
    leetcode solution: Bitwise Comparison
    Runtime 0ms Beats 100.00%
    Memory 19.20MB Beats 88.69%
    """

    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        while n > 0:
            x = n % 10
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
            n //= 10
        return first * second
