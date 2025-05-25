"""
Leetcode
2025-05-25
2131. Longest Palindrome by Concatenating Two Letter Words
Medium

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

 

Constraints:

    1 <= words.length <= 10^5
    words[i].length == 2
    words[i] consists of lowercase English letters.


Hint 1
A palindrome must be mirrored over the center. Suppose we have a palindrome. If we prepend the word "ab" on the left, what must we append on the right to keep it a palindrome?
Hint 2
We must append "ba" on the right. The number of times we can do this is the minimum of (occurrences of "ab") and (occurrences of "ba").
Hint 3
For words that are already palindromes, e.g. "aa", we can prepend and append these in pairs as described in the previous hint. We can also use exactly one in the middle to form an even longer palindrome.
"""

from typing import List


class Solution:
    """
    Runtime 95ms Beats 45.31%
    Memory 35.68MB Beats 40.25%
    """

    def longestPalindrome(self, words: List[str]) -> int:
        chars = [[0] * 26 for _ in range(26)]
        a = ord('a')

        for word in words:
            l, r = word
            l = ord(l) - a
            r = ord(r) - a
            chars[l][r] += 1

        ans = 0
        odd_same = False

        for l in range(26):
            for r in range(l + 1):
                if l == r:
                    cnt = chars[l][r]
                    if cnt & 1 == 1:
                        if odd_same:
                            cnt -= 1
                        else:
                            odd_same = True
                    ans += cnt * 2
                else:
                    ans += min(chars[l][r], chars[r][l]) * 4

        return ans
