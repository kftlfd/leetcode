"""
Leetcode
2025-08-01
118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30


"""

from typing import List


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 18.03MB Beats 16.18%
    """

    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]

        for n in range(2, numRows + 1):
            prev_row = out[-1]
            next_row = [1] * n
            for i in range(1, n - 1):
                next_row[i] = prev_row[i - 1] + prev_row[i]
            out.append(next_row)

        return out
