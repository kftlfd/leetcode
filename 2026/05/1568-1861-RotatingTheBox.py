"""
Leetcode
2026-05-06
1861. Rotating the Box
Medium

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:

Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:

Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:

Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

 

Constraints:

    m == boxGrid.length
    n == boxGrid[i].length
    1 <= m, n <= 500
    boxGrid[i][j] is either '#', '*', or '.'.


"""

from typing import List


class Solution01:
    """
    Runtime 64ms Beats 97.77%
    Memory 56.74MB Beats 62.68%
    """

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        out = [["."] * m for _ in range(n)]

        for r, row in enumerate(boxGrid):
            slot = cur = n - 1
            while cur >= 0:
                if row[cur] == "#":
                    out[slot][m - 1 - r] = "#"
                    slot -= 1
                    cur -= 1
                elif row[cur] == "*":
                    out[cur][m - 1 - r] = "*"
                    cur -= 1
                    slot = cur
                else:
                    cur -= 1

        return out


class Solution02:
    """
    Runtime 57ms Beats 99.39%
    Memory 57.02MB Beats 17.44%
    """

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        out = [["."] * m for _ in range(n)]

        for r, row in enumerate(boxGrid):
            slot = n - 1
            for cur in range(n - 1, -1, -1):
                if row[cur] == "#":
                    out[slot][m - 1 - r] = "#"
                    slot -= 1
                elif row[cur] == "*":
                    out[cur][m - 1 - r] = "*"
                    slot = cur - 1

        return out
