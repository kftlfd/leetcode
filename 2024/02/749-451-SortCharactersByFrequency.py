"""
Leetcode
451. Sort Characters By Frequency
Medium
2024-02-07

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

 

Constraints:

    1 <= s.length <= 5 * 105
    s consists of uppercase and lowercase English letters and digits.
"""

from collections import Counter


class Solution:
    """
    Runtime: 49 ms, faster than 53.32% of Python3 online submissions for Sort Characters By Frequency.
    Memory Usage: 17.9 MB, less than 66.85% of Python3 online submissions for Sort Characters By Frequency.
    """

    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = []

        for c, n in cnt.most_common():
            ans.append(c * n)

        return "".join(ans)
