"""
Leetcode
120. Triangle (medium)
2022-06-13

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
"""

from typing import List



# top-down
# Runtime: 122 ms, faster than 22.29% of Python3 online submissions for Triangle.
# Memory Usage: 15 MB, less than 37.66% of Python3 online submissions for Triangle.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0], float('inf')]
        for i in range(1, len(triangle)):
            row = [ dp[0] + triangle[i][0] ]
            for j in range(1, len(triangle[i])):
                row.append( min(dp[j-1], dp[j]) + triangle[i][j] )
            row.append(float('inf'))
            dp = row
        return min(dp)



# bottom-up
# Runtime: 126 ms, faster than 19.22% of Python3 online submissions for Triangle.
# Memory Usage: 15 MB, less than 60.15% of Python3 online submissions for Triangle.
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            dp = [ triangle[i][j] + min(dp[j], dp[j+1]) for j in range(len(triangle[i])) ]
        return dp[0]



s = Solution1()
tests = [
    [[2],[3,4],[6,5,7],[4,1,8,3]],
    [[-10]],
]
for t in tests:
    print(t)
    print(s.minimumTotal(t))
    print()
