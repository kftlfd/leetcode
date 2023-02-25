"""
Leetcode
121. Best Time to Buy and Sell Stock (easy)
2023-02-25

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List, Optional


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-:)-(In-case-if-interviewer-twists-the-input)
    Runtime: 1179 ms, faster than 27.92% of Python3 online submissions for Best Time to Buy and Sell Stock.
    Memory Usage: 25 MB, less than 32.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
    """

    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        max_curr = 0
        max_so_far = 0

        for i in range(1, len(prices)):
            max_curr += prices[i] - prices[i - 1]
            max_curr = max(0, max_curr)
            max_so_far = max(max_curr, max_so_far)

        return max_so_far


s = Solution()
tests = [
    ([7, 1, 5, 3, 6, 4],
     5),

    ([7, 6, 4, 3, 1],
     0),
]
for inp, exp in tests:
    res = s.maxProfit(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
