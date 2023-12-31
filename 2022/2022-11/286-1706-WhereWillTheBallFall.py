"""
Leetcode
1706. Where Will the Ball Fall (medium)
2022-11-01

You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

 - A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
 - A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.

We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

Example 1:
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:
Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:
Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]
"""

from typing import List, Optional


# Runtime: 397 ms, faster than 65.82% of Python3 online submissions for Where Will the Ball Fall.
# Memory Usage: 14.3 MB, less than 84.52% of Python3 online submissions for Where Will the Ball Fall.
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        balls = [x for x in range(n)]  # starting column for each ball

        for row in range(m):
            for ball, col in enumerate(balls):

                if col == -1:  # already stuck
                    continue

                if grid[row][col] == -1:  # redirect to left
                    if col == 0 or grid[row][col-1] == 1:  # will get stuck
                        balls[ball] = -1
                    else:
                        balls[ball] = col - 1
                    continue

                if grid[row][col] == 1:  # redirect to right
                    if col == n-1 or grid[row][col+1] == -1:  # will get stuck
                        balls[ball] = -1
                    else:
                        balls[ball] = col + 1

        return balls


# leetcode solution
# Runtime: 421 ms, faster than 61.47% of Python3 online submissions for Where Will the Ball Fall.
# Memory Usage: 14.2 MB, less than 98.48% of Python3 online submissions for Where Will the Ball Fall.
class Solution1:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        balls = [-1] * n

        for col in range(n):
            currCol = col

            for row in range(m):

                nextCol = currCol + grid[row][currCol]

                if nextCol < 0 or nextCol >= n or grid[row][currCol] != grid[row][nextCol]:
                    # will get stuck
                    balls[col] = -1
                    break

                balls[col] = nextCol
                currCol = nextCol

        return balls


s = Solution1()
tests = [
    ([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]],
     [1, -1, -1, -1, -1]),

    ([[-1]],
     [-1]),

    ([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]],
     [0, 1, 2, 3, 4, -1]),
]
for inp, exp in tests:
    res = s.findBall(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
