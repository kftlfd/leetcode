"""
Leetcode
451. Sort Characters By Frequency (medium)
2022-12-03

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from typing import List, Optional
from collections import Counter


# Runtime: 99 ms, faster than 44.96% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15.3 MB, less than 81.15% of Python3 online submissions for Sort Characters By Frequency.
class Solution:
    def frequencySort(self, s: str) -> str:
        chars = [c * n for c, n in Counter(s).items()]
        return "".join(sorted(chars, key=len, reverse=True))


# https://leetcode.com/problems/sort-characters-by-frequency/discuss/93410/1-line-Python-code./97904
# Runtime: 45 ms, faster than 93.51% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15.2 MB, less than 81.15% of Python3 online submissions for Sort Characters By Frequency.
class Solution1:
    def frequencySort(self, s: str) -> str:
        return "".join(c * n for c, n in Counter(s).most_common())


s = Solution1()
tests = [
    ("tree",
     "eert"),

    ("cccaaa",
     "aaaccc"),

    ("Aabb",
     "bbAa"),
]
for inp, exp in tests:
    res = s.frequencySort(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
