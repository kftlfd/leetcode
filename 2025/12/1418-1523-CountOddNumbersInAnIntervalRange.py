"""
Leetcode
2025-12-07
1523. Count Odd Numbers in an Interval Range
Easy

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

 

Constraints:

    0 <= low <= high <= 10^9


Hint 1
If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.
Hint 2
If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.
"""


class Solution:
    """
    Runtime 39ms Beats 44.79%
    Memory 17.89MB Beats 29.92%
    """

    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0:
            low -= 1
        if high % 2 != 0:
            high += 1
        return (high - low) // 2
