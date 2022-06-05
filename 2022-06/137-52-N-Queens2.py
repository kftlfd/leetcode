"""
Leetcode
52. N-Queens II (hard)
2022-06-05

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""



# modified https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
# Runtime: 82 ms, faster than 50.15% of Python3 online submissions for N-Queens II.
# Memory Usage: 13.9 MB, less than 39.44% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(result)



# modified https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments./789851
# Runtime: 145 ms, faster than 21.73% of Python3 online submissions for N-Queens II.
# Memory Usage: 14 MB, less than 39.44% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        queens = [-1] * n

        def dfs(index):
            if index == len(queens): # n queens have been placed correctly
                res.append(queens[:])
                return  # backtracking
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):  # pruning
                    dfs(index + 1, )

        def valid(n):
            for i in range(n):
                if abs(queens[i] - queens[n]) == n - i:  # same digonal
                    return False
                if queens[i] == queens[n]:  # same column
                    return False
            return True

        dfs(0)
        return len(res)



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
