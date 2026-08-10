"""
Leetcode
2026-08-10
1510. Stone Game IV
Hard

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

 

Constraints:

    1 <= n <= 10^5


"""


from functools import cache


class Solution01:
    """
    Memory Limit Exceeded
    72 / 72 testcases passed
    """

    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def turn(stones: int) -> bool:
            if stones < 1:
                return False

            opts = []
            i = 1
            take = 1
            while take <= stones:
                opts.append(take)
                i += 1
                take = i * i
            if not opts:
                return False

            if all(turn(stones - take) for take in opts):
                return False

            return True

        return turn(n)


class Solution02:
    """
    Runtime 227ms Beats 90.30%
    Memory 21.35MB Beats 43.64%
    """

    def winnerSquareGame(self, n: int) -> bool:
        memo: list[None | bool] = [None] * (n + 1)
        memo[0] = False
        memo[1] = True

        opts = []
        i = 1
        take = 1
        while take <= n:
            opts.insert(0, take)
            i += 1
            take = i * i

        def turn(stones: int) -> bool:
            if (m := memo[stones]) is not None:
                return m

            ans = not all(
                turn(stones - take)
                for take in (o for o in opts if o <= stones)
            )

            memo[stones] = ans
            return ans

        return turn(n)
