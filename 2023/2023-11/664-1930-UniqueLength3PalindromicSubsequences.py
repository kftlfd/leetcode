"""
Leetcode
1930. Unique Length-3 Palindromic Subsequences (medium)
2023-11-14

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

    3 <= s.length <= 105
    s consists of only lowercase English letters.

Hints:
- What is the maximum number of length-3 palindromic strings?
- How can we keep track of the characters that appeared to the left of a given position?
"""


class Solution:
    """
    leetcode solution 1: count letters in-between
    Time: O(n)
    Space: O(1)
    Runtime: 674 ms, faster than 50.55% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
    Memory Usage: 17.3 MB, less than 44.09% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
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


class Solution1:
    """
    leetcode solution 2: pre-compute first and last indicies
    Time: O(n)
    Space: O(1)
    Runtime: 784 ms, faster than 46.28% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
    Memory Usage: 17.3 MB, less than 24.40% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
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
