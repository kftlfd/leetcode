"""
Leetcode
2026-04-05
657. Robot Return to Origin
Easy

There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

 

Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

 

Constraints:

    1 <= moves.length <= 2 * 10^4
    moves only contains the characters 'U', 'D', 'L' and 'R'.


"""


from collections import Counter


class Solution01:
    """
    Runtime 15ms Beats 60.08%
    Memory 19.27MB Beats 67.40%
    """

    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        dmoves = {
            "U": (0, -1),
            "D": (0, 1),
            "L": (-1, 0),
            "R": (1, 0),
        }

        for move in moves:
            dx, dy = dmoves[move]
            x += dx
            y += dy

        return x == 0 and y == 0


class Solution02:
    """
    Runtime 13ms Beats 65.69%
    Memory 19.37MB Beats 33.52%
    """

    def judgeCircle(self, moves: str) -> bool:
        cnt = Counter(moves)
        return cnt["U"] == cnt["D"] and cnt["L"] == cnt["R"]


class Solution1:
    """
    leetcode solution
    Runtime 18ms Beats 28.11%
    Memory 19.24MB Beats 67.40%
    """

    def judgeCircle(self, moves: str) -> bool:
        x = y = 0

        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        return x == y == 0
