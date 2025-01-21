"""
Leetcode
2025-01-21
2017. Grid Game
Medium
Topics
Companies
Hint

You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.

 

Example 1:

Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.

Example 2:

Input: grid = [[3,3,1],[8,5,2]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 3 + 1 + 0 = 4 points.

Example 3:

Input: grid = [[1,3,1,15],[1,3,3,1]]
Output: 7
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.

 

Constraints:

    grid.length == 2
    n == grid[r].length
    1 <= n <= 5 * 10^4
    1 <= grid[r][c] <= 10^5

Hint 1
There are n choices for when the first robot moves to the second row.
Hint 2
Can we use prefix sums to help solve this problem?
"""

from typing import List


class Solution00:
    """
    wrong answer
    """

    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        sums = [[0] * n for _ in range(2)]
        sums[0][0] = grid[0][0]
        sums[1][-1] = grid[1][-1]

        for i in range(1, n):
            sums[0][i] = grid[0][i] + sums[0][i-1]
            sums[1][n-1-i] = grid[1][n-1-i] + sums[1][n-i]

        _, idx_1 = self.getMaxScoreIdx(sums)

        val_top = sums[0][idx_1]
        val_bottom = sums[1][idx_1]
        for i in range(n):
            if i == idx_1:
                sums[0][i] = 0
                sums[1][i] = 0
            elif i < idx_1:
                sums[0][i] = 0
                sums[1][i] -= val_bottom
            else:
                sums[0][i] -= val_top
                sums[1][i] = 0

        score_2, _ = self.getMaxScoreIdx(sums)

        return score_2

    def getMaxScoreIdx(self, sums: List[List[int]]) -> tuple[int, int]:
        return max((t + b, i) for i, (t, b) in enumerate(zip(sums[0], sums[1])))


class Solution01:
    """
    Runtime 155ms Beats 9.51%
    Memory 30.36MB Beats 19.34%
    """

    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        sums = [[0] * n for _ in range(2)]
        sums[0][0] = grid[0][0]
        sums[1][-1] = grid[1][-1]

        for i in range(1, n):
            sums[0][i] = grid[0][i] + sums[0][i-1]
            sums[1][n-1-i] = grid[1][n-1-i] + sums[1][n-i]

        max_top = sums[0][-1]
        max_bottom = sums[1][0]
        min_score_2 = float('inf')

        for i in range(n):
            min_score_2 = min(
                min_score_2,
                max(max_top - sums[0][i], max_bottom - sums[1][i])
            )

        return min_score_2


class Solution1:
    """
    leetcode solution: Prefix and Suffix Sum
    Runtime 83ms Beats 83.28%
    Memory 29.62MB Beats 62.95%
    """

    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float("inf")
        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            # Find the minimum maximum value out of first_row_sum and
            # second_row_sum.
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimum_sum


s = Solution01()
tests = [
    ([[20, 3, 20, 17, 2, 12, 15, 17, 4, 15], [20, 10, 13, 14, 15, 5, 2, 3, 14, 3]],
     63),

    ([[2, 5, 4], [1, 5, 1]],
     4),

    ([[3, 3, 1], [8, 5, 2]],
     4),

    ([[1, 3, 1, 15], [1, 3, 3, 1]],
     7),
]
for inp, exp in tests:
    res = s.gridGame(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
