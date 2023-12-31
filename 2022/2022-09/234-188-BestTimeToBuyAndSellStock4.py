"""
Leetcode
188. Best Time to Buy and Sell Stock IV (hard)
2022-09-10

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2555676/Python-Simple-DP-O(nk)-Uses-the-idea-of-"reinvesting"
# Runtime: 204 ms, faster than 53.52% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 13.8 MB, less than 95.05% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        min_price = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                min_price[i] = min(min_price[i], price - max_profit[i-1])
                max_profit[i] = max(max_profit[i], price - min_price[i])

        return max_profit[k]


s = Solution()
tests = [
    (2, [2, 4, 1]),
    (2, [3, 2, 6, 5, 0, 3]),
]
for k, prices in tests:
    print(k, prices)
    print(s.maxProfit(k, prices))
    print()
