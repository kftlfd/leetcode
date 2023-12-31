"""
Leetcode
808. Soup Servings (medium)
2023-07-29

There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

    Serve 100 ml of soup A and 0 ml of soup B,
    Serve 75 ml of soup A and 25 ml of soup B,
    Serve 50 ml of soup A and 50 ml of soup B, and
    Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Example 2:

Input: n = 100
Output: 0.71875

Constraints:

    0 <= n <= 10^9
"""

from math import ceil
from collections import defaultdict


class Solution:
    """
    leetcode solution 1: bottom-up dynamic programming
    Time: O(1)
    Space: O(1)
    Runtime: 476 ms, faster than 9.91% of Python3 online submissions for Soup Servings.
    Memory Usage: 18.7 MB, less than 29.72% of Python3 online submissions for Soup Servings.
    """

    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i-4)][j] +
                    dp[max(0, i-3)][j-1] +
                    dp[max(0, i-2)][max(0, j-2)] +
                    dp[i-1][max(0, j-3)]) / 4

        dp[0] = {0: 0.5}

        for k in range(1, m+1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k+1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1

        return dp[m][m]


class Solution1:
    """
    leetcode solution 2: top-down dynamic programming (memoization)
    Time: O(1)
    Space: O(1)
    Runtime: 240 ms, faster than 21.70% of Python3 online submissions for Soup Servings.
    Memory Usage: 23.5 MB, less than 14.62% of Python3 online submissions for Soup Servings.
    """

    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = defaultdict(dict)

        def calculate_dp(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5

            if i <= 0:
                return 1.0

            if j <= 0:
                return 0.0

            if i in dp and j in dp[i]:
                return dp[i][j]

            dp[i][j] = (
                calculate_dp(i - 4, j) +
                calculate_dp(i - 3, j - 1) +
                calculate_dp(i - 2, j - 2) +
                calculate_dp(i - 1, j - 3)
            ) / 4.0

            return dp[i][j]

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0

        return calculate_dp(m, m)
