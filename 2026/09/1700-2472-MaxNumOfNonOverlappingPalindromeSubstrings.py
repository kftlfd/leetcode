"""
Leetcode
2026-09-15
2472. Maximum Number of Non-overlapping Palindrome Substrings
Hard

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

    The length of each substring is at least k.
    Each substring is a palindrome.

Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

 

Constraints:

    1 <= k <= s.length <= 2000
    s consists of lowercase English letters.


Hint 1
Try to use dynamic programming to solve the problem.
Hint 2
let dp[i] be the answer for the prefix s[0…i].
Hint 3
The final answer to the problem will be dp[n-1]. How do you compute this dp?
"""


class Solution1:
    """
    leetcode solution 1: Dynamic Programming
    Runtime 2973ms Beats 8.24%
    Memory 50.70MB Beats 19.07%
    """

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = s[left] == s[right] and (
                    length <= 2 or is_palindrome[left + 1][right - 1]
                )

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if is_palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 3ms Beats 95.88%
    Memory 19.34MB Beats 72.68%
    """

    def maxPalindromes(self, s: str, k: int) -> int:
        def check(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        ans = 0
        start = 0

        for r in range(k - 1, n):
            l = r - k + 1
            if l >= start and check(l, r):
                ans += 1
                start = r + 1
                continue

            l = r - k
            if l >= start and check(l, r):
                ans += 1
                start = r + 1

        return ans
