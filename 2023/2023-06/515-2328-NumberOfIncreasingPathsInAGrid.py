"""
Leetcode
2328. Number of Increasing Paths in a Grid (hard)
2023-06-18

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 10^9 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

Example 1:

Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.

Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^5
"""

from typing import List


class Solution:
    """
    leetcode solution 1: Sorting + DP
    Runtime: 2436 ms, faster than 51.46% of Python3 online submissions for Number of Increasing Paths in a Grid.
    Memory Usage: 36.5 MB, less than 74.76% of Python3 online submissions for Number of Increasing Paths in a Grid.
    """

    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # initialize dp, 1 stands for the path made by a cell itself
        dp = [[1] * n for _ in range(m)]

        # sort cells by value
        cell_list = [[i, j] for i in range(m) for j in range(n)]
        cell_list = sorted(cell_list, key=lambda x: grid[x[0]][x[1]])

        # iterate over the sorted cells, for each cell grid[i][j]
        for i, j in cell_list:
            # check its four neighbor cells, if a neighbor cell has a
            # larger value, increment dp[curr_i][curr_j] by dp[i][j]
            for di, dj in directions:
                curr_i, curr_j = i + di, j + dj
                if 0 <= curr_i < m and 0 <= curr_j < n and grid[curr_i][curr_j] > grid[i][j]:
                    dp[curr_i][curr_j] += dp[i][j]
                    dp[curr_i][curr_j] %= mod

        # sum over dp[i][j]
        return sum(sum(row) % mod for row in dp) % mod


class Solution1:
    """
    leetcode solution 2: DFS with Memoization
    Runtime: 2011 ms, faster than 91.75% of Python3 online submissions for Number of Increasing Paths in a Grid.
    Memory Usage: 33.5 MB, less than 88.84% of Python3 online submissions for Number of Increasing Paths in a Grid.
    """

    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            # if dp[i][j] is non-zero, it means we have got the value of dfs(i, j)
            # so just return it
            if dp[i][j]:
                return dp[i][j]

            # otherwise set ans = 1, the path made by the cell itself
            ans = 1

            # if neighbor cell has a smaller value, we move to this cell and
            # solve the subproblem: dfs(prev_i, prev_j)
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    ans += dfs(prev_i, prev_j) % mod

            dp[i][j] = ans
            return ans

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
