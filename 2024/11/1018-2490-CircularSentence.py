"""
Leetcode
2024-11-02
2490. Circular Sentence
Easy

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

    For example, "Hello World", "HELLO", "hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

    The last character of a word is equal to the first character of the next word.
    The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

 

Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.

 

Constraints:

    1 <= sentence.length <= 500
    sentence consist of only lowercase and uppercase English letters and spaces.
    The words in sentence are separated by a single space.
    There are no leading or trailing spaces.
"""


class Solution:
    """
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Circular Sentence.
    Memory Usage: 16.6 MB, less than 45.68% of Python3 online submissions for Circular Sentence.
    """

    def isCircularSentence(self, sentence: str) -> bool:
        prev_char = sentence[-1]

        for word in sentence.split(' '):
            if word[0] != prev_char:
                return False
            prev_char = word[-1]

        return True


class Solution2:
    """
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Circular Sentence.
    Memory Usage: 16.5 MB, less than 80.88% of Python3 online submissions for Circular Sentence.
    """

    def isCircularSentence(self, sentence: str) -> bool:
        return sentence[0] == sentence[-1] and all(
            sentence[i] != ' ' or sentence[i-1] == sentence[i+1]
            for i in range(1, len(sentence)-1)
        )
