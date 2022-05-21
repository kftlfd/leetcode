"""
Leetcode
322. Coin Change (medium)
2022-05-21

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from typing import List



# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code/308569
# Runtime: 1679 ms, faster than 66.48% of Python3 online submissions for Coin Change.
# Memory Usage: 14.3 MB, less than 39.77% of Python3 online submissions for Coin Change.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]



s = Solution()
tests = [
    [[1,2,5], 11],
    [[2], 3],
    [[1], 0]
]
for t in tests:
    print(*t)
    print(s.coinChange(t[0], t[1]))
    print()
