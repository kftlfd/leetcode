"""
Leetcode
309. Best Time to Buy and Sell Stock with Cooldown (medium)
2022-12-23

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
"""

from typing import List, Optional


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75942/4-line-Python-solution-52-ms
# Runtime: 85 ms, faster than 49.10% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 14.1 MB, less than 81.39% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(
                hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)


s = Solution()
tests = [
    ([1, 2, 3, 0, 2],
     3),

    ([1],
     0)
]
for inp, exp in tests:
    res = s.maxProfit(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
