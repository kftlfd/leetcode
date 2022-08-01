"""
Leetcode
62. Unique Paths (medium)
2022-08-01

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

import math


# https://leetcode.com/problems/unique-paths/discuss/2362106/PYTHON-oror-EXPLAINED-oror
# Runtime: 56 ms, faster than 32.80% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.1 MB, less than 11.02% of Python3 online submissions for Unique Paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i, j):
            if i == m-1 or j == n-1:
                return 1
            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = solve(i+1, j) + solve(i, j+1)
            return dp[i][j]

        dp = [[0 for i in range(n)] for j in range(m)]
        return solve(0, 0)


# https://leetcode.com/problems/unique-paths/discuss/2363008/Python-oror-Detailed-Explanation-oror-Easy-Understand-oror-DP-oror-MATH
# Runtime: 26 ms, faster than 98.87% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 73.91% of Python3 online submissions for Unique Paths.
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] * m

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


# https://leetcode.com/problems/unique-paths/discuss/2363008/Python-oror-Detailed-Explanation-oror-Easy-Understand-oror-DP-oror-MATH
# Runtime: 43 ms, faster than 68.37% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 32.97% of Python3 online submissions for Unique Paths.
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n + m - 2, n - 1)


# https://leetcode.com/problems/unique-paths/discuss/2362191/Python3-oror-1-line-combinatorics-w-explanation-oror-TM:-8879
# Runtime: 66 ms, faster than 12.80% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 73.91% of Python3 online submissions for Unique Paths.
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2) // math.factorial(m-1) // math.factorial(n-1)


s = Solution3()
tests = [
    (3, 7),
    (3, 2),
]
for m, n in tests:
    print(m, n)
    print(s.uniquePaths(m, n))
    print()
