"""
Leetcode
2147. Number of Ways to Divide a Long Corridor (hard)
2023-11-28

Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 

Example 1:

Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.

Example 2:

Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.

Example 3:

Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.

 

Constraints:

    n == corridor.length
    1 <= n <= 10^5
    corridor[i] is either 'S' or 'P'.


"""


class Solution:
    """
    Runtime: 364 ms, faster than 82.86% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
    Memory Usage: 21.2 MB, less than 21.43% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
    """

    def numberOfWays(self, corridor: str) -> int:

        seats = []

        for i, c in enumerate(corridor):
            if c == 'S':
                seats.append(i)

        n = len(seats)

        if n == 0 or n % 2 != 0:
            return 0

        ans = 1
        MOD = 10**9 + 7
        for i in range(2, n, 2):
            ans = ans * (seats[i] - seats[i-1]) % MOD

        return ans


class Solution1:
    """
    optimized
    Runtime: 355 ms, faster than 84.29% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
    Memory Usage: 17.3 MB, less than 71.43% of Python3 online submissions for Number of Ways to Divide a Long Corridor.
    """

    def numberOfWays(self, corridor: str) -> int:

        ans = 1
        seats = 0
        prev_group_end = None
        MOD = 10**9 + 7

        for i, c in enumerate(corridor):
            if c == 'S':
                seats += 1

                if seats == 1 and prev_group_end is not None:
                    ans = ans * (i - prev_group_end) % MOD

                elif seats == 2:
                    prev_group_end = i
                    seats = 0

        if prev_group_end is None or seats != 0:
            return 0

        return ans
