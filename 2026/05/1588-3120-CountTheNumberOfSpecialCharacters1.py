"""
Leetcode
2026-05-26
3120. Count the Number of Special Characters I
Easy

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

 

Constraints:

    1 <= word.length <= 50
    word consists of only lowercase and uppercase English letters.


"""


import string


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.40MB Beats 25.31%
    """

    def numberOfSpecialChars(self, word: str) -> int:
        lower = [False] * 26
        upper = [False] * 26

        for c in word:
            if c.islower():
                lower[ord(c) - ord("a")] = True
            else:
                upper[ord(c) - ord("A")] = True

        return sum(lower[i] and upper[i] for i in range(26))


class Solution1:
    """
    leetcode solution
    Runtime 2ms Beats 42.11%
    Memory 19.30MB Beats 64.16%
    """

    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(c in s and c.upper() in s for c in string.ascii_lowercase)
