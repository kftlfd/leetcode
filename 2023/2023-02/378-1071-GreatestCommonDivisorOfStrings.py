"""
Leetcode
1071. Greatest Common Divisor of Strings (easy)
2023-02-01

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

from typing import List, Optional
from math import gcd


class Solution:
    """
    Runtime: 36 ms, faster than 66.52% of Python3 online submissions for Greatest Common Divisor of Strings.
    Memory Usage: 13.9 MB, less than 70.81% of Python3 online submissions for Greatest Common Divisor of Strings.
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def check_divisible(s: str, divisor: str) -> bool:
            n = len(s) / len(divisor)
            return not (n % 1 > 0) and (divisor * int(n) == s)

        gcd = ""

        shorter_str = str2 if len(str2) < len(str1) else str1

        for i in range(len(shorter_str), 0, -1):
            divisor = shorter_str[:i]
            if check_divisible(str1, divisor) and check_divisible(str2, divisor):
                gcd = divisor
                break

        return gcd


class Solution1:
    """
    leetcode solution
    Runtime: 36 ms, faster than 66.52% of Python3 online submissions for Greatest Common Divisor of Strings.
    Memory Usage: 13.9 MB, less than 70.81% of Python3 online submissions for Greatest Common Divisor of Strings.
    """

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]


s = Solution1()
tests = [
    (("ABCABC", "ABC"),
     "ABC"),

    (("ABABAB", "ABAB"),
     "AB"),

    (("LEET", "CODE"),
     "")
]
for inp, exp in tests:
    res = s.gcdOfStrings(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
