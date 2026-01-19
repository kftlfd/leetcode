"""
Leetcode
2026-01-19
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
Medium

Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 300
    0 <= mat[i][j] <= 10^4
    0 <= threshold <= 10^5

 
Hint 1
Store prefix sum of all grids in another 2D array.
Hint 2
Try all possible solutions and if you cannot find one return -1.
Hint 3
If x is a valid answer then any y < x is also valid answer. Use binary search to find answer.
"""

from typing import List


class Solution:
    """
    Runtime 199ms Beats 75.89%
    Memory 26.11MB Beats 29.91%
    """

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        mat_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_sum = 0
            for c in range(n):
                val = mat[r][c]
                row_sum += val
                mat_sum[r+1][c+1] = mat_sum[r][c+1] + row_sum

        def is_valid(size: int) -> bool:
            for r in range(m - size + 1):
                for c in range(n - size + 1):
                    if (mat_sum[r+size][c+size] + mat_sum[r][c]) - \
                            (mat_sum[r+size][c] + mat_sum[r][c+size]) <= threshold:
                        return True
            return False

        ans = 0
        l = 1
        r = min(m, n) + 1
        while l < r:
            mid = (l + r) // 2
            if is_valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid

        return ans


class Solution2:
    """
    leetcode solution 2: Enumeration + Optimization
    Runtime 163ms Beats 84.82%
    Memory 26.14MB Beats 29.91%
    """

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def getRect(x1, y1, x2, y2):
            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

        r, ans = min(m, n), 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, r + 1):
                    if (
                        i + c - 1 <= m
                        and j + c - 1 <= n
                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
                    ):
                        ans += 1
                    else:
                        break
        return ans
