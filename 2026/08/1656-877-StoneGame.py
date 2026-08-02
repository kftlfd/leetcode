"""
Leetcode
2026-08-02
877. Stone Game
Medium

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example 2:

Input: piles = [3,7,2,3]
Output: true

 

Constraints:

    2 <= piles.length <= 500
    piles.length is even.
    1 <= piles[i] <= 500
    sum(piles[i]) is odd.


"""

from functools import lru_cache
from typing import List


class Solution:
    """
    solution for "486. Predict the Winner"
    Runtime 83ms Beats 46.19%
    Memory 19.32MB Beats 55.87%
    """

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(piles[left] - dp[left + 1],
                               piles[right] - dp[left])

        return dp[0] >= 0


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 402ms Beats 18.00%
    Memory 137.39MB Beats 18.28%
    """

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j:
                return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                return min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))

        return dp(0, N - 1) > 0


class Solution2:
    """
    leetcode solution 2: Mathematical
    Runtime 0ms Beats 100.00%
    Memory 19.18MB Beats 93.91%
    """

    def stoneGame(self, piles: List[int]) -> bool:
        return True
