"""
Leetcode
1074. Number of Submatrices That Sum to Target (hard)
2022-07-18

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
"""

from typing import List
from collections import Counter
from itertools import accumulate, combinations


# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/1162611/Python-cumulative-sum-+-dp-explained
# Runtime: 4339 ms, faster than 5.22% of Python3 online submissions for Number of Submatrices That Sum to Target.
# Memory Usage: 102.3 MB, less than 6.64% of Python3 online submissions for Number of Submatrices That Sum to Target.
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i, j, k-1), 0) + t[j] - t[i]

        for i, j in combinations(range(n+1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1

        return ans


s = Solution()
tests = [
    ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0),
    ([[1, -1], [-1, 1]], 0),
    ([[904]], 0)
]
for t in tests:
    print(t)
    print(s.numSubmatrixSumTarget(t[0], t[1]))
    print()
