"""
Leetcode
2025-09-25
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

 

Constraints:

    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4

 
Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
 
"""

from typing import List


class Solution:
    """
    Runtime 3ms Beats 86.00%
    Memory 18.84MB Beats 74.79%
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        inf = 1 << 15
        n = len(triangle[-1])
        dp = [inf] * n
        dp[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            row = triangle[i]
            for j in range(len(row) - 1, -1, -1):
                val = row[j]
                dp[j] = val + (dp[j] if j == 0 else min(dp[j], dp[j - 1]))

        return min(dp)
