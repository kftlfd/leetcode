"""
Leetcode
59. Spiral Matrix II (medium)
2022-04-13

Given a positive integer n, generate an n x n matrix filled 
with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
"""

from typing import List



# https://leetcode.com/problems/spiral-matrix-ii/discuss/1941112/Python3-STRAIGHTFORWARD-()-Explained
# Runtime: 30 ms, faster than 92.84% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 13.8 MB, less than 85.84% of Python3 online submissions for Spiral Matrix II.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0] * n for _ in range(n)]
        
        def fill_circle(el, start, n):
            i = start
            j = start
            # top row            
            for k in range(j, j + n): 
                res[i][k] = el
                el = el + 1
            # right column
            for k in range(i + 1, i + n): 
                res[k][j + n - 1] = el
                el = el + 1
            # bottom row
            for k in reversed(range(j, j + n - 1)): 
                res[i + n - 1][k] = el
                el = el + 1
            # left column
            for k in reversed(range(i + 1, i + n - 1)): 
                res[k][j] = el
                el = el + 1
        
        el, start = 1, 0
        while n > 0:
            fill_circle(el, start, n)
            el = el + 4*(n - 1)
            n = n - 2
            start = start + 1
            
        return res



s = Solution()
tests = [1, 2, 3, 4, 5, 6]
for t in tests:
    print(t)
    matrix = s.generateMatrix(t)
    print(matrix)
    for row in matrix:
        print("\t".join([str(c) for c in row]))
    print()
