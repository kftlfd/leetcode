"""
Leetcode
1002. Find Common Characters
Easy
2024-06-05

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 49 ms, faster than 58.77% of Python3 online submissions for Find Common Characters.
    Memory Usage: 16.7 MB, less than 67.21% of Python3 online submissions for Find Common Characters.
    """

    def commonChars(self, words: List[str]) -> List[str]:
        chars = Counter(words[0])

        for word in words[1:]:
            w_cnt = Counter(word)
            to_del = []
            for c, f in chars.items():
                val = min(f, w_cnt.get(c, 0))
                chars[c] = val
                if val <= 0:
                    to_del.append(c)
            for c in to_del:
                del chars[c]

        ans = []
        for c, f in chars.items():
            if f > 0:
                ans += c * f

        return ans
