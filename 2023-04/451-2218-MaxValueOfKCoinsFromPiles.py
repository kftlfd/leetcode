"""
Leetcode
2218. Maximum Value of K Coins From Piles (hard)
2023-04-15

There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Example 1:
Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.

Example 2:
Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Bottom-up Dynamic Programming
    Runtime: 8335 ms, faster than 5.03% of Python3 online submissions for Maximum Value of K Coins From Piles.
    Memory Usage: 53.4 MB, less than 69.18% of Python3 online submissions for Maximum Value of K Coins From Piles.
    """

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            for coins in range(0, k + 1):
                current_sum = 0
                for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                    if current_coins > 0:
                        current_sum += piles[i - 1][current_coins - 1]
                    dp[i][coins] = max(dp[i][coins],
                                       dp[i - 1][coins - current_coins] + current_sum)
        return dp[n][k]


class Solution1:
    """
    leetcode solution 2: Top-Down Dynamic Programming (Memoization)
    Runtime: 5523 ms, faster than 32.08% of Python3 online submissions for Maximum Value of K Coins From Piles.
    Memory Usage: 44 MB, less than 76.10% of Python3 online submissions for Maximum Value of K Coins From Piles.
    """

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for i in range(n + 1)]

        def f(i, coins):
            if i == 0:
                return 0
            if dp[i][coins] != -1:
                return dp[i][coins]
            current_sum = 0
            for current_coins in range(0, min(len(piles[i - 1]), coins) + 1):
                if current_coins > 0:
                    current_sum += piles[i - 1][current_coins - 1]
                dp[i][coins] = max(dp[i][coins],
                                   f(i - 1, coins - current_coins) + current_sum)
            return dp[i][coins]

        return f(n, k)


s = Solution()
tests = [
    (([[1, 100, 3], [7, 8, 9]], 2),
     101),

    (([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7),
     706),
]
for inp, exp in tests:
    res = s.maxValueOfCoins(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
