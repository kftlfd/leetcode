"""
Leetcode
2026-03-02
1536. Minimum Swaps to Arrange a Binary Grid
Medium

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:

Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 200
    grid[i][j] is either 0 or 1


Hint 1
For each row of the grid calculate the most right 1 in the grid in the array maxRight.
Hint 2
To check if there exist answer, sort maxRight and check if maxRight[i] ≤ i for all possible i's.
Hint 3
If there exist an answer, simulate the swaps.
"""

from typing import List


class Solution:
    """
    Wrong Answer
    """

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_right = [-1] * n

        for i, row in enumerate(grid):
            for j in range(n - 1, -1, -1):
                if row[j] == 1:
                    max_right[i] = j
                    break

        is_possible = True
        for r, idx in enumerate(sorted(max_right)):
            if idx > r:
                is_possible = False
                break
        if not is_possible:
            return -1

        ans = 0
        swaps = True
        while swaps:
            swaps = False
            swap_val = n
            for i in range(n - 1):
                if max_right[i] <= i and swap_val >= n:
                    continue
                swaps = True
                swap_val = min(swap_val, i)
                if max_right[i + 1] != max_right:
                    max_right[i], max_right[i +
                                            1] = max_right[i + 1], max_right[i]
                    ans += 1

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 11ms Beats 50.00%
    Memory 20.88MB Beats 86.36%
    """

    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = [-1] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    pos[i] = j
                    break

        ans = 0
        for i in range(n):
            k = -1
            for j in range(i, n):
                if pos[j] <= i:
                    ans += j - i
                    k = j
                    break

            if k != -1:
                for j in range(k, i, -1):
                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
            else:
                return -1

        return ans
