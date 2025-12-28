"""
Leetcode
2025-12-28
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

    
Hint 1
Use binary search for optimization or simply brute force.
"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 18.36MB Beats 91.60%
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        maxRow = m - 1

        for col in range(n):
            for row in range(maxRow, -1, -1):
                if grid[row][col] >= 0:
                    break
                maxRow -= 1
            ans += m - maxRow - 1

        return ans
