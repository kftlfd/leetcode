"""
Leetcode
2025-09-29
1039. Minimum Score Triangulation of Polygon
Topics

You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

 

Example 1:

Input: values = [1,2,3]

Output: 6

Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:

Input: values = [3,7,4,5]

Output: 144

Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:

Input: values = [1,3,1,4,1,5]

Output: 13

Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

 

Constraints:

    n == values.length
    3 <= n <= 50
    1 <= values[i] <= 100


Hint 1
Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length). Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].
"""

from functools import cache, lru_cache
from typing import List


class Solution01:
    """
    Time Limit Exceeded
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        inf = float('inf')

        def dfs(vals: List[int]) -> int:
            if len(vals) < 3:
                return 0

            cur_min = inf

            ab = vals[0] * vals[-1]
            for i in range(1, len(vals) - 1):
                c = vals[i]
                cur_min = min(
                    cur_min,
                    ab * c + dfs(vals[:i+1]) + dfs(vals[i:])
                )

            return int(cur_min)

        return dfs(values)


class Solution02:
    """
    Time Limit Exceeded
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        inf = float('inf')

        def dfs(l: int, r: int) -> int:
            if r - l < 2:
                return 0

            cur_min = inf

            ab = values[l] * values[r]
            for i in range(l + 1, r):
                abc = ab * values[i]
                cur_min = min(
                    cur_min,
                    abc + dfs(l, i) + dfs(i, r)
                )

            return int(cur_min)

        return dfs(0, len(values) - 1)


class Solution03:
    """
    Runtime 57ms Beats 31.94%
    Memory 18.59MB Beats 31.39%
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        inf = float('inf')

        @cache
        def dfs(l: int, r: int) -> int:
            if r - l < 2:
                return 0

            cur_min = inf

            ab = values[l] * values[r]
            for i in range(l + 1, r):
                abc = ab * values[i]
                cur_min = min(
                    cur_min,
                    abc + dfs(l, i) + dfs(i, r)
                )

            return int(cur_min)

        return dfs(0, len(values) - 1)


class Solution1:
    """
    leetcode solution: Dynamic Programming
    Runtime 48ms Beats 43.06%
    Memory 18.77MB Beats 14.17%
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            return min(
                (values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)


class Solution2:
    """
    sample 31ms solution
    Runtime 33ms Beats 81.39%
    Memory 18.02MB Beats 43.61%
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                best = float('inf')
                for k in range(i + 1, j):
                    s = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    best = min(best, s)
                dp[i][j] = int(best)
        return dp[0][n - 1]
