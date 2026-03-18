"""
Leetcode
2026-03-18
3070. Count Submatrices with Top-Left Element and Sum Less Than k
Medium

You are given a 0-indexed integer matrix grid and an integer k.

Return the number of that contain the top-left element of the grid, and have a sum less than or equal to k.

 

Example 1:

Input: grid = [[7,6,3],[6,6,1]], k = 18
Output: 4
Explanation: There are only 4 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 18.

Example 2:

Input: grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20
Output: 6
Explanation: There are only 6 submatrices, shown in the image above, that contain the top-left element of grid, and have a sum less than or equal to 20.

 

Constraints:

    m == grid.length 
    n == grid[i].length
    1 <= n, m <= 1000 
    0 <= grid[i][j] <= 1000
    1 <= k <= 10^9


"""

from typing import List


class Solution:
    """
    Runtime 193ms Beats 91.72%
    Memory 54.56MB Beats 100.00%
    """

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        ans = 0
        mat_sum = [0] * n
        row_sum = [0] * n

        for row in grid:
            row_sum[:] = [0] * n
            for c, val in enumerate(row):
                if mat_sum[c] == -1:
                    break
                row_sum[c] = val + (row_sum[c - 1] if c > 0 else 0)
                mat_sum[c] += row_sum[c]
                if mat_sum[c] > k:
                    mat_sum[c] = -1
                    break
                ans += 1

        return ans


class Solution1:
    """
    leetcode solution: 2D Prefix Sum
    Runtime 123ms Beats 95.86%
    Memory 54.97MB Beats 95.86%
    """

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        cols = [0] * m
        res = 0

        for i in range(n):
            row_sum = 0
            for j in range(m):
                cols[j] += grid[i][j]
                row_sum += cols[j]
                if row_sum <= k:
                    res += 1

        return res
