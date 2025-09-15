"""
Leetcode
2025-09-15
1935. Maximum Number of Words You Can Type
Easy

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.

 

Constraints:

    1 <= text.length <= 10^4
    0 <= brokenLetters.length <= 26
    text consists of words separated by a single space without any leading or trailing spaces.
    Each word only consists of lowercase English letters.
    brokenLetters consists of distinct lowercase English letters.


"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.85MB Beats 57.65%
    """

    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        def can_type(word: str) -> bool:
            for c in word:
                if c in brokenLetters:
                    return False
            return True

        return sum(can_type(word) for word in text.split(" "))
