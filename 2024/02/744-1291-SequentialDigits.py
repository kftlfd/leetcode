"""
Leetcode
1291. Sequential Digits
Medium
2024-02-02

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

 

Constraints:

    10 <= low <= high <= 10^9

Hints:
- Generate all numbers with sequential digits and check if they are in the given range.
- Fix the starting digit then do a recursion that tries to append all valid digits.
"""

from typing import List


class Solution:
    """
    Runtime: 36 ms, faster than 58.70% of Python3 online submissions for Sequential Digits.
    Memory Usage: 16.5 MB, less than 72.98% of Python3 online submissions for Sequential Digits.
    """

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        def rec_add_digits(num: int):
            last_digit = int(str(num)[-1])

            if last_digit == 9:
                return

            next_num = num * 10 + (last_digit + 1)

            if next_num > high:
                return

            if next_num >= low:
                ans.append(next_num)

            rec_add_digits(next_num)

        for i in range(1, 9):
            rec_add_digits(i)

        return sorted(ans)


class Solution1:
    """
    Runtime: 29 ms, faster than 89.75% of Python3 online submissions for Sequential Digits.
    Memory Usage: 16.5 MB, less than 63.35% of Python3 online submissions for Sequential Digits.
    """

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [12, 23, 34, 45, 56, 67, 78, 89,
                123, 234, 345, 456, 567, 678, 789,
                1234, 2345, 3456, 4567, 5678, 6789,
                12345, 23456, 34567, 45678, 56789,
                123456, 234567, 345678, 456789,
                1234567, 2345678, 3456789,
                12345678, 23456789,
                123456789]

        return filter(lambda n: low <= n <= high, nums)
