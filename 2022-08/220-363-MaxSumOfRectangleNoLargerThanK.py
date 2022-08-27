"""
Leetcode
363. Max Sum of Rectangle No Larger Than K (hard)
2022-08-27

Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

Example 2:
Input: matrix = [[2,2,-1]], k = 3
Output: 3
"""

from typing import List
from itertools import product, combinations, accumulate
from bisect import bisect_left, insort


# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/1312722/Python-Two-solutions-explained
# Runtime: 3229 ms, faster than 74.31% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 14.7 MB, less than 92.49% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = matrix

        def countRangeSum(nums, U):
            SList, ans = [0], -float("inf")
            for s in accumulate(nums):
                idx = bisect_left(SList, s - U)
                if idx < len(SList):
                    ans = max(ans, s - SList[idx])
                insort(SList, s)
            return ans

        m, n, ans = len(M), len(M[0]), -float("inf")

        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i-1][j]

        M = [[0]*n] + M

        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))

        return ans


s = Solution()
tests = [
    ([[1, 0, 1], [0, -2, 3]], 2),
    ([[2, 2, -1]], 3),
]
for matrix, k in tests:
    print(matrix, k)
    print(s.maxSumSubmatrix(matrix, k))
    print()
