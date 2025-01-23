"""
Leetcode
2025-01-23
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


"""

from typing import List


class Solution:
    """
    Runtime 16ms Beats 66.67%
    Memory 19.59MB Beats 60.67%
    """

    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        row_cnt = [0] * m
        col_cnt = [0] * n
        ans = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1 and (row_cnt[r] > 1 or col_cnt[c] > 1):
                    ans += 1

        return ans


class Solution3:
    """
    leetcode solution 3: Server Grouping
    Runtime 7ms Beats 95.51%
    Memory 19.57MB Beats 60.67%
    """

    def countServers(self, grid: List[List[int]]) -> int:
        communicable_servers_count = 0
        row_counts = [0] * len(grid[0])
        last_server_in_col = [-1] * len(grid)

        # First pass to count servers in each row and column
        for row in range(len(grid)):
            server_count_in_row = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    server_count_in_row += 1
                    row_counts[col] += 1
                    last_server_in_col[row] = col

            # If there is more than one server in the row, increase the count
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_col[row] = -1

        # Second pass to check if servers can communicate
        for row in range(len(grid)):
            if (
                last_server_in_col[row] != -1
                and row_counts[last_server_in_col[row]] > 1
            ):
                communicable_servers_count += 1
        return communicable_servers_count
