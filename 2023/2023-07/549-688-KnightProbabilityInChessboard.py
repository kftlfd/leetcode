"""
Leetcode
688. Knight Probability in Chessboard (medium)
2023-07-22

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

Example 1:

Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Example 2:

Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:

    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n - 1
"""


class Solution:
    """
    leetcode solution 1: Bottom-up Dynamic Programming
    Time: O(k * n^2)
    Space: O(n^2)
    Runtime: 360 ms, faster than 33.17% of Python3 online submissions for Knight Probability in Chessboard.
    Memory Usage: 16.6 MB, less than 81.11% of Python3 online submissions for Knight Probability in Chessboard.
    """

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = ((2, -1), (2, 1), (-2, -1), (-2, 1),
                 (1, 2), (-1, 2), (1, -2), (-1, -2))

        prev_dp = [[0] * n for _ in range(n)]
        curr_dp = [[0] * n for _ in range(n)]

        prev_dp[row][column] = 1.0

        for _ in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    curr_dp[r][c] = 0

                    for dr, dc in moves:
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            curr_dp[r][c] += prev_dp[r + dr][c + dc] / 8

            prev_dp, curr_dp = curr_dp, prev_dp

        total_probability = sum(
            prev_dp[r][c]
            for r in range(n)
            for c in range(n)
        )

        return total_probability


class Solution1:
    """
    leetcode solution 3: Top-down Dynamic Programming (Memoization)
    Time: O(k * n^2)
    Space: O(k * n^2)
    Runtime: 558 ms, faster than 5.09% of Python3 online submissions for Knight Probability in Chessboard.
    Memory Usage: 23 MB, less than 46.49% of Python3 online submissions for Knight Probability in Chessboard.
    """

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        dp = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]

        def calculate_dp(moves, i, j):
            # Base case
            if moves == 0:
                if i == row and j == column:
                    return 1
                else:
                    return 0

            # Check if the value has already been calculated
            if dp[moves][i][j] != -1:
                return dp[moves][i][j]

            dp[moves][i][j] = 0

            # Iterate over possible directions
            for direction in directions:
                prev_i = i - direction[0]
                prev_j = j - direction[1]

                # Boundary check
                if 0 <= prev_i < n and 0 <= prev_j < n:
                    dp[moves][i][j] += calculate_dp(moves - 1, prev_i, prev_j)
            dp[moves][i][j] /= 8

            return dp[moves][i][j]

        # Calculate the total probability
        total_probability = sum(
            calculate_dp(k, i, j)
            for i in range(n)
            for j in range(n)
        )

        return total_probability


s = Solution()
tests = [
    ((3, 2, 0, 0),
     0.0625),

    ((1, 0, 0, 0),
     1.0),
]
for inp, exp in tests:
    res = s.knightProbability(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
