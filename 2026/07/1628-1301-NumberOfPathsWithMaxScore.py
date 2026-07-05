"""
Leetcode
2026-07-05
1301. Number of Paths with Max Score
Hard

You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]

Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]

Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]

 

Constraints:

    2 <= board.length == board[i].length <= 100


Hint 1
Use dynamic programming to find the path with the max score.
Hint 2
Use another dynamic programming array to count the number of paths with max score.
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)

        dp: list[dict[int, int]] = [{} for _ in range(n)]

        self._fill_first_row_dp(dp, board)

        for row in range(n - 2, -1, -1):
            cur_dp: list[dict[int, int]] = [{} for _ in range(n)]
            for col in range(n - 1, -1, -1):
                val = self._get_int_val(board[row][col])
                self._fill_cur_dp(cur_dp, dp, val, col)
            dp = cur_dp

        ans = dp[0]
        if -1 in ans:
            return [0, 0]

        keys = ans.keys()
        if not keys:
            return [0, 0]

        max_score = max(keys)
        if max_score < 0:
            return [0, 0]

        return [max_score, ans[max_score] % (10**9 + 7)]

    def _get_int_val(self, str_val: str) -> int:
        if str_val in "SE":
            return 0
        if str_val == "X":
            return -1
        return int(str_val)

    def _add_paths(self, cur: dict[int, int], prev: dict[int, int], cur_val: int):
        for score, paths_cnt in prev.items():
            cur[score + cur_val] = cur.get(score + cur_val, 0) + paths_cnt

    def _fill_first_row_dp(self, dp: list[dict[int, int]], board: list[str]):
        n = len(board)
        prev = 0
        is_blocked = False
        dp[n-1][0] = 1
        for col in range(n - 2, -1, -1):
            val = self._get_int_val(board[-1][col])
            if val < 0:
                is_blocked = True

            if is_blocked:
                dp[col][-1] = 1
            else:
                dp[col][val + prev] = 1
                prev += val

    def _fill_cur_dp(self, cur_dp: list[dict[int, int]], prev_dp: list[dict[int, int]], cur_val: int, col: int):
        n = len(cur_dp)

        if cur_val < 0:
            cur_dp[col][-1] = 1
            return

        if -1 not in prev_dp[col]:  # down
            self._add_paths(cur_dp[col], prev_dp[col], cur_val)

        if col == n - 1:
            return

        if -1 not in prev_dp[col+1]:  # down-right
            self._add_paths(cur_dp[col], prev_dp[col+1], cur_val)

        if -1 not in cur_dp[col+1]:  # right
            self._add_paths(cur_dp[col], cur_dp[col+1], cur_val)


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 127ms Beats 34.86%
    Memory 20.58MB Beats 43.12%
    """

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1, 0]] * n for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        def update(x, y, u, v):
            if u >= n or v >= n or dp[u][v][0] == -1:
                return
            if dp[u][v][0] > dp[x][y][0]:
                dp[x][y] = dp[u][v][:]
            elif dp[u][v][0] == dp[x][y][0]:
                dp[x][y][1] += dp[u][v][1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not (i == n - 1 and j == n - 1) and board[i][j] != "X":
                    update(i, j, i + 1, j)
                    update(i, j, i, j + 1)
                    update(i, j, i + 1, j + 1)
                    if dp[i][j][0] != -1:
                        dp[i][j][0] += (
                            0 if board[i][j] == "E" else ord(board[i][j]) - 48
                        )
        return (
            [dp[0][0][0], dp[0][0][1] % (10**9 + 7)]
            if dp[0][0][0] != -1
            else [0, 0]
        )


s = Solution1()
tests = [
    (["E1434", "41992", "1X216", "9371X", "X982S"],
     [36, 1]),

    (["EX", "XS"],
     [0, 1]),

    (["E23", "2X2", "12S"],
     [7, 1]),

    (["E12", "1X1", "21S"],
     [4, 2]),

    (["E11", "XXX", "11S"],
     [0, 0]),
]
for inp, exp in tests:
    res = s.pathsWithMaxScore(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
