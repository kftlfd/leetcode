"""
Leetcode
664. Strange Printer
Hard
2024-08-21

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

import itertools


class Solution1:
    """
    leetcode solution 1: Top Down Dynamic Programming (Memoization)
    Runtime: 220 ms, faster than 83.88% of Python3 online submissions for Strange Printer.
    Memory Usage: 19.5 MB, less than 23.81% of Python3 online submissions for Strange Printer.
    """

    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))

        memo = {}

        def _minimum_turns(start, end) -> int:
            # Base case: empty string requires 0 turns
            if start > end:
                return 0

            # If result is memoized, return it
            if (start, end) in memo:
                return memo[(start, end)]

            # Initialize with worst case: print each character separately
            min_turns = 1 + _minimum_turns(start + 1, end)

            # Try to optimize by finding matching characters
            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    # If match found, try splitting the problem
                    turns_with_match = _minimum_turns(
                        start, k - 1
                    ) + _minimum_turns(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)

            # Memoize and return the result
            memo[(start, end)] = min_turns
            return min_turns

        # Start the recursive process
        return _minimum_turns(0, len(s) - 1)


class Solution2:
    """
    leetcode solution 2: Bottom Up Dynamic Programming (Tabulation)
    Runtime: 799 ms, faster than 27.47% of Python3 online submissions for Strange Printer.
    Memory Usage: 16.7 MB, less than 80.95% of Python3 online submissions for Strange Printer.
    """

    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)

        # min_turns[i][j] represents the minimum number of turns to print s[i] to s[j]
        min_turns = [[0] * n for _ in range(n)]

        # Initialize base case
        for i in range(n):
            # It takes 1 turn to print a single character
            min_turns[i][i] = 1

        # Fill the dp table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                # Initialize with worst case: print each character separately
                min_turns[start][end] = length

                # Try all possible splits and find the minimum
                for split in range(length - 1):
                    total_turns = (
                        min_turns[start][start + split]
                        + min_turns[start + split + 1][end]
                    )

                    # If the characters at the split and end match, we can save one turn
                    if s[start + split] == s[end]:
                        total_turns -= 1

                    min_turns[start][end] = min(
                        min_turns[start][end], total_turns
                    )

        # Return the minimum turns needed to print the entire string
        return min_turns[0][n - 1] if n > 0 else 0
