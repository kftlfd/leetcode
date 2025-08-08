"""
Leetcode
2025-08-08
808. Soup Servings
Medium

You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

    pour 100 mL from type A and 0 mL from type B
    pour 75 mL from type A and 25 mL from type B
    pour 50 mL from type A and 50 mL from type B
    pour 25 mL from type A and 75 mL from type B

Note:

    There is no operation that pours 0 mL from A and 100 mL from B.
    The amounts from A and B are poured simultaneously during the turn.
    If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.

The process stops immediately after any turn in which one of the soups is used up.

Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 50
Output: 0.62500
Explanation: 
If we perform either of the first two serving operations, soup A will become empty first.
If we perform the third operation, A and B will become empty at the same time.
If we perform the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Example 2:

Input: n = 100
Output: 0.71875
Explanation: 
If we perform the first serving operation, soup A will become empty first.
If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.

 

Constraints:

    0 <= n <= 10^9


"""

from collections import defaultdict
from functools import cache
from math import ceil


class Solution00:
    """
    RecursionError: maximum recursion depth exceeded
    """

    def soupServings(self, n: int) -> float:

        @cache
        def dfs(a: int, b: int) -> float:
            if a < 1 and b < 1:
                return 0.5

            if b < 1:
                return 0

            if a < 1:
                return 1

            return 0.25 * (
                dfs(a - 100, b) +
                dfs(a - 75, b - 25) +
                dfs(a - 50, b - 50) +
                dfs(a - 25, b - 75))

        return dfs(n, n)


class Solution01:
    """
    Runtime 7ms Beats 93.07%
    Memory 20.07MB Beats 43.56%
    """

    def soupServings(self, n: int) -> float:

        # lol
        if n > 4500:
            return 1

        @cache
        def dfs(a: int, b: int) -> float:
            if a < 1 and b < 1:
                return 0.5

            if b < 1:
                return 0

            if a < 1:
                return 1

            return 0.25 * (
                dfs(a - 100, b) +
                dfs(a - 75, b - 25) +
                dfs(a - 50, b - 50) +
                dfs(a - 25, b - 75))

        return dfs(n, n)


class Solution1:
    """
    leetcode solution 1: Bottom-Up Dynamic Programming
    Runtime 473ms Beats 5.28%
    Memory 20.06MB Beats 43.56%
    """

    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (
                dp[max(0, i - 4)][j] +
                dp[max(0, i - 3)][j - 1] +
                dp[max(0, i - 2)][max(0, j - 2)] +
                dp[i - 1][max(0, j - 3)]
            ) / 4

        dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1

        return dp[m][m]


class Solution2:
    """
    leetcode solution 2: Top-Down Dynamic Programming (Memoization)
    Runtime 193ms Beats 7.92%
    Memory 25.91MB Beats 7.26%
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
                calculate_dp(i - 4, j)
                + calculate_dp(i - 3, j - 1)
                + calculate_dp(i - 2, j - 2)
                + calculate_dp(i - 1, j - 3)
            ) / 4.0
            return dp[i][j]

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0

        return calculate_dp(m, m)
