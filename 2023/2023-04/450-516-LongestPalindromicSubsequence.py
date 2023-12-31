"""
Leetcode
516. Longest Palindromic Subsequence (medium)
2023-04-14

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded. 61 / 86 test cases passed.
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        mask = (1 << n) - 1
        mask = f"{mask:b}"
        mask = '0' * (n - len(mask)) + mask
        masks = [mask]

        while masks:
            for m in masks:
                subsequence = [c for c, i in zip(s, m) if i == '1']
                if self.isPalindrome(subsequence):
                    return len(subsequence)

            next_masks = set()
            for m in masks:
                for i in range(n):
                    next_masks.add(m[:i] + '0' + m[i+1:])
            masks = next_masks

        return 0

    def isPalindrome(self, s: List[str]) -> bool:
        if len(s) in (0, 1):
            return True

        if len(s) % 2 == 0:
            mid = len(s) // 2
            return s[:mid] == s[mid:][::-1]

        mid = len(s) // 2
        return s[:mid] == s[mid+1:][::-1]


class Solution1:
    """
    leetcode solution 1: Recursive Dynamic Programming
    Runtime: 1276 ms, faster than 78.34% of Python3 online submissions for Longest Palindromic Subsequence.
    Memory Usage: 236.2 MB, less than 19.35% of Python3 online submissions for Longest Palindromic Subsequence.
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def lps(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = lps(l+1, r-1) + 2
            else:
                memo[(l, r)] = max(lps(l, r-1), lps(l+1, r))
            return memo[(l, r)]

        return lps(0, n-1)


class Solution2:
    """
    leetcode solution 3: Dynamic Programming with Space Optimization
    Runtime: 1028 ms, faster than 86.21% of Python3 online submissions for Longest Palindromic Subsequence.
    Memory Usage: 13.8 MB, less than 97.68% of Python3 online submissions for Longest Palindromic Subsequence.
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp, dpPrev = [0] * n, [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j - 1] + 2
                else:
                    dp[j] = max(dpPrev[j], dp[j - 1])
            dpPrev = dp[:]

        return dp[n - 1]


sol = Solution2()
tests = [
    ("cbbd",
     2),

    ("bbbab",
     4),
]
for inp, exp in tests:
    res = sol.longestPalindromeSubseq(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
