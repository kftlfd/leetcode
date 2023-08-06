"""
Leetcode
920. Number of Music Playlists (hard)
2023-08-06

Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

    Every song is played at least once.
    A song can only be played again only if k other songs have been played.

Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].

Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].

Constraints:

    0 <= k < n <= goal <= 100
"""


class Solution:
    """
    leetcode solution 1: Bottom-up Dynamic Programming
    Time: O(goal * n)
    Space: O(goal * n)
    Runtime: 64 ms, faster than 65.15% of Python3 online submissions for Number of Music Playlists.
    Memory Usage: 16.5 MB, less than 71.97% of Python3 online submissions for Number of Music Playlists.
    """

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # the i-th song is a new song
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % mod

                # the i-th song is a song we have played before
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % mod

        return dp[goal][n]


class Solution1:
    """
    leetcode solution 2: Top-down Dynamic Programming (Memoization)
    Time: O(goal * n)
    Space: O(goal * n)
    Runtime: 87 ms, faster than 37.88% of Python3 online submissions for Number of Music Playlists.
    Memory Usage: 17.3 MB, less than 34.85% of Python3 online submissions for Number of Music Playlists.
    """

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        dp = [[-1 for _ in range(n + 1)] for _ in range(goal + 1)]

        def playlists(i, j):
            if i == 0 and j == 0:
                return 1
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            # add a new song or replay an old one
            dp[i][j] = (playlists(i - 1, j - 1) * (n - j + 1)) % mod
            if j > k:
                dp[i][j] += (playlists(i - 1, j) * (j - k)) % mod
                dp[i][j] %= mod
            return dp[i][j]

        return playlists(goal, n)


class Solution2:
    """
    leetcode solution 3: Combinatorics
    Time: O(n * log(goal))
    Space: O(n)
    Runtime: 53 ms, faster than 87.12% of Python3 online submissions for Number of Music Playlists.
    Memory Usage: 16.3 MB, less than 90.91% of Python3 online submissions for Number of Music Playlists.
    """

    MOD = 1_000_000_007

    def power(self, base, exponent):
        result = 1
        # Loop until exponent is not zero
        while exponent > 0:
            # If exponent is odd, multiply result with base
            if exponent & 1:
                result = (result * base) % self.MOD
            # Divide the exponent by 2 and square the base
            exponent >>= 1
            base = (base * base) % self.MOD
        return result

    def precalculate_factorials(self, n):
        self.factorial = [1] * (n + 1)
        self.inv_factorial = [1] * (n + 1)
        # Calculate factorials and inverse factorials for each number up to 'n'
        for i in range(1, n + 1):
            self.factorial[i] = (self.factorial[i - 1] * i) % self.MOD
            # Inverse factorial calculated using Fermat's Little Theorem
            self.inv_factorial[i] = self.power(self.factorial[i], self.MOD - 2)

    def numMusicPlaylists(self, n, goal, k):
        # Pre-calculate factorials and inverse factorials
        self.precalculate_factorials(n)
        # Initialize variables for calculation
        sign = 1
        answer = 0
        # Loop from 'n' down to 'k'
        for i in range(n, k - 1, -1):
            # Calculate temporary result for this iteration
            temp = self.power(i - k, goal - k)
            temp = (temp * self.inv_factorial[n - i]) % self.MOD
            temp = (temp * self.inv_factorial[i - k]) % self.MOD
            # Add or subtract temporary result to/from answer
            answer = (answer + sign * temp + self.MOD) % self.MOD
            # Flip sign for next iteration
            sign *= -1
        # Final result is n! * answer, all under modulo
        return (self.factorial[n] * answer) % self.MOD
