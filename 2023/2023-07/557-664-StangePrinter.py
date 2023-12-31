"""
Leetcode
664. Strange Printer (hard)
2023-07-30

There is a strange printer with the following two special properties:

    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

Constraints:

    1 <= s.length <= 100
    s consists of lowercase English letters.
"""


class Solution:
    """
    leetcode solution 1: bottom-up dynamic programming
    Time: O(n^3)
    Space: O(n^2)
    Runtime: 1433 ms, faster than 32.25% of Python3 online submissions for Strange Printer.
    Memory Usage: 16.3 MB, less than 92.90% of Python3 online submissions for Strange Printer.
    """

    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]

        for length in range(1, n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1

                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(
                            dp[left][right], 1 + dp[j][i] + dp[i + 1][right])

                if j == -1:
                    dp[left][right] = 0

        return dp[0][n - 1] + 1


class Solution1:
    """
    leetcode solution 2: top-down dynamic programming
    Time: O(n^3)
    Space: O(n^2)
    Runtime: 2121 ms, faster than 12.90% of Python3 online submissions for Strange Printer.
    Memory Usage: 17.5 MB, less than 50.97% of Python3 online submissions for Strange Printer.
    """

    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(left, right):
            if dp[left][right] != -1:
                return dp[left][right]

            dp[left][right] = n
            j = -1

            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    dp[left][right] = min(
                        dp[left][right], 1 + solve(j, i) + solve(i + 1, right))

            if j == -1:
                dp[left][right] = 0

            return dp[left][right]

        return solve(0, n - 1) + 1


sol = Solution()
tests = [
    ('aaabbb',
     2),

    ('aba',
     2),
]
for inp, exp in tests:
    res = sol.strangePrinter(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
