"""
Leetcode
2025-08-29
3021. Alice and Bob Playing Flower Game
Medium

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.

The game proceeds as follows:

    Alice takes the first turn.
    In each turn, a player must choose either one of the lane and pick one flower from that side.
    At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.

Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

    Alice must win the game according to the described rules.
    The number of flowers x in the first lane must be in the range [1,n].
    The number of flowers y in the second lane must be in the range [1,m].

Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

 

Example 1:

Input: n = 3, m = 2
Output: 3
Explanation: The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

Example 2:

Input: n = 1, m = 1
Output: 0
Explanation: No pairs satisfy the conditions described in the statement.

 

Constraints:

    1 <= n, m <= 105


Hint 1
(x, y) is valid if and only if they have different parities.
"""

from math import ceil


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.79MB Beats 61.11%
    """

    def flowerGame(self, n: int, m: int) -> int:
        # ceil(x / 2) = number of odd numbers in [1, x]
        # x // 2 = number of even numbers in [1, x]
        return (ceil(n / 2) * (m // 2)) + ((n // 2) * ceil(m / 2))


class Solution1:
    """
    leetcode solution: Mathematics
    Runtime 0ms Beats 100.00%
    Memory 17.74MB Beats 61.11%
    """

    def flowerGame(self, n: int, m: int) -> int:
        # the total number of pairs (x,y) that meet the conditions is
        # ceil(n/2)*floor(m/2) + floor(n/2)*ceil(m/2)
        # which simplifies to
        # floor(m * n / 2)
        return (m * n) // 2
