"""
Leetcode
2026-03-22
1886. Determine Whether Matrix Can Be Obtained By Rotation
Easy

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:

Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

 

Constraints:

    n == mat.length == target.length
    n == mat[i].length == target[i].length
    1 <= n <= 10
    mat[i][j] and target[i][j] are either 0 or 1.


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.20MB Beats 97.54%
    """

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(grid: List[List[int]]) -> List[List[int]]:
            rot = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    rot[n - 1 - c][r] = grid[r][c]
            return rot

        def is_same(mat1: List[List[int]], mat2: List[List[int]]) -> bool:
            for r in range(n):
                if mat1[r] != mat2[r]:
                    return False
            return True

        if is_same(mat, target):
            return True

        cur = mat
        for _ in range(3):
            rot = rotate(cur)
            if is_same(rot, target):
                return True
            cur = rot

        return False


class Solution1:
    """
    leetcode solution: Simulate Rotation Operation
    in-place rotations
    Runtime 3ms Beats 14.06%
    Memory 19.34MB Beats 59.42%
    """

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # at most 4 rotations
        for _ in range(4):
            # rotation operation
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    (
                        mat[i][j],
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                    ) = (
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                        mat[i][j],
                    )

            if mat == target:
                return True
        return False
