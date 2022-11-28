"""
Leetcode
2225. Find Players With Zero or One Losses (medium)
2022-11-28

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""

from typing import List, Optional
from collections import defaultdict


# Runtime: 4446 ms, faster than 47.87% of Python3 online submissions for Find Players With Zero or One Losses.
# Memory Usage: 69.9 MB, less than 13.81% of Python3 online submissions for Find Players With Zero or One Losses.
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        players = set()
        loses = defaultdict(int)

        for match in matches:
            winner, loser = match
            players.add(winner)
            players.add(loser)
            loses[loser] += 1

        noLoses = []
        oneLose = []

        for player in players:
            if loses[player] == 0:
                noLoses.append(player)
            elif loses[player] == 1:
                oneLose.append(player)

        return [sorted(noLoses), sorted(oneLose)]


s = Solution()
tests = [
    ([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
     [[1, 2, 10], [4, 5, 7, 8]]),

    ([[2, 3], [1, 3], [5, 4], [6, 4]],
     [[1, 2, 5, 6], []])
]
for inp, exp in tests:
    res = s.findWinners(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
