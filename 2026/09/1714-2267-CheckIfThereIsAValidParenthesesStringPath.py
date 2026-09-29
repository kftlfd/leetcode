"""
Leetcode
2026-09-29
2267. Check if There Is a Valid Parentheses String Path
Hard

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.

You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

    The path starts from the upper left cell (0, 0).
    The path ends at the bottom-right cell (m - 1, n - 1).
    The path only ever moves down or right.
    The resulting parentheses string formed by the path is valid.

Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

 

Example 1:

Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

Example 2:

Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is either '(' or ')'.


Hint 1
What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?
Hint 2
The number of open brackets must always be greater than or equal to the number of close brackets.
Hint 3
Could you use dynamic programming?
"""


from collections import deque


class Solution:
    """
    Runtime 2700ms Beats 5.00%
    Memory 79.74MB Beats 33.00%
    """

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != "(" or grid[-1][-1] != ")":
            return False

        q = deque([(0, 0, 1)])
        seen = {(0, 0, 1)}
        dirs = [(1, 0), (0, 1)]

        while q:
            r, c, cnt = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr >= m or nc >= n:
                    continue

                n_cnt = cnt + 1 if grid[nr][nc] == "(" else cnt - 1
                if n_cnt < 0:
                    continue

                n_cell = (nr, nc, n_cnt)
                if n_cell in seen:
                    continue

                seen.add(n_cell)

                if nr == m - 1 and nc == n - 1 and n_cnt == 0:
                    return True

                q.append(n_cell)

        return False


class Solution1:
    """
    leetcode solution
    Runtime 19ms Beats 77.00%
    Memory 21.10MB Beats 81.00%
    """

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        path_len = n + m - 1

        if path_len % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[n - 1][m - 1] != ")":
            return False

        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1 << 1

        for i in range(n):
            for j in range(m):
                change = 1 if grid[i][j] == "(" else -1

                if i > 0:
                    if change == 1:
                        dp[i][j] |= dp[i - 1][j] << 1
                    else:
                        dp[i][j] |= dp[i - 1][j] >> 1

                if j > 0:
                    if change == 1:
                        dp[i][j] |= dp[i][j - 1] << 1
                    else:
                        dp[i][j] |= dp[i][j - 1] >> 1

        return bool(dp[n - 1][m - 1] & 1)
