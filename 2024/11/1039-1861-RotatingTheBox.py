"""
Leetcode
2024-11-23
1861. Rotating the Box
Medium

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:

Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:

Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:

Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

 

Constraints:

    m == box.length
    n == box[i].length
    1 <= m, n <= 500
    box[i][j] is either '#', '*', or '.'.
"""

from typing import List


class Solution:

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box = [row[:] for row in box]

        for row in box:
            right = len(row) - 1
            left = right
            while left >= 0:
                if row[left] == '.':
                    left -= 1
                elif row[left] == '*':
                    left -= 1
                    right = left
                elif left != right:  # row[left] == '#'
                    row[left], row[right] = row[right], row[left]
                    left -= 1
                    right -= 1
                else:
                    left -= 1
                    right = left

            return self.rotate_2(box)

    def rotate_1(self, box: List[List[str]]) -> List[List[str]]:
        """
        Runtime: 1889 ms, faster than 66.77% of Python3 online submissions for Rotating the Box.
        Memory Usage: 28.9 MB, less than 78.97% of Python3 online submissions for Rotating the Box.
        """
        return list(zip(*reversed(box)))

    def rotate_2(self, box: List[List[str]]) -> List[List[str]]:
        """
        Runtime: 1878 ms, faster than 75.63% of Python3 online submissions for Rotating the Box.
        Memory Usage: 28.7 MB, less than 83.45% of Python3 online submissions for Rotating the Box.
        """
        m, n = len(box), len(box[0])
        ans = [[''] * m for _ in range(n)]
        for r, row in enumerate(box):
            for c, val in enumerate(row):
                ans[c][m - r - 1] = val
        return ans


class Solution3:
    """
    leetcode solution 3: Combine rotation and gravity operations
    Runtime: 1852 ms, faster than 91.46% of Python3 online submissions for Rotating the Box.
    Memory Usage: 29.1 MB, less than 19.83% of Python3 online submissions for Rotating the Box.
    """

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["." for _ in range(m)] for _ in range(n)]

        # Apply gravity to let stones fall to the lowest possible empty cell in each column
        for i in range(m):
            lowest_row_with_empty_cell = n - 1
            # Process each cell in row `i` in reversed order
            for j in range(n - 1, -1, -1):
                # Found a stone - let it fall to the lowest empty cell
                if box[i][j] == "#":
                    # Place it in the correct position in the rotated grid
                    result[lowest_row_with_empty_cell][m - i - 1] = "#"
                    lowest_row_with_empty_cell -= 1
                # Found an obstacle - reset `lowest_row_with_empty_cell` to the row directly above it
                if box[i][j] == "*":
                    # Place the obstacle in the correct position in the rotated grid
                    result[j][m - i - 1] = "*"
                    lowest_row_with_empty_cell = j - 1

        return result


class Solution4:
    """
    https://leetcode.com/problems/rotating-the-box/solution/2733547
    Runtime: 1829 ms, faster than 97.47% of Python3 online submissions for Rotating the Box.
    Memory Usage: 26.4 MB, less than 100.00% of Python3 online submissions for Rotating the Box.
    """

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def tilt(row):
            bottom = len(row) - 1
            for i in reversed(range(len(row))):
                match row[i]:
                    case '*':
                        bottom = i - 1
                    case '#':
                        row[i], row[bottom] = '.', '#'
                        bottom = bottom - 1
            return row

        return zip(*map(tilt, reversed(box)))
