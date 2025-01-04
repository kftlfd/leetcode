"""
Leetcode
2025-01-04
1930. Unique Length-3 Palindromic Subsequences
Medium

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

 

Constraints:

    3 <= s.length <= 10^5
    s consists of only lowercase English letters.

Hint 1
What is the maximum number of length-3 palindromic strings?
Hint 2
How can we keep track of the characters that appeared to the left of a given position?
"""


class Solution:
    """
    Runtime 1527ms Beats 43.51%
    Memory 18.40MB Beats 22.86%
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        first_idx = [-1] * 26
        last_idx = [-1] * 26
        cnt = [0] * 26
        a = ord('a')
        seen = [[False] * 26 for _ in range(26)]

        for idx, c in enumerate(s):
            i = ord(c) - a
            cnt[i] += 1
            last_idx[i] = idx
            if first_idx[i] == -1:
                first_idx[i] = idx

        for idx, c in enumerate(s):
            i = ord(c) - a
            for j in range(26):
                if cnt[j] < (2 + (i == j)) or first_idx[j] > idx or last_idx[j] < idx:
                    continue
                seen[i][j] = True

        return sum(int(seen[i][j]) for i in range(26) for j in range(26))


class Solution1:
    """
    leetcode solution 1: Count Letters In-Between
    Runtime 480ms Beats 68.79%
    Memory 18.43MB Beats 18.68%
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans


class Solution2:
    """
    leetcode solution 2: Pre-Compute First and Last Indices
    Runtime 533ms Beats 58.90%
    Memory 18.44MB Beats 18.68%
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            curr = ord(c) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0
        for i in range(26):
            if first[i] == -1:
                continue

            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans
