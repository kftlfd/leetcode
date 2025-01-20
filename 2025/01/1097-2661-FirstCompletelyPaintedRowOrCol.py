"""
Leetcode
2025-01-20
2661. First Completely Painted Row or Column
Medium
Topics
Companies
Hint

You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:
image explanation for example 1

Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

Example 2:
image explanation for example 2

Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].

 

Constraints:

    m == mat.length
    n = mat[i].length
    arr.length == m * n
    1 <= m, n <= 10^5
    1 <= m * n <= 10^5
    1 <= arr[i], mat[r][c] <= m * n
    All the integers of arr are unique.
    All the integers of mat are unique.
"""

from typing import List


class Solution:
    """
    Runtime 109ms Beats 83.28%
    Memory 43.04MB Beats 97.48%
    """

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [0] * m
        cols = [0] * n
        pos = [(0, 0) for _ in range(m*n + 1)]

        for r, row in enumerate(mat):
            for c, cell in enumerate(row):
                pos[cell] = (r, c)

        for i, val in enumerate(arr):
            r, c = pos[val]
            rows[r] += 1
            cols[c] += 1
            if rows[r] >= n or cols[c] >= m:
                return i

        return -1


class Solution3:
    """
    leetcode solution 3: Reverse Mapping
    Runtime 167ms Beats 17.98%
    Memory 47.33MB Beats 81.39%
    """

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Map to store the index of each number in the arr
        num_to_index = {}
        for i, val in enumerate(arr):
            num_to_index[val] = i

        result = float("inf")
        num_rows, num_cols = len(mat), len(mat[0])

        # Check for the earliest row to be completely painted
        for row in range(num_rows):
            # Tracks the greatest index in this row
            last_element_index = float("-inf")
            for col in range(num_cols):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this row is fully painted
            result = min(result, last_element_index)

        # Check for the earliest column to be completely painted
        for col in range(num_cols):
            last_element_index = float("-inf")
            for row in range(num_rows):
                index_val = num_to_index[mat[row][col]]
                last_element_index = max(last_element_index, index_val)

            # Update result with the minimum index where this column is fully painted
            result = min(result, last_element_index)

        return result
