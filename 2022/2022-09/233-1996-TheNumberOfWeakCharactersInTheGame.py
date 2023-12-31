"""
Leetcode
1996. The Number of Weak Characters in the Game (medium)
2022-09-09

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

Example 1:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
"""

from typing import List
from collections import defaultdict


# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445192/Python-sort-+-greedy-explained
# Runtime: 5851 ms, faster than 5.04% of Python3 online submissions for The Number of Weak Characters in the Game.
# Memory Usage: 70.9 MB, less than 9.58% of Python3 online submissions for The Number of Weak Characters in the Game.
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        X = sorted(properties)
        n = len(X)
        ans, d, max_y = 0, defaultdict(list), -1

        for a, b in X:
            d[a] += [b]

        for t in sorted(list(d.keys()))[::-1]:
            for q in d[t]:
                if q < max_y:
                    ans += 1
            for q in d[t]:
                max_y = max(max_y, q)

        return ans


s = Solution()
tests = [
    [[5, 5], [6, 3], [3, 6]],
    [[2, 2], [3, 3]],
    [[1, 5], [10, 4], [4, 3]],
]
for t in tests:
    print(t)
    print(s.numberOfWeakCharacters(t))
    print()
