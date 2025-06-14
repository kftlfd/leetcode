"""
Leetcode
2025-06-14
2566. Maximum Difference by Remapping a Digit
Easy

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

    When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
    Bob can remap a digit to itself, in which case num does not change.
    Bob can remap different digits for obtaining minimum and maximum values respectively.
    The resulting number after remapping can contain leading zeroes.

 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.

Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.

 

Constraints:

    1 <= num <= 10^8


Hint 1
Try to remap the first non-nine digit to 9 to obtain the maximum number.
Hint 2
Try to remap the first non-zero digit to 0 to obtain the minimum number.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.74MB Beats 45.89%
    """

    def minMaxDifference(self, num: int) -> int:
        num_list = list(str(num))

        max_remap = num
        for c in num_list:
            if c != "9":
                max_remap = self.remap(num_list, c, "9")
                break

        min_remap = num
        for c in num_list:
            if c != "0":
                min_remap = self.remap(num_list, c, "0")
                break

        return max_remap - min_remap

    def remap(self, num: List[str], d1: str, d2: str) -> int:
        out = num[:]

        for i, d in enumerate(num):
            if d == d1:
                out[i] = d2

        return int("".join(out))


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 0ms Beats 100.00%
    Memory 17.61MB Beats 76.62%
    """

    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], "9")
        t = t.replace(t[0], "0")
        return int(s) - int(t)
