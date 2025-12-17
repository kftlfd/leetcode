"""
Leetcode
2025-12-17
3573. Best Time to Buy and Sell Stock V
Medium

You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

    Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

    Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

 

Example 1:

Input: prices = [1,7,9,8,2], k = 2

Output: 14

Explanation:
We can make $14 of profit through 2 transactions:

    A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
    A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.

Example 2:

Input: prices = [12,16,19,19,8,1,19,13,9], k = 3

Output: 36

Explanation:
We can make $36 of profit through 3 transactions:

    A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
    A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
    A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.

 

Constraints:

    2 <= prices.length <= 10^3
    1 <= prices[i] <= 10^9
    1 <= k <= prices.length / 2


Hint 1
Use dynamic programming.
Hint 2
Keep the following states: idx, transactionsDone, transactionType, isTransactionRunning.
Hint 3
Transactions transition from completed -> running and from running -> completed.
"""

from functools import cache
from typing import List


class Solution1:
    """
    leetcode solution 1: Memoization Search
    Runtime 3963ms Beats 21.13%
    Memory 184.64MB Beats 6.85%
    """

    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, state):
            if j == 0:
                return 0
            if i == 0:
                return (
                    0 if state == 0 else -
                    prices[0] if state == 1 else prices[0]
                )
            p = prices[i]
            if state == 0:
                res = max(
                    dfs(i - 1, j, 0), dfs(i - 1, j, 1) +
                    p, dfs(i - 1, j, 2) - p
                )
            elif state == 1:
                res = max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            else:
                res = max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)

            return res

        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans


class Solution2:
    """
    leetcode solution 2: Dynamic Programming
    Runtime 1716ms Beats 58.85%
    Memory 17.95MB Beats 96.19%
    """

    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(k + 1)]
        # initialize the state on day 0
        for j in range(1, k + 1):
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(
                    dp[j][0], max(dp[j][1] + prices[i], dp[j][2] - prices[i])
                )
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])

        return dp[k][0]


class Solution3:
    """
    sample 1227ms solution
    Runtime 1213ms Beats 93.14%
    Memory 18.18MB Beats 76.19%
    """

    def maximumProfit(self, prices: List[int], k: int) -> int:
        def makeTransaction(dp: List[int]) -> List[int]:
            update = [0] * n
            nrml, shrt = -prices[0], prices[0]

            for idx, price in (enumerate(prices[1:])):
                update[idx + 1] = max(update[idx], nrml + price, shrt - price)
                nrml, shrt = max(
                    nrml, dp[idx] - price), max(shrt, dp[idx] + price)
            return update

        n = len(prices)
        dp = [0] * n

        for _ in range(k):
            dp = makeTransaction(dp)
        return dp[-1]
