"""
Leetcode
2026-10-28
3882. Minimum XOR Path in a Grid
Medium

You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

 

Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

    (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
    (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

    (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

 

Constraints:

    1 <= m == grid.length <= 1000
    1 <= n == grid[i].length <= 1000
    m * n <= 1000
    0 <= grid[i][j] <= 1023


Hint 1
Use dynamic programming with state dp[i][j][x], where x is a possible XOR value.
Hint 2
dp[i][j][x] indicates whether it is possible to reach cell (i, j) with XOR equal to x.
Hint 3
Transition from the top left cell by updating x ^ grid[i][j], and track all reachable XOR values to find the minimum at the end cell.
"""


class Solution:
    """
    Runtime 4529ms Beats 25.00%
    Memory 27.51MB Beats 79.17%
    """

    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        N = 1024

        dp = [[[False] * N for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if r > 0:
                    for i in range(N):
                        if dp[r-1][c][i]:
                            dp[r][c][val ^ i] = True
                if c > 0:
                    for i in range(N):
                        if dp[r][c-1][i]:
                            dp[r][c][val ^ i] = True

        for i in range(N):
            if dp[-1][-1][i]:
                return i

        return -1


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 732ms Beats 90.83%
    Memory 26.11MB Beats 84.17%
    """

    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                reachable = dp[j] | (dp[j - 1] if j > 0 else set())

                dp[j] = {k ^ value for k in reachable}

        return min(dp[-1])
