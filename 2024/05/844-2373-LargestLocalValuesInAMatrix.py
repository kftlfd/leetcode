"""
Leetcode
2373. Largest Local Values in a Matrix
Easy
2024-05-12

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

    maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

 

Example 1:

Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.

Example 2:

Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

 

Constraints:

    n == grid.length == grid[i].length
    3 <= n <= 100
    1 <= grid[i][j] <= 100
"""

from typing import List


class Solution:
    """
    Runtime: 131 ms, faster than 53.08% of Python3 online submissions for Largest Local Values in a Matrix.
    Memory Usage: 17 MB, less than 97.85% of Python3 online submissions for Largest Local Values in a Matrix.
    """

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]

        for r in range(n-2):
            for c in range(n-2):
                cur_max = 0

                for i in range(3):
                    for j in range(3):
                        cur_max = max(cur_max, grid[r+i][c+j])

                ans[r][c] = cur_max

        return ans
