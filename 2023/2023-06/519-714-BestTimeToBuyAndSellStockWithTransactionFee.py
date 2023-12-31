"""
Leetcode
714. Best Time to Buy and Sell Stock with Transaction Fee (medium)
2023-06-22

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:

    1 <= prices.length <= 5 * 10^4
    1 <= prices[i] < 5 * 10^4
    0 <= fee < 5 * 10^4
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Dynamic Programming
    Time: O(n)
    Space: O(n)
    Runtime: 776 ms, faster than 61.59% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    Memory Usage: 23.3 MB, less than 67.04% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [0] * n
        free = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]


class Solution1:
    """
    leetcode solution 2: Space-Optimized Dynamic Programming
    Time: O(n)
    Space: O(1)
    Runtime: 680 ms, faster than 86.79% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    Memory Usage: 23.2 MB, less than 96.30% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = -prices[0]
        free = 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free


s = Solution1()
tests = [
    (([1, 3, 2, 8, 4, 9], 2),
     8),

    (([1, 3, 7, 5, 10, 3], 3),
     6),
]
for inp, exp in tests:
    res = s.maxProfit(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
