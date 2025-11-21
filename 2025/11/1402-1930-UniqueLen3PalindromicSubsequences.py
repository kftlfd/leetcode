"""
Leetcode
2025-11-21
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

    3 <= s.length <= 105
    s consists of only lowercase English letters.



Hint 1
What is the maximum number of length-3 palindromic strings?
Hint 2
How can we keep track of the characters that appeared to the left of a given position?
"""


class Solution:
    """
    Runtime 3078ms Beats 5.11%
    Memory 21.67MB Beats 12.53%
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        a = ord('a')
        chars_right = [0] * n
        palindromes = set()

        mask = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            chars_right[i] = mask
            mask |= 1 << (ord(c) - a)

        mask_left = 1 << (ord(s[0]) - a)
        for c in range(1, n - 1):
            char = s[c]
            mask_right = chars_right[c]

            for i in range(26):
                mask = 1 << i
                if mask_left & mask != mask or mask_right & mask != mask:
                    continue
                mask_char = chr(i + a)
                palindromes.add(mask_char + char + mask_char)

            mask_left |= 1 << (ord(char) - a)

        return len(palindromes)


class Solution1:
    """
    leetcode solution 1: Count Letters In-Between
    Runtime 479ms Beats 52.94%
    Memory 18.22MB Beats 59.85%
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


class Solution1a:
    """
    leetcode solution 1: Count Letters In-Between (One-liner)
    Runtime 83ms Beats 93.35%
    Memory 18.04MB Beats 93.09%
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])


class Solution2:
    """
    leetcode solution 2: Pre-Compute First and Last Indices
    Runtime 526ms Beats 46.54%
    Memory 18.40MB Beats 39.64%
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
