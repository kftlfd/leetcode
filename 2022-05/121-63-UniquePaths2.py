"""
Leetcode
63. Unique Paths II (medium)
2022-05-20

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

from typing import List
from collections import defaultdict



# leetcode solution's bad(wrong) implementation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = 1
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # first row and column
        i = 0
        j = 1
        while j < n:
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i][j-1]
            j += 1
        i = 1
        j = 0
        while i < m:
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j]
            i += 1

        # iterate through the rest of the array
        i = 1
        j = 1
        while True:

            col = j
            while col < n:
                if obstacleGrid[i][col] == 1:
                    obstacleGrid[i][col] = 0
                else:
                    obstacleGrid[i][col] = obstacleGrid[i][col-1] + obstacleGrid[i-1][col]
                col += 1

            row = i+1
            while row < m:
                if obstacleGrid[row][j] == 1:
                    obstacleGrid[row][j] = 0
                else:
                    obstacleGrid[row][j] = obstacleGrid[row-1][j] + obstacleGrid[row][j-1]
                row += 1
            
            if i == m-1 and j == n-1: break
            
            if i < m: i += 1
            if j < n: j += 1
        
        # print modified grid
        # print('-')
        # for row in obstacleGrid:
        #     print(*row)
        # print('-')

        return obstacleGrid[m-1][n-1]



# leetcode solution
# Runtime: 54 ms, faster than 57.67% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14 MB, less than 42.47% of Python3 online submissions for Unique Paths II.
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]



s = Solution1()
tests = [
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,1],[0,0]]
]
for t in tests:
    for row in t:
        print(*row)
    print(s.uniquePathsWithObstacles(t))
    print()
