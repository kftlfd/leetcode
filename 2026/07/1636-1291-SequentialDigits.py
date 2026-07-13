"""
Leetcode
2026-07-13
1291. Sequential Digits
Medium

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


"""

from typing import List


digits = "123456789"
nums = []
for l in range(2, 10):
    for s in range(10 - l):
        nums.append(int(digits[s:s+l]))


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.33MB Beats 30.59%
    """

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        return list(filter(lambda x: low <= x <= high, nums))
