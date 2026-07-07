"""
Leetcode
2026-07-07
3754. Concatenate Non-Zero Digits and Multiply by Sum I
Easy

You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

 

Example 1:

Input: n = 10203004

Output: 12340

Explanation:

    The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
    The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
    Therefore, the answer is x * sum = 1234 * 10 = 12340.

Example 2:

Input: n = 1000

Output: 1

Explanation:

    The non-zero digit is 1, so x = 1 and sum = 1.
    Therefore, the answer is x * sum = 1 * 1 = 1.

 

Constraints:

    0 <= n <= 10^9


"""


class Solution01:
    """
    Runtime 3ms Beats 22.16%
    Memory 19.28MB Beats 51.25%
    """

    def sumAndMultiply(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        x = 0
        s = 0

        for d in digits:
            if d != 0:
                x = (x * 10) + d
                s += d

        return x * s


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.48MB Beats 14.68%
    """

    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0

        for d in map(int, str(n)):
            if d != 0:
                x = (x * 10) + d
                s += d

        return x * s
