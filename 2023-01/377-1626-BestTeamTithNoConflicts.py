"""
Leetcode
1626. Best Team With No Conflicts (medium)
2023-01-31

You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

Example 1:
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Example 2:
Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.

Example 3:
Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
"""

from typing import List, Optional
from math import inf


# leetcode solution
# Runtime: 7044 ms, faster than 6.39% of Python3 online submissions for Best Team With No Conflicts.
# Memory Usage: 80.6 MB, less than 5.67% of Python3 online submissions for Best Team With No Conflicts.
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        players = sorted(zip(ages, scores))

        n = len(players)
        dp = [[None for _ in range(n)] for _ in range(n)]

        def find_max_score(prev: int, index: int) -> int:
            if index >= n:
                return 0
            if dp[prev+1][index] != None:
                return dp[prev+1][index]
            if prev == -1 or players[index][1] >= players[prev][1]:
                dp[prev+1][index] = max(
                    find_max_score(prev, index+1),
                    players[index][1] + find_max_score(index, index+1)
                )
                return dp[prev+1][index]
            dp[prev+1][index] = find_max_score(prev, index+1)
            return dp[prev+1][index]

        return find_max_score(-1, 0)


s = Solution()
tests = [
    (([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]),
     34),

    (([4, 5, 6, 5], [2, 1, 2, 1]),
     16),

    (([1, 2, 3, 5], [8, 9, 10, 1]),
     6)
]
for inp, exp in tests:
    res = s.bestTeamScore(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
