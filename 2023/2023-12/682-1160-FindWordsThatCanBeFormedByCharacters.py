"""
Leetcode
1160. Find Words That Can Be Formed by Characters
Easy
2023-12-02

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    words[i] and chars consist of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    """
    Runtime: 200 ms, faster than 24.20% of Python3 online submissions for Find Words That Can Be Formed by Characters.
    Memory Usage: 16.7 MB, less than 83.02% of Python3 online submissions for Find Words That Can Be Formed by Characters.
    """

    def countCharacters(self, words: List[str], chars: str) -> int:

        def get_freqs(word: str):
            freqs = defaultdict(int)
            for c in word:
                freqs[c] += 1
            return freqs

        char_freqs = get_freqs(chars)
        ans = 0

        for word in words:
            word_freqs = get_freqs(word)
            is_good = True
            for c, f in word_freqs.items():
                if char_freqs[c] < f:
                    is_good = False
                    break
            if is_good:
                ans += len(word)

        return ans
