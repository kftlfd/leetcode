"""
Leetcode
1832. Check if the Sentence Is Pangram (easy)
2022-10-17

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
"""

from typing import List, Optional


# Runtime: 35 ms, faster than 90.06% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 13.9 MB, less than 54.73% of Python3 online submissions for Check if the Sentence Is Pangram.
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        seen = set()

        def record(c: str) -> int:
            seen.add(c)
            return len(seen)

        for c in sentence:
            if record(c) == 26:
                return True

        return False


# Runtime: 66 ms, faster than 21.15% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.
class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:

        return len(set(sentence)) == 26


# leetcode solytion - 4: bit manipulation
# Runtime: 68 ms, faster than 15.99% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 14 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.
class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:

        req = (1 << 26) - 1
        seen = 0
        a = ord('a')

        for c in sentence:
            idx = ord(c) - a
            seen |= 1 << idx
            if seen == req:
                return True

        return False

    # original implementation
    def checkIfPangramLC(self, sentence: str) -> bool:
        # Initialize seen = 0 since we start with no letter.
        seen = 0

        # Iterate over 'sentence'.
        for curr_char in sentence:
            # Map each 'curr_char' to its index using its ASCII code.
            mapped_index = ord(curr_char) - ord('a')

            # 'curr_bit' represents the bit for 'curr_char'.
            curr_bit = 1 << mapped_index

            # Use 'OR' operation since we only add its bit for once.
            seen |= curr_bit

        # Once we finish iterating, check if 'seen' contains 26 bits of 1.
        return seen == (1 << 26) - 1


s = Solution2()
tests = [
    "thequickbrownfoxjumpsoverthelazydog",
    "leetcode",
]
for t in tests:
    print(t)
    print(s.checkIfPangram(t))
    print()
