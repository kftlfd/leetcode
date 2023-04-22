"""
Leetcode
1312. Minimum Insertion Steps to Make a String Palindrome (hard)
2023-04-22

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
"""


class Solution:
    """
    https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/solution/1870542
    Runtime: 529 ms, faster than 98.52% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
    Memory Usage: 13.7 MB, less than 99.79% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
    """

    def minInsertions(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        for start in reversed(range(N)):
            prev = 0
            for end in range(start, N):
                tmp = dp[end]
                if s[start] == s[end]:
                    dp[end] = prev
                else:
                    dp[end] = 1 + min(dp[end], dp[end - 1])
                prev = tmp
        return dp[N - 1]


sol = Solution()
tests = [
    ("zzazz",
     0),

    ("mbadm",
     2),

    ("leetcode",
     5),
]
for inp, exp in tests:
    res = sol.minInsertions(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
