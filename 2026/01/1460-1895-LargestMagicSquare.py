"""
Leetcode
2026-01-18
1895. Largest Magic Square
Medium

A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

Example 1:

Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:

Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    1 <= grid[i][j] <= 10^6


"""

from typing import List


class Solution:
    """
    Runtime 119ms Beats 67.24%
    Memory 19.72MB Beats 12.07%
    """

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_sum = [[0] * (n + 1) for _ in range(m + 1)]
        col_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                row_sum[r][c + 1] = row_sum[r][c] + val
                col_sum[r + 1][c] = col_sum[r][c] + val

        def is_magic_square(r: int, c: int, size: int) -> bool:
            target = row_sum[r][c + size] - row_sum[r][c]
            return all(
                row_sum[rr][c + size] - row_sum[rr][c] == target
                for rr in range(r + 1, r + size)
            ) and all(
                col_sum[r + size][cc] - col_sum[r][cc] == target
                for cc in range(c, c + size)
            ) and sum(
                grid[r + x][c + x]
                for x in range(size)
            ) == target and sum(
                grid[r + x][c + size - 1 - x]
                for x in range(size)
            ) == target

        for size in range(min(m, n), 1, -1):
            for r in range(m - size + 1):
                for c in range(n - size + 1):
                    if is_magic_square(r, c, size):
                        return size

        return 1
