"""
Leetcode
2025-07-13
2410. Maximum Matching of Players With Trainers
Medium

You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

 

Example 1:

Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.

Example 2:

Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.

 

Constraints:

    1 <= players.length, trainers.length <= 10^5
    1 <= players[i], trainers[j] <= 10^9


Hint 1
Sort both the arrays.
Hint 2
Construct the matching greedily.
"""

from typing import List


class Solution:
    """
    Runtime 80ms Beats 42.63%
    Memory 33.68MB Beats 59.41%
    """

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players, reverse=True)
        trainers = sorted(trainers, reverse=True)
        p_len, t_len = len(players), len(trainers)
        p, t = 0, 0
        ans = 0

        while p < p_len and t < t_len:
            if players[p] > trainers[t]:
                p += 1
            else:
                ans += 1
                t += 1
                p += 1

        return ans


class Solution1:
    """
    leetcode solution: Sorting + Two Pointers + Greedy
    Runtime 74ms Beats 74.26%
    Memory 33.46MB Beats 91.95%
    """

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count
