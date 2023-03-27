"""
Leetcode
64. Minimum Path Sum (medium)
2023-03-27

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

from typing import List


class Solution:
    """
    Runtime: 98 ms, faster than 73.26% of Python3 online submissions for Minimum Path Sum.
    Memory Usage: 14.6 MB, less than 99.75% of Python3 online submissions for Minimum Path Sum.
    """

    def minPathSum(self, grid: List[List[int]]) -> int:

        window_row = grid[0][:]
        for i in range(1, len(window_row)):
            window_row[i] += window_row[i-1]

        for i in range(1, len(grid)):
            window_row[0] = grid[i][0] + window_row[0]
            for j in range(1, len(window_row)):
                window_row[j] = grid[i][j] + \
                    min(window_row[j-1], window_row[j])

        return window_row[-1]


s = Solution()
tests = [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]],
     7),

    ([[1, 2, 3], [4, 5, 6]],
     12),
]
for inp, exp in tests:
    res = s.minPathSum(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
