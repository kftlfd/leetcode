"""
Leetcode
2466. Count Ways To Build Good Strings (medium)
2023-05-13

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
"""


class Solution1:
    """
    leetcode solution 1: DP iterative
    Runtime: 225 ms, faster than 86.61% of Python3 online submissions for Count Ways To Build Good Strings.
    Memory Usage: 21 MB, less than 66.14% of Python3 online submissions for Count Ways To Build Good Strings.
    """

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + ([0] * high)
        mod = 10**9 + 7

        for end in range(1, high + 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        return sum(dp[low:high + 1]) % mod


class Solution2:
    """
    leetcode solution 2: DP recursive
    Runtime: 297 ms, faster than 64.57% of Python3 online submissions for Count Ways To Build Good Strings.
    Memory Usage: 94.2 MB, less than 58.27% of Python3 online submissions for Count Ways To Build Good Strings.
    """

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + ([-1] * high)
        mod = 10**9 + 7

        def dfs(end):
            if dp[end] != -1:
                return dp[end]

            count = 0

            if end >= zero:
                count += dfs(end - zero)

            if end >= one:
                count += dfs(end - one)

            dp[end] = count % mod

            return dp[end]

        return sum(dfs(end) for end in range(low, high + 1)) % mod


s = Solution2()
tests = [
    ((3, 3, 1, 1),
     8),

    ((2, 3, 1, 2),
     5),
]
for inp, exp in tests:
    res = s.countGoodStrings(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
