"""
Leetcode
2025-12-15
2110. Number of Smooth Descent Periods of a Stock
Medium

You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 

Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.

Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.

Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]

 

Constraints:

    1 <= prices.length <= 10^5
    1 <= prices[i] <= 10^5


Hint 1
Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].
Hint 2
Think of a 2-pointer approach to traverse the array and find each longest possible period.
Hint 3
Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k.
"""

from typing import List


class Solution:
    """
    Runtime 70ms Beats 28.36%
    Memory 29.64MB Beats 90.30%
    """

    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        streak = 0

        for i in range(1, len(prices)):
            prev, cur = prices[i-1], prices[i]
            if cur == prev - 1:
                streak += 1
                ans += streak
            else:
                streak = 0

        return ans


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 47ms Beats 87.31%
    Memory 29.86MB Beats 70.52%
    """

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        # total number of smooth descending periods, initial value is dp[0]
        res = 1
        # total number of smooth descending periods ending with the previous element, initial value is dp[0]
        prev = 1
        # traverse the array starting from 1, and update prev and the total res according to the recurrence relation
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev
        return res
