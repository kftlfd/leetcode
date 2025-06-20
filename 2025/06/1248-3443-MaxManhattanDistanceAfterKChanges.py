"""
Leetcode
2025-06-20
3443. Maximum Manhattan Distance After K Changes
Medium
Topics
premium lock iconCompanies
Hint

You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

    'N' : Move north by 1 unit.
    'S' : Move south by 1 unit.
    'E' : Move east by 1 unit.
    'W' : Move west by 1 unit.

Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".
Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3

The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

Constraints:

    1 <= s.length <= 10^5
    0 <= k <= s.length
    s consists of only 'N', 'S', 'E', and 'W'.


Hint 1
We can brute force all the possible directions (NE, NW, SE, SW).
Hint 2
Change up to k characters to maximize the distance in the chosen direction.
"""


class Solution:
    """
    Runtime 4999ms Beats 13.29%
    Memory 18.25MB Beats 12.50%
    """

    def maxDistance(self, s: str, k: int) -> int:
        d = {'N': 0, 'S': 1, 'E': 2, 'W': 3}
        dist = [0] * 4
        ans = 0

        for c in s:
            dist[d[c]] += 1

            N, S, E, W = dist
            ans = max(ans, abs(N - S) + abs(W - E))

            dist_changed = dist[:]
            kk = k
            for da, db in [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]:
                if kk < 1:
                    break
                a, b = d[da], d[db]
                if dist_changed[a] >= dist_changed[b]:
                    diff = min(dist_changed[b], kk)
                    dist_changed[a] += diff
                    dist_changed[b] -= diff
                    kk -= diff
            N, S, W, E = dist_changed
            ans = max(ans, abs(N - S) + abs(W - E))

        return ans


class Solution1:
    """
    leetcode solution 1: Step-by-step Solution
    Runtime 2441ms Beats 83.59%
    Memory 18.12MB Beats 37.50%
    """

    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        for it in s:
            if it == "N":
                north += 1
            elif it == "S":
                south += 1
            elif it == "E":
                east += 1
            elif it == "W":
                west += 1
            times1 = min(north, south, k)  # modification times for N and S
            times2 = min(
                east, west, k - times1
            )  # modification times for E and W
            ans = max(
                ans,
                self.count(north, south, times1)
                + self.count(east, west, times2),
            )
        return ans

    def count(self, drt1: int, drt2: int, times: int) -> int:
        return (
            abs(drt1 - drt2) + times * 2
        )  # Calculate modified Manhattan distance


class Solution2:
    """
    leetcode solution 2: Overall Solution
    Runtime 1435ms Beats 97.66%
    Memory 18.02MB Beats 69.53%
    """

    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans
