"""
Leetcode
1496. Path Crossing
Easy
2023-12-23

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

 

Constraints:

    1 <= path.length <= 104
    path[i] is either 'N', 'S', 'E', or 'W'.
"""


class Solution:
    """
    Runtime: 36 ms, faster than 72.53% of Python3 online submissions for Path Crossing.
    Memory Usage: 17.4 MB, less than 5.49% of Python3 online submissions for Path Crossing.
    """

    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (-1, 0),
            "W": (1, 0)
        }

        x, y = 0, 0
        seen = {(0, 0)}

        for move in path:
            dx, dy = moves[move]
            x, y = x + dx, y + dy
            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False
