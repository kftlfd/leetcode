"""
Leetcode
2025-04-11
2843. Count Symmetric Integers
Easy

You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

 

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.

 

Constraints:

    1 <= low <= high <= 10^4


Hint 1
Iterate over all numbers from low to high
Hint 2
Convert each number to a string and compare the sum of the first half with that of the second.
"""

from itertools import chain


class Solution:
    """
    Runtime 975ms Beats 9.16%
    Memory 17.61MB Beats 96.13%
    """

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for num in chain(range(max(11, low), min(100, high+1)), range(max(1001, low), min(10000, high+1))):
            num_s = str(num)
            n = len(num_s) // 2
            half_1, half_2 = num_s[:n], num_s[n:]
            ans += sum(int(x) for x in list(half_1)) == sum(int(x)
                                                            for x in list(half_2))

        return ans


class Solution1:
    """
    leetcode solution
    Runtime 106ms Beats 96.74%
    Memory 17.83MB Beats 54.99%
    """

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res
