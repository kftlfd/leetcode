"""
Leetcode
118. Pascal's Triangle (easy)
2023-09-08

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
"""

from typing import List


class Solution:
    """
    Runtime: 42 ms, faster than 60.08% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 16.2 MB, less than 94.68% of Python3 online submissions for Pascal's Triangle.
    """

    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for _ in range(1, numRows):
            row = []
            prev = ans[-1]
            for i in range(1, len(prev)):
                row.append(prev[i-1] + prev[i])
            ans.append([1] + row + [1])

        return ans
