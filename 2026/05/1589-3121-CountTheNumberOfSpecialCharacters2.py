"""
Leetcode
2026-05-27
3121. Count the Number of Special Characters II
Medium

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

    1 <= word.length <= 2 * 10^5
    word consists of only lowercase and uppercase English letters.


"""


from string import ascii_lowercase, ascii_uppercase


class Solution:
    """
    Runtime 228ms Beats 72.35%
    Memory 21.64MB Beats 28.82%
    """

    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 26
        first_upper = [-1] * 26
        ord_a = ord("a")
        ord_A = ord("A")

        for i, c in enumerate(word):
            if c.islower():
                last_lower[ord(c) - ord_a] = i
                continue
            idx = ord(c) - ord_A
            if first_upper[idx] == -1:
                first_upper[idx] = i

        return sum(
            li >= 0 and ui >= 0 and ui > li
            for li, ui in zip(last_lower, first_upper)
        )


class Solution1:
    """
    sample 46ms solution
    Runtime 46ms Beats 99.41%
    Memory 21.40MB Beats 62.94%
    """

    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0

        for ch, CH in zip(ascii_lowercase, ascii_uppercase):
            if ch not in word or CH not in word:
                continue
            ans += word.rfind(ch) < word.find(CH)

        return ans
