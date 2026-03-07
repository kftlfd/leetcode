"""
Leetcode
2026-03-07
1888. Minimum Number of Flips to Make the Binary String Alternating
Medium

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

    Type-1: Remove the character at the start of the string s and append it to the end of the string.
    Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.

Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

    For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".

Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

 

Constraints:

    1 <= s.length <= 10^5
    s[i] is either '0' or '1'.


Hint 1
Note what actually matters is how many 0s and 1s are in odd and even positions
Hint 2
For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity
"""


class Solution:
    """
    Time Limit Exceeded
    """

    def minFlips(self, s: str) -> int:
        n = len(s)
        ans = n

        for _ in range(n):
            ans = min(ans, self.min_flips(s))
            s = s[1:] + s[0]

        return ans

    def min_flips(self, s: str) -> int:
        count = 0
        for i, c in enumerate(s):
            if i % 2:
                if c == "0":
                    count += 1
            else:
                if c == "1":
                    count += 1
        return min(count, len(s) - count)


class Solution1:
    """
    leetcode solution: Analysis + Prefix Sum + Suffix Sum
    Runtime 611ms Beats 11.29%
    Memory 49.37MB Beats 5.11%
    """

    def minFlips(self, s: str) -> int:
        # Characteristic function
        def I(ch, x):
            return int(ord(ch) - ord("0") == x)

        n = len(s)
        pre = [[0, 0] for _ in range(n)]
        # Note the boundary case when i=0
        for i in range(n):
            pre[i][0] = (0 if i == 0 else pre[i - 1][1]) + I(s[i], 1)
            pre[i][1] = (0 if i == 0 else pre[i - 1][0]) + I(s[i], 0)

        ans = min(pre[n - 1][0], pre[n - 1][1])
        if n % 2 == 1:
            # If n is an odd number, it is also necessary to calculate suf
            suf = [[0, 0] for _ in range(n)]
            # Note the boundary case when i = n - 1
            for i in range(n - 1, -1, -1):
                suf[i][0] = (0 if i == n - 1 else suf[i + 1][1]) + I(s[i], 1)
                suf[i][1] = (0 if i == n - 1 else suf[i + 1][0]) + I(s[i], 0)

            for i in range(n - 1):
                ans = min(ans, pre[i][0] + suf[i + 1][0])
                ans = min(ans, pre[i][1] + suf[i + 1][1])

        return ans
