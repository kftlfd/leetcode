"""
Leetcode
2026-11-17
2911. Minimum Changes to Make K Semi-palindromes
Hard

Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.

Return the minimum number of letter changes required.

A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:

    Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.
    For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.
    The string is considered a semi-palindrome if each of these groups forms a palindrome.

Consider the string "abcabc":

    The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.
    For d = 1: The entire string "abcabc" forms one group. Not a palindrome.
    For d = 2:
        Group 1 (positions 1, 3, 5): "acb"
        Group 2 (positions 2, 4, 6): "bac"
        Neither group forms a palindrome.
    For d = 3:
        Group 1 (positions 1, 4): "aa"
        Group 2 (positions 2, 5): "bb"
        Group 3 (positions 3, 6): "cc"
        All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.

 

Example 1:

Input: s = "abcac", k = 2

Output: 1

Explanation: Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

Example 2:

Input: s = "abcdef", k = 2

Output: 2

Explanation: Divide s into substrings "abc" and "def". Each needs one change to become semi-palindrome.

Example 3:

Input: s = "aabbaa", k = 3

Output: 0

Explanation: Divide s into substrings "aa", "bb" and "aa". All are already semi-palindromes.

 

Constraints:

    2 <= s.length <= 200
    1 <= k <= s.length / 2
    s contains only lowercase English letters.


Hint 1
Define dp[i][j] as the minimum count of letter changes needed to split the suffix of string s starting from s[i] into j valid parts.
Hint 2
We have dp[i][j] = min(dp[x + 1][j - 1] + v[i][x]). Here v[i][x] is the minimum number of letter changes to change substring s[i..x] into semi-palindrome.
Hint 3
v[i][j] can be calculated separately by brute-force. We can create a table of v[i][j] independently to improve the complexity. Also note that semi-palindrome's length is at least 2.
"""


from functools import cache


class Solution1:
    """
    leetcode solution 1: Precomputing Segment Costs + Top-Down Dynamic Programming
    Runtime 2506ms Beats 70.97%
    Memory 25.94MB Beats 25.81%
    """

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = [[] for _ in range(n + 1)]
        # Precompute the proper divisors of each number
        for d in range(1, n // 2 + 1):
            for m in range(d * 2, n + 1, d):
                factors[m].append(d)
        cost = [[0] * n for _ in range(n)]
        for l in range(n - 1):
            for r in range(
                l + 1, n
            ):  # Each substring must have length at least 2
                cost[l][r] = self.segmentCost(s, l, r - l + 1, factors)

        @cache
        def solve(seg: int, start: int) -> int:
            if seg == 1:  # Only one segment remains
                return cost[start][n - 1]
            limit = (
                n - 1 - 2 * (seg - 1)
            )  # Leave room for seg-1 segments after the first segment
            return min(
                cost[start][e] + solve(seg - 1, e + 1)
                for e in range(start + 1, limit + 1)
            )

        return solve(k, 0)

    def segmentCost(self, s: str, l: int, m: int, factors: list) -> int:
        best = m
        for d in factors[m]:
            groups = m // d  # Each group contains groups characters
            changes = 0
            for offset in range(d):
                for t in range(
                    groups // 2
                ):  # Pair characters from opposite ends of the group
                    if (
                        s[l + offset + t * d]
                        != s[l + offset + (groups - 1 - t) * d]
                    ):
                        changes += 1
            best = min(best, changes)
        return best


class Solution2:
    """
    leetcode solution 2: Bottom-Up Dynamic Programming
    Runtime 3023ms Beats 45.16%
    Memory 19.31MB Beats 87.10%
    """

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = [[] for _ in range(n + 1)]
        # Precompute the proper divisors of each number
        for d in range(1, n // 2 + 1):
            for m in range(d * 2, n + 1, d):
                factors[m].append(d)
        cost = [[0] * n for _ in range(n)]
        for l in range(n - 1):
            for r in range(
                l + 1, n
            ):  # Each substring must have length at least 2
                cost[l][r] = self.segmentCost(s, l, r - l + 1, factors)

        prev = [cost[start][n - 1] for start in range(n)]  # The case seg = 1
        for seg in range(
            2, k + 1
        ):  # Increase the number of segments from 2 to k
            cur = [n] * n
            limit = n - 1 - 2 * (seg - 1)
            for start in range(
                n - 2 * seg + 1
            ):  # Leave at least 2*seg characters
                cur[start] = min(
                    cost[start][e] + prev[e + 1]
                    for e in range(start + 1, limit + 1)
                )
            prev = cur
        return prev[0]

    def segmentCost(self, s: str, l: int, m: int, factors: list) -> int:
        best = m
        for d in factors[m]:
            groups = m // d  # Each group contains groups characters
            changes = 0
            for offset in range(d):
                for t in range(
                    groups // 2
                ):  # Pair characters from opposite ends of the group
                    if (
                        s[l + offset + t * d]
                        != s[l + offset + (groups - 1 - t) * d]
                    ):
                        changes += 1
            best = min(best, changes)
        return best
