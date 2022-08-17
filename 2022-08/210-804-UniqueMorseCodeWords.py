"""
Leetcode
804. Unique Morse Code Words (easy)
2022-08-17

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

 - 'a' maps to ".-",
 - 'b' maps to "-...",
 - 'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

 - For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1
"""

from typing import List


# leetcode solution
# Runtime: 48 ms, faster than 67.93% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.9 MB, less than 24.27% of Python3 online submissions for Unique Morse Code Words.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)


s = Solution()
tests = [
    ["gin", "zen", "gig", "msg"],
    ["a"],
]
for t in tests:
    print(t)
    print(s.uniqueMorseRepresentations(t))
    print()
