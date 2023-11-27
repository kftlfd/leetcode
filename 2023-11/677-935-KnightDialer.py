"""
Leetcode
935. Knight Dialer (medium)
2023-11-27

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

 

Constraints:

    1 <= n <= 5000
"""


from functools import cache


class Solution:
    """
    Runtime: 1266 ms, faster than 54.88% of Python3 online submissions for Knight Dialer.
    Memory Usage: 16.5 MB, less than 67.69% of Python3 online submissions for Knight Dialer.
    """

    def knightDialer(self, n: int) -> int:
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        endings = {n: 1 for n in range(10)}

        ans = 10

        for _ in range(1, n):  # jumps
            new_endings = {n: 0 for n in range(10)}

            for digit, ends_in in endings.items():
                for nxt_digit in moves[digit]:
                    new_endings[nxt_digit] += ends_in

            ans = sum(new_endings.values())
            endings = new_endings

        return ans % (10**9 + 7)


class Solution1:
    """
    leetcode solution 1: Top-Down DP
    Runtime: 1313 ms, faster than 53.57% of Python3 online submissions for Knight Dialer.
    Memory Usage: 46.8 MB, less than 34.17% of Python3 online submissions for Knight Dialer.
    Time: O(n)
    Space: O(n)
    """

    def knightDialer(self, n: int) -> int:

        @cache
        def dp(remain, square):
            if remain == 0:
                return 1

            ans = 0
            for next_square in jumps[square]:
                ans = (ans + dp(remain - 1, next_square)) % MOD

            return ans

        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        ans = 0
        MOD = 10 ** 9 + 7
        for square in range(10):
            ans = (ans + dp(n - 1, square)) % MOD

        return ans


class Solution2:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming (space optimized)
    Time: O(n)
    Space: O(1)
    Runtime: 553 ms, faster than 83.46% of Python3 online submissions for Knight Dialer.
    Memory Usage: 16.2 MB, less than 91.46% of Python3 online submissions for Knight Dialer.
    """

    def knightDialer(self, n: int) -> int:

        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        MOD = 10 ** 9 + 7
        dp = [0] * 10
        prev_dp = [1] * 10

        for remain in range(1, n):
            dp = [0] * 10
            for square in range(10):
                ans = 0
                for next_square in jumps[square]:
                    ans = (ans + prev_dp[next_square]) % MOD

                dp[square] = ans

            prev_dp = dp

        ans = 0
        for square in range(10):
            ans = (ans + prev_dp[square]) % MOD

        return ans


class Solution3:
    """
    leetcode solution 4: Efficient Iteration On States
    Time: O(n)
    Space: O(1)
    Runtime: 93 ms, faster than 97.59% of Python3 online submissions for Knight Dialer.
    Memory Usage: 16.1 MB, less than 98.03% of Python3 online submissions for Knight Dialer.
    """

    def knightDialer(self, n: int) -> int:

        if n == 1:
            return 10

        A = 4
        B = 2
        C = 2
        D = 1
        MOD = 10 ** 9 + 7

        for _ in range(n - 1):
            A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C

        return (A + B + C + D) % MOD


class Solution4:
    """
    leetcode solution 5: Linear Algebra
    Time: O(log(n))
    Space: O(1)
    Runtime: 223 ms, faster than 92.99% of Python3 online submissions for Knight Dialer.
    Memory Usage: 16.4 MB, less than 73.06% of Python3 online submissions for Knight Dialer.
    """

    def knightDialer(self, n: int) -> int:

        if n == 1:
            return 10

        def multiply(A, B):
            result = [[0] * len(B[0]) for _ in range(len(A))]

            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD

            return result

        A = [
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        ]

        v = [[1] * 10]
        MOD = 10 ** 9 + 7

        n -= 1
        while n:
            if n & 1:
                v = multiply(v, A)

            A = multiply(A, A)
            n >>= 1

        return sum(v[0]) % MOD
