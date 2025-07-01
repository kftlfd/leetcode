"""
Leetcode
2025-07-01
3330. Find the Original Typed String I
Easy

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

 

Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

Example 3:

Input: word = "aaaa"

Output: 4

 

Constraints:

    1 <= word.length <= 100
    word consists only of lowercase English letters.


Hint 1
Any group of consecutive characters might have been the mistake.
"""

from collections import Counter


class Solution00:
    """
    Wrong Answer 553 / 780 testcases passed
    """

    def possibleStringCount(self, word: str) -> int:
        return 1 + sum(n - 1 for n in Counter(word).values())


class Solution01:
    """
    Runtime 39ms Beats 61.69%
    Memory 17.67MB Beats 72.11%
    """

    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                ans += 1
        return ans
