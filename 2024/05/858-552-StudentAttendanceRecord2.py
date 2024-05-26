"""
Leetcode
552. Student Attendance Record II
Hard
2024-05-26

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.

Any student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.

Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:

Input: n = 1
Output: 3

Example 3:

Input: n = 10101
Output: 183236316

 

Constraints:

    1 <= n <= 10^5
"""


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming
    Runtime: 6857 ms, faster than 9.01% of Python3 online submissions for Student Attendance Record II.
    Memory Usage: 76.9 MB, less than 31.75% of Python3 online submissions for Student Attendance Record II.
    """

    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # Initialize the cache to store sub-problem results.
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Recursive function to return the count of combinations
        # of length 'n' eligible for the award.
        def eligible_combinations(n, total_absences, consecutive_lates):
            # If the combination has become not eligible for the award,
            # then we will not count any combinations that can be made using it.
            if total_absences >= 2 or consecutive_lates >= 3:
                return 0
            # If we have generated a combination of length 'n' we will count it.
            if n == 0:
                return 1

            # If we have already seen this sub-problem earlier,
            # we return the stored result.
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]

            # We choose 'P' for the current position.
            count = eligible_combinations(n - 1, total_absences, 0)

            # We choose 'A' for the current position.
            count = (
                count +
                eligible_combinations(n - 1, total_absences + 1, 0)
            ) % MOD

            # We choose 'L' for the current position.
            count = (
                count +
                eligible_combinations(n - 1,
                                      total_absences,
                                      consecutive_lates + 1)
            ) % MOD

            # Return and store the current sub-problem result in the cache.
            memo[n][total_absences][consecutive_lates] = count
            return count

        # Return count of combinations of length 'n' eligible for the award.
        return eligible_combinations(n, 0, 0)


class Solution2:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    Runtime: 5113 ms, faster than 32.71% of Python3 online submissions for Student Attendance Record II.
    Memory Usage: 64.1 MB, less than 46.45% of Python3 online submissions for Student Attendance Record II.
    """

    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # Cache to store sub-problem results.
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Base case: there is 1 string of length 0 with zero 'A' and zero 'L'.
        dp[0][0][0] = 1

        # Iterate on smaller sub-problems and use the current smaller sub-problem
        # to generate results for bigger sub-problems.
        for length in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    # Store the count when 'P' is chosen.
                    dp[length + 1][total_absences][0] = (
                        dp[length + 1][total_absences][0] +
                        dp[length][total_absences][consecutive_lates]
                    ) % MOD

                    # Store the count when 'A' is chosen.
                    if total_absences < 1:
                        dp[length + 1][total_absences + 1][0] = (
                            dp[length + 1][total_absences + 1][0] +
                            dp[length][total_absences][consecutive_lates]
                        ) % MOD

                    # Store the count when 'L' is chosen.
                    if consecutive_lates < 2:
                        dp[length + 1][total_absences][consecutive_lates + 1] = (
                            dp[length + 1][total_absences][consecutive_lates + 1] +
                            dp[length][total_absences][consecutive_lates]
                        ) % MOD

        # Sum up the counts for all combinations of length 'n' with different absent and late counts.
        count = 0
        for total_absences in range(2):
            for consecutive_lates in range(3):
                count = (count +
                         dp[n][total_absences][consecutive_lates]) % MOD

        return count


class Solution3:
    """
    leetcode solution 3: Bottom-Up Dynamic Programming, Space Optimized
    Runtime: 3839 ms, faster than 47.87% of Python3 online submissions for Student Attendance Record II.
    Memory Usage: 16.5 MB, less than 99.53% of Python3 online submissions for Student Attendance Record II.
    """

    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # Cache to store current sub-problem results.
        dp_curr_state = [[0] * 3 for _ in range(2)]
        # Cache to store next sub-problem results.
        dp_next_state = [[0] * 3 for _ in range(2)]

        # Base case: there is 1 string of length 0 with zero 'A' and zero 'L'.
        dp_curr_state[0][0] = 1

        # Iterate on smaller sub-problems and use the current smaller sub-problem
        # to generate results for bigger sub-problems.
        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    # Store the count when 'P' is chosen.
                    dp_next_state[total_absences][0] = (
                        dp_next_state[total_absences][0] +
                        dp_curr_state[total_absences][consecutive_lates]
                    ) % MOD

                    # Store the count when 'A' is chosen.
                    if total_absences < 1:
                        dp_next_state[total_absences + 1][0] = (
                            dp_next_state[total_absences + 1][0] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD

                    # Store the count when 'L' is chosen.
                    if consecutive_lates < 2:
                        dp_next_state[total_absences][consecutive_lates + 1] = (
                            dp_next_state[total_absences][consecutive_lates + 1] +
                            dp_curr_state[total_absences][consecutive_lates]
                        ) % MOD

            # Next state sub-problems will become current state sub-problems in the next iteration.
            dp_curr_state = [row[:] for row in dp_next_state]
            # Next state sub-problem results will reset to zero.
            dp_next_state = [[0] * 3 for _ in range(2)]

        # Sum up the counts for all combinations of length 'n' with different absent and late counts.
        count = sum(dp_curr_state[total_absences][consecutive_lates]
                    for total_absences in range(2)
                    for consecutive_lates in range(3)) % MOD
        return count
