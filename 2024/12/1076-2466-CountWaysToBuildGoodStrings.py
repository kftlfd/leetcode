"""
Leetcode
2024-12-30
2466. Count Ways To Build Good Strings
Medium

Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

    Append the character '0' zero times.
    Append the character '1' one times.

This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

 

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.

Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".

 

Constraints:

    1 <= low <= high <= 10^5
    1 <= zero, one <= low
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        lens = [0] * (high + max(zero, one) + 1)
        lens[zero] += 1
        lens[one] += 1

        for i in range(1, high+1):
            if lens[i] == 0:
                continue
            lens[i+zero] += lens[i]
            lens[i+one] += lens[i]

        return sum(lens[low:high+1]) % (10**9 + 7)


class Solution1:
    """
    leetcode solution 1: Dynamic Programming (Iterative).
    """

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [0] * (high)
        mod = 10 ** 9 + 7

        # Iterate over each length `end`.
        for end in range(1, high + 1):
            # check if the current string can be made by append zero `0`s or one `1`s.
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        # Add up the number of strings with each valid length [low ~ high].
        return sum(dp[low: high + 1]) % mod
