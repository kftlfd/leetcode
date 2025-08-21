"""
Leetcode
2025-08-21
1504. Count Submatrices With All Ones
Medium

Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:

Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:

Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

 

Constraints:

    1 <= m, n <= 150
    mat[i][j] is either 0 or 1.


Hint 1
For each row i, create an array nums where: if mat[i][j] == 0 then nums[j] = 0 else nums[j] = nums[j-1] +1.
Hint 2
In the row i, number of rectangles between column j and k(inclusive) and ends in row i, is equal to SUM(min(nums[j, .. idx])) where idx go from j to k. Expected solution is O(n^3).
"""

from typing import List


class Solution00:
    """
    Time Limit Exceeded 72 / 73 testcases passed
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                if val == 0:
                    dp[r][c] = 0
                else:
                    dp[r][c] = (dp[r][c-1] if c > 0 else 0) + 1

        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                ans += sum(
                    min(dp[i][c] for i in range(j, r+1))
                    for j in range(r+1)
                )

        return ans


class Solution1:
    """
    leetcode solution 1: Enumeration
    Runtime 352ms Beats 41.43%
    Memory 18.57MB Beats 88.79%
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        row = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    row[i][j] = mat[i][j]
                else:
                    row[i][j] = 0 if mat[i][j] == 0 else row[i][j - 1] + 1
                cur = row[i][j]
                for k in range(i, -1, -1):
                    cur = min(cur, row[k][j])
                    if cur == 0:
                        break
                    res += cur
        return res


class Solution01:
    """
    Runtime 339ms Beats 47.66%
    Memory 18.63MB Beats 67.91%
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                if val == 0:
                    dp[r][c] = 0
                else:
                    dp[r][c] = (dp[r][c-1] if c > 0 else 0) + 1

                cur = 9999
                for i in range(r, -1, -1):
                    cur = min(cur, dp[i][c])
                    if cur < 1:
                        break
                    ans += cur

        return ans


class Solution2:
    """
    leetcode solution 2: Monotonic Stack
    Runtime 35ms Beats 88.47%
    Memory 18.83MB Beats 28.97%
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0])
        res = 0
        for row in mat:
            for i, x in enumerate(row):
                heights[i] = 0 if x == 0 else heights[i] + 1
            stack = [[-1, 0, -1]]
            for i, h in enumerate(heights):
                while stack[-1][2] >= h:
                    stack.pop()
                j, prev, _ = stack[-1]
                cur = prev + (i - j) * h
                stack.append([i, cur, h])
                res += cur
        return res
