"""
Leetcode
2026-03-27
2946. Matrix Similarity After Cyclic Shifts
Easy

You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:

    Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.

    Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.

Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4

Output: false

Explanation:

In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).

Example 2:

Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2

Output: true

Explanation:

Example 3:

Input: mat = [[2,2],[2,2]], k = 3

Output: true

Explanation:

As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

 

Constraints:

    1 <= mat.length <= 25
    1 <= mat[i].length <= 25
    1 <= mat[i][j] <= 25
    1 <= k <= 50


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.28MB Beats 91.18%
    """

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        for r in range(m):
            even = r % 2 == 0
            for c in range(n):
                new_idx = (c + k if even else c - k) % n
                if mat[r][c] != mat[r][new_idx]:
                    return False

        return True


class Solution1:
    """
    leetcode solution
    Runtime 3ms Beats 63.53%
    Memory 19.50MB Beats 10.59%
    """

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        """
        Determining whether a row cyclically shifted to the right by k positions is
        identical to the original is equivalent to checking whether it remains the
        same when shifted to the left by k positions. Therefore, we do not need to
        distinguish between even and odd rows.

        shift right: mat[i][j] -> mat[i][(j + k) % n]
        shift left: mat[i][(j + k) % n] -> mat[i][j]
        """

        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
