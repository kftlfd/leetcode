"""
Leetcode
2025-07-15
3136. Valid Word
Easy

A word is considered valid if:

    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.

You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.

 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

    1 <= word.length <= 20
    word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.


Hint 1
Use if-else to check all the conditions.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.73MB Beats 54.18%
    """

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        digits = '1234567890'
        vowels = 'aeiouAEIOU'
        A, Z = ord('A'), ord('Z')
        a, z = ord('a'), ord('z')

        has_vowel = False
        has_consonant = False

        for c in word:
            c_ord = ord(c)
            if c in vowels:
                has_vowel = True
            elif A <= c_ord <= Z or a <= c_ord <= z:
                has_consonant = True
            elif c not in digits:
                return False

        return has_vowel and has_consonant


class Solution1:
    """
    leetcode solution
    Runtime 3ms Beats 18.53%
    Memory 17.80MB Beats 34.46%
    """

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_vowel and has_consonant
