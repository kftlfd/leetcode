"""
Leetcode
2026-11-08
1267. Count Servers that Communicate
Medium

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1


Hint 1
Store number of computer in each row and column.
Hint 2
Count all servers that are not isolated.
"""


class Solution:
    """
    Runtime 19ms Beats 50.85%
    Memory 21.50MB Beats 65.82%
    """

    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        active_rows = [0] * m
        active_cols = [0] * n
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    active_rows[r] += 1
                    active_cols[c] += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if active_rows[r] > 1 or active_cols[c] > 1:
                        ans += 1

        return ans


class Solution3:
    """
    leetcode solution 3: Server Grouping
    Runtime 8ms Beats 95.48%
    Memory 21.59MB Beats 36.72%
    """

    def countServers(self, grid: list[list[int]]) -> int:
        communicable_servers_count = 0
        col_count = [0] * len(grid[0])
        last_server_in_row = [-1] * len(grid)

        # First pass to count servers in each row and column
        for r, row in enumerate(grid):
            server_count_in_row = 0
            for c, cell in enumerate(row):
                if cell:
                    server_count_in_row += 1
                    col_count[c] += 1
                    last_server_in_row[r] = c

            # If there is more than one server in the row, increase the count
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_row[r] = -1

        # Second pass to check if servers can communicate
        for row in range(len(grid)):
            if (
                last_server_in_row[row] != -1
                and col_count[last_server_in_row[row]] > 1
            ):
                communicable_servers_count += 1
        return communicable_servers_count
