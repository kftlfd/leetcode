"""
Leetcode
1647. Minimum Deletions to Make Character Frequencies Unique (medium)
2023-09-12

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

    1 <= s.length <= 105
    s contains only lowercase English letters.
"""

from collections import defaultdict


class Solution:
    """
    Runtime: 186 ms, faster than 41.26% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    Memory Usage: 17.1 MB, less than 93.71% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
    """

    def minDeletions(self, s: str) -> int:
        char_counts = defaultdict(int)
        for c in s:
            char_counts[c] += 1

        freqs = sorted(char_counts.values())

        ans = 0

        seen_freqs = set()

        for freq in freqs:
            cur = freq
            while cur > 0 and cur in seen_freqs:
                cur -= 1
                ans += 1
            seen_freqs.add(cur)

        return ans
