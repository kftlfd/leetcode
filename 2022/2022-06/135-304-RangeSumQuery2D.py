"""
Leetcode
304. Range Sum Query 2D - Immutable (medium)
2022-06-03

Given a 2D matrix matrix, handle multiple queries of the following type:

 - Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

 - NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
 - int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

from typing import List



# try 1
# Time Limit Exceeded
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sr = 0
        for m in range(row1, row2 + 1):
            for n in range(col1, col2 + 1):
                sr += self.matrix[m][n]
        return sr
        


# leetcode solution - caching
# Runtime: 2651 ms, faster than 28.43% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 23.3 MB, less than 99.84% of Python3 online submissions for Range Sum Query 2D - Immutable.
class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            # dp[r+1][c+1] = sum of rectangle in matrix from (0,0) to (r,c)
            # first row and column are zeroes for convenience
            self.dp = [ [0] * (n+1) for _ in range(m+1) ]
            for r in range(m):
                for c in range(n):
                    self.dp[r+1][c+1] = matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]
        return
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sr  = self.dp[row2 + 1][col2 + 1]
        sr -= self.dp[row2 + 1][col1]
        sr += self.dp[row1][col1]
        sr -= self.dp[row1][col2 + 1]
        return sr



instr = ["NumMatrix","sumRegion","sumRegion","sumRegion","sumRegion"]
args = [
    [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]],
    [2,1,4,3],
    [1,1,2,2],
    [1,2,2,4],
    [0,0,4,4]
]
print(instr)
print(args[0])
print(args[1:])
out = []
for i in range(len(instr)):
    if instr[i] == 'NumMatrix':
        s = NumMatrix1(args[i])
        out.append(None)
    elif instr[i] == 'sumRegion':
        out.append(s.sumRegion(*args[i]))
print(out)
print()
