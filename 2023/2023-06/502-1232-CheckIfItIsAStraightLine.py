"""
Leetcode
1232. Check If It Is a Straight Line (easy)
2023-06-05

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""

from typing import List


class Solution:
    """
    division by zero
    """

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        slope = (y2 - y1) / (x2 - x1)

        def on_line(x, y):
            return y - y1 == slope * (x - x1)

        return all(on_line(x, y) for x, y in coordinates[2:])


class Solution1:
    """
    Runtime: 67 ms, faster than 67.56% of Python3 online submissions for Check If It Is a Straight Line.
    Memory Usage: 16.7 MB, less than 50.49% of Python3 online submissions for Check If It Is a Straight Line.
    """

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        def on_line(x, y):
            return (y - y1) * dx == (x - x1) * dy

        return all(on_line(x, y) for x, y in coordinates[2:])


s = Solution1()
tests = [
    ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
     True),

    ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]],
     False),

    ([[0, 0], [0, 1], [0, -1]],
     True),
]
for inp, exp in tests:
    res = s.checkStraightLine(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
