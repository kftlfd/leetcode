"""
Leetcode
119. Pascal's Triangle II (easy)
2023-10-16

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

 

Constraints:

    0 <= rowIndex <= 33
"""

from typing import List


class Solution:
    """
    Runtime: 38 ms, faster than 59.57% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 16 MB, less than 99.67% of Python3 online submissions for Pascal's Triangle II.
    """

    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for r in range(1, rowIndex + 1):
            nextRow = row[:]
            for c in range(1, r + 1):
                nextRow[c] += row[c - 1]
            row = nextRow

        return row


class Solution1:
    """
    Runtime: 28 ms, faster than 97.74% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 16.2 MB, less than 53.14% of Python3 online submissions for Pascal's Triangle II.
    """

    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for r in range(1, rowIndex + 1):
            for c in range(r, 0, -1):
                row[c] += row[c - 1]

        return row
