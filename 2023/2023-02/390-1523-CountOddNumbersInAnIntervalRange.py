"""
Leetcode
1523. Count Odd Numbers in an Interval Range (easy)
2023-02-13

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9]
"""

from typing import List, Optional


class Solution:
    """
    Runtime: 41 ms, faster than 19.45% of Python3 online submissions for Count Odd Numbers in an Interval Range.
    Memory Usage: 13.9 MB, less than 7.11% of Python3 online submissions for Count Odd Numbers in an Interval Range.
    """

    def countOdds(self, low: int, high: int) -> int:
        n_between = high - low
        if n_between % 2 == 0:
            return (n_between // 2) + (high % 2)
        return (n_between + 1) // 2


class Solution1:
    """
    https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/solution/1798856
    Runtime: 27 ms, faster than 88.64% of Python3 online submissions for Count Odd Numbers in an Interval Range.
Memory Usage: 13.8 MB, less than 95.07% of Python3 online submissions for Count Odd Numbers in an Interval Range.
    """

    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (high % 2 or low % 2)


s = Solution()
tests = [
    ((3, 7),
     3),

    ((8, 10),
     1)
]
for inp, exp in tests:
    res = s.countOdds(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
