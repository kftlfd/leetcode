"""
Leetcode
85. Maximal Rectangle
Hard
2024-04-13

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

 

Constraints:

    rows == matrix.length
    cols == matrix[i].length
    1 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/maximal-rectangle/discuss/1603766/Python-O(mn)-solution-explained
    Runtime: 220 ms, faster than 60.37% of Python3 online submissions for Maximal Rectangle.
    Memory Usage: 17.9 MB, less than 34.51% of Python3 online submissions for Maximal Rectangle.
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def hist(heights):
            stack, ans = [], 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    H = heights[stack.pop()]
                    W = i if not stack else i-stack[-1]-1
                    ans = max(ans, H*W)
                stack.append(i)
            return ans

        if not matrix or not matrix[0]:
            return 0
        m, n, ans = len(matrix[0]), len(matrix), 0
        row = [0]*m
        for i in range(n):
            for j in range(m):
                row[j] = 0 if matrix[i][j] == "0" else row[j] + 1
            ans = max(ans, hist(row))

        return ans
