"""
Leetcode
51. N-Queens (hard)
2022-06-04

he n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""



# https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments./789851
# Runtime: 175 ms, faster than 20.55% of Python3 online submissions for N-Queens.
# Memory Usage: 14.5 MB, less than 45.52% of Python3 online submissions for N-Queens.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1] * n
        # queens is a one-dimension array, like [1, 3, 0, 2] means
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        # index represents row no and value represents col no

        def dfs(index):
            if index == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):  # pruning
                    dfs(index + 1, )

        # check whether nth queens can be placed
        def valid(n):
            for i in range(n):
                if abs(queens[i] - queens[n]) == n - i:  # same digonal
                    return False
                if queens[i] == queens[n]:  # same column
                    return False
            return True


        # given queens = [1,3,0,2] this function returns 
        # [.Q..]
        # [...Q]
        # [Q...]
        # [..Q.]
        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] = 'Q'
            for row in board_temp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards

        dfs(0)
        return make_all_boards(res)



# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
# Runtime: 92 ms, faster than 55.94% of Python3 online submissions for N-Queens.
# Memory Usage: 14.4 MB, less than 84.03% of Python3 online submissions for N-Queens.
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
