"""
Leetcode
91. Decode Ways
Medium
2023-12-25

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

 

Constraints:

    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
"""


class Solution:
    """
    Time Limit Exceeded
    """

    def numDecodings(self, s: str) -> int:
        ans = 0

        def dfs(index: int):
            nonlocal ans

            if index >= len(s):
                ans += 1
                return

            if s[index] == "0":
                return

            dfs(index + 1)

            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                dfs(index + 2)

        dfs(0)
        return ans


class Solution1:
    """
    https://leetcode.com/problems/decode-ways/discuss/253018/Python:-Easy-to-understand-explanation-bottom-up-dynamic-programming/356723
    Runtime: 40 ms, faster than 53.87% of Python3 online submissions for Decode Ways.
    Memory Usage: 17.3 MB, less than 5.57% of Python3 online submissions for Decode Ways.
    """

    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):

            # One step jump
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i - 1]

            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
