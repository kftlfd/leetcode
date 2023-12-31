"""
Leetcode
518. Coin Change II (medium)
2023-08-11

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10]
Output: 1

Constraints:

    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""

from typing import List


class Solution:
    """
    wrong answer
    """

    def change(self, amount: int, coins: List[int]) -> int:

        coins = sorted(coins)

        def combinations(target_amount: int) -> int:
            ans = 0
            for coin in coins:
                if coin < target_amount:
                    ans += combinations(target_amount - coin)
                elif coin == target_amount:
                    ans += 1
                else:
                    break
            return ans

        return combinations(amount)


class Solution1:
    """
    leetcode solution 1: top-down DP
    Time: O(n * amount)
    Space: O(n * amount)
    Runtime: 350 ms, faster than 56.13% of Python3 online submissions for Coin Change II.
    Memory Usage: 40.8 MB, less than 28.03% of Python3 online submissions for Coin Change II.
    """

    def change(self, amount: int, coins: List[int]) -> int:

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        def numberOfWays(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                memo[i][amount] = numberOfWays(
                    i, amount - coins[i]) + numberOfWays(i + 1, amount)

            return memo[i][amount]

        return numberOfWays(0, amount)


class Solution2:
    """
    leetcode solution 2: bottom-up DP
    Time: O(n * amount)
    Space: O(n * amount)
    Runtime: 272 ms, faster than 64.24% of Python3 online submissions for Coin Change II.
    Memory Usage: 25.9 MB, less than 60.04% of Python3 online submissions for Coin Change II.
    """

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]


class Solution3:
    """
    leetcode solution 3: DP with space optimization
    Time: O(n * amount)
    Space: O(amount)
    Runtime: 111 ms, faster than 97.97% of Python3 online submissions for Coin Change II.
    Memory Usage: 16.5 MB, less than 77.22% of Python3 online submissions for Coin Change II.
    """

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]


s = Solution1()
tests = [
    ((5, [1, 2, 5]),
     4),

    ((3, [2]),
     0),

    ((10, [10]),
     1),
]
for inp, exp in tests:
    res = s.change(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
