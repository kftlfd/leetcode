"""
Leetcode
2025-04-30
1295. Find Numbers with Even Number of Digits
Easy

Given an array nums of integers, return how many of them contain an even number of digits.



Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.



Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5


Hint 1
How to compute the number of digits of a number ?
Hint 2
Divide the number by 10 again and again to get the number of digits.
"""

from typing import List


class Solution00:
    """
    Runtime 4ms Beats 16.54%
    Memory 17.71MB Beats 83.23%
    """

    def findNumbers(self, nums: List[int]) -> int:
        def is_even_digits(n: int) -> bool:
            return 10 <= n < 100 or 1_000 <= n < 10_000 or 100_000 <= n < 1_000_000

        return sum(is_even_digits(n) for n in nums)


class Solution01:
    """
    Runtime 4ms Beats 16.54%
    Memory 18.04MB Beats 13.14%
    """

    def findNumbers(self, nums: List[int]) -> int:
        def is_even_digits(num: int) -> bool:
            n = 0
            while num > 0:
                n += 1
                num //= 10
            return n % 2 == 0

        return sum(is_even_digits(n) for n in nums)


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.72MB Beats 83.23%
    """

    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            if len(str(num)) & 1 == 0:
                ans += 1

        return ans
