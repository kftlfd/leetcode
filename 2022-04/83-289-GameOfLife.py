"""
Leetcode
289. Game of Life (medium)
2022-04-12

According to Wikipedia's article: "The Game of Life, also known simply 
as Life, is a cellular automaton devised by the British mathematician 
John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an 
initial state: live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, 
diagonal) using the following four rules (taken from the above 
Wikipedia article):

 1. Any live cell with fewer than two live neighbors dies as if caused 
    by under-population.
 2. Any live cell with two or three live neighbors lives on to the next 
    generation.
 3. Any live cell with more than three live neighbors dies, as if by 
    over-population.
 4. Any dead cell with exactly three live neighbors becomes a live cell, 
    as if by reproduction.

The next state is created by applying the above rules simultaneously to 
every cell in the current state, where births and deaths occur 
simultaneously. Given the current state of the m x n grid board, return 
the next state.
"""

from typing import List

"""
Do not return anything, modify board in-place instead.
"""



# try 1
# Runtime: 44 ms, faster than 60.61% of Python3 online submissions for Game of Life.
# Memory Usage: 13.9 MB, less than 51.25% of Python3 online submissions for Game of Life.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        def neighbors(row: int, col: int, grid: List[List[int]]) -> int:
            
            m = len(grid)
            n = len(grid[0])

            coords = []

            if row != 0:
                if col != 0: coords.append((-1,-1))
                coords.append((-1,0))
                if col != n-1: coords.append((-1,1))

            if col != 0: coords.append((0,-1))
            if col != n-1: coords.append((0,1))

            if row != m-1:
                if col != 0: coords.append((1,-1))
                coords.append((1,0))
                if col != n-1: coords.append((1,1))

            nbrs = 0
            for r,c in coords:
                nbrs += grid[row+r][col+c]
            
            return nbrs
        
        m = len(board)
        n = len(board[0])
        
        # determine next state
        changed = []
        for i in range(m):
            for j in range(n):
                nbrs = neighbors(i, j, board)
                if board[i][j] == 1:
                    if nbrs < 2:
                        changed.append(0)
                    elif nbrs <= 3:
                        changed.append(1)
                    elif nbrs > 3:
                        changed.append(0)
                elif nbrs == 3:
                    changed.append(1)
                else:
                    changed.append(0)

        # write state
        for i in range(m):
            for j in range(n):
                board[i][j] = changed.pop(0)

        return



s = Solution()
tests = [
    [[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
    [[1,1],[1,0]]
]
for t in tests:
    print(t)
    s.gameOfLife(t)
    print(t)
    print()
