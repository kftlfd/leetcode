"""
Leetcode
2025-01-07
1408. String Matching in an Array
Easy

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string



Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.



Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    All the strings of words are unique.
"""

from typing import List


class Solution:
    """
    Runtime 3ms Beats 64.01%
    Memory 17.87MB Beats 12.59%
    """

    def stringMatching(self, words: List[str]) -> List[str]:
        return [word for i, word in enumerate(words) if any(word in w for w in words[:i] + words[i+1:])]


class Solution2:
    """
    leetcode solution 2: KMP Algorithm
    Runtime 55ms Beats 5.67%
    Memory 17.70MB Beats 19.52%
    """

    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []

        for current_word_index, current_word in enumerate(words):
            lps = self._compute_lps_array(current_word)
            # Compare the current word with all other words.
            for other_word_index, other_word in enumerate(words):
                if current_word_index == other_word_index:
                    continue  # Skip comparing the word with itself.

                # Check if the current word is a substring of another word.
                if self._is_substring_of(current_word, other_word, lps):
                    matching_words.append(current_word)
                    break  # No need to check further for this word.

        return matching_words

    # Function to compute the LPS (Longest Prefix Suffix) array for the substring 'sub'.
    def _compute_lps_array(self, sub: str) -> List[int]:
        lps = [0] * len(sub)
        current_index = 1
        length = 0

        while current_index < len(sub):
            if sub[current_index] == sub[length]:
                length += 1
                lps[current_index] = length
                current_index += 1
            else:
                if length > 0:
                    length = lps[
                        length - 1
                    ]  # Backtrack using LPS array to find a shorter match.
                else:
                    current_index += 1
        return lps

    # Function to check if 'sub' is a substring of 'main' using the KMP algorithm.
    def _is_substring_of(self, sub: str, main: str, lps) -> bool:
        main_index = 0
        sub_index = 0

        while main_index < len(main):
            if main[main_index] == sub[sub_index]:
                main_index += 1
                sub_index += 1
                if sub_index == len(sub):
                    return True  # Found a match.
            else:
                if sub_index > 0:
                    # Use the LPS to skip unnecessary comparisons.
                    sub_index = lps[sub_index - 1]
                else:
                    main_index += 1
        return False  # No match found.
