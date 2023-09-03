"""
Leetcode
62. Unique Paths (medium)
2023-09-03

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

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

Constraints:

    1 <= m, n <= 100
"""

from math import comb


class Solution:
    """
    Runtime: 30 ms, faster than 97.08% of Python3 online submissions for Unique Paths.
    Memory Usage: 16.1 MB, less than 99.71% of Python3 online submissions for Unique Paths.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        l = min(m, n)
        h = max(m, n)
        dp = [1] * l

        for _ in range(1, h):
            for i in range(1, l):
                dp[i] += dp[i-1]

        return dp[-1]


class Solution1:
    """
    https://leetcode.com/problems/unique-paths/discuss/254228/Python-3-solutions:-Bottom-up-DP-Math-Picture-Explained-Clean-and-Concise
    Runtime: 41 ms, faster than 59.21% of Python3 online submissions for Unique Paths.
    Memory Usage: 16.4 MB, less than 47.37% of Python3 online submissions for Unique Paths.
    """

    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)


s = Solution()
tests = [
    ((3, 7),
     28),

    ((3, 2),
     3),
]
for inp, exp in tests:
    res = s.uniquePaths(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
