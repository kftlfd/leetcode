"""
Leetcode
1704. Determine if String Halves Are Alike
Easy
2024-01-12

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

 

Constraints:

    2 <= s.length <= 1000
    s.length is even.
    s consists of uppercase and lowercase letters.
"""


class Solution:
    """
    Runtime: 38 ms, faster than 78.54% of Python3 online submissions for Determine if String Halves Are Alike.
    Memory Usage: 17.3 MB, less than 33.46% of Python3 online submissions for Determine if String Halves Are Alike.
    """

    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0

        for c in s[:len(s)//2]:
            if c in vowels:
                count += 1

        for c in s[len(s)//2:]:
            if c in vowels:
                count -= 1

        return count == 0
